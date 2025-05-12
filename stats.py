def num_words_in_text(text):
    return len(text.split())


def char_frequence_in_text(text: str):
    text = text.lower()
    char_freq_dict = {}
    for c in text:
        if c not in char_freq_dict:
            char_freq_dict[c] = 0
        char_freq_dict[c] += 1

    return char_freq_dict
