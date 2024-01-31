import pickle
import pandas as pd
from deep_translator import GoogleTranslator
import time

# Load in previous dictionairy of dataframes, that need to be converterd to spark dataframes
with open('sparks_dfs.pkl', 'rb') as fp:
    pdfs = pickle.load(fp)

keys = list(pdfs.keys())
df = pdfs[keys[0]]
print('len file',len(pdfs))
start_time = time.time()

translations = {}

i=-1

print(len(pdfs))
for key in keys[2700:2720]:
  df = pdfs[key]
  i+=1
  print(i,len(df))
  sens = df.Sentence.tolist()
  df['NL translation'] = GoogleTranslator(source='auto',target='nl').translate_batch(sens)
  
  translations[key] = df

with open('NewOldDlocaltranslations37.pkl','wb') as fp:
  pickle.dump(translations,fp)
  print('dictionairy succesful saves to file!')

print("--- %s minutes ---" % (float(time.time() - start_time)/60))

print(translations[key])
print('Length?',len(translations))


