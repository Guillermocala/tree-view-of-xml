from tkinter import *
from tkinter import ttk, messagebox
import xml.etree.ElementTree as ET


tree = ET.parse('./xml/colegio.xml')
raiz = tree.getroot()

class AppXmlInPy(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("XML viewer")
        main_window.geometry("500x500")
        self.treeview = ttk.Treeview(self)
        
        self.lista1 = raiz.findall("./")
        print(self.lista1)

        self.add_tree("", self.lista1)
        
        
        self.treeview.pack(fill = BOTH, expand = True)
        self.pack(fill = BOTH, expand = True)

    def add_tree(self, parent, text):
        for item in range(len(text)):
            self.treeview.insert(parent, END, None, text=text[item].tag)

    def show_children(self):
        treeview_children = self.treeview.get_children()
        print(treeview_children)


root = Tk()
app = AppXmlInPy(root)
app.mainloop()