# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 09:16:40 2018

@authors: Tobias & Kristian

Run LDA-estimation
"""

##############################
##### Set parameters #########
num_topics      = 40        ##
                            ##
random_state    = 1000      ##
                            ##
update_every    = 1         ##
                            ##
chunksize       = 500       ##
                            ##
passes          = 20        ##
                            ##
alpha           = 'auto'    ##
                            ##
per_word_topics = True      ##
                            ##
##############################
##############################

# We are currently interested in the recursive LDA model starting in year 2000 
years = list(range(2000,2018))


mainpath   = 'C:\\Users\\Tobias\\Dropbox\\Master\\sandbox\\S3\\corpfolder'
resultpath = 'C:\\Users\\Tobias\\Dropbox\\Master\\sandbox\\S3\\resultfolder'



mainpath  = 'C:\\Users\\Tobias\\Dropbox\\Master\\sandbox\\S3\\corpfolderNonRec'
corpFiles = fnmatch.filter(os.listdir(mainpath), '*corpus*')
dictFiles = fnmatch.filter(os.listdir(mainpath), '*dictionary*')
year      = [i.split('.', 2)[1] for i in corpFiles]

"""
#########################################################
This loop will create NEW LDA models for each iteration #
#########################################################
"""
mainpath  = 'C:\\Users\\Tobias\\Dropbox\\Master\\Annual Reports OBX'

companies = os.listdir(mainpath)
for nn in range(len(companies)):
    
    modelpath = mainpath + '\\' + companies[nn] + '\\model'
    corppath  = mainpath + '\\' + companies[nn] + '\\corpora'
#    models    = os.listdir(modelpath)
#    
#    models = os.listdir(testpath)
#    
#    
#    cleanVecT    = [i.split('.', 1)[0] for i in models]
#    cleanVec    = list(set(fnmatch.filter(cleanVecT, 'LDA*')))
 #   # Identify missing models
 #   cleanVec    = [i.split('.', 1)[0] for i in pdffiles]
  #  cleanVec    = [i.replace(' ', '') for i in cleanVec]
  #  textVec     = [element + '.txt' for element in cleanVec]
    
    # Check if the file already exists
  #  textfiles =  fnmatch.filter(os.listdir(textpath), '*.txt')
  #  newFiles  = [newfiles for newfiles in textVec if not newfiles in textfiles]
    corpFiles = fnmatch.filter(os.listdir(corppath), '*corpus*')
    dictFiles = fnmatch.filter(os.listdir(corppath), '*dictionaryFULL*')
  #  dictFiles = fnmatch.filter(os.listdir(corppath), '*dictionary*')
    for ii in range(0,len(corpFiles)):
        os.chdir(corpuspath)
        dictionary = gensim.corpora.Dictionary.load(dictFiles[ii])
        corpus     = pickle.load(open(corpFiles[ii], 'rb'))
        
        # Build recursive LDA model
        lda_model = gensim.models.ldamodel.LdaModel(corpus         = corpus,
                                                   id2word         = dictionary,
                                                   num_topics      = num_topics, 
                                                   random_state    = random_state,
                                                   update_every    = update_every,
                                                   chunksize       = chunksize,
                                                   passes          = passes,
                                                   alpha           = alpha,
                                                   per_word_topics = per_word_topics)
        os.chdir(modelpath)
        lda_model.save('LDAREC'+str(year[ii]))
        top_words_per_topic = []
        for t in range(num_topics):
            top_words_per_topic.extend([(t, ) + x for x in lda_model.show_topic(t, topn = 10)])
            
        
       
        pd.DataFrame(top_words_per_topic, columns=['Topic', 'Word', 'P']).to_csv("LDAtopics."+ str(year[ii])+".csv")
        print('Finished with model number ' + str(ii) + ' of ' + str(len(corpFiles))  + ' for ' + companies[nn])
    
"""
######################################################
This loop will recursively update the same LDA model #
######################################################
"""

mainpath = 'C:\\Users\\Tobias\\Dropbox\\Master\\Quarterly Reports OBX\\'
mainpath = 'C:\\Users\\Tobias\\Dropbox\\Master\\Quarterly Reports U.S\\'
companies = os.listdir(mainpath)
for nn in range(len(companies)):
    comppath = mainpath + companies[nn] 
    modelpath = comppath + '\\model'
    corppath  = comppath + '\\corpora'
    corpFiles = fnmatch.filter(os.listdir(corppath), 'corpus*')
    dictFiles  = fnmatch.filter(os.listdir(corppath), '*FULL*')
    # Quarterly or annually?
    #year = range(len(corpFiles))
    cleanVec = [i.split('corpus.', 1)[1] for i in corpFiles]
    year     = [i.replace('.txt', '') for i in cleanVec]
    
    for ii in range(len(corpFiles)): 
        os.chdir(corppath)
        # If we are in the first iteration we must build the initial model
        if ii==0:
            
            dictionary = gensim.corpora.Dictionary.load(dictFiles[-1])
            corpus     = pickle.load(open(corpFiles[0], 'rb'))
            # Build initial LDA-model
            lda_model = gensim.models.ldamodel.LdaModel(corpus   = corpus,
                                                 id2word         = dictionary,
                                                 num_topics      = num_topics, 
                                                 random_state    = random_state,
                                                 update_every    = update_every,
                                                 chunksize       = chunksize,
                                                 passes          = passes,
                                                 alpha           = alpha,
                                                 per_word_topics = per_word_topics)
            
            os.chdir(modelpath)
            # Save the model
            lda_model.save('LDAREC.'+year[0])
            top_words_per_topic = []
            for jj in range(num_topics):
                top_words_per_topic.extend([(jj, ) + x for x in lda_model.show_topic(jj, topn = 10)])
            
    
            os.chdir(modelpath)
            pd.DataFrame(top_words_per_topic, columns=['Topic', 'Word', 'P']).to_csv("LDAtopics."+ year[0]+".csv")
            print(str(0))
            continue
        os.chdir(modelpath)
        # Otherwise load the preceding model
        lda_model = gensim.models.ldamodel.LdaModel.load('LDAREC.'+year[ii-1])    
        
        os.chdir(corppath)
        # Find the new corpus to train the model with
        newCorps = pickle.load(open(corpFiles[ii], 'rb'))
        
        # Update model with the new  corpus
        lda_model.update(newCorps)
        
        os.chdir(modelpath)
        # Save model to Dropbox
        lda_model.save('LDAREC.'+year[ii])
        
        top_words_per_topic = []
        for t in range(num_topics):
            top_words_per_topic.extend([(t, ) + x for x in lda_model.show_topic(t, topn = 10)])
            
        os.chdir(modelpath)
        pd.DataFrame(top_words_per_topic, columns=['Topic', 'Word', 'P']).to_csv("LDAtopics."+ year[ii]+".csv")
        print('Finished with model number ' + str(ii+1) + ' of ' + str(len(corpFiles))  + ' for ' + companies[nn])


#######################

     import re
     sorted(cleanVec, key=lambda x: int(x[-1]))
     sorted(cleanVec, key=lambda x: int(re.search(r'(\d+)',x).group()))
    
     cleanVec.sort(key = lambda x: int(x.rsplit('',1)[1]))
     
     a = sorted(a, key=lambda x: float(x))
     
     
########################
     
     
#### FOR POOLED CORPORAS (ANNUAL) ####
"""
######################################################
This loop will recursively update the same LDA model #
######################################################
"""
corpuspath = 'C:\\Users\\Tobias\\Dropbox\\Master\\Annual Reports Pooled\\corpora'
modelpath  = 'C:\\Users\\Tobias\\Dropbox\\Master\\Annual Reports Pooled\\model'
years      = range(2000,2019)
for year in years:
#    comppath = mainpath + companies[nn] 
##    modelpath = comppath + '\\model'
##    corppath  = comppath + '\\corpora'
 #   corpFiles = fnmatch.filter(os.listdir(corppath), 'corpus*')
 ##   dictFiles  = fnmatch.filter(os.listdir(corppath), '*FULL*')
 #   # Quarterly or annually?
#    #year = range(len(corpFiles))
 #   cleanVec = [i.split('corpus.', 1)[1] for i in corpFiles]
#    year     = [i.replace('.txt', '') for i in cleanVec]
    corpFiles = fnmatch.filter(os.listdir(corpuspath), 'corpus.'+str(year)+'*')
    dictFiles = fnmatch.filter(os.listdir(corpuspath), 'dictionary.'+str(year)+'*')
    os.chdir(corpuspath)
    # If we are in the first iteration we must build the initial model
    
    dictionary = gensim.corpora.Dictionary.load(dictFiles[0])
    corpus     = pickle.load(open(corpFiles[0], 'rb'))
    # Build initial LDA-model
    lda_model = gensim.models.ldamodel.LdaModel(corpus   = corpus,
                                         id2word         = dictionary,
                                         num_topics      = num_topics, 
                                         random_state    = random_state,
                                         update_every    = update_every,
                                         chunksize       = chunksize,
                                         passes          = passes,
                                         alpha           = alpha,
                                         per_word_topics = per_word_topics)
    
    os.chdir(modelpath)
    # Save the model
    lda_model.save('LDAREC.'+str(year))
    top_words_per_topic = []
    for jj in range(num_topics):
        top_words_per_topic.extend([(jj, ) + x for x in lda_model.show_topic(jj, topn = 10)])
    

    os.chdir(modelpath)
    pd.DataFrame(top_words_per_topic, columns=['Topic', 'Word', 'P']).to_csv("LDAtopics."+ str(year)+".csv")
    print(str(0))
    print('Finished with year ' + str(year) + ' of ' + str(years[-1])+'.'  )     
#   os.chdir(modelpath)
#   # Otherwise load the preceding model
#   lda_model = gensim.models.ldamodel.LdaModel.load('LDAREC.'+ str(year-1))    
#   
#   os.chdir(corpuspath)
#   # Find the new corpus to train the model with
#   newCorps = pickle.load(open(corpFiles[0], 'rb'))
#   
#   # Update model with the new  corpus
#    lda_model.update(newCorps)
#    
#    os.chdir(modelpath)
#    # Save model to Dropbox
#    lda_model.save('LDAREC.'+str(year))
#    
#    top_words_per_topic = []
#    for t in range(num_topics):
#        top_words_per_topic.extend([(t, ) + x for x in lda_model.show_topic(t, topn = 10)])
#        
#    os.chdir(modelpath)
#    pd.DataFrame(top_words_per_topic, columns=['Topic', 'Word', 'P']).to_csv("LDAtopics." + str(year) +".csv")
#   
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
    
    