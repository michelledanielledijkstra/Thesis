# A multilingual Temporal Convolutional Network for Speaker Change Detection on Movie and Series Scripts Data

All the code is in Google Colab, instead of the translator.py. This file contains information about files and folders.

Structure, folders are in bold:
- **Other**
  - translator.py _In this file, the numbers were changed on every run (and not kept)_
  - ds2translator.py _In this file, the numbers were changed on every run (and not kept)_
- **Code**
  - EDA OpenSubtitles.ipynb
  - OpenSubtitles Data Anlysis and Cleaning.ipynb
  - CreateBERTS and data split.ipynb
  - Model selection TCNs.ipynb
  - Test_TCNs.ipynb
  - **EXTRA DATASET**
  - **DATA** (Not sure if this is allowed to be included or send per e-mail or something but structure;)
    - WTranslationsOpenSubtitles.pkl _Dictionairy of all dataframes of OpenSubtitles data with translations_
    - WTranslationsConcatOS.pkl _Concatenated dataframe of all dataframes of OpenSubtitles data with translations_    
    - **sentences**
      - 7467 sentence (script sentences) and speaker files (speaker tags)
    - **translations**
      - All translations on OpenSubtitles data (original frames, with an extra column with sentences translated from English to Dutch)
      - **DS2andDS3 translations**
        - All translations on The Cornell (DS2) and Friends (DS3) Corpus (original frames, with an extra column with sentences translated from English to Dutch)    
  
