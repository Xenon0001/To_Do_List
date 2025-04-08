# database.py
import sqlite3
import config

def init_db():
    ruta_db = config.obtener_ruta_db()
    with sqlite3.connect(ruta_db) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                definicion TEXT NOT NULL
            )
        ''')
        conn.commit()

def guardar_en_db(titulo, definicion):
    ruta_db = config.obtener_ruta_db()
    with sqlite3.connect(ruta_db) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tareas (titulo, definicion) VALUES (?, ?)', (titulo, definicion))
        conn.commit()

def eliminar_de_db(titulo):
    ruta_db = config.obtener_ruta_db()
    with sqlite3.connect(ruta_db) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tareas WHERE titulo = ?', (titulo,))
        conn.commit()

def obtener_tareas():
    ruta_db = config.obtener_ruta_db()
    with sqlite3.connect(ruta_db) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT titulo, definicion FROM tareas')
        return cursor.fetchall()
