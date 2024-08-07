from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, src_lang="en", tgt_lang="de"):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    
    # Load the translation model and tokenizer
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    translator = MarianMTModel.from_pretrained(model_name)
    
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    translated = translator.generate(**tokens)
    translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    
    return translated_text[0]
