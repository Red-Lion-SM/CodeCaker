# Some Important Imports
from tkinter import *
import tkinter as tk
import math
import re
import urllib.request
from bs4 import BeautifulSoup
import filecmp
import subprocess
from tkinter.scrolledtext import ScrolledText
import pyautogui
import time
from tkinter import filedialog
from tkinter import font
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

# Collection of some commonly used keywords in C++, also colors for text editor
dicc=[
    ["for","#Ff00d5"],["#include", "#Ff00d5"],
    ["#define", "#Ff00d5"],["=", "#Ff00d5"],
    ["-", "#Ff00d5"],["+", "#Ff00d5"],
    ["/", "#Ff00d5"],["*", "#Ff00d5"],
    [">", "#Ff00d5"],["<", "#Ff00d5"],
    ["const", "#Ff00d5"],["using", "#Ff00d5"],
    ["namespace", "#Ff00d5"],[".", "#Ff00d5"],
    ["if", "#Ff00d5"],["else", "#Ff00d5"],
    ["#ifndef", "#Ff00d5"],[":","#Ff00d5"],
    ["while", "#Ff00d5"],["do", "#Ff00d5"],
    ["return", "#Ff00d5"],["size", "#35C607"],
    ["begin", "#35C607"],["end", "#35C607"],
    ["forr", "#35C607"],["all", "#35C607"],
    ["sz", "#35C607"],["solve", "#35C607"],
    ["push_back", "#35C607"],["pop_back", "#35C607"],
    ["__gcd", "#35C607"],["ios_base::sync_with_stdio", "#35C607"],
    ["tie", "#35C607"],["main", "#35C607"],
    ["0", "#D269F9"],["1", "#D269F9"],["2", "#D269F9"],["3", "#D269F9"],
    ["4", "#D269F9"],["5", "#D269F9"],["6", "#D269F9"],["7", "#D269F9"],
    ["8", "#D269F9"],["9", "#D269F9"],
    ["int", "#89D3EB"],["string", "#89D3EB"],
    ["char", "#89D3EB"],["void", "#89D3EB"],
    ["long", "#89D3EB"],["double", "#89D3EB"],
    ["abs", "#89D3EB"],["signed", "#89D3EB"],
    ["freopen", "#89D3EB"],["auto", "#89D3EB"],
    ["bool", "#89D3EB"],["<bits/stdc++.h>", "yellow"],
    ["#endif", "#Ff00d5"],["Correct Answer","#35C607"],
    ["Wrong answer!!!","#E5071B"],
]

# Geometry for TKinter Window
root = Tk()
root.title('CodeCaker')
root.geometry("1800x860")
root["bg"] = "black"
color = ["#282a36","white","blue","green","black","#201F2D"]

# Count of test_cases
test_case_cnt = 0

# Input Output Parser Code
def parse():
    x = str(cntst_id.get("1.0",END))   # Contest ID
    y = str(prblm_id.get("1.0",END))   # Problem ID
    x = x[:-1]
    y = y[:-1]
    html = urllib.request.urlopen('https://codeforces.com/problemset/problem/' + x + '/' + y)     # Problem URL

    # Filtering of text part from the HTML
    soup = BeautifulSoup(html)
    data = soup.findAll(text=True)

    def visible(element):
        if element.parent.name in ['style', 'script', '[document]','head', 'title']:   # Ignore HTML and other parts
            return False
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):                      # Ignore Comments
            return False
        return True
    result = list(filter(visible, data))    # This is storing only the visible text part

    # Finding the sample Input and Output
    x = 0
    for _ in range(len(list(result)) - 5):
        if (list(result)[_] == 'Example' and list(result)[_ + 1]=='Input'):
            x = _+2
            break
    global test_case_cnt
    test_case_cnt+=1          # Increase Testcase count by 1
    file_name = "input"+str(test_case_cnt)+".txt"
    sample = open(file_name, 'w+')
    f = str(result[x][1:])
    print(f, file=sample)    # Inserting sample input in file
    sample.close()
    file_name = "requiredop" + str(test_case_cnt) + ".txt"
    sample = open(file_name, 'w+')
    f = str(result[x + 2][1:])
    print(f, file=sample)    # Inserting sample output in file
    sample.close()

components_to_remove = []

# Auto-Completition using Trie Data Structure
class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []

    def formTrie(self, keys):
        for key in keys:
            self.insert(key)

    # Insert key Function
    def insert(self, key):
        node = self.root
        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
        node.last = True

    # Search key
    def search(self, key):
        node = self.root
        found = True
        for a in list(key):
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
        if node.last != True:
            return False
        return node and node.last and found

    # Recursively find all words with given prefix
    def suggestionsRec(self, node, word):
        if node.last:
            self.word_list.append(word)
        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    # Find the maximum length upto which any prefix is matching the key
    def printAutoSuggestions(self, key):
        if(len(key) == 0):
            return 0
        node = self.root
        not_found = False
        temp_word = ''
        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]
        if not_found:
            return 0
        elif node.last and not node.children:
            return -1
        self.suggestionsRec(node, temp_word)
        t = ""
        for s in self.word_list:
            t += s
            t += " | "
        t = t[:-2]
        cmpp = Label(main_frame, height=1, font=("UBUNTU", 14), bg="white", fg=color[0], text=t)
        cmpp.place(x=15, y=900)
        components_to_remove.append(cmpp)
        self.word_list.clear()
        return 1

# Inserting keys into Trie
keys = ["for(int i = 0; i < n; i++)"]
for _ in dicc:
    keys.append(_[0])
status = ["Not found", "Found"]
t = Trie()
t.formTrie(keys)

# A function that is called every time whenever any key is pressed in the editor (Binded to the editor).
# This functiion is used for 2 purposes :
#     1. Autocompletion
#     2. Autocoloring
def on_key_release(text_widget):
    x = editor.text.index('current')
    if(x[-2:] != ".0"):
        tt = x
        if x[-1] == '0':
            x = x[:-1]
        else:
            x = x[:-1] + str((ord(x[-1]) - ord('0')) - 1)
        c = editor.text.get(x)

        # AutoClosing Brackets
        if c == "[":
            print("]")
            editor.text.insert(tt,"]")
        elif c == "{":
            editor.text.insert(tt, "}")
        elif c == "(":
            editor.text.insert(tt, ")")

    # It stores last typed line in the form of string
    last_typed = editor.text.get(str(float(editor.text.index('current')) - 1), editor.text.index('current'))
    if(len(last_typed) == 0):
        return
    if last_typed[0] in [' ', '\t', '\n', '{', '}', ',', '.', '/', '[', ']']:
        for _ in components_to_remove:
            _.destroy()
        components_to_remove.clear()
    last_typed = last_typed[::-1]

    # cmp will store the last typed word
    cmp = ""
    for _ in last_typed:
        if _ in [' ', '\t', '\n', '{', '}', ',', '.', '/', '[', ']'] :
            break
        cmp += _

    # Call for prefix search in the trie tree
    t.printAutoSuggestions(cmp[::-1])

    # This part deals with auto-coloring using python-tags
    for _ in dicc:
        ss=_[0]
        colo=_[1]
        idx='1.0'
        while 1:
            idx = text_widget.text.search(ss,idx,nocase=str(math.floor(float(editor.text.index('current')))),stopindex=END)
            if not idx:
                break
            lastidx = '%s+%dc' % (idx, len(ss))
            text_widget.text.tag_add(ss, idx, lastidx)    # Attaching tag to a particular word
            idx = lastidx
        text_widget.text.tag_config(ss, foreground=colo)  # Configuring tags

def change_color(k):
    global editor
    editor.text.configure(bg = color[k], fg = color[1 - k], insertbackground=color[1 - k])

def open_file():
    root.filename=filedialog.askopenfilename(title="Select file to open",filetypes=(("Text Files","*txt"),("C++ Files","*.cpp"),("Python Files","*.py"),("html Files","*.html"),("Java Files","*.java")))
    file_ = open(root.filename,'r')
    file_data = file_.read()
    editor.text.insert(END,file_data)

def startup_code():
    file_ = open("code_database.cpp", 'r')
    file_data = file_.read()
    editor.text.insert(END, file_data)
    sample = open('input.txt', 'w')
    f = ""
    print(f, file=sample)
    sample.close()
    sample = open('requiredop.txt', 'w')
    print(f, file=sample)
    sample.close()

def close_editor():
    global test_case_cnt
    for _ in range(100):
        s="input"+str(_)+".txt"
        t="requiredop"+str(_)+".txt"
        if os.path.exists(s):
            os.remove(s)
        if os.path.exists(t):
            os.remove(t)
    x = editor.text.get("1.0", END)
    file_ = open("code_database.cpp", 'w')
    file_.write(x)
    file_.close()
    root.quit()

def save():
    x = editor.get("1.0", END)
    file_ = open("code_database.cpp", 'w')
    file_.write(x)
    file_.close()

def load_template():
    file_ = open("template.cpp", 'r')
    file_data = file_.read()
    editor.text.insert(END, file_data)
    file_.close()

def add_testcase():
    x = str(add_input.text.get("1.0", END))
    y = str(add_output.text.get("1.0", END))
    global test_case_cnt
    test_case_cnt += 1
    file_name = "input" + str(test_case_cnt) + ".txt"
    sample = open(file_name, 'w+')
    print(x, file=sample)
    sample.close()
    file_name = "requiredop" + str(test_case_cnt) + ".txt"
    sample = open(file_name, 'w+')
    print(y, file=sample)
    sample.close()

# Function which compares output with required output
def check_answer(f1,c):
    f1=open(f1, "r")
    f2 = open("output.txt", "r")
    file_data = f2.read()
    f2.close()
    s="Testcase "+str(c)+":\n"
    result.text.insert(END,s)
    result.text.insert(END, file_data)
    f2 = open("output.txt", "r")
    i=0
    fl=0
    for x in f1:
        i+=1
        for y in f2:
            if(x!=y):
                s="Wrong answer!!! On line "+str(i)+" of testcase "+str(c)
                s += '\n'
                result.text.insert(END,s)
                s="Required: "+str(x[:-1])
                s+='\n'
                result.text.insert(END, s)
                s="Found: "+str(y)
                s += '\n'
                result.text.insert(END, s)
                fl=1
    if fl==0:
        s="Correct Answer"
        s+='\n'
        s+='\n'
        result.text.insert(END,s)

# Run code using Terminal, here using g++ command, with pipped input and output files
def run_code():
    result.text.delete("1.0", "end")
    x = editor.text.get("1.0", END)
    file_ = open("code_database.cpp", 'w')
    file_.write(x)
    file_.close()
    os.system("g++ code_database.cpp")
    global test_case_cnt
    for _ in range(1,test_case_cnt+1):
        s="./a.out "+"<input"+str(_)+".txt >output.txt"
        os.system(s)
        s="requiredop"+str(_)+".txt"
        check_answer(s,_)
    result.text.insert(END, "Process Finshed...\n")

# This part of the code if submitting Code on Codeforces at given xpath and URL
def subb():
    # Saving the code in file, here we will submit our code in .cpp file
    x = editor.text.get("1.0", END)
    file_ = open("code_database.cpp", 'w')
    file_.write(x)
    file_.close()
    prblm=prblm_id.get("1.0",END)      # Problem ID
    cntst = cntst_id.get("1.0", END)   # Contest ID
    linkk="https://codeforces.com/problemset/problem/"+cntst+'/'+prblm   # Link to the actual problem
    pathh="/home/ankit-sharma/Documents/CodeCaker/code_database.cpp"     # Path of the code file of editor (to be submitted)
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=/home/ankit-sharma/.config/google-chrome/Default")
    driver = webdriver.Chrome(executable_path='/home/ankit-sharma/Downloads/chromedriver',chrome_options=options)
    language = "GNU G++17 7.3.0"     # language selection
    driver.get(linkk)                # driver.get(link)
    js = "var op = document.getElementsByTagName('option');for(var i=0;i<op.length;i++){if(op[i].innerHTML == arguments[0]){op[i].setAttribute('selected','selected');}}"
    driver.execute_script(js, language)    # Excecuting the above script
    dropFileArea = driver.find_element_by_xpath("//input[@name='sourceFile']")    # Inserting code file at particualar xpath
    dropFileArea.send_keys(pathh)
    driver.find_element_by_xpath("//input[@value='Submit']").click()    # Click on submit Button

# This is the Top Menubar (Navigation Bar)
def menubar():
    topMenuBar = Menu(root)
    root.config(menu = topMenuBar)
    topMenuBar.config(bg="#44464a",fg="white")
    fileMenu = Menu(topMenuBar, tearoff = "False")
    topMenuBar.add_cascade(label = "File", menu = fileMenu)
    fileMenu.add_command(label = "Open",command=open_file)
    fileMenu.add_command(label = "Save",command=save)
    fileMenu.add_command(label = "Exit", command = close_editor)

    editMenu = Menu(topMenuBar, tearoff = "False")
    topMenuBar.add_cascade(label = "Edit", menu = editMenu)
    editMenu.add_command(label = "Cut")
    editMenu.add_command(label = "Copy")
    editMenu.add_command(label = "Paste")
    editMenu.add_command(label = "Undo")
    editMenu.add_command(label = "Redo")

    findMenu = Menu(topMenuBar, tearoff = "False")
    topMenuBar.add_cascade(label = "Find", menu = findMenu)
    findMenu.add_command(label = "Find")
    findMenu.add_command(label = "Find Next")
    findMenu.add_command(label = "Find and Replace")

    viewMenu = Menu(topMenuBar, tearoff = "False")
    topMenuBar.add_cascade(label = "View", menu = viewMenu)
    viewMenu.add_command(label = "Fullscreen")
    viewMenu.add_command(label = "Hide Menu")

    themeMenu = Menu(topMenuBar, tearoff="False")
    topMenuBar.add_cascade(label="Theme", menu=themeMenu)
    themeMenu.add_command(label="Dark",command=(lambda :change_color(0)))
    themeMenu.add_command(label="Light",command=(lambda :change_color(1)))
    topMenuBar.add_command(label="Template",command=load_template)
    topMenuBar.add_command(label="Run",command=run_code)
    topMenuBar.add_command(label="Submit",command=subb)

# The below 3 classes are used for making the Editor (The most Important part of this project)

# This class is helpful to bind line number to the left of our text editor, here we are using tkcanvas
class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        self.delete("all")
        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill = "white")
            i = self.textwidget.index("%s+1line" % i)

class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)
        if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")
        return result

# This is the Important class, as our editor is of this type, it contains Text Box + Line Numbers + Scroll Bars.
class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "128", "bold"))
        self.linenumbers = TextLineNumbers(self, width=26, bg = color[0])
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        # The below _on_change function is bunded to the textbox
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    # Whenever we do any changes in the textbox, lines numbers are changed accordingly, by calling the redraw function
    def _on_change(self, event):
        self.linenumbers.redraw()

# The part below this area is mainly consisting of GUI, not much logical thinking below, proceed only if you are interested
# Main frame, on which all the components are lying
main_frame = Frame(root)
main_frame.pack(fill=BOTH,expand=YES)
main_frame.configure(bg="#323454")

code_label = Label(main_frame,height=1,font=("UBUNTU",14), bg="white",fg=color[0],text=" Code ")
code_label.place(x=15,y=8)

# Intialising Editor
editor = Example(root)
editor.pack(side="top", fill="both", expand=True)
editor.place(x=13,y=40)
editor.text.configure(width=80,height=30,font=("CONSOLAS",16),bg=color[0],wrap="none",undo=True,fg=color[1], insertbackground="white")
editor.text.bind("<KeyRelease>", lambda event: on_key_release(editor))   # Binding function for each change
editor.text.bind("<Enter>", lambda event: on_key_release(editor))        # Binding function for ENTER press

startup_code()   # On start of the editor the code from history is restored from the database file

# These text boxes take input for problem id and contest id
cntst_id = Text(main_frame,width=10,height=1,font=("UBUNTU",14),bg=color[0],fg="white",wrap="none",insertbackground=color[1])
prblm_id = Text(main_frame,width=10,height=1,font=("UBUNTU",14),bg=color[0],fg="white",wrap="none",insertbackground=color[1])
cntst_id.place(x=1350,y=20)
prblm_id.place(x=1350,y=60)

cntst_id_label = Label(main_frame,height=1,font=("UBUNTU",14), bg="white",fg=color[0],text="Contest ID  ")
prblm_id_label = Label(main_frame,height=1,font=("UBUNTU",14), bg="white",fg=color[0],text="Problem ID ")
cntst_id_label.place(x=1232,y=22)
prblm_id_label.place(x=1233,y=60)

# This button call the parsing function on getting clicked
parse_button = Button(main_frame,command=parse,font=("UBUNTU",14),text="Parse",height=1,bd=1, fg="black",bg="white")
parse_button.place(x=1480,y=40)

# To input more text cases this text box is used, this is of same datatype of editor
add_input = Example(root)
add_input.text.configure(height=10,width=34,wrap="none",bd=1, bg=color[0], fg=color[1],undo=True, insertbackground="white")
add_input.place(x=1135, y=160)

# To output more text cases this text box is used, this is of same datatype of editor
add_output = Example(root)
add_output.text.configure(height=10,width=34,wrap="none",bd=1, bg=color[0],fg=color[1],undo=True, insertbackground="white")
add_output.place(x=1500, y=160)

add_input_label = Label(main_frame,height=1,font=("UBUNTU",12), fg="black",bg="white",text="Input")
add_output_label = Label(main_frame,height=1,font=("UBUNTU",12),fg="black",bg="white",text="Expected Output")
add_input_label.place(x=1135,y=133)
add_output_label.place(x=1500,y=133)

# Add testcase button
add_button = Button(main_frame,command=add_testcase,text="Add Test Case to checker",height=1,fg="black",bg="white")
add_button.place(x=1625,y=440)

autocomplete = Label(main_frame,height=1,font=("UBUNTU",14), fg="black",bg="white",text="Suggestions -- ")
autocomplete.place(x=13,y=850)

result_head = Label(main_frame,height=1,font=("UBUNTU",14),fg="black",bg="white",text="Result")
result_head.place(x=1135,y=500)

# Result on running the test cases is shown here, same datatype as of Editor
result = Example(root)
result.text.configure(width=64,height=13,font=("CONSOLAS",13),bg=color[0],wrap="none",fg=color[1],undo=True,insertbackground=color[1])
result.place(x=1135,y=530)

# Calling the Menubar
menubar()
root.mainloop()