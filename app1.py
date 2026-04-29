import streamlit as st
import random

st.set_page_config(page_title="Trivia Villanas Disney", page_icon="👑")

st.title("👑 Trivia: Villanas de Disney")

# Preguntas
preguntas = [
    {
        "pregunta": "¿Cómo se llama la villana de La Sirenita?",
        "opciones": ["Úrsula", "Maléfica", "Cruella", "Yzma"],
        "respuesta": "Úrsula"
    },
    {
        "pregunta": "¿Qué villana odia a los dálmatas?",
        "opciones": ["Cruella", "Madrastra", "Maléfica", "Gothel"],
        "respuesta": "Cruella"
    },
    {
        "pregunta": "¿Quién es la villana de La Bella Durmiente?",
        "opciones": ["Maléfica", "Úrsula", "Yzma", "Cruella"],
        "respuesta": "Maléfica"
    },
    {
        "pregunta": "¿Qué villana aparece en Enredados?",
        "opciones": ["Gothel", "Cruella", "Úrsula", "Maléfica"],
        "respuesta": "Gothel"
    },
    {
        "pregunta": "¿Quién es la villana en El emperador y sus locuras?",
        "opciones": ["Yzma", "Úrsula", "Cruella", "Maléfica"],
        "respuesta": "Yzma"
    }
]

# Mezclar opciones
for p in preguntas:
    random.shuffle(p["opciones"])

respuestas_usuario = []

# Formulario
with st.form("trivia_form"):
    for i, p in enumerate(preguntas):
        resp = st.radio(p["pregunta"], p["opciones"], key=i)
        respuestas_usuario.append(resp)
    
    submit = st.form_submit_button("Enviar respuestas")

# Evaluación
if submit:
    score = 0
    for i, p in enumerate(preguntas):
        if respuestas_usuario[i] == p["respuesta"]:
            score += 1
    
    st.subheader(f"Tu puntaje: {score}/5")

    if score == 5:
        st.balloons()
        st.success("¡Perfecto! 🎉 Adivinaste todas las respuestas")
    else:
        st.warning("Sigue intentando 👀")
