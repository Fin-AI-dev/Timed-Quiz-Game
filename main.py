import random
import time

def split_file(file_name):
  text = open(file_name)
  line = text.read()
  result = line.split("\n")
  return result

qa = split_file(file_name="SmarterThana5thGrader.csv")

def split_question(y):
  find_comma = y[::-1].find(",")
  comma_position = len(y)-find_comma -1
  return y[0:comma_position], y[comma_position +1:]

def multiple_choice(question):
  if "Which" or "which" in question:
    return True
  else:
    return False

def randomiser(qa):
  random_qa = random.choice(qa)
  question, answer = split_question(random_qa) 
  return question, answer

def asked_questions(question):
  asked_questions = []
  if question in asked_questions:
    return True
  else:
    return False

def respond_correctly_in_time(question, answer, seconds):
  start = time.time()
  print(question)
  print(answer)
  user_response = input("Answer: ").upper()
  joined_response = user_response.replace(" ", "")
  end = time.time()
  joined_answer = answer.replace(" ", "")
  if end - start > seconds and joined_response == joined_answer:
    print("Correct answer, but you failed to answer this questions in time.")
    print()
  elif end - start < seconds and joined_response == joined_answer:
    print("Correct answer, and answered in time. Noice.")
    print()
    return False
  elif end - start < seconds and joined_response != joined_answer:
    print("Well at least you did it in time... wrong answer.")
    print()
  else:
      print("Wrong answer, and you took too long. Ouch.")
      print()

print("====================================\nWELCOME TO THE PUB QUIZ GENERATOR \n------------------------------------ ")

print("You will be presented with 10 questions and will have 10 seconds to give you answer to each question.\n")

for i in range(5, 0, -1):
    time.sleep(1)
    print(i)
print("Go!")
print()

score = 0
rounds = 9
question_number = 1

while rounds >= 0:
  
  print(question_number,".")
  question, answer = randomiser(qa)
  if asked_questions(question) == True:
    question, answer = randomiser(qa)
  if multiple_choice(question) == True:
    question, answer = randomiser(qa)
  rounds -=1
  question_number +=1  
  if respond_correctly_in_time(question, answer, 10) == False:
    score +=1

if score < 3:
  print("Oh dear, that really didn't go to plan did it? You got", score, "questions correct...")
elif score > 8:
  print("My god, you must be one of them there geniuses I hear about. You got", score, "questions correct!")
else:
  print("Not setting the world alight, but not a total disaster. Good going. You got", score, "questions correct.")

print()
print()
print()
