from tkinter import *
from tkinter import ttk

root = Tk()
root.title("XML viewer")
root.geometry("500x500")

arbol = ttk.Treeview(root)

def ingresa_arbol(parent, listaTexto):
    for item in listaTexto:
        arbol.insert(parent, END, text=item)


"""ingreso grados"""
grado_a = arbol.insert("", END, text="grado_a")
grado_b = arbol.insert("", END, text="grado_b")
grado_c = arbol.insert("", END, text="grado_c")
"""ingreso grado_a"""
grado_a_estudiantes = ["estudiante1", "estudiante2", "estudiante3"]
ingresa_arbol(grado_a, grado_a_estudiantes)
"""ingreso grado_b"""
grado_b_estudiantes = ["estudiante1", "estudiante2", "estudiante3"]
ingresa_arbol(grado_b, grado_a_estudiantes)
"""ingreso grado_c"""
grado_c_estudiantes = ["estudiante1", "estudiante2", "estudiante3"]
ingresa_arbol(grado_c, grado_c_estudiantes)


arbol.pack(fill = BOTH, expand = True)



root.mainloop()