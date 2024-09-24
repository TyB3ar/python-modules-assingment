# lists for matching word to define mood type: 
good_words = ['happy', 'awesome', 'acceptable', 'excellent', 'exceptional', 'favorable', 'great', 'marvelous', 'superb', 'wonderful', 'super']
bad_words = ['awful', 'dreadful', 'bad', 'terrible', 'lousy', 'poor', 'mediocre']
neutral_words = ['ok', 'okay', 'alright', 'fine', 'calm', 'nonchalant', 'whatever', 'chill']
sad_words = ['sad', 'depressed', 'heartbroken', 'mournful', 'somber', 'hurting', 'unhappy', 'down', 'cheerless']
excited_words = ['excited', 'eager', 'enthusiatic', 'delighted', 'thrilled', 'nervous', 'stimulated', 'moved', 'wired', 'stoked']  


def mood_type(mood):
    try:
        if mood.lower() in good_words: # if mood is 'good' 
            print("Great to hear! It always feels good to be in a good mood!")
        elif mood.lower() in bad_words: # if mood is 'bad' 
            print("Sorry to hear that! We all have bad days, but that just means it will only get better!")
        elif mood.lower() in neutral_words: # if mood is 'neutral' 
            print("Very chill, everything is at peace.")
        elif mood.lower() in sad_words: # if mood is 'sad' 
            print("It's human to feel that way, and it's also perfectly fine. There's only a better place to go to from here.") 
        elif mood.lower() in excited_words: # if mood is 'excited' 
            print("Woah! Whatever is making you feel this way has to be big! Don't let the opportunity slip by you!")
        else: # if mood is anything other than words in lists 
            print("Emotions are part of what make all of us human, so it's great that you're feeling something!")
    except Exception as e:
        print(f"Error: {e}")  
 