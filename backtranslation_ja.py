from transformers import MarianMTModel, MarianTokenizer
import torch

model_path_2en = "Helsinki-NLP/opus-mt-ja-en"
model_name_2ja = 'Helsinki-NLP/opus-mt-en-mul'

class BackTranslation_ja:

    def __init__(
        self,
        en_id="en",
        ja_id="jpn",
    ):
        # Japanese to English
        self.tokenizer_2en = MarianTokenizer.from_pretrained(model_path_2en)
        self.model_2en = MarianMTModel.from_pretrained(model_path_2en)
        # English to Japanese
        self.tokenizer_2ja = MarianTokenizer.from_pretrained(model_name_2ja)
        self.model_2ja = MarianMTModel.from_pretrained(model_name_2ja)
        
        self.en_id = en_id
        self.ja_id = ja_id
    
    def translate(self, texts, model, tokenizer, language="en"):
        # Prepare the text data into appropriate format for the model
        template = lambda text: f"{text}" if language == "en" else f">>{language}<< {text}"
        src_texts = [template(text) for text in texts]
        
        # Tokenize the texts
        encoded = tokenizer.prepare_seq2seq_batch(src_texts, return_tensors='pt')

        # Generate translation using model
        translated = model.generate(**encoded)

        # Convert the generated tokens indices back into text
        translated_texts = tokenizer.batch_decode(translated, skip_special_tokens=True)

        return translated_texts
    
    def backtranslate(self, texts):
        # To English
        english_texts = self.translate(texts, self.model_2en, self.tokenizer_2en, language=self.en_id)
        
        # To Japanese
        return self.translate(english_texts, self.model_2ja, self.tokenizer_2ja, language=self.ja_id)