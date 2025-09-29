import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
input_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return(file_contents)

#from stats import count_words
#from stats import count_chars

def count_words(text):
    split = text.split()
    count = len(split)
    return count

def count_chars(text):
    lower_string = text.lower()
    freq = {}
    for c in lower_string:
        if c in freq:
            freq[c] += 1 
        else:
            freq[c] = 1
    return freq

def chars_to_sorted_list(freq):
    char_list = []
    for ch, in_list_count in freq.items():
        if ch.isalpha():
            char_list.append({"char": ch, "num": in_list_count})

    def sort_key(item):
        return item["num"]

    char_list.sort(key=sort_key, reverse=True)

    return char_list

def main():
    file_path = str(input_path)
    text = get_book_text(file_path)
    count = count_words(text)
    freq = count_chars(text)
    char_list = chars_to_sorted_list(freq)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for character in char_list:
        print(f"{character['char']}: {character['num']}")
    print("============= END ===============")
main()
