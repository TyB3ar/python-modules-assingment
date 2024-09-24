

import mood_responses
import text_utils 

def main(): 
    try:
        while True:
            mood = input("In one word, how are you feeling today?") 
            
            if mood.isalpha() == False:  #  if input is non-alphabetical 
                print("Sorry, but I was expecting a single word.")  
            else: 
                mood_responses.mood_type(mood) 
                break       
        
        while True:   
            print("How would you like to edit your mood word?\n1. Reverse Word\n2. Captialize Word\n3. Uppercase Word\n4. Lowercase Word\n5. Extract Vowels from Word\n6. Exit") 
            edit_word = input("Please enter the number of the option you wish to choose: ") 
            
            if edit_word.isdigit() == False: # if user enters anything other than a number
                print("Sorry, but that is not an option to choose from.\n")
            elif edit_word == '1':
                text_utils.reverse_word(mood) 
            elif edit_word == '2':
                text_utils.caps_word(mood) 
            elif edit_word == '3':
                text_utils.upper_case(mood) 
            elif edit_word == '4': 
                text_utils.lower_case(mood) 
            elif edit_word == '5':
                text_utils.vowels(mood)  
            elif edit_word == '6':
                break
            else:
                print("Sorry, but that is not an option to choose from.\n")
    except Exception as e:
        print(f"Error: {e}") 
        

if __name__ == '__main__':
    main()
    