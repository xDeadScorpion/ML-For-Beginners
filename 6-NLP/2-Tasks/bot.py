from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
# import and create a Conll extractor to use later 
extractor = ConllExtractor()

if __name__ == "__main__":
    initial_message = ['Hello, I am Marvin, the simple robot.'
                       'You can end this conversation at any time by typing \'bye\'',
                       'After typing each answer, press \'enter\'',
                       'How are you today?']
    for m in initial_message:
        print(m)

    while True:
        user_input = input("> ")
        if user_input.lower() == 'bye':
            break
        else:
            # later when you need a noun phrase extractor:
            user_input_blob = TextBlob(user_input, np_extractor=extractor)  # note non-default extractor specified
            np = user_input_blob.noun_phrases

            if user_input_blob.polarity <= -0.5:
                response = "Oh dear, that sounds bad."
            elif user_input_blob.polarity <= 0:
                response = "Hmm, that's not great."
            elif user_input_blob.polarity <= 0.5:
                response = "Well, that sounds positive."
            elif user_input_blob.polarity <= 1:
                response = "Wow, that sounds great."

            ask_start = 'Can you tell me more'
            ask_connector = 'about'

            try:
                print(f'{response} {ask_start} {ask_connector} {user_input_blob.noun_phrases[-1]}?')
            except IndexError:
                print(f'{response} {ask_start}?')


    print('It was nice talking to you, goodbye!')