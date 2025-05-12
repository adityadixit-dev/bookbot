import sys

from stats import char_frequency_in_text, freq_dict_to_sorted_list, num_words_in_text


def main():
    # book_file_path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file_path = sys.argv[1]

    book_text = get_book_text(book_file_path)
    # print(book_text)
    num_words_in_book = num_words_in_text(book_text)
    # print(f"{num_words_in_book} words found in the document")
    char_freq_dict = char_frequency_in_text(book_text)
    # print(char_freq_dict)
    sorted_char_list = freq_dict_to_sorted_list(char_freq_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words_in_book} total words")
    print("--------- Character Count -------")
    for char_data in sorted_char_list:
        if char_data["char"].isalpha():
            print(f"{char_data['char']}: {char_data['num']}")
    print("============= END ===============")


def get_book_text(book_filepath):
    with open(book_filepath) as book:
        book_text = book.read()
    return book_text


if __name__ == "__main__":
    main()
