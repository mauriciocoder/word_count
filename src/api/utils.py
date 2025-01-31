import re

def word_count(sentence: str) -> int:
    if not isinstance(sentence, str):
        raise ValueError("sentence must be a string")
    return len(re.findall(r'\b[\w\'-]+\b', sentence))