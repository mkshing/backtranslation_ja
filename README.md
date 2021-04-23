# Backtranslation_ja
Transformers-based back translation for Japanese via English.

Back translation is a powerful data augmentation method. 
In fact, many successful Kagglers apply it. 

Here is an easy-to-use back translation package for Japanese.

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
- [Text Data Augmentation with MarianMT](https://amitness.com/back-translation/)
