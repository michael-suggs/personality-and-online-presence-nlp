from typing import List, Tuple
import nltk


def clean_and_tokenize(text: str) -> Tuple[List[str], List[str]]:
    text_out = nltk.Text(nltk.wordpunct_tokenize(text))
    words = [w.lower() for w in text_out]
    return words, sorted(set(words))
