import random

print("Welcome to my Programming Quiz!")

playing = input("Do you want to play? ")

if playing not in ["yes", "y"]:
    quit()

print("Okay! Let's begin! :)")

def ask_question(question, correct_answer, score):
    answer = input(question).strip().lower()
    if answer == correct_answer:
        print('Correct!')
        score += 1
    else:
        print(f"Incorrect! The correct answer is ({correct_answer}).")
    return score

def play_quiz():
    questions_and_answers = [
    #Android Questio
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
    ("What is the Android class used for accessing system services? \n(a) SystemService\n(b) ServiceManager\n(c) Context\n(d) Application\n", "c"),
    ("Which method is used to inflate a layout in an Activity? \n(a) onCreate()\n(b) onStart()\n(c) setContentView()\n(d) onResume()\n", "c"),
    ("Which file contains the definitions for an Android app's permissions? \n(a) MainActivity.java\n(b) build.gradle\n(c) AndroidManifest.xml\n(d) res/values/strings.xml\n", "c"),
    ("What is the minimum Android API level required to use Jetpack Compose? \n(a) 16\n(b) 21\n(c) 23\n(d) 30\n", "b"),
    ("Which component is used to handle navigation between different screens in an Android app? \n(a) ViewModel\n(b) LiveData\n(c) Navigation Component\n(d) RecyclerView\n", "c"),
    ("What is the purpose of the `R.java` file in Android? \n(a) Define UI layouts\n(b) Store resource IDs\n(c) Declare app permissions\n(d) Handle network operations\n", "b"),
    ("Which method is used to register a BroadcastReceiver in an Android app? \n(a) onReceive()\n(b) registerReceiver()\n(c) sendBroadcast()\n(d) unregisterReceiver()\n", "b"),
    ("What is the primary function of the `gradle.properties` file? \n(a) Define build configurations\n(b) Store application resources\n(c) Declare app permissions\n(d) Manage layout files\n", "a"),
    ("Which component in Android Jetpack is responsible for managing UI-related data in a lifecycle-conscious way? \n(a) LiveData\n(b) ViewModel\n(c) Room\n(d) DataBinding\n", "b"),
    ("Which tool is used to interact with an Android device from the command line? \n(a) Gradle\n(b) ADB\n(c) SDK Manager\n(d) JDK\n", "b"),
    ("Which Android component provides the architecture to share data between apps? \n(a) Activity\n(b) ContentProvider\n(c) BroadcastReceiver\n(d) Service\n", "b"),
    ("Which UI component is used to display a list of scrollable items in Android? \n(a) ListView\n(b) RecyclerView\n(c) ScrollView\n(d) GridView\n", "b"),
    ("Which attribute is used to specify the orientation of a LinearLayout? \n(a) layout_orientation\n(b) android:orientation\n(c) android:layout_direction\n(d) layout_direction\n", "b"),
    ("What is the purpose of `ProGuard` in an Android project? \n(a) Enhance UI performance\n(b) Obfuscate code and reduce APK size\n(c) Manage application resources\n(d) Handle network operations\n", "b"),
    ("Which method is used to start an Activity for a result? \n(a) startActivity()\n(b) startActivityForResult()\n(c) startIntentSender()\n(d) startActivityFromFragment()\n", "b"),
    ("Which class in Android is used to handle touch events on the screen? \n(a) GestureDetector\n(b) MotionEvent\n(c) ViewGroup\n(d) TouchHandler\n", "a"),
    ("Which Android component is designed to handle background work that needs to be completed even if the app is not running? \n(a) Service\n(b) BroadcastReceiver\n(c) JobScheduler\n(d) WorkManager\n", "d"),
    ("What is the purpose of `LiveData` in Android Architecture Components? \n(a) Store UI-related data\n(b) Handle background tasks\n(c) Observe data changes\n(d) Manage network operations\n", "c"),
    ("Which layout allows you to position child views in relation to each other or the parent container? \n(a) LinearLayout\n(b) RelativeLayout\n(c) ConstraintLayout\n(d) FrameLayout\n", "b"),
    ("Which class do you use to create a custom View in Android? \n(a) ViewGroup\n(b) View\n(c) ViewParent\n(d) ViewTreeObserver\n", "b"),
    
    #Python Questions
    ("What is the output of the following code: print(2 ** 3)? \n(a) 6\n(b) 8\n(c) 9\n(d) 11\n", "b"),
    ("Which of the following data types is not immutable in Python? \n(a) tuple\n(b) list\n(c) string\n(d) frozenset\n", "b"),
    ("What is the correct way to create a dictionary in Python? \n(a) dict = {}\n(b) dict = []\n(c) dict = ()\n(d) dict = ||\n", "a"),
    ("Which method is used to add an element to the end of a list in Python? \n(a) append()\n(b) add()\n(c) insert()\n(d) extend()\n", "a"),
    ("What does the `len()` function do in Python? \n(a) Returns the length of an object\n(b) Returns the maximum value\n(c) Returns the minimum value\n(d) Returns the sum of values\n", "a"),
    ("Which of the following is used to create an alias for a module in Python? \n(a) alias\n(b) as\n(c) with\n(d) from\n", "b"),
    ("What will be the output of `print('Hello World'[-1])`? \n(a) H\n(b) d\n(c) o\n(d) W\n", "b"),
    ("Which keyword is used for function declaration in Python? \n(a) func\n(b) def\n(c) function\n(d) lambda\n", "b"),
    ("How do you start a comment in Python? \n(a) //\n(b) /*\n(c) #\n(d) <!--\n", "c"),
    ("What is the output of `type([])` in Python? \n(a) <class 'tuple'>\n(b) <class 'list'>\n(c) <class 'dict'>\n(d) <class 'set'>\n", "b"),
    ("Which method is used to convert a string to lowercase in Python? \n(a) lower()\n(b) tolower()\n(c) downcase()\n(d) strlower()\n", "a"),
    ("How do you insert comments in Python code? \n(a) /* ... */\n(b) <!-- ... -->\n(c) # ...\n(d) { ... }\n", "c"),
    ("Which function can be used to execute a string containing Python code? \n(a) eval()\n(b) exec()\n(c) compile()\n(d) run()\n", "b"),
    ("What is the output of `bool([])` in Python? \n(a) True\n(b) False\n(c) None\n(d) Error\n", "b"),
    ("Which of the following is a correct way to create a set in Python? \n(a) set = {}\n(b) set = []\n(c) set = ()\n(d) set = set()\n", "d"),
    ("What will be the output of `print(5 / 2)` in Python 3? \n(a) 2\n(b) 2.5\n(c) 3\n(d) 2.0\n", "b"),
    ("Which operator is used for string concatenation in Python? \n(a) &\n(b) +\n(c) *\n(d) $\n", "b"),
    ("What is the correct file extension for Python files? \n(a) .pyth\n(b) .py\n(c) .pt\n(d) .p\n", "b"),
    ("How do you create a variable with the numeric value 5 in Python? \n(a) x = int(5)\n(b) x = 5\n(c) Both a and b\n(d) None of the above\n", "c"),
    ("Which keyword is used to check if a value is present in a list, tuple, etc.? \n(a) exists\n(b) present\n(c) in\n(d) includes\n", "c"),
    ("What is the output of `print(2 * 3 ** 2)`? \n(a) 36\n(b) 18\n(c) 12\n(d) 10\n", "b"),
    ("Which method is used to remove whitespace characters from the beginning and end of a string? \n(a) strip()\n(b) lstrip()\n(c) rstrip()\n(d) removewhite()\n", "a"),
    ("How do you create a function in Python? \n(a) def myFunction():\n(b) function myFunction():\n(c) create myFunction():\n(d) func myFunction():\n", "a"),
    ("What is the correct syntax to return the first character in a string? \n(a) x = sub('Hello', 0, 1)\n(b) x = 'Hello'[0]\n(c) x = 'Hello'.sub(0, 1)\n(d) x = substring('Hello', 0, 1)\n", "b"),
    ("Which statement is used to stop a loop in Python? \n(a) exit\n(b) stop\n(c) break\n(d) return\n", "c"),
    ("How do you start writing an if statement in Python? \n(a) if x > y then:\n(b) if x > y:\n(c) if (x > y)\n(d) if x > y {}\n", "b"),
    ("What is the output of `print(type({}))`? \n(a) <class 'list'>\n(b) <class 'set'>\n(c) <class 'dict'>\n(d) <class 'tuple'>\n", "c"),
    ("What is the output of `print(10 // 3)` in Python 3? \n(a) 3\n(b) 3.33\n(c) 4\n(d) 4.0\n", "a"),
    ("Which function is used to convert an integer to a string in Python? \n(a) str()\n(b) int()\n(c) float()\n(d) chr()\n", "a"),
    ("Which keyword is used to create a class in Python? \n(a) class\n(b) struct\n(c) object\n(d) def\n", "a"),
    ("How do you access the last element of a list in Python? \n(a) list[len(list)-1]\n(b) list[-1]\n(c) list[-0]\n(d) list[last]\n", "b"),
    ("What is the correct way to create a lambda function in Python? \n(a) lambda x: x + 2\n(b) lambda(x: x + 2)\n(c) (lambda x: x + 2)\n(d) def lambda x: x + 2\n", "a"),
    ("What does the `random.shuffle()` function do in Python? \n(a) Randomly shuffle the elements of a list\n(b) Select a random element from a list\n(c) Sort the elements of a list\n(d) Reverse the elements of a list\n", "a"),
    ("Which of the following is used to handle exceptions in Python? \n(a) try/except\n(b) try/catch\n(c) do/except\n(d) do/catch\n", "a"),
    ("What will be the output of `print([1, 2, 3] + [4, 5, 6])`? \n(a) [1, 2, 3, 4, 5, 6]\n(b) [1, 2, 3, [4, 5, 6]]\n(c) [5, 7, 9]\n(d) Error\n", "a"),
    ("Which of the following functions can be used to get the length of a list in Python? \n(a) length()\n(b) len()\n(c) size()\n(d) count()\n", "b"),
    ("What will be the output of `print(2 ** 2 ** 3)`? \n(a) 64\n(b) 256\n(c) 512\n(d) 128\n", "b"),
    ("What is the output of `print('5' + '7')` in Python? \n(a) 12\n(b) 57\n(c) Error\n(d) 5 7\n", "b"),
    ("What will be the output of `print(10 % 3)`? \n(a) 1\n(b) 3\n(c) 0.3\n(d) 0.1\n", "a"),
    ("What is the result of `print(4 and 5)`? \n(a) True\n(b) False\n(c) 5\n(d) 4\n", "c")
]
    
    while True:
        # Initialize the score
        score = 0

        # Randomize the order of questions and select the first 10
        random.shuffle(questions_and_answers)
        selected_questions = questions_and_answers[:10]

        # Ask each question and update the score
        for question, correct_answer in selected_questions:
            score = ask_question(question, correct_answer, score)

        # Calculate the total number of questions
        total_questions = len(selected_questions)

        # Calculate the percentage score as an integer
        score_in_percentage = int((score / total_questions) * 100)

        # Print the final score and percentage
        print(f"Your final score is: {score} out of {total_questions}. That's {score_in_percentage}%!")

        # Ask the user if they want to play again
        print()
        replay = input("Would you like to play again? (yes or no): ").strip().lower()
        if replay not in ['yes', 'y']:
            print("Thanks for playing! See you soon!")
            break

# Start the quiz game
play_quiz()