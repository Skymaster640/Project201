from tkinter import *
window = Tk()

window.title("Interest Calculator")
window.geometry("380x400")
window.configure(bg="blue")

def interestcalculate():
    p = float(principle_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100
    interest = round(i,2)
    showlabel=Label(result_frame,text="Your result will be displayed here",bg="grey",font=("Calibri",12),width=55)
    showlabel.place(x=20,y=20)
    showlabel.pack()

    message=Label(result_frame,text="Interest on ??."+str(p)+"at rate of interest "+str(r)+"X for "+str(t)+" years is ??."+str(interest),bg="grey",font=("Calibri",12),width=55)
    message.place(x=20,y=40)
    message.pack()
    showlabel.destroy()

result_frame = LabelFrame(window,text="Result",bg="grey",font=("Calibri",12))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)


principle_label=Label(window,text="Enter principle in dollars",fg="green",bg="red",font=("Calibri",12))
principle_label.place(x=20,y=100)

principle_entry=Entry(window,text="",bd=2,width=15)
principle_entry.place(x=190,y=102)

rate_label=Label(window,text="Enter rate in dollars",fg="green",bg="red",font=("Calibri",12))
rate_label.place(x=20,y=140)

rate_entry=Entry(window,text="",bd=2,width=15)
rate_entry.place(x=150,y=142)

time_label=Label(window,text="Enter time in years",fg="green",bg="red",font=("Calibri",12))
time_label.place(x=20,y=185)

time_entry=Entry(window,text="",bd=2,width=15)
time_entry.place(x=150,y=187)

calculate_button = Button(window,text="Calculate BMI",bg="red",fg="green",bd=4,command=interestcalculate)
calculate_button.place(x=20,y=250)

window.mainloop()