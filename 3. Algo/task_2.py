import random
from itertools import *

def is_anagram_method1(s1,s2):
    count = 0
    len_s1 = len(s1)
    for i in s1:
        for j in s2:
            if i == j:
                count+=1
                if len_s1 == count:
                    return True
                else:
                    return False
def is_anagram_method2(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
def is_anagram_method3(s1,s2):
    if len(s1) <= 7:
        for i in s1:
            if permutations(s1, repeat = len(s2)) == s2:
                return True
            else:
                return False
def is_anagram_method4(s1,s2):
    words_1 = {}
    words_2 = {}
    for i in s1:
        if i in words_1:
            words[i] += 1
        else:
            words_1[i] = 1
    for i in s2:
        if i in words_2:
            words_2[i] += 1
        else:
            words_2[i] = 1
    if sorted(words_1) == sorted(words_2):
        return True
    else:
        return False

def find_anagrams_for_random_word(method_func):
    dictionary = open("words.txt")
    word = random.choice(dictionary)
    print(f"Исходное слово: {word}")

    anagrams = []
    for candidate in dictionary:
        if candidate != word and method_func(word, candidate):
            anagrams.append(candidate)

    print(f"Найдено анаграмм: {len(anagrams)}")
    print("Примеры:", anagrams[:10])
    return anagrams
find_anagrams_for_random_word(is_anagram_method1)
find_anagrams_for_random_word(is_anagram_method2)
find_anagrams_for_random_word(is_anagram_method3)
find_anagrams_for_random_word(is_anagram_method4)
