print("Welcome to my Programming Quiz!")

playing = input("Do you want to play? ")

if playing not in ["yes", "y"]:
    quit()

print("Okay! Let's begin! :)")
score = 0

def ask_question(question, correct_answer, score):
    answer = input(question)
    if answer.lower() == correct_answer.lower():
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    return score

# Initialize the score
score = 0

# Define questions and answers
questions_and_answers = [
    ("What is the primary programming language used for Android app development? ", "java"),
    ("Which component of an Android application is responsible for managing the app's user interface? ", "activity"),
    ("What is the file extension for Android application packages? ", ".apk"),
    ("Which of the following is used to store persistent data in an Android application? ", "sharedPreferences")
]

# Ask each question and update the score
for question, correct_answer in questions_and_answers:
    score = ask_question(question, correct_answer, score)

print(f"Your final score is: {score}")
