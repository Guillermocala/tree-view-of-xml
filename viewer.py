from tkinter import *
from tkinter import ttk
root = Tk()
root.title("XML viewer")
root.geometry("500x500")

arbol = ttk.Treeview(root)
"""ingreso grados"""
grado_a = arbol.insert("", END, text="grado_a")
grado_b = arbol.insert("", END, text="grado_b")
grado_c = arbol.insert("", END, text="grado_c")
"""ingreso grado_a"""
grado_a_estudiante_1 = arbol.insert(grado_a, END, text="estudiante1")
grado_a_estudiante_2 = arbol.insert(grado_a, END, text="estudiante2")
grado_a_estudiante_3 = arbol.insert(grado_a, END, text="estudiante3")
"""ingreso grado_b"""
grado_b_estudiante_1 = arbol.insert(grado_b, END, text="estudiante1")
grado_b_estudiante_2 = arbol.insert(grado_b, END, text="estudiante2")
grado_b_estudiante_3 = arbol.insert(grado_b, END, text="estudiante3")
"""ingreso grado_c"""
grado_c_estudiante_1 = arbol.insert(grado_c, END, text="estudiante1")
grado_c_estudiante_2 = arbol.insert(grado_c, END, text="estudiante2")
grado_c_estudiante_3 = arbol.insert(grado_c, END, text="estudiante3")


arbol.pack()



root.mainloop()