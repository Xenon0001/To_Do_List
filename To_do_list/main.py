# main.py
from tkinter import *
import customtkinter
import config
from database import init_db, guardar_en_db, eliminar_de_db, obtener_tareas

class ToDoList(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("To Do List")
        self.resizable(False, False)
        self.geometry(config.centrar_ventana(self, 700, 450))
        self.elementos_de_la_ventana_principal()
        self.mostrar_tareas()

    def elementos_de_la_ventana_principal(self):
        self.frame_padre = customtkinter.CTkFrame(self)
        self.frame_padre.pack()

        self.frame_top = customtkinter.CTkFrame(self.frame_padre)
        self.frame_top.pack(padx=10, pady=10, side='top', fill=BOTH, expand=True)
        
        self.frame_bottom = customtkinter.CTkFrame(self.frame_padre, width=600, height=350)
        self.frame_bottom.pack(side='bottom', fill=BOTH, expand=False)

        self.lblframe_cont_list = customtkinter.CTkFrame(self.frame_bottom, width=600, height=350)
        self.lblframe_cont_list.pack(side=BOTTOM, fill=BOTH, expand=False)
        self.lblframe_cont_list.pack_propagate(False)
        self.lblframe_cont_list.grid_propagate(False)

        btn_new_tarea = customtkinter.CTkButton(self.frame_top,
                                                text="Añadir tarea +",
                                                text_color='white', fg_color='black',
                                                width=13, font=('Georgia', 14), border_width=1,
                                                border_color='white', height=30, 
                                                command=self.abrir_toplevel)
        btn_new_tarea.pack(side=RIGHT)

    def abrir_toplevel(self):
        toplevel = TopLevelCall(self)
        toplevel.focus_force()
        toplevel.grab_set()

    def mostrar_tareas(self):
        for widget in self.lblframe_cont_list.winfo_children():
            widget.destroy()

        tareas = obtener_tareas()
        for tarea in tareas:
            lbl_frm_list = customtkinter.CTkFrame(self.lblframe_cont_list, width=600, height=35)
            lbl_frm_list.pack(padx=10)
            lbl_frm_list.pack_propagate(False)

            btn_list_title = customtkinter.CTkButton(lbl_frm_list, text=tarea[0], width=400, height=40)
            btn_list_title.pack(side=LEFT)

            elimina_tarea = customtkinter.CTkButton(lbl_frm_list, text='Borrar', fg_color="red",
                                                    hover_color="grey",
                                                    width=100, height=40, text_color='black',
                                                    command=lambda t=tarea: self.eliminar_tarea(t[0]))
            elimina_tarea.pack(side=RIGHT)

            edit_tarea = customtkinter.CTkButton(lbl_frm_list, text='Editar',
                                                 fg_color="lightgreen", 
                                                 hover_color="green",
                                                 width=100, height=40,
                                                 command=lambda t=tarea: self.abrir_editar_tarea(t[0], t[1]))
            edit_tarea.pack(padx=1, side=RIGHT)

    def eliminar_tarea(self, titulo):
        eliminar_de_db(titulo)
        self.mostrar_tareas()

    def abrir_editar_tarea(self, titulo_actual, definicion_actual):
        EditarTareaToplevel(self, titulo_actual, definicion_actual)

class TopLevelCall(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Crear tarea')
        self.resizable(False, False)
        self.geometry(config.centrar_ventana(self, 350, 330))
        self.frames_toplevel()

    def frames_toplevel(self):
        self.cont_toplevel = customtkinter.CTkFrame(self)
        self.cont_toplevel.pack()
        
        self.frm_toplevel_top = customtkinter.CTkFrame(self.cont_toplevel)
        self.frm_toplevel_top.pack(side=TOP, expand=True, pady=10)
        self.frm_toplevel_bottom = customtkinter.CTkFrame(self.cont_toplevel)
        self.frm_toplevel_bottom.pack(side=BOTTOM, padx=10, pady=10)

        self.frames_elementos()

    def frames_elementos(self):
        self.titulo_tarea = customtkinter.CTkEntry(self.frm_toplevel_top, width=200,
                                                   placeholder_text='Título de la tarea')
        self.titulo_tarea.pack(pady=5)
        
        self.definir_tarea = Text(self.frm_toplevel_bottom, height=10)
        self.definir_tarea.pack(pady=(5, 10))
        
        self.btn_guardar_tarea = customtkinter.CTkButton(self, text='Guardar', width=20,
                                                         command=self.guardar_tarea)
        self.btn_guardar_tarea.pack(pady=10)

    def guardar_tarea(self):
        titulo = self.titulo_tarea.get()
        definicion = self.definir_tarea.get('1.0', 'end-1c')
        
        guardar_en_db(titulo, definicion)
        
        self.destroy()
        self.master.mostrar_tareas()

# Similar changes can be applied to the EditarTareaToplevel class

if __name__ == '__main__':
    init_db()
    app = ToDoList()
    app.mainloop()
