# Code Editor for Competitive Programmers 👨‍💻
It is a C++/Python Code editor which can be very helpful for Competitive Programmers due its amazing features.

It Parses Input and Output from Codeforces website by providing contest ID and problem ID so that user will not have to spend time in manually copying inputs and comparing outputs, everything is done on single click. I implemented this part using ***Beautiful Soup*** and ***Requests*** in Python.

<img src="https://i.ibb.co/1dgwwGd/Screenshot-from-2021-05-23-23-37-05.png" border="0">

On single click it compile and run the code, which will take input from parsed data, and also give verdict of correct or wrong answer by comparing it to the parsed output. Here I used linux ***os.system*** calls.

<img src="https://i.ibb.co/6Wft7dM/Screenshot-from-2021-05-23-23-45-11.png" border="0">

#### Auto Compelete - 
It automatically detects the code and show suggestions for completion, this part is implemented using ***Trie Data Structure*** for better efficiency.


#### Auto Coloring - 
Color different parts of code with diffrent colors to make better experience, this part is also implemented using ***Python Tags*** and ***Search function***.

<img src="https://i.ibb.co/BCNKPsc/Screenshot-from-2021-05-23-23-55-22.png" border="0">

#### Auto-Submit -
On single click it submit the code on Codeforces so that you save your time. Implemented using Selenium driver.

<img src="https://i.ibb.co/qFNntSh/Screenshot-from-2021-05-23-23-59-00.png" border="0">

There are also other features, you can explore them by installing and using it. 😁

# Installation Instructions
Download this project as ZIP file and extract somewhere.

Now Run this Command on linux terminal to use selenium -
```sudo pip3 install selenium```

Download chromedriver zip file according to your chrome version (you can check your chrome version on ```chrome://version```) from here.

Go to chrome://version and copy the path given in heading of profile path and paste it in place of line:
```options.add_argument("user-data-dir=/home/ankit/.config/google-chrome/Default")```
in main.py file. Mention that profile path instead of ```/home/USER/.config/google-chrome/Default```.

Get path of your chromedriver which you downloaded in pre-requisites and copy it in line:

```driver=webdriver.Chrome(executable_path='/home/ankit/Documents/chromedriver/chromedriver',chrome_options=options)``` in main.py file. Mention your path instead of ```/home/ankit/Documents/chromedriver/chromedriver```

Now just run the main.py file and enjoy. 🙂

## Please feel free to open a PR or submit an issue with your feedback!
