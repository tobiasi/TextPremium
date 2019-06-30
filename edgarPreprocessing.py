# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 09:35:11 2019

@author: Tobias

We are interested in extracting three things: 
    (i)   The company tickers/cik codes 
    (ii)  The filing date          -> Keep filtration in check when forecasting
    (iii) The text from the filings-> Create corporas & dictionaries
"""
import datetime
import edgar
import bs4 as bs
import os
import pickle
import requests
import numpy as np
import sys
import gensim
import en_core_web_sm
import fnmatch
import gensim.corpora as corpora
from nltk.corpus import stopwords
from gensim.utils import simple_preprocess
from fuzzywuzzy   import fuzz

def new_files(filenames,filepath):
    '''
    Checks whether the proposed filename already exists. It will return all 
    filenames which are not found in the indicated folder.
    
    Inputs:
     - filenames : A list with filenames to be evaluated
         
     - filepath  : Path for existing files
         
    Outputs:
     - filenames : The non-existing filenames
     
    filepath = 'C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Corpora U.S\\10-K\\3M CO'
    ''' 
    existing = os.listdir(filepath)
    existing = [filename.replace('.txt','') for filename in existing]
    return [newfiles for newfiles in filenames if not newfiles in existing]

def get_sp500_tickers_cik_industry_name(f_dir):
    '''
    ---------------------------------------------------------------------------
    Scraping function to get the tickers, cik codes, sector and names for all 
    companies on the S&P 500 index
    
    Input: 
    
    - f_dir : The directory where you want to save the output
    
    Outputs: 
        
    - data  : A list with company tickers, cik code, sector and name.

    Example:
        
    f_dir = 'C:\\Users\\Tobias\\Dropbox\\Master\\US\\ticks_cik'
    
    get_sp500_tickers_cik_industry_name(f_dir)
    ---------------------------------------------------------------------------
    '''
    
    resp    = requests.get('http://en.wikipedia.org/wiki/'+
                           'List_of_S%26P_500_companies')
    soup    = bs.BeautifulSoup(resp.text, 'lxml')
    table   = soup.find('table', {'class': 'wikitable sortable'})
    data    = []
    for row in table.findAll('tr')[1:]:
        name   = row.findAll('td')[0].text
        ticker = row.findAll('td')[1].text
        sector = row.findAll('td')[3].text
        cik    = row.findAll('td')[7].text
        data   = np.append(data,(ticker,cik.replace('\n',''),sector,name))
    data = tuple(np.reshape(data,(int(len(data)/4),4)))
    os.chdir(f_dir)
    with open('sp500tickcik.pickle', 'wb') as file:
        pickle.dump(data, file)
    return data

def get_comp_tuples(companies,data_folder):
    '''
    
    '''
    
    with open('sp500tickcik', 'rb') as file:
        data = pickle.load(file)
    names = []
    for idx in range(len(data)):
        names = np.append(names,data[idx][3])
    
    tick_cik = []
    edgar_t    = edgar.Edgar()
    for name in companies: 
        score=[]
        for textTemp in names:
            score = np.append(score, fuzz.ratio(textTemp, name))
        
        maxInd   = np.where(score == np.amax(score))[0][0]
        bmc      = str(data[maxInd][3])
        bmc      = bmc.replace("'" , "")
        bmc      = bmc.replace("." , "")
        comp     = edgar_t.findCompanyName(bmc)
        tick_cik = np.append(tick_cik,(comp[0],data[maxInd][1]))
        
    
    
    
def get_edgar_filing_date(comp_tuples,f_type,f_dir):
    '''
    ---------------------------------------------------------------------------
    Scraping function to get filing dates from the SEC website. It will save
    the dates to the given directory.

    Inputs:
        
    - comp_tuples : A list of tuples. First element of the tuple is the company 
                    name. Second element is the CIK code.
                    
    - type        : A string with the filing type.
    
    - f_dir       : A string with the master directory of all company dates
    
    Outputs: NONE

    Example:
    comp_tuples = [['APPLE INC'     , '0000320193'],
                  ['MCDONALDS CORP', '0000063908']]

    f_type      = '10-K'     [Or '10-Q']
    
    f_dir       = 'C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\...
                                                            Dates Reports U.S'
    
    get_edgar_filing_date(comp_tuples,f_type,f_dir)   
    ---------------------------------------------------------------------------
    '''
    
    print('\nFetching dates...')
    print('-'*80+ '\n')
    for idx, comp_tuple in enumerate(comp_tuples):
        resp    = requests.get('https://www.sec.gov/cgi-bin/browse-edgar?'+
                            'action=getcompany&CIK=' + comp_tuple[1]      +
                            '&type='+f_type+'&dateb=&owner=exclude&count=100')
        soup    = bs.BeautifulSoup(resp.text, 'lxml')
        table   = soup.find('table', {'class': 'tableFile2'})
        dates = []
        for row in table.findAll('tr')[1:]:
            if '/A' in row.findAll('td')[0].text: continue
            date = row.findAll('td')[3].text
            dates.append(date)
        if '.' in comp_tuple[0][-1]: 
            comp_tuple[0] = comp_tuple[0][:-1]
        if not os.path.exists(f_dir + '\\' + f_type + '\\' +  comp_tuple[0]):
            os.mkdir(f_dir +'\\'+ f_type + '\\' + comp_tuple[0])
        os.chdir(f_dir +'\\' + f_type + '\\' + comp_tuple[0])
        with open(comp_tuple[0] + '.pickle', 'wb') as file:
            pickle.dump(dates, file)
            
        mes=('Status: '+str( int((idx+1)/len(comp_tuples)*100) )+ '% done')
        sys.stdout.write('\r'+mes)     
        
def get_edgar_filing_text(comp_tuples,f_type,n_docs,file_dir,dates_dir):
    '''
    ---------------------------------------------------------------------------
    Scraping function to get the text from company filings from EDGAR. 
    
    Inputs:
        
    - comp_tuples : A list with pairwise company tuples. The first element must 
                    be a string with the company name as listed on the EDGAR
                    database. The second element must be a string with the CIK
                    identifier. See get_sp500_tickers_cik_industry(argin) to 
                    easily get the tuples from the S&P500 listed firms.
                
    - f_type      : A string with the filing type.
    
    - n_docs      : Number of filings to be fetched, in descending order, i.e.
                    n_docs = 3 will fetch the three newest filings of type 
                    f_type. As a double integer.
                    
    - file_dir    : The master directory where all filings are to be saved. As
                    a string.
                    
    - dates_dir   : The master directory where all filing dates are saved. If 
                    a directory is missing, the function will instead scrape 
                    the dates using get_edgar_filing_date(argin), and create a 
                    new folder with the dates.
                    
    Example: 
        
    comp_tuples = [['APPLE INC'     , '0000320193'],
                   ['MCDONALDS CORP', '0000063908'],
                   ['MICROSOFT CORP', '0000789019']]

    f_type      = '10-K'     [Or '10-Q']
    
    n_docs      = 3
    
    file_dir    = 'C:\\Users\\Tobias\\Dropbox\\Master\\Text Reports U.S.'
    
    dates_dir   = 'C:\\Users\\Tobias\\Dropbox\\Master\\Dates Reports U.S' 
                   
    get_edgar_filing_text(comp_tuples,f_type,n_docs,file_dir,dates_dir)
    ---------------------------------------------------------------------------
    '''
    
    print('Fetching data...')
    print('-'*80+ '\n')
    for idx, comp_tuple in enumerate(comp_tuples):
        comp = edgar.Company(comp_tuple[0],comp_tuple[1])
        tree = comp.getAllFilings(filingType = f_type)
        docs = edgar.getDocuments(tree, noOfDocuments=n_docs)
        
        # Now that we have the filings, find get the filing dates for each 
        # document. If we have them already, then great, let's load them. If 
        # not, call get_edgar_filing_date to get them for this company.
        if not os.path.exists(dates_dir+ '\\' + f_type + '\\' + comp_tuple[0]):
            print(('\nCannot find the dates for ' + comp_tuple[0] +
                   '. Attempts to download them...'))
            get_edgar_filing_date([comp_tuple],f_type,dates_dir)
        else:
            os.chdir(dates_dir + '\\' + f_type + '\\' + comp_tuple[0])
            if '.' in comp_tuple[0][-1]: 
                comp_tuple[0] = comp_tuple[0][:-1]
            with open(comp_tuple[0] + '.pickle', 'rb') as file:
                dates = pickle.load(file)
                dates = dates[:n_docs]
        if not os.path.exists(file_dir + '\\' + f_type + '\\'+comp_tuple[0]):
            os.mkdir(file_dir + '\\' + f_type +'\\'+comp_tuple[0])
        os.chdir(file_dir + '\\' + f_type +'\\'+comp_tuple[0])
        for date, doc in zip(dates,docs):
           f = open(date.replace('.pickle','')+'.txt','w',encoding='utf8')
           f.write(str(doc))
           f.close()
        mes=('Status: '+str( int((idx+1)/len(comp_tuples)*100) )+ '% done')
        sys.stdout.write('\r'+mes) 
        
'''
-------------------------------------------------------------------------------
Helping functions for edgar_text_to_corpora
-------------------------------------------------------------------------------
'''

def sent_to_words(sentences):
    '''
    Split sentences up in to tokens
    '''
    for sentence in sentences: 
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True)) 
        
def remove_stopwords(texts,stop_words):
    return [[word for word in simple_preprocess(str(doc)) if word 
             not in stop_words] for doc in texts]
    
def make_bigrams(texts,bigram_mod):
    return [bigram_mod[doc] for doc in texts]

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    nlp       = en_core_web_sm.load()
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent)) 
        texts_out.append([token.lemma_ for token in doc if token.pos_ in
                         allowed_postags])
    return texts_out

def text_prep(text):
#        text = max(text, key=len)
#        if len(text)<1000000:
#            dataTe     = list(sent_to_words(text))
#        else:
#            dataTe1 = list(sent_to_words(text[:500000]))
#            dataTe2 = list(sent_to_words(text[500000:]))
#            dataTe  = dataTe1+dataTe2
        dataTe     = list(sent_to_words(text))
        dataTe     = [x for x in dataTe if x != '']
        data_words = [x for x in dataTe if x != []]
        stop_words = stopwords.words('english')
        stop_words.extend(['statoil', 'salmar', 'equinor', 'quarterly',
                           'report'])
        bigram             = gensim.models.Phrases(data_words, min_count=1, 
                                                   threshold=20)
        bigram_mod = gensim.models.phrases.Phraser(bigram)
        data_words_nostops = remove_stopwords(data_words,stop_words)
        data_words_bigrams = make_bigrams(data_words_nostops,bigram_mod)

        data_lemmatized = lemmatization(data_words_bigrams,allowed_postags=[
                                        'NOUN', 'ADJ', 'VERB', 'ADV']) 
        return data_lemmatized

def query_yes_no(question, default = "yes"):
    '''
    Function to print question to console. 
    '''
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")    
            
'''
-------------------------------------------------------------------------------
'''

def edgar_text_to_corpora(companies,file_dir,date_dir,corp_dir,f_type):
    '''
    Function to convert the EDGAR text files to corporas that can be used in 
    LDA-estimation. Creates a corpora and a dictionary for each filing.
    
    companies = 'all'
    f_type    = '10-K'
    date_dir  = 'C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Dates Reports U.S'
    file_dir  = 'C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Text Reports U.S'
    corp_dir  = 'C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Corpora U.S'
    '''
    if 'all' in companies:
        companies = os.listdir(file_dir+'\\'+f_type)
    start =  datetime.datetime.now().time
    if not os.path.exists(corp_dir + '\\' + f_type):
          os.mkdir(corp_dir + '\\' + f_type)
    for company in companies:
        comp_path = file_dir + '\\' + f_type + '\\' + company
        date_path = date_dir + '\\' + f_type + '\\' + company
        corp_path = corp_dir + '\\' + f_type +'\\'+company
        
        if not os.path.exists(corp_path):
            os.mkdir(corp_path)
        corpfiles  = fnmatch.filter(os.listdir(corp_path), '*corpus*')
        ex_text_t    = [file.split('.')[-2] for file in corpfiles]
        # Find all existing dates
        os.chdir(date_path)
        with open(company + '.pickle', 'rb') as file:
               dates = pickle.load(file)
               
        ex_text = [date for date in dates if not date in ex_text_t]
        
#        non_existing =  [non_existing for non_existing in dates if not 
#                         non_existing in ex_text]
#        if len(non_existing):
#            q   = ('\n'+company + ':: There are '+str(len(non_existing))+
#                   ' text files missing'+
#                  '. Do you want to download these before you continue?')
#            bol =  query_yes_no(q, default = "yes")
#            
#            if bol:
#                print(('\nAutomatic exectuion not yet supported. Please run '+
#                       'get_edgar_filing_text() manually.'))
#                return
        if not ex_text:
            continue
        print('Estimation started: ' +str(start()) +'\n')
        for idx, date in enumerate(ex_text):
             os.chdir(comp_path)
             with open(date+'.txt',encoding='utf8') as file:
               text = file.read().splitlines()
               if len(max(text, key=len))>1000000: break                   
               data_lemmatized = text_prep(text)
               
             id2word    = corpora.Dictionary(data_lemmatized)
             corpus     = [id2word.doc2bow(text) for text in data_lemmatized]
             dictionary = corpora.Dictionary(data_lemmatized)
             corpus     =[dictionary.doc2bow(text) for text in data_lemmatized]
             if not os.path.exists(corp_path):
                 os.mkdir(corp_path)
             os.chdir(corp_path)
             pickle.dump(corpus, open(('corpus.'+company+'.'+date+'.txt'), 'wb'))
             dictionary.save('dictionary.'+company+'.'+date+'.txt')
             mes = (
             str(int((idx+1)/len(ex_text)*100))+'% done with '+company+'.')
             sys.stdout.write('\r'+mes) 
            
###############################################################################

# Some useful tuples
comp_tuples = [['APPLE INC'                           , '0000320193'],
               ['MCDONALDS CORP'                      , '0000063908'],
               ['MICROSOFT CORP'                      , '0000789019'],
               ['AMAZON COM INC'                      , '0001018724'],
               ['Facebook Inc'                        , '0001326801'],
               ['BERKSHIRE HATHAWAY INC'              , '0001067983'],
               ['JOHNSON & JOHNSON'                   , '0000200406'],
               ['Alphabet Inc.'                       , '0001652044'],
               ['JPMORGAN CHASE & CO'                 , '0000019617'],
               ['EXXON MOBIL CORP'                    , '0000034088'],
               ['VISA INC.'                           , '0001403161'],
               ['BANK OF AMERICA CORP'                , '0000070858'],
               ['PROCTER & GAMBLE Co'                 , '0000080424'],
               ['INTEL CORP'                          , '0000050863'],
               ['PFIZER INC'                          , '0000078003'],
               ['UNITEDHEALTH GROUP INC'              , '0000731766'],
               ['VERIZON COMMUNICATIONS INC'          , '0000732712'],
               ['CHEVRON CORP'                        , '0000093410'],
               ['CISCO SYSTEMS, INC.'                 , '0000858877'],
               ['AT&T INC.'                           , '0000732717'],
               ['HOME DEPOT INC'                      , '0000354950'],
               ['Merck & Co. Inc.'                    , '0000310158'],
               ['Mastercard Inc'                      , '0001141391'],
               ['WELLS FARGO & CO'                    , '0000072971'],
               ['BOEING CO'                           , '0000012927'],
               ['TWDC Enterprises 18 Corp.'           , '0001001039'],
               ['COMCAST CORP'                        , '0001166691'],
               ['COCA COLA CO'                        , '0000021344'],
               ['PEPSICO INC'                         , '0000077476'],
               ['NETFLIX INC'                         , '0001065280'],
               ['CITIGROUP INC'                       , '0000831001'],
               ['WAL MART STORES INC'                 , '0000104169'],
               ['ABBOTT LABORATORIES'                 , '0000001800'],
               ['Philip Morris International Inc.'    , '0001413329'],
               ['ORACLE CORP'                         , '0001341439'],
               ['ADOBE SYSTEMS INC'                   , '0000796343'],
               ['INTERNATIONAL BUSINESS MACHINES CORP', '0000051143'],
               ['PayPal Holdings, Inc.'               , '0001633917'],
               ['MEDTRONIC INC'                       , '0000064670'],
               ['3M CO'                               , '0000066740'],
               ['DowDuPont Inc.'                      , '0001666700'],
               ['SALESFORCE COM INC'                  , '0001108524'],
               ['AbbVie Inc.'                         , '0001551152'],
               ['UNION PACIFIC CORP'                  , '0000100885'],
               ['Avago Technologies LTD'              , '0001441634'],
               ['AMGEN INC'                           , '0000318154'],
               ['HONEYWELL INTERNATIONAL INC'         , '0000773840'],
               ['LILLY ELI & CO'                      , '0000059478'],
               ['THERMO FISHER SCIENTIFIC INC.'       , '0000097745']]









