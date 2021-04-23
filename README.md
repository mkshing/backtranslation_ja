# Backtranslation_ja
Transformers-based Backtranslation for Japanese via English.

Backtranslation is a powerful data augmentation method. 
In fact, many successful Kagglers apply it. 

Here is an easy-to-use backtranslation package for Japanese.

## Installation
```
https://github.com/mkshing/backtranslation_ja.git
pip install -r requirements.txt
```

## Usage
```
from backtranslation_ja import BackTranslation_ja

# Initialize
bt_ja = BackTranslation_ja()

texts = ["今日は何の日？"]
bt_ja.backtranslate(texts)
>>['どんな日だ?']
```


## Reference
- This is a python implementation of the algorithm as mentioned in paper [Automatic keyword extraction from individual documents by Stuart Rose, Dave Engel, Nick Cramer and Wendy Cowley](https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents)
- [rake-nltk](https://github.com/csurfer/rake-nltk)

