# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    word = input('input word: ')
    anagram = input('input anagram: ')

    sorted_word1 = sorted(word)
    sorted_word2 = sorted(anagram)

    if sorted_word1 == sorted_word2:
        return True
    else:
        return False


print(find_anagram('word', 'anagram'))
