# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:59:06 2019

@author: Tobias
"""
import fnmatch
import os
import pickle
import sys
import gensim
import pandas as pd
import numpy  as np
import datetime


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

def lda_estimation(corp_path,model_path,f_type,options):
    '''
    Function to run LDA estimation on corpora. 
    
    Inputs:
     - corp_path  : Path to master directory for all corporas, both 10-K and
                    10-Q
     
     - model_path : Path to master directory for all models, both 10-K and
                    10-Q
     
     - f_type     : Filing type. E.g. '10-K'
     
     - options    : Estimation options. 
     
     - overwrite  : True if you want to overwrite potential existing model 
                    files, false otherwise. If false, it will search for 
                    existing files and only estimate models for periods that 
                    does not exist in model directory.
         
    Output: NONE

    Examples:
        
     corp_path  = 'C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Corpora U.S'
     model_path = 'C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Model U.S'
     f_type     = '10-K'
     
     # Set parameters
     num_topics      = 40        
                         
     random_state    = 1000     
                         
     update_every    = 1         
                         
     chunksize       = 500       
                         
     passes          = 20      
                         
     alpha           = 'auto'    
                        
     per_word_topics = True    
                      
     overwrite       = False
   
     options = [num_topics,random_state,update_every,
                chunksize,passes,alpha,per_word_topics,overwrite]
     lda_estimation(corp_path,model_path,f_type,options)
    '''
    
    corp_path_ex = corp_path  + '\\' + f_type
    mod_path_ex  = model_path + '\\' + f_type
    companies    = os.listdir(corp_path_ex)
    start =  datetime.datetime.now().time
    print('Estimation started: ' +str(start()) +'\n')
    for idx, company in enumerate(companies):
        folder =  fnmatch.filter(os.listdir(mod_path_ex), company)
        if not folder:
             os.mkdir(mod_path_ex + '\\' + company)
             
        comp_path_corp = corp_path_ex + '\\' + company
        comp_path_mod  = mod_path_ex  + '\\' + company
        corpFiles = fnmatch.filter(os.listdir(comp_path_corp), '*corpus*')
        dictFiles = fnmatch.filter(os.listdir(comp_path_corp), '*dictionary*')
        ex_models = fnmatch.filter(os.listdir(comp_path_mod), 'LDAtopics.*')
        periods   = [filename.split('.')[2] for filename in corpFiles]
        if options[7] or not ex_models:
            corpFilesOut = corpFiles
            dictFilesOut = dictFiles
            newFiles     = periods
        else:
            cleanVec_c = [filename.split('.')[2] for filename in corpFiles]
            cleanVec_m = [filename.split('.')[1] for filename in ex_models]
            newFiles   = [newfiles for newfiles in cleanVec_c if not newfiles
                          in cleanVec_m]
            p1_corp    = 'corpus.'     + company + '.'
            p1_dict    = 'dictionary.' + company + '.'
            p2         = '.txt'
             
            corpFilesOut = []
            dictFilesOut = []
            for period in newFiles:
                corpFilesOut = np.append(corpFilesOut,p1_corp+period+p2)
                dictFilesOut = np.append(dictFilesOut,p1_dict+period+p2)
            
        files = zip(newFiles,corpFilesOut,dictFilesOut)
        for idy, (period,corpfile,dictfile) in enumerate(files):
            os.chdir(comp_path_corp)
            dictionary = gensim.corpora.Dictionary.load(dictfile)
            corpus     = pickle.load(open(corpfile, 'rb'))
            lda_model  = gensim.models.ldamodel.LdaModel(
                                            corpus          = corpus,
                                            id2word         = dictionary,
                                            num_topics      = options[0], 
                                            random_state    = options[1],
                                            update_every    = options[2],
                                            chunksize       = options[3],
                                            passes          = options[4],
                                            alpha           = options[5],
                                            per_word_topics = options[6])
            os.chdir(comp_path_mod)
            lda_model.save(period)
            top_words_per_topic = []
            for t in range(num_topics):
                top_words_per_topic.extend([(t, ) + x for x in 
                                           lda_model.show_topic(t, topn = 10)])
                
            if idx == 0:
                mes = (str(int((idy+1)/len(corpFilesOut)*100))+ '% done with ' 
                       + company +
                       '.  || This is the first company in the folder.')
            else:
                mes = (str(int((idy+1)/len(corpFilesOut)*100)) + '% done with ' 
                       + company + '.  ||  ' +
                       str(int((idx+1)/len(companies)*100))+ 
                       '% done with folder.' + ' '*50)
            sys.stdout.write('\r'+mes) 
            pd.DataFrame(top_words_per_topic,
            columns=['Topic', 'Word', 'P']).to_csv(("LDAtopics."+ 
                                                         period +".csv"))
        
###############################################################################        
        

# Set parameters
num_topics      = 100        
                            
random_state    = 1000     
                            
update_every    = 1         
                            
chunksize       = 500       
                            
passes          = 20      
                            
alpha           = 'auto'    
                           
per_word_topics = True    
                         
overwrite       = False
  
options = [num_topics,random_state,update_every,
           chunksize,passes,alpha,per_word_topics,overwrite]

corp_path  = 'C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Corpora U.S'
model_path = 'C:\\Users\\Tobias\\Dropbox\\Master\\U.S. Data\\Model U.S'
f_type     = '10-K'     

 
# Run LDA estimation 
lda_estimation(corp_path,model_path,f_type,options)       
        
        
        
        
        
        
        
        
 