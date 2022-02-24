# Author: Wladimir Ponomarenko
# main entry point
# calls main program gui


from tkinter import *
import tkinter.messagebox
import pdf_loader as pl
import result_reader as rr

msg = 'Idle'

win = Tk()
win.title('SLR helper tool')
win.geometry('800x600')

def screening():
    res = tkinter.messagebox.askquestion('askquestion', 'You are about to start screening. This might take a while. Do you want to proceed?')
    if res == 'yes':
        results.delete(0, END)
        pl.screen()
        results.insert(END, 'Done!')
    else:
        pass
    

def load_ok():
    res = rr.ok()
    results.delete(0, END)
    i = 1
    results.insert(0, 'Accepted documents:')
    if len(res) == 0:
        results.insert(1, 'The list is empty')
    else :
        
        for item in res:
            results.insert(i, item)
            i += 1

def load_no():
    res = rr.no()
    results.delete(0, END)
    i = 1
    results.insert(0, 'Declined documents:')
    if len(res) == 0:
        results.insert(1, 'The list is empty')
    else :
        for item in res:
            results.insert(i, item)
            i += 1

def load_maybe():
    res = rr.maybe()
    results.delete(0, END)
    i = 1
    results.insert(0, 'Documents to be manually reviewed:')
    if len(res) == 0:
        results.insert(1, 'The list is empty')
    else :
        for item in res:
            results.insert(i, item)
            i += 1

def load_uk():
    res = rr.uk()
    results.delete(0, END)
    i = 1
    results.insert(0, 'Documents with unknown format or language:')
    if len(res) == 0:
        results.insert(1, 'The list is empty')
    else :
        for item in res:
            results.insert(i, item)
            i += 1


btn=Button(win, text="Start pdf screening", width=50, height=3,command=screening)
btn.pack( side = TOP)

btn=Button(win, text="Show accepted documents", width=50, height=3,command=load_ok)
btn.pack( side = TOP)

btn=Button(win, text="Show declined documents", width=50, height=3,command=load_no)
btn.pack( side = TOP)

btn=Button(win, text="Show documents to be checked manually", width=50, height=3,command=load_maybe)
btn.pack( side = TOP)

btn=Button(win, text="Show documents in unsupported languages or formats", width=50, height=3,command=load_uk)
btn.pack( side = TOP)

scroll = Scrollbar(win) 
scroll.pack( side = RIGHT, fill = Y ) 
results = Listbox(win, yscrollcommand = scroll.set, x=100 ) 
results.insert(END, msg) 
results.pack( side = LEFT, expand =True, fill = "both") 
scroll.config( command = results.yview ) 

win.mainloop()