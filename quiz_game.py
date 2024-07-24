print("Welcome to my Programming Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's begin! :)")
score = 0

answer = input("What is the primary programming language used for Android app development? ")
if answer.lower() == "java":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which component of an Android application is responsible for managing the app's user interface? ")
if answer.lower() == "activity":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the file extension for Android application packages? ")
if answer.lower() == ".apk":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which of the following is used to store persistent data in an Android application? ")
if answer.lower() == "sharedPreferences":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")