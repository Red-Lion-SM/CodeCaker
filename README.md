# CodeCaker
<h1>Code Editor for Competitive Programmers 👨‍💻</h1>
<p><font size = "11">
It is a C++/Python Code editor which can be very helpful for Competitive Programmers due its amazing features.</br></br>
<t>It <b>Parses Input and Output</b> from <i>Codeforces</i> website by providing contest ID and problem ID so that user will not have to spend time in manually copying inputs and comparing outputs, everything is done on single click. I implemented this part using <b><i>Beautiful Soup</i></b> and <b><i>Requests</b></i> in Python.</br></br>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/1dgwwGd/Screenshot-from-2021-05-23-23-37-05.png" alt="Screenshot-from-2021-05-23-23-37-05" border="0"></a></br></br>
On single click it <i>compile</i> and <i>run</i> the code, which will take input from parsed data, and also give <i>verdict</i> of correct or wrong answer by comparing it to the parsed output. Here I used linux <b><i>os.system calls</i></b>.</br></br>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/6Wft7dM/Screenshot-from-2021-05-23-23-45-11.png" alt="Screenshot-from-2021-05-23-23-45-11" border="0"></a>
</br></br>
<b>Auto Compelete</b> - </br>It automatically detects the code and show suggestions for completion, this part is implemented using <b><i>Trie Data Structure</i></b> for better efficiency.</br></br>
<b>Auto Coloring</b> -</br> Color different parts of <i>code</i> with diffrent colors to make better experience, this part is also implemented using <b><i>Python Tags</i></b> and <b><i>Search function</i></b>.</br></br>
<a href="https://ibb.co/4VdgfNK"><img src="https://i.ibb.co/BCNKPsc/Screenshot-from-2021-05-23-23-55-22.png" alt="Screenshot-from-2021-05-23-23-55-22" border="0"></a></br></br>
<b>Auto-Submit</b> - </br>On single click it submit the code on Codeforces so that you save your time. Implemented using <b><i>Selenium driver</i></b>.</br></br>
 <a href="https://ibb.co/YTcWzCJ"><img src="https://i.ibb.co/qFNntSh/Screenshot-from-2021-05-23-23-59-00.png" alt="Screenshot-from-2021-05-23-23-59-00" border="0"></a>
 </font>
 </p>
 </br>
 There are also other features, you can explore them by installing and using it. 😁
 </p>
 
 <h2>Installation instructions - </h2> 
 1. Download this project as ZIP file and extract somewhere. </br>
 2. Now Run this Command on linux terminal to use selenium - </br>
<i><b>sudo pip3 install selenium</i></b></br>
 4. Download chromedriver zip file according to your chrome version (you can check your chrome version on <i>chrome://version</i>) from here. </br>
 5. Go to chrome://version and copy the path given in heading of profile path and paste it in place of line:</br>
    <i><b>options.add_argument("user-data-dir=/home/ankit/.config/google-chrome/Default")</b></i></br>in main.py file.</br> 
    &ensp;&ensp;&ensp;Mention that profile path instead of <i>/home/USER/.config/google-chrome/Default</i>.</br>
 6. Get path of your chromedriver which you downloaded in pre-requisites and copy it in line:</br>
    <i>driver=webdriver.Chrome(executable_path='/home/ankit/Documents/chromedriver/chromedriver',chrome_options=options)</i></br>
    in <i>main.py</i> file. Mention your path instead of /home/ankit/Documents/chromedriver/chromedriver.</br>
 7. Now just run the main.py file and enjoy. 🙂 </br></br>

<h3> Please feel free to open a PR or submit an issue with your feedback!<h3>
