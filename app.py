import streamlit as st
import time

st.set_page_config(page_title="PulseFit - App de Treino", page_icon="🏋️‍♂️", layout="wide")

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #00E676;
        color: #000000;
        font-weight: bold;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

EXERCICIOS = {
    "Peito & Tríceps": [
        {
            "nome": "Flexão de Braço",
            "series": "4 séries x 12-15 reps",
            "instrucoes": "Mantenha o corpo reto e cotovelos a 45 graus.",
            "gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdW93NnhudTZpdzJ3YmUzNDFzMWkxbGV0aGZwbmJ0MXE3MXRkYTZoeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kFvdA169Q686n9Q3aN/giphy.gif"
        }
    ],
    "Pernas": [
        {
            "nome": "Agachamento Livre",
            "series": "4 séries x 12 reps",
            "instrucoes": "Pés na largura dos ombros, desça controlando.",
            "gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjRybDFsbWhuZHR0Z2c4NWNrdDkwdnNmOWlwdXRtMmF5dW4ycDVsZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKspb1m7Z207tC0/giphy.gif"
        }
    ]
}

st.title("🏋️‍♂️ PULSEFIT - Treino & Performance")

categoria = st.sidebar.selectbox("Selecione a Rotina:", list(EXERCICIOS.keys()))
st.subheader(f"Rotina de {categoria}")

for i, ex in enumerate(EXERCICIOS[categoria]):
    with st.expander(f"📌 {ex['nome']}", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.image(ex["gif"], use_container_width=True)
        with col2:
            st.markdown(f"**Meta:** {ex['series']}")
            st.write(f"**Dica:** {ex['instrucoes']}")
            if st.button(f"Concluir Série", key=f"btn_{i}"):
                st.success("Série concluída com sucesso!")

st.write("---")
st.header("⏱️ Cronômetro de Descanso")
tempo = st.slider("Segundos:", 15, 120, 60, step=15)

if st.button("Iniciar Descanso"):
    bar = st.progress(100)
    for t in range(tempo, -1, -1):
        bar.progress(int((t / tempo) * 100))
        time.sleep(1)
    st.balloons()