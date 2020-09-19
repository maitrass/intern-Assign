from tkinter import *
from tkinter.messagebox import *
font=('Times New Roman',22,'bold')

def clear():
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)
def AC():
    textField.delete(0,END)

def click_btn_function(event):
    print("btn clicked")
    b=event.widget
    text=b['text']
    print(text)

    if text=='x':
        textField.insert(0,'*')
        return

    if text=='=':
        try:
            ex=textField.get()
            answer=eval(ex)
            textField.delete(0,END)
            textField.insert(0,answer)
        except Exception as e:
            print("Error",e)
            showerror("Error",e)
        return
    textField.insert(END,text)

window=Tk()
window.title('Calculator')
window.geometry('600x450')



#textfield
textField =Entry(window,font=font,justify=CENTER)
textField.pack(side=TOP,pady=15,fill=X,padx=15)

#Buttons
buttonFrame=Frame(window)
buttonFrame.pack(side=TOP,pady=15)
#adding Button
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn1 = Button(buttonFrame, font=font, text=str(temp),width=4, activebackground='blue',activeforeground='white')
        btn1.grid(row=i,column=j, padx=5, pady=5)
        temp=temp+1
        btn1.bind('<Button--1>',click_btn_function)


btnZero= Button(buttonFrame, font=font, text=0, width=4, activebackground='blue',activeforeground='white')
btnZero.grid(row=3,column=0, padx=5, pady=5)
btnZero.bind('<Button--1>', click_btn_function)

btnDot= Button(buttonFrame, font=font, text='.',width=4, activebackground='blue',activeforeground='white')
btnDot.grid(row=3,column=1, padx=5, pady=5)
btnDot.bind('<Button--1>', click_btn_function)

btnequal= Button(buttonFrame, font=font, text='=', width=4, activebackground='blue',activeforeground='white')
btnequal.grid(row=3,column=2, padx=5, pady=5)
btnequal.bind('<Button--1>', click_btn_function)

btnclear= Button(buttonFrame, font=font, text='<--', width=9, activebackground='blue',activeforeground='white',command=clear)
btnclear.grid(row=4,column=0, columnspan=2)


btnAC= Button(buttonFrame, font=font, text='AC', width=9, activebackground='blue',activeforeground='white',command=AC)
btnAC.grid(row=4,column=2, columnspan=2)

btnpluse= Button(buttonFrame, font=font, text='+', width=4, activebackground='blue',activeforeground='white')
btnpluse.grid(row=0,column=3, padx=5, pady=5)
btnpluse.bind('<Button--1>', click_btn_function)

btnsub= Button(buttonFrame, font=font, text='-', width=4, activebackground='blue',activeforeground='white')
btnsub.grid(row=1,column=3, padx=5, pady=5)
btnsub.bind('<Button--1>',click_btn_function)

btnmult= Button(buttonFrame, font=font, text='*', width=4, activebackground='blue',activeforeground='white')
btnmult.grid(row=2,column=3, padx=5, pady=5)
btnmult.bind('<Button--1>', click_btn_function)

btndivision= Button(buttonFrame, font=font, text='/', width=4, activebackground='blue',activeforeground='white')
btndivision.grid(row=3,column=3, padx=5, pady=5)
btndivision.bind('<Button--1>', click_btn_function)



window.mainloop()