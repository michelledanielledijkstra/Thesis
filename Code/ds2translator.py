import pickle
import pandas as pd
from deep_translator import GoogleTranslator
import time

# Load in previous dictionairy of dataframes, that need to be converterd to spark dataframes
with open('processedDS2sparks.pkl', 'rb') as fp:
    pdfs = pickle.load(fp)

keys = list(pdfs.keys())
df = pdfs[keys[0]]
print('len file',len(pdfs))
start_time = time.time()

translations = {}

i=-1
for key in keys:
  df = pdfs[key]
  i+=1
  print(i,len(df))
  sens = df.text.tolist()
  df['NL translation'] = GoogleTranslator(source='auto',target='nl').translate_batch(sens)
  
  translations[key] = df


with open('DS2lllocaltranslations28.pkl','wb') as fp:
  pickle.dump(translations,fp)
  print('dictionairy succesful saves to file!')

print("--- %s minutes ---" % (float(time.time() - start_time)/60))

print('Length?',len(translations))




