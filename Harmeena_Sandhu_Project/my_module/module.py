#These are the necessary import statements

import random
from IPython.display import Audio 
from IPython.display import Image



# Below I have a "data base" of sorts
#It will be used when generating the quiz itself, 
#and within helpers that will generate the quiz

player_list = ["Kobe Bryant", "Lebron James", "Kyle Kuzma", "Anthony Davis"]
mp3_list = ["sad1.mp3", "sad2.mp3", "sad3.mp3", "sad4.mp3", "sad5.mp3"]

first_statement = "Type 'yes!' if you are ready!"
second_statement_1 = "\nGreat! The player you will be quizzed on is "
second_statement_2 = "OOPS! Looks like you are not ready for a quiz!"
third_statement_1 = "Type 'Let's do this!' to proceed with the quiz!"
third_statement_2 = "Awee, I guess you need to study up then! "

quiz_questions = ["\nI play on the Lakers.\n\na) True\nb) False", 
                  "\nWhat number do I wear?\n\na) 0\nb) 24\nc) 23\nd) 3",
                  "\nWhat city did I grow up in?\n\na) Flint\nb) Philadelphia\nc) Chicago\nd) Akron",
                  "\nI play(ed) Center and sometimes Power Forward.\n\na) True\nb) False",
                  "\nHow much do/did I wiegh as a player (in pounds) ?\n\na) 254\nb) 212\nc) 250\nd) 221"]


winning_remarks = ["Great! You know a LITTLE something... on to the next!", 
                  "So you know a bit! Let's see how much more!",
                  "Not bad! You are on a roll!", 
                  "AYYYYEEEE!! You're killin it!",
                  "Nice one! You know me inside and out!"]

losing_remarks = ["AHHH! You know NOTHING about me!", 
                  "You only know a little bit, sorry :(",
                  "You did't get TOO far, but you know me on the court!",
                  "AHH! You slipped up a little but you still know a lot about me",
                  "You came so close! Impressive but you don't know me all the way!"]

#Below are dictionaries that match the correct answer to the question 
#depending on which player was randomly chosen to base the quiz off of

questions_Kobe = {quiz_questions[0] : 'a',
                  quiz_questions[1] : 'b',
                  quiz_questions[2] : 'b',
                  quiz_questions[3] : 'b',
                  quiz_questions[4] : 'b'}
                  
questions_Lebron = {quiz_questions[0] : 'a',
                    quiz_questions[1] : 'c',
                    quiz_questions[2] : 'd',
                    quiz_questions[3] : 'b',
                    quiz_questions[4] : 'c'}

questions_Kyle = {quiz_questions[0] : 'a',
                  quiz_questions[1] : 'a',
                  quiz_questions[2] : 'a',
                  quiz_questions[3] : 'a',
                  quiz_questions[4] : 'd'}

questions_Anthony = {quiz_questions[0] : 'a',
                     quiz_questions[1] : 'd',
                     quiz_questions[2] : 'c',
                     quiz_questions[3] : 'a',
                     quiz_questions[4] : 'a'}


#The below function acts to randomly 
#select the player (out of four possible choices) that the quiz will be based on

def random_player(lst):
    ans = random.choice(lst)
    return(ans)

#The below function generates the appropriate question /answer pairings
#based on which player was randomly selected, using the above dictionaries

def create_questions(player):
    if player == "Kobe Bryant":
        answer_key = questions_Kobe
    elif player == "Lebron James":
        answer_key = questions_Lebron
    elif player == "Kyle Kuzma":
        answer_key = questions_Kyle
    else:
        answer_key = questions_Anthony
    return(answer_key)

#below is a function that generates the image of the player that the 
#quiz was based on at the end of the quiz
#The player will only show if the quiz taker misses a question 

def generate_image(player):

    if player == "Kobe Bryant":
        image = Image(filename = "kobe.png")
    elif player == "Lebron James":
        image = Image(filename ="lebron.png")
    elif player == "Kyle Kuzma":
        image = Image(filename ="kyle.png")
    else:
        image = Image(filename ="ad.png")
    return(image)

#this function is used when the person taking the quiz
#indicates that they are not following instructions / they
#are not ready to start. It will play an audio recording from a list
#above with words of encouragement 

def select_random_encouragement(audio):
    for sound in audio:
        ans = random.choice(audio)
        return (Audio(ans, autoplay = True))

#below is the quiz itself

def the_quiz():
    #the below line randomly selects a player from
    #the player list that the participant will be
    #quizzed on
   
    player = random_player(player_list)
    
    #here I am setting up the quiz for the participant
    #hopefully to increase user experience
    
    ans = input(first_statement)
    
    if ans == "yes!":
        print(second_statement_1 + player)
    else:
        print(second_statement_2)
        return(select_random_encouragement(mp3_list))
    
    #Since the above player hase been selected, and the 
    #participant is ready, I am generating the correct 
    #answer key pertinant to the player selected
    
    proper_quiz = create_questions(player)
        
    ans2 = input(third_statement_1)
    
    #Now, the quiz is officially starting / beign displayed
    
    if ans2 == "Let's do this!":
        
        for i in range(len(quiz_questions)):
            i += 1
            answer = input(quiz_questions[i-1])
            if answer == proper_quiz[quiz_questions[i-1]]:
                print(winning_remarks[i-1])
                   
            else:
                print(losing_remarks[i-1])
                return(generate_image(player))
    else:
        return(select_random_encouragement(mp3_list))
