import tkinter as t

r=t.Tk()  
r.title("CalC")
r.configure(bg='#000000')

x=t.Entry(r,width=30,borderwidth=5) 
x.grid(row=0,column=0,columnspan=4)  
r.config(bg="#1e2f45")   


def click(n):
     c=x.get()
     x.delete(0,t.END)
     x.insert(0,c+str(n))
     
def clear():
    x.delete(0,t.END)
    
def equalto():
    try:
        result=eval(x.get())
        x.delete(0,t.END)
        x.insert(0,result)
    except Exception:
        x.delete(0,t.END)
        x.insert(0,"ERROR")
        
button=[("7",1,0),("8",1,1),("9",1,2),("+",1,3),
        ("4",2,0),("5",2,1),("6",2,2),("-",2,3),
        ("1",3,0),("2",3,1),("3",3,2),("/",3,3),
        ("0",4,0),(".",4,1),("*",4,3),
        ("C",5,0),("=",5,1)]

for (text,row,col) in button:
    if text=='=':
        t.Button(r,bg="#8fffbc",text=text,width=9,command=equalto).grid(row=row,column=col)
    elif text=='C':
        t.Button(r,bg="#f5426f",text=text,width=9,command=clear).grid(row=row,column=col)
    else:
        t.Button(r,bg='#8fbfff',text=text,width=9,height=2,command=lambda tk=text:click(tk)).grid(row=row,column=col)

r.mainloop()