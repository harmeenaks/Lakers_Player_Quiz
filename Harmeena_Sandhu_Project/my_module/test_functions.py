#These are the necessary import statements

import random
from IPython.display import Audio 
from IPython.display import Image

import module as mod

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



##Testing 
def test_random_player():
    assert callable(mod.random_player)
    assert mod.random_player(player_list) == "Kobe Bryant"or "Lebron James" or "Kyle Kuzma" or"Anthony Davis"
    
def test_create_questions():
    assert callable(mod.create_questions)
    assert mod.create_questions("Kobe Bryant") == questions_Kobe
    assert mod.create_questions("Lebron James") == questions_Lebron
    assert mod.create_questions("Anthony Davis") == questions_Anthony
    assert mod.create_questions("Kyle Kuzma") == questions_Kyle

#these last three tests are only being tested on whether or not they are callable
#beacuse they were tested to work in terms of what they should output within the 
#quiz itself. 

def test_generate_image():
    assert callable(mod.generate_image)

def test_select_random_encouragement():
    assert callable(mod.select_random_encouragement)

    
def test_the_quiz():
    assert callable(mod.the_quiz)

    