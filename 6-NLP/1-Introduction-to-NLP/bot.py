import random

random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]


if __name__ == "__main__":
    initial_message = ['Hello, I am Marvin, the simple robot.'
                       'You can end this conversation at any time by typing \'bye\'',
                       'After typing each answer, press \'enter\'',
                       'How are you today?']
    for m in initial_message:
        print(m)

    while True:
        user_message = input()
        if user_message == 'bye':
            print('It was nice talking to you, goodbye!')
            break
        else:
            response = random_responses[random.randint(0, len(random_responses)-1)]
            print(response)