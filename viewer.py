"""This code is based on Intermezzo coding style
-check it out: https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style
"""

from tkinter import *
from tkinter import ttk
import xml.etree.ElementTree as ET

class AppXmlInPy(ttk.Frame):

    def __init__(self, main_window):
        
        super().__init__(main_window)
        main_window.title("XML viewer")
        main_window.geometry("500x500")
        "el selectmode es para que solo deje selecciona 1 a la vez"
        self.treeview = ttk.Treeview(self, selectmode=BROWSE)
        "invocamos la raiz con el ET parse y el getroot()"
        self.tree = ET.parse('./xml/breakfast_menu.xml')
        self.raiz = self.tree.getroot()
        "icons time!"
        self.icon_folder = PhotoImage(file="./icons/folder.png")
        self.icon_file = PhotoImage(file="./icons/file.png")
        "aqui insertamos el primer tag y lo guardamos como referencia para insertar lo demas"
        self.nodo_principal = self.treeview.insert("", END, None, text=self.raiz.tag, image=self.icon_folder)
        "esa raiz se la pasamos a la funcion que dibujara el arbol"
        self.insert_treeview(self.raiz, parent=self.nodo_principal)
        "opciones para visualizar mejor el treeview"
        self.treeview.pack(fill = BOTH, expand = True)
        self.pack(fill = BOTH, expand = True)
    
    def insert_treeview(self, raiz, parent=""):
        "recorremos la raiz"
        for child in raiz:
            node_name = child.tag
            item = self.treeview.insert(parent, END, None, text=node_name, image=self.icon_folder)
            if len(child) > 0:
                "si tiene hijos volvemos a invocar"
                self.insert_treeview(child, parent=item)
            else:
                """si no tiene hijos solo insertamos pero con el text
                se supone que el ultimo nivel es donde se guardan los valores en el
                campo de texto"""
                if(child.text != None):
                    self.treeview.insert(item, END, None, text=child.text, image=self.icon_file)

main_window = Tk()
app = AppXmlInPy(main_window)
app.mainloop()