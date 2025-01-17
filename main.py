def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    character_dict = {}
    words = len(file_contents.split())
    for c in file_contents.lower():
        if c in alphabet:
            if c in character_dict:
                character_dict[c] += 1
            else:
                character_dict[c] = 1
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for letter in character_dict:
        print(f"The '{letter}' character was found {character_dict[letter]} times")
    print("--- End report ---")
    


main()