from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Diferencia finitas')
# Para editar el tamanno de la interfaz
root.geometry('925x550+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='logoAN.png')
Label(root,image=img,bg='white').place(x=50,y=50)

# Declaracion  donde ingresara los datos
frame=Frame(root,width=380,height=430,bg="white")
frame.place(x=480,y=70)

# Titulo del formulario
# fg = color
# bg = color de fondo
# font = fuente
heading=Label(frame,text='Texto',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=125,y=5)

#===========================================================================================
#Funciones limpieza
def user_input(e):
    user.delete(0,'end')

def code_input(e):
    code.delete(0,'end')

def number_input(e):
    number.delete(0,'end')

def num_input(e):
    num.delete(0,'end')

def method_input(e):
    method.delete(0,'end')


#Funciones para rellanar
def user_info(e):
    input = user.get()
    if input =='':
        user.insert(0,'texto:')

def code_info(e):
    input1 = code.get()
    if input1 =='':
        code.insert(0,'texto2:')


def number_info(e):
    input2 = number.get()
    if input2 =='':
        number.insert(0,'texto3:')


def method_info(e):
    input4 = method.get()
    if input4 == '':
        method.insert(0,'texto4:')

def num_info(e):
    input3 = num.get()
    if input3 == '':
        num.insert(0,'texto5:')


#Definicion de funcion para nueva GUI dentro de otra
def showPdf():
    input1 = user.get()
    input2 = code.get()
    input3 = number.get()
    input4 = method.get()
    input5 = num.get()

    print(len(input1))
    print(len(input2))


    #todo:realizar mas validaciones
    if len(input1)>5 and len(input2)>7:
        screen = Toplevel(root)
        screen.title("PDF")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        Label(screen,text='Hello Everyone',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()

# ===========================================================================================

# Primer input
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'texto')
user.bind('<FocusIn>',user_input)
user.bind('<FocusOut>',user_info)

# Linea sobre el input
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

# ===========================================================================================

# Segundo input
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'texto2:')
code.bind('<FocusIn>',code_input)
code.bind('<FocusOut>',code_info)

# Linea sobre el input
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
# ===========================================================================================
number = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
number.place(x=30,y=220)
number.insert(0,'texto3:')
number.bind('<FocusIn>',number_input)
number.bind('<FocusOut>',number_info)

# Linea sobre el input
Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
# ===========================================================================================
method = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
method.place(x=30,y=290)
method.insert(0,'texto4:')
method.bind('<FocusIn>',method_input)
method.bind('<FocusOut>',method_info)

# Linea sobre el input
Frame(frame,width=295,height=2,bg='black').place(x=25,y=317)
# ============================================================================================
num = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
num.place(x=30,y=350)
num.insert(0,'texto5:')
num.bind('<FocusIn>',num_input)
num.bind('<FocusOut>',num_info)

# Linea sobre el input
Frame(frame,width=295,height=2,bg='black').place(x=25,y=377)

#============================================================================================

# Button
Button(frame,width=41,pady=7,text='Generar PDF',bg='#57a1f8',fg='white',border=0,command=showPdf).place(x=35,y=395)




# Presentacion visual del codigo
root.mainloop()


