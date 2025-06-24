from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("ml6team/keyphrase-extraction-distilbert-inspec")
model = AutoModelForTokenClassification.from_pretrained("ml6team/keyphrase-extraction-distilbert-inspec")

def extract_keyphrases(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probs = torch.nn.functional.softmax(logits, dim=-1)[0]
    tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])

    keyphrases = []
    current_phrase = []

    for i, (token, prob) in enumerate(zip(tokens, probs)):
        if token.startswith("##"):
            if current_phrase:
                current_phrase[-1] += token[2:]
        elif prob[1] > 0.5:
            current_phrase.append(token)
        else:
            if current_phrase:
                keyphrases.append(" ".join(current_phrase))
                current_phrase = []

    if current_phrase:
        keyphrases.append(" ".join(current_phrase))

    return list(set([kp.replace(" ##", "") for kp in keyphrases]))
