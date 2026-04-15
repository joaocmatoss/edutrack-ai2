import streamlit as st

st.set_page_config(page_title='edutrack AI', page_icon='📔')

if 'subjects' not in st.session_state:
    st.session_state.subjects = []

st.title('📔 edutrack AI')

st.sidebar.header('menu')
opcoes_menu = st.sidebar.radio('navegar', ['dashboard', 'disciplinas', 'tarefas'])

if opcoes_menu == 'dashboard':
    st.write('Bem-vindo ao seu assistente acadêmico!')
    st.info('Conecte ao xano para ver seus dados reais')
    col1, col2 = st.columns(2)
    col1.metric('Disciplinas ativadas', len(st.session_state.subjects))
    col2.metric('Tarefas pendentes', '0')

elif opcoes_menu == 'disciplinas':
    st.subheader('minhas disciplinas')
    st.write('aqui listaremos as disciplinas cadastradas no backend')

    with st.form('add_subject_form'):
        subject_name = st.text_input('Nome da disciplina')
        subject_teacher = st.text_input('Professor (opcional)')
        submitted = st.form_submit_button('Adicionar disciplina')

        if submitted:
            if subject_name.strip():
                st.session_state.subjects.append({
                    'name': subject_name.strip(),
                    'teacher': subject_teacher.strip(),
                })
                st.success(f'Disciplina "{subject_name.strip()}" adicionada')
            else:
                st.error('Informe o nome da disciplina.')

    if st.session_state.subjects:
        for index, subject in enumerate(st.session_state.subjects, start=1):
            teacher_text = f" — {subject['teacher']}" if subject['teacher'] else ''
            st.markdown(f"**{index}. {subject['name']}**{teacher_text}")
    else:
        st.info('Nenhuma disciplina adicionada ainda.')

else:
    st.subheader('gerenciamento de tarefas')
    st.checkbox('Exemplo: estudar python')
    st.checkbox('Exemplo: estudar streamlit')