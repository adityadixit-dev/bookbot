from stats import char_frequence_in_text, num_words_in_text


def main():
    book_file_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_file_path)
    # print(book_text)
    num_words_in_book = num_words_in_text(book_text)
    print(f"{num_words_in_book} words found in the document")
    char_freq_dict = char_frequence_in_text(book_text)
    print(char_freq_dict)


def get_book_text(book_filepath):
    with open(book_filepath) as book:
        book_text = book.read()
    return book_text


if __name__ == "__main__":
    main()
