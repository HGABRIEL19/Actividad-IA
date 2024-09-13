import streamlit as st

# Título de la aplicación
st.title("Cuestionario de Ciencias de Datos")

# Opciones de los formularios
form_1_questions = {
    "Programación": [
        ("¿Cuánto interés tienes en aprender a programar?", ["Mucho", "Algo", "Poco", "Ninguno"]),
        ("¿Qué lenguajes de programación conoces o te gustaría aprender?", ["Python", "JavaScript", "Java", "Otro"]),
        ("¿Has desarrollado algún proyecto de software o aplicación?", ["Sí, por mi cuenta", "Sí, en un curso o taller", "No, pero me gustaría", "No, y no me interesa"]),
    ],
    "Tecnología": [
        ("¿Cuánto tiempo al día utilizas dispositivos tecnológicos?", ["Menos de 2 horas", "2-4 horas", "4-6 horas", "Más de 6 horas"]),
        ("¿Qué tan cómodo te sientes utilizando nuevas tecnologías?", ["Muy cómodo", "Cómodo", "Poco cómodo", "Incómodo"]),
        ("¿Qué dispositivo tecnológico consideras indispensable en tu día a día?", ["Teléfono", "Computadora", "Tablet", "Otro"]),
    ],
    "Análisis de Datos": [
        ("¿Sabes qué es el análisis de datos?", ["Sí, lo conozco bien", "Sí, he oído hablar de ello", "No, pero me gustaría saber más", "No, y no me interesa"]),
        ("¿Has utilizado alguna vez herramientas para analizar datos?", ["Sí, frecuentemente", "Sí, algunas veces", "No, pero me gustaría aprender", "No, y no me interesa"]),
        ("¿Qué tan importante crees que es el análisis de datos en la toma de decisiones?", ["Muy importante", "Algo importante", "Poco importante", "No es importante"]),
    ],
    "Inteligencia Artificial": [
        ("¿Qué tan familiarizado estás con el concepto de inteligencia artificial (IA)?", ["Muy familiarizado", "Algo familiarizado", "Poco familiarizado", "Nada familiarizado"]),
        ("¿Crees que la inteligencia artificial será útil en tu futura carrera profesional?", ["Sí, definitivamente", "Probablemente", "No estoy seguro", "No, no lo creo"]),
        ("¿Qué aplicaciones de inteligencia artificial te parecen más interesantes?", ["Asistentes virtuales", "Recomendaciones personalizadas", "Automóviles autónomos", "Chat, GPT"]),
    ]
}

# Formulario 1: Ciencias de Datos
st.header("Cuestionario 1: Las Ciencias de Datos")
responses_1 = {}
for category, questions in form_1_questions.items():
    st.subheader(category)
    for question, options in questions:
        responses_1[question] = st.radio(question, options)

# Botón para mostrar respuestasif st.button("Mostrar Resultados"):
    st.subheader("Respuestas del Cuestionario 1")
    for question, response in responses_1.items():
        st.write(f"**{question}**: {response}")

