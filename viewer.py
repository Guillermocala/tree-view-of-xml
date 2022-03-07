from tkinter import *
from tkinter import ttk, messagebox

class AppXmlInPy(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("XML viewer")
        main_window.geometry("500x500")
        self.treeview = ttk.Treeview(self)
        self.my_iid = "id_unico"        
        self.my_courses = ["Curso_a", "Curso_b", "Curso_c"]
        self.my_courses_id = ["Curso_a1", "Curso_b2", "Curso_c3"]
        self.add_tree("", self.my_courses, self.my_courses_id)

        self.my_course_a = ["Estudiante 1", "Estudiante 2", "Estudiante 3"]
        self.my_course_a_id = ["Estudiante1a", "Estudiante2a", "Estudiante3a"]
        self.add_tree("Curso_a1", self.my_course_a, self.my_course_a_id)

        self.my_course_b = ["Estudiante 1", "Estudiante 2", "Estudiante 3"]
        self.my_course_b_id = ["Estudiante1b", "Estudiante2b", "Estudiante3b"]
        self.add_tree("Curso_b2", self.my_course_b, self.my_course_b_id)

        self.my_course_c = ["Estudiante 1", "Estudiante 2", "Estudiante 3"]
        self.my_course_c_id = ["Estudiante1c", "Estudiante2c", "Estudiante3c"]
        self.add_tree("Curso_c3", self.my_course_c, self.my_course_c_id)
        
        
        
        self.treeview.pack(fill = BOTH, expand = True)
        self.show_children()
        self.pack(fill = BOTH, expand = True)

    def add_tree(self, parent, text, iid):
        for item in range(len(text)):
            self.treeview.insert(parent, END, text=text[item], iid=iid[item])

    def show_children(self):
        treeview_children = self.treeview.get_children()
        print(treeview_children)

root = Tk()
app = AppXmlInPy(root)
app.mainloop()