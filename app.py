import streamlit as st
import database as db


db.criar_tabela()

st.title("esse é um título")
st.header("esse é um cabeçalho")
st.subheader("esse é um cabeçalho menor")

with st.form("nome_do_formulario"):

    nome = st.text_input("nome")
    idade = st.number_input("idade",value=50)
    xuxu = st.text_input("cargo")
    
    

    btn_cadastro_aluno = st.form_submit_button("botão?", help= "botão?")


if btn_cadastro_aluno:
    msg = db.criar_aluno(nome, idade, xuxu)
    st.warning(msg)


with st.form("deleta_aluno"):
    id_aluno = st.number_input("id do aluno", value=0, step=1, min_value=0)

    btn_deleta_aluno = st.form_submit_button("deletar", help= "clica pra deletar?")


if btn_deleta_aluno:
    msg = db.deletar_aluno(id_aluno)
    st.success(msg)

