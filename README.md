# CodeCaker
<h1>Code Editor for Competitive Programmers 👨‍💻</h1>
<p><font size = "11">
A C++/Python code editor. </br>
Single click compile and run (used linux <b><i>os.system calls</i></b>).</br>
Parse Input and Output from Codeforces problem by getting problem ID and contest ID. Now no need to copy all inputs one by one and run on each, in sigle click  it fetches all input and all output, on run it compares the excepted output and code output and give result accordingly. This is implemented using <b><i>Beautiful Soup and Requests</i></b>.</br></br>
<b>Auto-Submit</b> - </br>On single click it submit the code on Codeforces so that you save your time. Implemented using <b><i>Selenium driver</i></b>.</br></br>
<b>Auto Compelete</b> - </br>It automatically detects the code and show suggestions for completion, this part is implemented using <b><i>Trie Data Structure</i></b> for better efficiency.</br></br>
<b>Auto Coloring</b> - Color diffrent parts with diffrent colors to make better experience, this part is also implemented using Trie data structure.
 </br></font>
 </p>
 </br>
 <a href="https://ibb.co/n1kYL9r"><img src="https://i.ibb.co/WzKM2Zn/Screenshot-from-2021-05-22-12-51-39.png" alt="Screenshot-from-2021-05-22-12-51-39" border="0"></a></br>
 
 <h2>Installation instructions - </h2> 
 1. Download this project as ZIP file and extract somewhere. </br>
 2. Now Run this Command on linux terminal - sudo pip3 install selenium </br>
 3. Download chromedriver zip file according to your chrome version (you can check your chrome version on chrome://version) from here. </br>
 4. Go to chrome://version and copy the path given in heading of profile path and paste it in place of line:</br>
    `options.add_argument("user-data-dir=/home/ankit/.config/google-chrome/Default") in main.py file.`</br> 
    Mention that profile path instead of /home/USER/.config/google-chrome/Default </br>
 5. Get path of your chromedriver which you downloaded in pre-requisites and copy it in line :</br>
    driver=webdriver.Chrome(executable_path='/home/ankit/Documents/chromedriver/chromedriver',chrome_options=options) </br>in main.py file. Mention your path       instead of /home/ankit/Documents/chromedriver/chromedriver. </br>
 6. Now just run the main.py file and enjoy. 🙂 </br></br>


<a href="https://ibb.co/9rvJrbm"><img src="https://i.ibb.co/jr5dry9/Screenshot-from-2021-05-22-12-53-18.png" alt="Screenshot-from-2021-05-22-12-53-18" border="0"></a></br></br>
<a href="https://ibb.co/fVWLC7X"><img src="https://i.ibb.co/CpyDnFw/Screenshot-from-2021-05-22-12-54-31.png" alt="Screenshot-from-2021-05-22-12-54-31" border="0"></a>

<h3> Please feel free to open a PR or submit an issue with your feedback!<h3>
