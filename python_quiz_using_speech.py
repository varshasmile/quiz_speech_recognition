from gtts import gTTS
import os
import time
import speech_recognition as sr
r = sr.Recognizer()
language = 'en'

sequence = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

QUESTIONS = [
    ("Which built-in function can get information from the user in Python? ", "input"),
    ("Indentation is a special and necessary feature in python. True or False?", "true"),
    ("Lambda is an Anonymous Function in python. True or False?", "true"),
    (" What does pip stand for python?", "preferred installer program"),
    ("Which keyword do you use to loop over a given list of elements?", "for"),
    ("Which collection doesn't include duplicates?", "set"),
    ("In order to store values in terms of key and value we use which data type?", "dictionary"),
    ("Which Exception Handling block will always be executed whether an exception is encountered or not?", "finally"),
    ("'What do you call the Variables that are declared outside a function & can be accessed anywhere in the program?", "global"),
    ("To use a module in another module, you must import it using which keyword?", "import")
]

count = 0
order = 0
correct = " Great! You scored 2 points. "

welcome_txt = '''
    WELCOME TO THE QUIZ on Python created by 'Varsha'!
(This is a quiz that will read the questions to you and you have to give answers by speaking.)
(Please Note That you have to speak CLEARLY only the correct answer when you are asked to and nothing else, THERE SHOULD'NT BE ANY BACKGROUND NOISES either or else it will grab it as wrong answer.)
(There are total 10 questions, 2 marks each.)
    '''
print(welcome_txt)

myobj1 = gTTS(text=welcome_txt, lang=language, slow=False, )
myobj1.save("welcome_quiz.mp3")
os.system("welcome_quiz.mp3")

time.sleep(28)

for question, correct_answer in QUESTIONS:
    ques_announce = f" Here goes your {sequence[order]} Question! "
    print(ques_announce)

    myobj2 = gTTS(text=ques_announce, lang=language, slow=False)
    myobj2.save("ques_announce.mp3")
    os.system("ques_announce.mp3")

    time.sleep(3)

    print(f'''{question}
                WAIT...''')
    myobj3 = gTTS(text=question, lang=language, slow=False)
    myobj3.save("question.mp3")
    os.system("question.mp3")

    time.sleep(8)

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say your answer NOW...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            text = r.recognize_google(audio)
            print("I think you said '" + text + "'.")
            if text == correct_answer:
                print(correct)
                myobj4 = gTTS(text=correct, lang=language, slow=False)
                myobj4.save("correct.mp3")
                os.system("correct.mp3")
                count += 2
                order += 1
            
            else:
                wrong = f"Sorry! Correct Answer is '{correct_answer}'. You scored no points for this question. Try Next."
                print(wrong)
                myobj5 = gTTS(text=wrong, lang=language, slow=False)
                myobj5.save("wrong.mp3")
                os.system("wrong.mp3")
                order += 1

        except sr.RequestError as e:  
            print("error; {0}".format(e))
            print("COULD'NT HEAR ANYTHING!")
            order += 1

        except Exception as e:
            print (e)
            print("COULD'NT HEAR ANYTHING!")
            order += 1

    time.sleep(8)

print("WAIT FOR YOUR FINAL SCORE!")
time.sleep(3)

points_scored = f"The quiz ends here. Your final score is {count} out of 20! Thank You for Playing!"
print(points_scored)
myobj6 = gTTS(text=points_scored, lang=language, slow=False)
myobj6.save("score.mp3")
os.system("score.mp3")

time.sleep(10)
