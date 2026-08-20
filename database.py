import sqlite3

def conectar():
    conn = sqlite3.connect("escola.db") 
    return conn 
                        
def criar_tabela():

    conn = conectar() 
    cursor = conn.cursor()  
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            xuxu REAL) 
    """) 
    conn.commit()   
    conn.close()



def criar_aluno(nome: str, idade, nota):
   
    if nome.strip() == "":
        return "nome de aluno não pode ficar em branco"

    elif idade > 22:
        return "idade acima de 22 anos"
    
    else:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO alunos(nome, idade, nota) VALUES(?, ?, ?)",(nome, idade, nota))
        
        conn.commit()
        conn.close()
        return "aluno cadastrado com sucesso!"

def deletar_aluno(ID):
    if ID > 0:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM alunos WHERE ID=?", (ID,))

        conn.commit()
        conn.close()

        return f"o aluno de id {ID} foi deletado"
       
    else:
        return "ID inválido"




 
#READ= retornar na tela as infos que foram colocadas no create
def buscar_aluno(nome):
    conn = conectar()   
    cursor = conn.cursor()
# o 'select*from( o asteristico é todos os campos)/where' diz que= selecione todos os campos onde nome=?(?= o que eu nao sei)
    cursor.execute("SELECT * FROM alunos WHERE nome = ?", (nome))

    conn.commit()
    conn.close()

#UPDATE= modificar o que tava la em cima 
def editar_aluno(ID,nome,idade, nota):
    conn = conectar() 
    cursor = conn.cursor()
# o 'update/set/where' esta dizendo= atualize a tabela alunos fazendo nome=? (?=nao sabemos oq é), idade=? e nota=? para quem tiver o id=?
    cursor.execute("UPDATE alunos SET nome = ?, idade=?, nota=? WHERE ID=?", (nome, idade, nota, ID) )

    conn.commit()
    conn.close()

#DELETE= deletar tudo o que fez 
def excluir_aluno(ID):
    conn = conectar()
    cursor = conn.cursor()
# o 'delete from/where' diz que= deletar a linha da tabela alunos onde o id=?(?= o que eu nao sei)
    cursor.execute("DETELE FROM alunos WHERE id=?", (ID))

    conn.commit()
    conn.close()
