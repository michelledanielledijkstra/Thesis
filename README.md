# A multilingual Temporal Convolutional Network for Speaker Change Detection on Movie and Series Scripts Data

All the code is in Google Colab, instead of the translator.py. This file contains information about files and folders.
Files that include analysis, can have commented print statements in there. To see the output, uncomment these.

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
    - Data Loading and Cleaning Cornell Corpus.ipynb
    - processedDS2sparks.pkl _Dictionary of Cornell Corpus movie frames processed with Spark_
    - processedDS2concattedframe.pkl _Concatenated frame of alle separate Cornell Corpus frames_
    - EDA DS2 Cornell Corpus.ipynb
    - Data Cleaning and Loading Friends Corpus.ipynb
    - friendssparks.pkl _Dictionary of Friends episode frames processed with Spark_
    - friendsconcattedframe _Concatenated frame of alle separate Friends frames_
    - EDA DS3 Friends.ipynb
    - **movie-corpus**
      - utterances.json _Contains movie data_
      - index.json _Not used_
      - speakers.json
      - conversations.json _Not used_
      - corpus.json _Containts movie titles, used to link to frames_  
  - **DATA** (Not sure if this is allowed to be included or send per e-mail or something but structure;)
    - WTranslationsOpenSubtitles.pkl _Dictionairy of all dataframes of OpenSubtitles data with translations_
    - WTranslationsConcatOS.pkl _Concatenated dataframe of all dataframes of OpenSubtitles data with translations_
    - newdfs.pkl _OpenSubtitles dictionairy of dataframes_
    - sparks_dfs.pkl _OpenSubtitles dictionairy of dataframes processed with Spark_
    - concattedframe.pkl _OpenSubtitles concattenated from of all frames_
    - WTLOpenSubtitlesTrainingSet.pkl
    - WTLOpenSubtitlesValidationSet.pkl
    - WTLOpenSubtitlesTestSet.pkl
    - YSWTLOpenSubtitlesTrainingSet.pkl _List of train, validation and test labels_
    - WTLOpenSubtitlesTrainEmbeddings.pkl _On English sentences_
    - WTLOpenSubtitlesValidEmbeddings.pkl _On English sentences_
    - DutchWTLOpenSubtitlesTrainEmbeddings.pkl
    - DutchWTLOpenSubtitlesValidEmbeddings.pkl
    - EDembeddingsTrainValid.pkl _Training and validation set of matrix multiplication on English and Dutch BERT sentence embeddings_
    - 4dilationsTCN.keras _Saved Keras model, including all training weights, good for reuse - trained on English OpenSubtitles data_
    - EDosTCN.keras _Saved Keras model, including all training weights, good for reuse - trained on English-Dutch (matrix multiplication) OpenSubtitles data_
    - **sentences**
      - 7467 sentence (script sentences) and speaker files (speaker tags)
    - **translations**
      - All translations on OpenSubtitles data (original frames, with an extra column with sentences translated from English to Dutch)
      - **DS2andDS3 translations**
        - All translations on The Cornell (DS2) and Friends (DS3) Corpus (original frames, with an extra column with sentences translated from English to Dutch)    
  
