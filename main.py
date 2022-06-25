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

# ===========================================================================================

# Primer input
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'texto:')

# Linea sobre el input
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

# ===========================================================================================

# Segundo input
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'texto2:')

# Linea sobre el input
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
# ===========================================================================================
number = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
number.place(x=30,y=220)
number.insert(0,'texto3:')

# Linea sobre el input
Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
# ===========================================================================================
method = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
method.place(x=30,y=290)
method.insert(0,'texto4:')

# Linea sobre el input
Frame(frame,width=295,height=2,bg='black').place(x=25,y=317)
# ============================================================================================
num = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
num.place(x=30,y=350)
num.insert(0,'texto5:')

# Linea sobre el input
Frame(frame,width=295,height=2,bg='black').place(x=25,y=377)

#============================================================================================

# Button
Button(frame,width=41,pady=7,text='Generar PDF',bg='#57a1f8',fg='white',border=0).place(x=35,y=395)


# Presentacion visual del codigo
root.mainloop()


