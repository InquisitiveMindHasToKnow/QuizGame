import random

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
        print()
        score += 1
    else:
        print(f"Incorrect! The correct answer is ({correct_answer}).")
        print()

    return score


# Initialize the score
score = 0

# Define questions and answers
questions_and_answers = [

    #Android Questions
    ("What is the primary programming language used for Android app development? \n(a) Java\n(b) Kotlin\n(c) Python\n(d) C++\n", "a"),
    ("Which component of an Android application is responsible for managing the app's user interface? \n(a) Service\n(b) BroadcastReceiver\n(c) Activity\n(d) ContentProvider\n", "c"),
    ("What is the file extension for Android application packages? \n(a) .exe\n(b) .app\n(c) .apk\n(d) .zip\n", "c"),
    ("Which of the following is used to store persistent data in an Android application? \n(a) SQLite Database\n(b) SharedPreferences\n(c) File Storage\n(d) Network Storage\n", "b"),
    ("What is the main file used to define the user interface layout in Android? \n(a) layout.xml\n(b) AndroidManifest.xml\n(c) strings.xml\n(d) styles.xml\n", "a"),
    ("What is the Android component that handles background tasks? \n(a) Activity\n(b) Service\n(c) BroadcastReceiver\n(d) ContentProvider\n", "b"),
    ("Which class is used to start a new activity in Android? \n(a) Activity\n(b) Intent\n(c) Service\n(d) Context\n", "b"),
    ("What is the purpose of the `AndroidManifest.xml` file? \n(a) Define UI layout\n(b) Declare permissions and app components\n(c) Store strings\n(d) Define styles\n", "b"),
    ("Which method is called when an Activity is first created? \n(a) onStart()\n(b) onCreate()\n(c) onResume()\n(d) onPause()\n", "b"),
    ("What is the default layout for an Android application if not specified? \n(a) LinearLayout\n(b) RelativeLayout\n(c) ConstraintLayout\n(d) FrameLayout\n", "d"),
    ("Which class provides access to application-specific resources and classes? \n(a) Application\n(b) Context\n(c) Activity\n(d) Service\n", "b"),
    ("How can an Android app interact with other apps? \n(a) Using Intents\n(b) Using Services\n(c) Using BroadcastReceivers\n(d) Using ContentProviders\n", "a"),
    ("Which lifecycle method is called when an Activity becomes visible to the user? \n(a) onCreate()\n(b) onStart()\n(c) onResume()\n(d) onPause()\n", "b"),
    ("What is an Android Fragment? \n(a) A component for handling background tasks\n(b) A reusable UI component within an Activity\n(c) A class for storing data\n(d) A type of service\n", "b"),
    ("Which tool is used to compile Android applications? \n(a) Android Studio\n(b) Gradle\n(c) ADB\n(d) Android SDK\n", "b"),
    ("What is the purpose of the `proguard-rules.pro` file? \n(a) Define UI layout\n(b) Optimize and obfuscate code\n(c) Declare permissions\n(d) Store app strings\n", "b"),
    ("Which class is used for handling network operations in Android? \n(a) HttpURLConnection\n(b) NetworkManager\n(c) NetworkHandler\n(d) NetworkService\n", "a"),
    ("What is the primary purpose of Android's `BroadcastReceiver`? \n(a) Handle user interactions\n(b) Start background services\n(c) Receive and respond to broadcast messages\n(d) Manage data storage\n", "c"),
    ("Which method in `Activity` is called when an Activity is no longer visible to the user? \n(a) onCreate()\n(b) onStop()\n(c) onPause()\n(d) onDestroy()\n", "b"),
    ("What is the Android class used for accessing system services? \n(a) SystemService\n(b) ServiceManager\n(c) Context\n(d) Application\n", "c")
]

# Randomize the order of questions
random.shuffle(questions_and_answers)

# Ask each question and update the score
for question, correct_answer in questions_and_answers:
    score = ask_question(question, correct_answer, score)

total_questions = len(questions_and_answers)

score_in_percentage = int(score / total_questions) * 100

print(f"Your final score is: {score} out of {total_questions}. That's {score_in_percentage}%!")
