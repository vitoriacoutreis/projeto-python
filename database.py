import sqlite3

def conectar():
    conn = sqlite3.connect("escola.db")
    return conn

def criar_tabela():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            nota REAL)
    """)

    conn.commit()
    conn.close()