import streamlit as st
import database as db
import base64

db.criar_tabela()

st.title("esse é um título")
st.header("esse é um cabeçalho")
st.subheader("esse é um cabeçalho menor")

with st.form("nome_do_formulario"):

    nome = st.text_input("nome")
    idade = st.number_input("idade",value=50)
    xuxu = st.text_input("cargo")
    dt_nascimento = st.date_input("data de nascimento",value="today")
    

    btn_form = st.form_submit_button("botão?")


if btn_form:
    st.write(f"o seu nome é:{nome}")
    st.write(f"a sua idade é:{idade}")
    st.write(f"o seu cargo é:{xuxu}")
    st.write(f"seu aniversário é:{dt_nascimento}")
            
    
st.markdown(
    """
    <style>
    .stpython-senai {
        background-image: url("https://i.pinimg.com/736x/0b/a4/3e/0ba43e4fed49f5c1a61d007784f80490.jpg");
        background-size: cover;
    }
    </style>
    <div class="stpython-senai">
    </div>
    """,
    unsafe_allow_html=True,        
)
 