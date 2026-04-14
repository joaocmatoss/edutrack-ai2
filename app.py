import streamlit as st


st.set_page_config(page_title='edutrack AI', page_icon='📔')




st.title('📔 edutrack AI')

st.sidebar.header('menu')
opcoes_menu = st.sidebar.radio('navegar', ['dashboard','disciplinas','tarefas'])

#conteudo denamico
if opcoes_menu == 'dashboard':
    st.write('Bem-vindo ao seu assistente academico!')
    st.info('Conecte ao xano para ver seus dados reais')

    #exemplo de métrica de visual 
    col1, col2 = st.columns(2)
    col1.metric('Disciplinas ativadas', '0')
    col2.metric('Tarefas pendentes', '0')

elif opcoes_menu == 'disciplinas':
    st.subheader('minhas disciplinas')
    st.write('aqui listaremos as disciplinas cadastradas no backend')

else:
    st.subheader('gerenciamento de tarefas')
    st.checkbox('Exemplo: estudar python')
    st.checkbox('Exemplo: estudar streamlit')


