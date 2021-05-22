from tkinter import *
import re
import urllib.request
from bs4 import BeautifulSoup
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from selenium import webdriver
import os

root = Tk()
root.title('CodeCaker Editor')
root.geometry("1200x660")
root["bg"]="black"
root.configure(background='black')
color = ["#282a36","white","blue","green","black","#201F2D"]

test_case_cnt=0

dicc=[["for","#0C29FA"],["#include", "#0C29FA"],["#define ", "#0C29FA"],["=", "#0C29FA"],["-", "#0C29FA"],["+", "#0C29FA"],["/", "#0C29FA"], ["*", "#0C29FA"],    [">", "#0C29FA"],    ["<", "#0C29FA"],    ["const ", "#0C29FA"],    ["using ", "#0C29FA"],    ["namespace ", "#0C29FA"],    [". ", "#0C29FA"],    ["if", "#0C29FA"],    ["else", "#0C29FA"],    ["#ifndef ", "#0C29FA"],    [":","#0C29FA"],    ["while", "#0C29FA"],    ["do", "#0C29FA"],    ["return ", "#0C29FA"],    ["size", "#FD4381"],    ["begin", "#FD4381"],    ["end", "#FD4381"],    ["forr", "#FD4381"],    ["all", "#FD4381"],    ["sz", "#FD4381"],    ["solve", "#FD4381"],    ["push_back", "#FD4381"],    ["pop_back", "#FD4381"],    ["__gcd", "#FD4381"],    ["ios_base::sync_with_stdio", "#FD4381"],    ["tie", "#FD4381"],    ["main", "#FD4381"],    ["0", "#A03B9D"],    ["1", "#A03B9D"],    ["2", "#A03B9D"],    ["3", "#A03B9D"],    ["4", "#A03B9D"],    ["5", "#A03B9D"],    ["6", "#A03B9D"],    ["7", "#A03B9D"],    ["8", "#A03B9D"],    ["9", "#A03B9D"],    ["int ", "#EE7521"],    ["string ", "#EE7521"],    ["char ", "#EE7521"],    ["void ", "#EE7521"],    ["long ", "#EE7521"],    ["double ", "#EE7521"],["abs", "#EE7521"],    ["signed ", "#EE7521"],    ["freopen", "#EE7521"],    ["auto ", "#EE7521"],    ["bool ", "#EE7521"],    ["<bits/stdc++.h>", "#EE7521"],    ["#endif", "#0C29FA"],    ["Correct Answer","#FD4381"],["Wrong answer!!!","#E5071B"]]

def on_key_release(text_widget):
    for _ in dicc:
        ss=_[0]
        colo=_[1]
        idx='1.0'
        while 1:
            idx = text_widget.search(ss,idx,nocase=1,stopindex=END)
            if not idx:
                break
            lastidx = '%s+%dc' % (idx, len(ss))
            text_widget.tag_add(ss, idx, lastidx)
            idx = lastidx
        text_widget.tag_config(ss, foreground=colo)

def change_color(k):
    global editor
    if(k==0):
        editor.configure(bg=color[k],fg=color[1],insertbackground=color[1])
    elif(k==1):
        editor.configure(bg=color[k], fg=color[0],insertbackground=color[0])
    else:
        editor.configure(bg=color[k], fg=color[0],insertbackground=color[0])


def open_file():
    root.filename=filedialog.askopenfilename(title="Select file to open",filetypes=(("Text Files","*txt"),("C++ Files","*.cpp"),("Python Files","*.py"),("html Files","*.html"),("Java Files","*.java")))
    file_ = open(root.filename,'r')
    file_data = file_.read()
    editor.insert(END,file_data)


def startup_code():
    file_ = open("code_database.cpp", 'r')
    file_data = file_.read()
    editor.insert(END, file_data)
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
    x = editor.get("1.0", END)
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
    editor.insert(END, file_data)
    file_.close()


def add_testcase():
    x = str(add_input.get("1.0", END))
    y = str(add_output.get("1.0", END))
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


def parse():
    x = str(cntst_id.get("1.0",END))
    y = str(prblm_id.get("1.0",END))
    x=x[:-1]
    y=y[:-1]
    html = urllib.request.urlopen('https://codeforces.com/problemset/problem/' + x + '/' + y)
    soup = BeautifulSoup(html)
    data = soup.findAll(text=True)
    def visible(element):
        if element.parent.name in ['style', 'script', '[document]','head', 'title']:
            return False
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True
    result = list(filter(visible, data))
    x = 0
    for _ in range(len(list(result)) - 5):
        if (list(result)[_] == 'Example' and list(result)[_ + 1]
                =='Input'):
            x = _+2
            break
    global test_case_cnt
    test_case_cnt+=1
    file_name = "input"+str(test_case_cnt)+".txt"
    sample = open(file_name, 'w+')
    f = str(result[x][1:])
    print(f, file=sample)
    print(f)
    sample.close()
    file_name = "requiredop" + str(test_case_cnt) + ".txt"
    sample = open(file_name, 'w+')
    f = str(result[x + 2][1:])
    print(f, file=sample)
    print(f)
    sample.close()


def check_answer(f1,c):
    f1=open(f1, "r")
    f2 = open("output.txt", "r")
    file_data = f2.read()
    f2.close()
    s="Testcase "+str(c)+":\n"
    result.insert(END,s)
    result.insert(END, file_data)
    f2 = open("output.txt", "r")
    i=0
    fl=0
    for x in f1:
        i+=1
        for y in f2:
            if(x!=y):
                s="Wrong answer!!! On line "+str(i)+" of testcase "+str(c)
                s += '\n'
                result.insert(END,s)
                s="Required: "+str(x[:-1])
                s+='\n'
                result.insert(END, s)
                s="Found: "+str(y)
                s += '\n'
                result.insert(END, s)
                fl=1
    if fl==0:
        s="Correct Answer"
        s+='\n'
        s+='\n'
        result.insert(END,s)


def run_code():
    result.delete("1.0", "end")
    x = editor.get("1.0", END)
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
    result.insert(END, "Process Finshed...\n")


def subb():
    x = editor.get("1.0", END)
    file_ = open("code_database.cpp", 'w')
    file_.write(x)
    file_.close()
    prblm=prblm_id.get("1.0",END)
    cntst = cntst_id.get("1.0", END)
    linkk="https://codeforces.com/problemset/problem/"+cntst+'/'+prblm
    pathh="/home/anjali/pythonProject1/code_database.cpp"
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=/home/anjali/.config/google-chrome/Profile 1")
    driver = webdriver.Chrome(executable_path='/home/anjali/Downloads/chromedriver',chrome_options=options)
    language = "GNU G++17 7.3.0"
    driver.get(linkk)
    js = "var op = document.getElementsByTagName('option');for(var i=0;i<op.length;i++){if(op[i].innerHTML == arguments[0]){op[i].setAttribute('selected','selected');}}"
    driver.execute_script(js, language)
    dropFileArea = driver.find_element_by_xpath("//input[@name='sourceFile']")
    dropFileArea.send_keys(pathh)
    driver.find_element_by_xpath("//input[@value='Submit']").click()

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
    themeMenu.add_command(label="Blue",command=(lambda :change_color(2)))
    themeMenu.add_command(label="Green",command=(lambda :change_color(3)))
    topMenuBar.add_command(label="Template",
                           command=load_template)
    topMenuBar.add_command(label="Run",command=run_code)
    topMenuBar.add_command(label="Submit",command=subb)


main_frame = Frame(root)
main_frame.pack(fill=BOTH,expand=YES)
main_frame.configure(bg="black")

text_scroll_Y = Scrollbar(main_frame)
text_scroll_X = Scrollbar(main_frame,orient='horizontal')

# editor = Text(main_frame,width=66,height=23,font=("UBUNTU",16),
#               bg=color[0],wrap="none",fg=color[1],undo=True,yscrollcommand=text_scroll_Y.set,insertbackground=color[1],xscrollcommand=text_scroll_X.set,bd=5)

editor = Text(main_frame,width=73,height=28,font=("CONSOLAS",14),
              bg="white",wrap="none",fg="black",undo=True,
              yscrollcommand=text_scroll_Y.set,
              xscrollcommand=text_scroll_X.set,bd=1)

editor.place(x=3,y=3)
editor.tag_configure("start", background="black", foreground="red")
editor.bind("<KeyRelease>", lambda event: on_key_release(editor))
editor.bind("<Enter>", lambda event: on_key_release(editor))

startup_code()

text_scroll_Y.pack(side=RIGHT,fill=Y)
text_scroll_X.pack(side=BOTTOM,fill=X)

text_scroll_Y.config(command=editor.yview)
text_scroll_X.config(command=editor.xview)

cntst_id = Text(main_frame,width=10,height=1,font=("UBUNTU",12),bg="white",fg="black",wrap="none")
prblm_id = Text(main_frame,width=10,height=1,font=("UBUNTU",12),bg="white",fg="black",wrap="none")
cntst_id.place(x=920,y=20)
prblm_id.place(x=920,y=50)

cntst_id_label = Label(main_frame,height=1,font=("UBUNTU",12), fg="white",bg="black",text="Contest ID")
prblm_id_label = Label(main_frame,height=1,font=("UBUNTU",12), fg="white",bg="black",text="Problem")
cntst_id_label.place(x=832,y=22)
prblm_id_label.place(x=833,y=50)

parse_button = Button(main_frame,command=parse,text="Parse",height=2,bd=1, fg="white",bg="black")
parse_button['background']="black"
parse_button.place(x=1037,y=20)

add_input = ScrolledText(root, height=10,width=28,wrap="none",bd=1, bg="white",fg="black")
add_input.place(x=835, y=130)

add_output = ScrolledText(root, height=10,width=28,wrap="none", bd=1,bg="white",fg="black")
add_output.place(x=1100, y=130)

add_input_label = Label(main_frame,height=1,font=("UBUNTU",12), fg="white",bg="black",text="Input")
add_output_label = Label(main_frame,height=1,font=("UBUNTU",12),
                         fg="white",bg="black",text="Expected Output")
add_input_label.place(x=910,y=103)
add_output_label.place(x=1150,y=103)

add_button = Button(main_frame,command=add_testcase,text="Add Test "
                                                         "Case to " \
                                            "checker",
                    height=1,fg="white",bg="black")
add_button.place(x=1130,y=320)

result_head = Label(main_frame,height=1,font=("UBUNTU",14),fg="white",bg="black",text="Result")
result_head.place(x=838,y=350)

result = ScrolledText(main_frame,width=47,height=12,font=("CONSOLAS",13),bg="white",wrap="none",fg="black",undo=True,yscrollcommand=text_scroll_Y.set,xscrollcommand=text_scroll_X.set)
result.place(x=840,y=374)

menubar()
root.mainloop()
