from tkinter import*
count=0
def click():
    global count
    count+=1
    label.config(text=count)
    label2.pack()

window = Tk()
button=Button(window,text='Button Here, Click Me!!')
button.config(command=click)
button.config(font=('Ink Free',50,'bold'))
button.config(bg='#fffb1f')
button.config(fg='#ff0000')
button.config(activebackground='#ff6200')
button.config(activeforeground='#ff0000')

label=Label(window,text=count)
label.pack()
button.pack()
label2=Label(window)
window.mainloop()