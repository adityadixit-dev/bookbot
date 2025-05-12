def num_words_in_text(text):
    return len(text.split())


def char_frequency_in_text(text: str):
    text = text.lower()
    char_freq_dict = {}
    for c in text:
        if c not in char_freq_dict:
            char_freq_dict[c] = 0
        char_freq_dict[c] += 1

    return char_freq_dict


def freq_dict_to_sorted_list(char_freq_dict):
    list_from_dict = [{"char": k, "num": val} for k, val in char_freq_dict.items()]
    # print(list_from_dict)
    list_from_dict.sort(
        reverse=True,
        key=lambda x: x["num"],
    )
    return list_from_dict
