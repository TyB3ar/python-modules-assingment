# functions for string manipulation of word entered for 'mood' 

def reverse_word(mood): # function to reverse letters of word entered for 'mood' 
    backwards = mood[::-1] 
    print(f"{mood} reversed is {backwards}\n") 

def caps_word(mood): # function to capitalize word for 'mood' 
    cap_word = mood[0].upper() + mood[1:] 
    print(f"{mood} capitalized is {cap_word}\n")

def upper_case(mood): # function to uppercase whole word for 'mood' 
    big_word = mood.upper()
    print(f"{mood} upper case is {big_word}\n") 

def lower_case(mood): # function to lowercase whole word for 'mood' 
    small_word = mood.lower()
    print(f"{mood} lower case is {small_word}\n")

def vowels(mood): # function to extract all vowels from word for 'mood'abs
    vowel = 'aAeEiIoOuU'
    mood_vowels = []
    for letter in mood:
        if letter in vowel:
            mood_vowels.append(letter) 
            
    print(f"Vowels found in {mood}: {mood_vowels}") 