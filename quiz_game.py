import random

android_questions = [
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
]

python_questions = [
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
    ("What is the result of `print(4 and 5)`? \n(a) True\n(b) False\n(c) 5\n(d) 4\n", "c"),
]

dsa_questions = [
    ("Which data structure uses LIFO (Last In First Out) ordering? \n(a) Queue\n(b) Stack\n(c) Linked List\n(d) Binary Tree\n", "b"),
    ("What is the time complexity of searching for an element in a balanced binary search tree? \n(a) O(n)\n(b) O(log n)\n(c) O(n^2)\n(d) O(1)\n", "b"),
    ("Which data structure is best suited for implementing a priority queue? \n(a) Stack\n(b) Queue\n(c) Heap\n(d) Linked List\n", "c"),
    ("What is the worst-case time complexity of Quick Sort? \n(a) O(n)\n(b) O(n log n)\n(c) O(n^2)\n(d) O(log n)\n", "c"),
    ("Which of the following sorting algorithms has the best average-case time complexity? \n(a) Bubble Sort\n(b) Insertion Sort\n(c) Merge Sort\n(d) Selection Sort\n", "c"),
    ("What is the time complexity of inserting an element at the beginning of a linked list? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "a"),
    ("In a binary tree, each node has at most how many children? \n(a) 1\n(b) 2\n(c) 3\n(d) 4\n", "b"),
    ("Which of the following data structures is non-linear? \n(a) Array\n(b) Stack\n(c) Queue\n(d) Graph\n", "d"),
    ("What is the space complexity of Depth First Search (DFS) in terms of number of vertices (V)? \n(a) O(1)\n(b) O(V)\n(c) O(E)\n(d) O(V + E)\n", "b"),
    ("Which traversal method is used in a binary search tree to get the elements in ascending order? \n(a) Preorder\n(b) Inorder\n(c) Postorder\n(d) Level Order\n", "b"),
    ("What is the time complexity of accessing an element in an array by index? \n(a) O(n)\n(b) O(log n)\n(c) O(n^2)\n(d) O(1)\n", "d"),
    ("Which data structure uses FIFO (First In First Out) ordering? \n(a) Stack\n(b) Queue\n(c) Array\n(d) Tree\n", "b"),
    ("What is the best-case time complexity of Bubble Sort? \n(a) O(n)\n(b) O(n log n)\n(c) O(n^2)\n(d) O(log n)\n", "a"),
    ("Which algorithm is used to find the shortest path in a weighted graph? \n(a) Depth First Search\n(b) Breadth First Search\n(c) Dijkstra's Algorithm\n(d) Kruskal's Algorithm\n", "c"),
    ("What is the time complexity of deleting an element from a linked list? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "c"),
    ("In a Max-Heap, the parent node is always ____ than the child nodes. \n(a) smaller\n(b) larger\n(c) equal\n(d) None of the above\n", "b"),
    ("Which of the following data structures can be used to implement a graph? \n(a) Stack\n(b) Queue\n(c) Hash Table\n(d) Adjacency List\n", "d"),
    ("What is the worst-case time complexity of Merge Sort? \n(a) O(n)\n(b) O(n log n)\n(c) O(n^2)\n(d) O(log n)\n", "b"),
    ("Which data structure is used for Breadth First Search (BFS) of a graph? \n(a) Stack\n(b) Queue\n(c) Tree\n(d) Linked List\n", "b"),
    ("What is the time complexity of searching for an element in a hash table? \n(a) O(n)\n(b) O(log n)\n(c) O(n^2)\n(d) O(1)\n", "d"),
    ("In a doubly linked list, each node contains pointers to _____. \n(a) next node\n(b) previous node\n(c) both next and previous nodes\n(d) None of the above\n", "c"),
    ("Which of the following sorting algorithms is not stable? \n(a) Bubble Sort\n(b) Merge Sort\n(c) Quick Sort\n(d) Insertion Sort\n", "c"),
    ("What is the time complexity of finding the minimum element in an unsorted array? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "c"),
    ("Which data structure is used in implementing recursion? \n(a) Queue\n(b) Stack\n(c) Linked List\n(d) Tree\n", "b"),
    ("Which of the following is a self-balancing binary search tree? \n(a) Binary Heap\n(b) AVL Tree\n(c) B-Tree\n(d) Trie\n", "b"),
    ("What is the time complexity of heap sort in the worst case? \n(a) O(n)\n(b) O(n log n)\n(c) O(n^2)\n(d) O(log n)\n", "b"),
    ("In a circular linked list, the last node points to _____. \n(a) first node\n(b) last node\n(c) middle node\n(d) None of the above\n", "a"),
    ("What is the time complexity of inserting an element in a max-heap? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "b"),
    ("Which data structure is used in breadth first traversal of a graph? \n(a) Stack\n(b) Queue\n(c) Linked List\n(d) Hash Table\n", "b"),
    ("What is the time complexity of accessing an element in a linked list? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "c"),
    ("In a binary search tree, which of the following traversals is equivalent to the sorted order of elements? \n(a) Preorder\n(b) Inorder\n(c) Postorder\n(d) Level Order\n", "b"),
    ("What is the auxiliary space complexity of merge sort? \n(a) O(1)\n(b) O(n)\n(c) O(n log n)\n(d) O(n^2)\n", "b"),
    ("Which of the following is not a divide and conquer algorithm? \n(a) Merge Sort\n(b) Quick Sort\n(c) Binary Search\n(d) Bubble Sort\n", "d"),
    ("What is the time complexity of finding an element in a balanced binary search tree? \n(a) O(n)\n(b) O(log n)\n(c) O(n^2)\n(d) O(1)\n", "b"),
    ("Which of the following is not an application of stack? \n(a) Expression evaluation\n(b) Expression conversion\n(c) Recursion\n(d) Routing algorithms\n", "d"),
    ("Which of the following data structures allows insertion, deletion, and access in O(1) time? \n(a) Array\n(b) Linked List\n(c) Stack\n(d) Hash Table\n", "d"),
    ("Which of the following algorithms is used for finding the minimum spanning tree in a graph? \n(a) Dijkstra's Algorithm\n(b) Prim's Algorithm\n(c) Bellman-Ford Algorithm\n(d) Floyd-Warshall Algorithm\n", "b"),
    ("What is the worst-case time complexity of searching for an element in an AVL tree? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "b"),
    ("Which of the following data structures is best for implementing a LRU (Least Recently Used) cache? \n(a) Stack\n(b) Queue\n(c) Hash Table\n(d) Linked List\n", "c"),
    ("What is the time complexity of deleting an element from a binary search tree? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "b"),
    ("In a graph, which of the following algorithms is used to find the shortest path from a single source to all other vertices? \n(a) Kruskal's Algorithm\n(b) Prim's Algorithm\n(c) Dijkstra's Algorithm\n(d) Bellman-Ford Algorithm\n", "c"),
    ("Which data structure is used to represent a sparse matrix efficiently? \n(a) Array\n(b) Linked List\n(c) Hash Table\n(d) Graph\n", "b"),
    ("What is the time complexity of building a heap from an unsorted array? \n(a) O(n)\n(b) O(n log n)\n(c) O(n^2)\n(d) O(log n)\n", "a"),
    ("Which traversal method is used in Depth First Search (DFS) of a graph? \n(a) Preorder\n(b) Inorder\n(c) Postorder\n(d) Level Order\n", "a"),
    ("What is the time complexity of inserting an element in a binary search tree (BST) in the average case? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "b"),
    ("Which of the following is a linear data structure? \n(a) Tree\n(b) Graph\n(c) Array\n(d) Hash Table\n", "c"),
    ("What is the time complexity of the best case of Quick Sort? \n(a) O(n)\n(b) O(n log n)\n(c) O(n^2)\n(d) O(log n)\n", "b"),
    ("Which data structure is used to handle the recursion in programs? \n(a) Queue\n(b) Stack\n(c) Linked List\n(d) Hash Table\n", "b"),
    ("What is the purpose of a hash function in a hash table? \n(a) To sort the data\n(b) To search the data\n(c) To map keys to array indices\n(d) To perform arithmetic operations\n", "c"),
    ("Which of the following sorting algorithms is in-place and stable? \n(a) Merge Sort\n(b) Quick Sort\n(c) Bubble Sort\n(d) Selection Sort\n", "c"),
    ("What is the worst-case time complexity of searching for an element in a red-black tree? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "b"),
    ("Which of the following data structures is used to implement a graph? \n(a) Array\n(b) Stack\n(c) Queue\n(d) Adjacency Matrix\n", "d"),
    ("What is the time complexity of deleting an element from a max-heap? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "b"),
    ("Which of the following is a property of a B-tree? \n(a) All leaves are at different levels\n(b) All leaves are at the same level\n(c) It is a binary tree\n(d) It has a maximum of two children\n", "b"),
    ("What is the auxiliary space complexity of quick sort? \n(a) O(1)\n(b) O(n)\n(c) O(n log n)\n(d) O(n^2)\n", "a"),
    ("Which data structure allows efficient range queries? \n(a) Array\n(b) Binary Search Tree\n(c) AVL Tree\n(d) Segment Tree\n", "d"),
    ("What is the time complexity of Breadth First Search (BFS) in terms of number of vertices (V) and edges (E)? \n(a) O(V + E)\n(b) O(V)\n(c) O(E)\n(d) O(V^2)\n", "a"),
    ("Which of the following is an example of a greedy algorithm? \n(a) Merge Sort\n(b) Quick Sort\n(c) Dijkstra's Algorithm\n(d) Dynamic Programming\n", "c"),
    ("What is the time complexity of accessing an element in an unsorted array by value? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "c"),
    ("Which data structure is used in the implementation of depth first search (DFS)? \n(a) Queue\n(b) Stack\n(c) Priority Queue\n(d) Hash Table\n", "b"),
    ("What is the best case time complexity of insertion sort? \n(a) O(n)\n(b) O(n log n)\n(c) O(n^2)\n(d) O(1)\n", "a"),
    ("Which of the following algorithms is used to find the shortest path in an unweighted graph? \n(a) Dijkstra's Algorithm\n(b) Prim's Algorithm\n(c) Bellman-Ford Algorithm\n(d) Breadth First Search\n", "d"),
    ("What is the time complexity of searching for an element in a balanced AVL tree? \n(a) O(1)\n(b) O(log n)\n(c) O(n)\n(d) O(n log n)\n", "b")
]

javascript_questions = [
    ("Which of the following is a JavaScript framework?\n(a) Django\n(b) Flask\n(c) Angular\n(d) Laravel\n", "c"),
    ("Which company developed JavaScript?\n(a) Microsoft\n(b) Netscape\n(c) Google\n(d) Apple\n", "b"),
    ("Which symbol is used for comments in JavaScript?\n(a) //\n(b) <!-- -->\n(c) /* */\n(d) #\n", "a"),
    ("What is the output of 'typeof null' in JavaScript?\n(a) 'null'\n(b) 'object'\n(c) 'undefined'\n(d) 'boolean'\n", "b"),
    ("How do you declare a variable in JavaScript?\n(a) var\n(b) let\n(c) const\n(d) All of the above\n", "d"),
    ("Which method converts a JSON string into a JavaScript object?\n(a) JSON.stringify()\n(b) JSON.parse()\n(c) JSON.toObject()\n(d) JSON.convert()\n", "b"),
    ("Which of the following is a JavaScript package manager?\n(a) npm\n(b) pip\n(c) gem\n(d) composer\n", "a"),
    ("Which of the following is not a reserved word in JavaScript?\n(a) interface\n(b) throws\n(c) program\n(d) short\n", "c"),
    ("Which event occurs when the user clicks on an HTML element?\n(a) onmouseover\n(b) onchange\n(c) onclick\n(d) onmouseclick\n", "c"),
    ("Which function is used to serialize an object into a JSON string in JavaScript?\n(a) JSON.stringify()\n(b) JSON.parse()\n(c) JSON.objectify()\n(d) JSON.encode()\n", "a"),
    ("How do you create a function in JavaScript?\n(a) function = myFunction()\n(b) function myFunction()\n(c) function:myFunction()\n(d) create myFunction()\n", "b"),
    ("Which built-in method combines the text of two strings and returns a new string?\n(a) append()\n(b) concat()\n(c) attach()\n(d) add()\n", "b"),
    ("Which built-in method sorts the elements of an array?\n(a) changeOrder(order)\n(b) order()\n(c) sort()\n(d) arrange()\n", "c"),
    ("Which of the following is not a valid JavaScript variable name?\n(a) 2names\n(b) _first_and_last_names\n(c) FirstAndLast\n(d) None of the above\n", "a"),
    ("Which JavaScript method is used to access an HTML element by its id?\n(a) getElementById()\n(b) getElement(id)\n(c) getElementByIdentifier()\n(d) getElementByIdName()\n", "a"),
    ("Which operator is used to assign a value to a variable in JavaScript?\n(a) =\n(b) ==\n(c) ===\n(d) <-\n", "a"),
    ("Which method removes the last element from an array and returns that element?\n(a) pop()\n(b) last()\n(c) remove()\n(d) None of the above\n", "a"),
    ("What is the correct JavaScript syntax to change the content of the HTML element below?\n<p id='demo'>This is a demonstration.</p>\n(a) document.getElementByName('p').innerHTML = 'Hello World!';\n(b) document.getElement('p').innerHTML = 'Hello World!';\n(c) document.getElementById('demo').innerHTML = 'Hello World!';\n(d) demo.innerHTML = 'Hello World!';\n", "c"),
    ("What will the following code return: Boolean(10 > 9)?\n(a) true\n(b) false\n(c) NaN\n(d) undefined\n", "a"),
    ("Which JavaScript method is used to write on a browser's console?\n(a) console.write()\n(b) console.output()\n(c) console.log()\n(d) console.print()\n", "c"),
    ("How can you add a comment in JavaScript?\n(a) 'This is a comment\n(b) <!--This is a comment-->\n(c) //This is a comment\n(d) *This is a comment*\n", "c"),
    ("Which JavaScript method is used to call a function after a specified time interval?\n(a) setTimeout()\n(b) setTime()\n(c) setInterval()\n(d) setTimer()\n", "a"),
    ("Which of the following is a string method in JavaScript?\n(a) get()\n(b) element()\n(c) indexOf()\n(d) querySelector()\n", "c"),
    ("How do you create an array in JavaScript?\n(a) var arr = '1, 2, 3'\n(b) var arr = (1, 2, 3)\n(c) var arr = [1, 2, 3]\n(d) var arr = {1, 2, 3}\n", "c"),
    ("Which of the following methods is used to access HTML elements using JavaScript?\n(a) getElementById()\n(b) getElementsByClassName()\n(c) getElementsByTagName()\n(d) All of the above\n", "d"),
    ("Which of the following is correct about features of JavaScript?\n(a) JavaScript is a lightweight, interpreted programming language.\n(b) JavaScript is designed for creating network-centric applications.\n(c) JavaScript is complementary to and integrated with Java.\n(d) All of the above\n", "d"),
    ("Which built-in method reverses the order of the elements of an array?\n(a) changeOrder(order)\n(b) reverse()\n(c) sort(order)\n(d) None of the above\n", "b"),
    ("Which of the following function of String object returns the characters in a string between two indexes into the string?\n(a) slice()\n(b) split()\n(c) substr()\n(d) substring()\n", "d"),
    ("Which of the following function of Array object adds and/or removes elements from an array?\n(a) toSource()\n(b) sort()\n(c) splice()\n(d) unshift()\n", "c"),
    ("Which of the following function of Array object extracts a section of an array and returns a new array?\n(a) reverse()\n(b) shift()\n(c) slice()\n(d) some()\n", "c"),
    ("Which of the following function of String object creates an HTML anchor that is used as a hypertext target?\n(a) anchor()\n(b) link()\n(c) blink()\n(d) big()\n", "a"),
    ("Which of the following function of String object returns the calling string value converted to upper case?\n(a) toLocaleUpperCase()\n(b) toUpperCase()\n(c) toString()\n(d) substring()\n", "b"),
    ("Which of the following function of Array object represents the source code of an object?\n(a) splice()\n(b) toSource()\n(c) toString()\n(d) unshift()\n", "b"),
    ("Inside which HTML element do we put the JavaScript?\n(a) <javascript>\n(b) <script>\n(c) <js>\n(d) <scripting>\n", "b"),
    ("What is the correct JavaScript syntax to write 'Hello World'?\n(a) response.write('Hello World')\n(b) 'Hello World'\n(c) document.write('Hello World')\n(d) ('Hello World')\n", "c"),
    ("What is the correct place to insert a JavaScript?\n(a) Both the <head> section and the <body> section are correct\n(b) The <head> section\n(c) The <body> section\n(d) The <footer> section\n", "a"),
    ("How do you call a function named 'myFunction'?\n(a) call function myFunction()\n(b) call myFunction()\n(c) myFunction()\n(d) Call.myFunction()\n", "c"),
    ("How to write an IF statement in JavaScript?\n(a) if i = 5 then\n(b) if i == 5 then\n(c) if (i == 5)\n(d) if i = 5\n", "c"),
    ("How does a WHILE loop start?\n(a) while (i <= 10; i++)\n(b) while (i <= 10)\n(c) while i = 1 to 10\n(d) while (i <= 10; i+)\n", "b"),
    ("How can you detect the client's browser name?\n(a) navigator.appName\n(b) client.navName\n(c) browser.name\n(d) user.navName\n", "a"),
]

css_questions = [
    ("Which property is used to change the background color?\n(a) bgcolor\n(b) color\n(c) background-color\n(d) back-color\n", "c"),
    ("Which property is used to change the text color of an element?\n(a) fgcolor\n(b) color\n(c) text-color\n(d) font-color\n", "b"),
    ("Which property is used to change the font of an element?\n(a) font-family\n(b) font-style\n(c) font-weight\n(d) font-variant\n", "a"),
    ("How do you add a background color for all <h1> elements?\n(a) all.h1 {background-color: #FFFFFF;}\n(b) h1.all {background-color: #FFFFFF;}\n(c) h1 {background-color: #FFFFFF;}\n(d) all-h1 {background-color: #FFFFFF;}\n", "c"),
    ("Which CSS property is used to change the text alignment?\n(a) align\n(b) text-align\n(c) text-decoration\n(d) text-style\n", "b"),
    ("Which property is used to change the left margin of an element?\n(a) padding-left\n(b) margin-left\n(c) indent\n(d) margin\n", "b"),
    ("How do you make each word in a text start with a capital letter?\n(a) text-transform: capitalize\n(b) text-style: capitalize\n(c) text-decoration: capitalize\n(d) transform: capitalize\n", "a"),
    ("Which property is used to change the space between lines of text?\n(a) line-height\n(b) spacing\n(c) text-spacing\n(d) line-spacing\n", "a"),
    ("How do you select an element with id 'demo'?\n(a) .demo\n(b) #demo\n(c) *demo\n(d) demo\n", "b"),
    ("How do you select elements with class name 'test'?\n(a) .test\n(b) #test\n(c) *test\n(d) test\n", "a"),
    ("Which property is used to change the font size?\n(a) font-height\n(b) text-size\n(c) font-size\n(d) text-height\n", "c"),
    ("How do you make the text bold?\n(a) style: bold\n(b) font: bold\n(c) font-weight: bold\n(d) text-weight: bold\n", "c"),
    ("Which property is used to change the bottom margin of an element?\n(a) margin-bottom\n(b) margin\n(c) padding-bottom\n(d) padding\n", "a"),
    ("How do you display a border like this: The top border = 10 pixels, bottom border = 5 pixels, left border = 20 pixels, right border = 1 pixel?\n(a) border-width: 10px 1px 5px 20px\n(b) border-width: 10px 20px 5px 1px\n(c) border-width: 10px 5px 20px 1px\n(d) border-width: 5px 20px 10px 1px\n", "a"),
    ("Which property is used to change the left padding of an element?\n(a) padding-left\n(b) padding\n(c) margin-left\n(d) margin\n", "a"),
    ("Which property is used to change the width of an element?\n(a) width\n(b) length\n(c) size\n(d) height\n", "a"),
    ("How do you make a list that lists its items with squares?\n(a) list-type: square\n(b) list-style-type: square\n(c) list: square\n(d) list-style: square\n", "b"),
    ("How do you select all p elements inside a div element?\n(a) div p\n(b) div + p\n(c) div.p\n(d) div ~ p\n", "a"),
    ("Which property is used to change the height of an element?\n(a) height\n(b) width\n(c) length\n(d) size\n", "a"),
    ("How do you make a list that lists its items with numbers?\n(a) list-style-type: number\n(b) list: number\n(c) list-style-type: decimal\n(d) list-type: decimal\n", "c"),
    ("Which property is used to make the text italic?\n(a) font-weight: italic\n(b) font-style: italic\n(c) text-decoration: italic\n(d) text-style: italic\n", "b"),
    ("Which property is used to change the right margin of an element?\n(a) padding-right\n(b) margin-right\n(c) indent\n(d) margin\n", "b"),
    ("How do you display hyperlinks without an underline?\n(a) a {text-decoration: none;}\n(b) a {underline: none;}\n(c) a {decoration: no-underline;}\n(d) a {text-decoration: no-underline;}\n", "a"),
    ("Which property is used to change the cursor to a hand?\n(a) cursor: hand\n(b) cursor: pointer\n(c) cursor: grab\n(d) cursor: move\n", "b"),
    ("How do you make each letter in a text uppercase?\n(a) text-transform: uppercase\n(b) text-style: uppercase\n(c) text-decoration: uppercase\n(d) transform: uppercase\n", "a"),
    ("Which property is used to change the background image of an element?\n(a) bg-image\n(b) background-image\n(c) bg-image-set\n(d) background-img\n", "b"),
    ("Which property is used to change the text color of an element?\n(a) text-color\n(b) font-color\n(c) color\n(d) fgcolor\n", "c"),
    ("How do you make the first letter of every word in a text capitalized?\n(a) text-transform: capitalize\n(b) text-style: capitalize\n(c) text-decoration: capitalize\n(d) transform: capitalize\n", "a"),
    ("How do you make a text shadow?\n(a) text-shadow\n(b) text-shadowing\n(c) text-shadow-effect\n(d) shadow-text\n", "a"),
    ("Which property is used to change the top margin of an element?\n(a) margin-top\n(b) padding-top\n(c) top-margin\n(d) top-padding\n", "a"),
    ("Which property is used to set the background image of an element?\n(a) background-image\n(b) bg-image\n(c) background-url\n(d) image-background\n", "a"),
    ("Which CSS property controls the text size?\n(a) font-size\n(b) text-style\n(c) text-size\n(d) font-style\n", "a"),
    ("How do you make the text bold?\n(a) font-weight: bold\n(b) style: bold\n(c) font-style: bold\n(d) text-decoration: bold\n", "a"),
    ("Which property is used to change the space between the content and the border?\n(a) margin\n(b) padding\n(c) spacing\n(d) border-spacing\n", "b"),
    ("Which property is used to change the text color of an element?\n(a) fgcolor\n(b) text-color\n(c) font-color\n(d) color\n", "d"),
    ("How do you select all elements of a given class?\n(a) .classname\n(b) #classname\n(c) classname\n(d) *classname\n", "a"),
    ("Which CSS property controls the text alignment?\n(a) align\n(b) text-align\n(c) text-decoration\n(d) text-style\n", "b"),
    ("Which CSS property is used to change the space between letters?\n(a) letter-spacing\n(b) spacing\n(c) text-spacing\n(d) font-spacing\n", "a"),
    ("Which CSS property is used to change the space between words?\n(a) word-spacing\n(b) spacing\n(c) text-spacing\n(d) font-spacing\n", "a"),
    ("Which CSS property is used to change the font of an element?\n(a) font-family\n(b) font-style\n(c) font-weight\n(d) font-variant\n", "a"),
    ("Which CSS property is used to change the border color of an element?\n(a) border-color\n(b) border-style\n(c) border-background\n(d) border-fill\n", "a"),
    ("How do you make the text underline?\n(a) text-decoration: underline\n(b) font-decoration: underline\n(c) text-style: underline\n(d) font-style: underline\n", "a"),
    ("How do you make the text italic?\n(a) font-style: italic\n(b) text-style: italic\n(c) font-weight: italic\n(d) text-weight: italic\n", "a"),
    ("Which property is used to set the background color of an element?\n(a) bgcolor\n(b) background-color\n(c) color\n(d) bg-color\n", "b"),
    ("Which property is used to add or subtract space between the letters in a text?\n(a) letter-spacing\n(b) font-spacing\n(c) character-spacing\n(d) text-spacing\n", "a"),
    ("Which property is used to control the order of flexible items in a container?\n(a) order\n(b) flex-order\n(c) item-order\n(d) order-flex\n", "a"),
    ("Which CSS property is used to change the style of a list marker?\n(a) list-style\n(b) marker-style\n(c) list-type\n(d) list-marker\n", "a"),
    ("How do you add shadow to text?\n(a) text-shadow\n(b) font-shadow\n(c) shadow-text\n(d) text-effect\n", "a"),
    ("Which property is used to change the size of the background image?\n(a) background-size\n(b) background-stretch\n(c) background-fit\n(d) background-scale\n", "a"),
    ("Which CSS property is used to change the style of the font?\n(a) font-style\n(b) font-weight\n(c) font-family\n(d) font-variant\n", "a"),
    ("Which CSS property controls the alignment of text within an element?\n(a) text-align\n(b) align-text\n(c) align\n(d) text-position\n", "a"),
    ("Which property is used to change the transparency of an element?\n(a) opacity\n(b) visibility\n(c) transparent\n(d) filter\n", "a"),
    ("How do you make a rounded border?\n(a) border-radius\n(b) border-curve\n(c) border-round\n(d) border-corner\n", "a"),
    ("Which property is used to control the position of an element?\n(a) position\n(b) location\n(c) placement\n(d) top\n", "a"),
    ("Which property is used to set the width of an element?\n(a) width\n(b) height\n(c) size\n(d) dimension\n", "a"),
    ("Which property is used to set the height of an element?\n(a) height\n(b) width\n(c) size\n(d) dimension\n", "a"),
    ("Which property is used to add a border to an element?\n(a) border\n(b) outline\n(c) border-style\n(d) frame\n", "a"),
    ("Which property is used to control the margin of an element?\n(a) margin\n(b) padding\n(c) spacing\n(d) border\n", "a"),
    ("Which property is used to add padding inside an element?\n(a) padding\n(b) margin\n(c) spacing\n(d) border\n", "a"),
    ("How do you display an element as a block-level element?\n(a) display: block\n(b) display: inline\n(c) display: inline-block\n(d) display: none\n", "a"),
    ("How do you display an element as an inline element?\n(a) display: inline\n(b) display: block\n(c) display: inline-block\n(d) display: none\n", "a"),
    ("Which property is used to control the visibility of an element?\n(a) visibility\n(b) display\n(c) opacity\n(d) transparent\n", "a"),
    ("How do you hide an element?\n(a) display: none\n(b) visibility: hidden\n(c) opacity: 0\n(d) All of the above\n", "d"),
    ("Which property is used to change the font weight of an element?\n(a) font-weight\n(b) font-style\n(c) font-family\n(d) font-variant\n", "a"),
    ("Which property is used to control the z-index of an element?\n(a) z-index\n(b) layer\n(c) stack\n(d) depth\n", "a"),
    ("How do you set a minimum width for an element?\n(a) min-width\n(b) width-min\n(c) minimum-width\n(d) width\n", "a"),
    ("How do you set a maximum width for an element?\n(a) max-width\n(b) width-max\n(c) maximum-width\n(d) width\n", "a"),
    ("Which property is used to set the line height?\n(a) line-height\n(b) height-line\n(c) text-height\n(d) height\n", "a"),
    ("Which property is used to set the bottom margin of an element?\n(a) margin-bottom\n(b) padding-bottom\n(c) bottom-margin\n(d) bottom-padding\n", "a"),
    ("Which property is used to set the top margin of an element?\n(a) margin-top\n(b) padding-top\n(c) top-margin\n(d) top-padding\n", "a"),
    ("Which property is used to set the right margin of an element?\n(a) margin-right\n(b) padding-right\n(c) right-margin\n(d) right-padding\n", "a"),
    ("Which property is used to set the left margin of an element?\n(a) margin-left\n(b) padding-left\n(c) left-margin\n(d) left-padding\n", "a"),
    ("How do you set the background color of an element?\n(a) background-color\n(b) bgcolor\n(c) color\n(d) back-color\n", "a"),
    ("How do you set the background image of an element?\n(a) background-image\n(b) bg-image\n(c) back-image\n(d) image-background\n", "a"),
    ("How do you set the background position of an element?\n(a) background-position\n(b) bg-position\n(c) back-position\n(d) position-background\n", "a"),
    ("How do you set the background repeat of an element?\n(a) background-repeat\n(b) bg-repeat\n(c) back-repeat\n(d) repeat-background\n", "a"),
    ("How do you set the background size of an element?\n(a) background-size\n(b) bg-size\n(c) back-size\n(d) size-background\n", "a"),
    ("How do you set the border of an element?\n(a) border\n(b) border-style\n(c) border-width\n(d) border-color\n", "a"),
    ("How do you set the border color of an element?\n(a) border-color\n(b) border\n(c) border-style\n(d) border-width\n", "a"),
    ("How do you set the border style of an element?\n(a) border-style\n(b) border\n(c) border-color\n(d) border-width\n", "a"),
    ("How do you set the border width of an element?\n(a) border-width\n(b) border\n(c) border-color\n(d) border-style\n", "a"),
    ("How do you set the width of an element?\n(a) width\n(b) height\n(c) size\n(d) dimension\n", "a"),
    ("How do you set the height of an element?\n(a) height\n(b) width\n(c) size\n(d) dimension\n", "a"),
    ("How do you add padding inside an element?\n(a) padding\n(b) margin\n(c) spacing\n(d) border\n", "a"),
    ("How do you add margin outside an element?\n(a) margin\n(b) padding\n(c) spacing\n(d) border\n", "a"),
    ("How do you set the font family of an element?\n(a) font-family\n(b) font-style\n(c) font-weight\n(d) font-variant\n", "a"),
    ("How do you set the font size of an element?\n(a) font-size\n(b) text-size\n(c) size\n(d) font-style\n", "a"),
    ("How do you set the font style of an element?\n(a) font-style\n(b) font-family\n(c) font-weight\n(d) font-variant\n", "a"),
    ("How do you set the font weight of an element?\n(a) font-weight\n(b) font-style\n(c) font-family\n(d) font-variant\n", "a"),
    ("How do you set the text color of an element?\n(a) color\n(b) text-color\n(c) font-color\n(d) fgcolor\n", "a"),
    ("How do you set the text alignment of an element?\n(a) text-align\n(b) align\n(c) align-text\n(d) text-position\n", "a"),
    ("How do you set the text decoration of an element?\n(a) text-decoration\n(b) decoration\n(c) decorate\n(d) text-style\n", "a"),
    ("How do you set the text transform of an element?\n(a) text-transform\n(b) transform\n(c) text-change\n(d) text-style\n", "a"),
    ("How do you set the letter spacing of an element?\n(a) letter-spacing\n(b) spacing\n(c) text-spacing\n(d) font-spacing\n", "a"),
    ("How do you set the word spacing of an element?\n(a) word-spacing\n(b) spacing\n(c) text-spacing\n(d) font-spacing\n", "a"),
    ("How do you set the line height of an element?\n(a) line-height\n(b) height\n(c) text-height\n(d) line\n", "a"),
    ("How do you set the vertical alignment of an element?\n(a) vertical-align\n(b) align\n(c) align-vertical\n(d) valign\n", "a"),
    ("How do you set the overflow of an element?\n(a) overflow\n(b) flow\n(c) scroll\n(d) hidden\n", "a"),
    ("How do you set the position of an element?\n(a) position\n(b) location\n(c) placement\n(d) top\n", "a"),
    ("How do you set the z-index of an element?\n(a) z-index\n(b) layer\n(c) stack\n(d) depth\n", "a"),
    ("How do you set the display of an element?\n(a) display\n(b) show\n(c) visibility\n(d) block\n", "a"),
    ("How do you set the visibility of an element?\n(a) visibility\n(b) display\n(c) hidden\n(d) show\n", "a"),
]

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

def ask_question(question, correct_answer, score):
    print(question)
    user_answer = input("Your answer: ").strip()
    if user_answer.lower() == correct_answer.lower():
        print("Correct!\n")
        return score + 1
    else:
        print(f"Incorrect! The correct answer is: {correct_answer}\n")
        return score

def generate_quiz(topic):
    if topic == "android":
        return android_questions
    elif topic == "python":
        return python_questions
    elif topic == "dsa":
        return dsa_questions
    elif topic == "javascript":
        return javascript_questions
    elif topic == "css":
        return css_questions
    else:
        return []

while True:
    # Let the user choose a topic
    topic_choice = input("Choose a topic (android, python, dsa, javascript, css): ").strip().lower()
    questions_and_answers = generate_quiz(topic_choice)

    if not questions_and_answers:
        print("Invalid topic choice. Please choose 'android', 'python','dsa', 'javascript', 'css'.")
        continue

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
