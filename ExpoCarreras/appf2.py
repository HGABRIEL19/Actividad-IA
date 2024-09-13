import streamlit as st
import random
import pandas as pd
# Título de la aplicación
st.title("Cuestionario de Habilidades Blandas")

form_2_questions = {
    "Comunicación": [
        ("¿Qué tan cómodo te sientes al expresar tus ideas en grupo?", ["Muy cómodo", "Cómodo", "Poco cómodo", "Incómodo"]),
        ("¿Consideras que eres un buen oyente cuando otros comparten sus ideas?", ["Sí, siempre", "Generalmente sí", "A veces", "No, me cuesta prestar atención"]),
    ],
    "Trabajo en Equipo": [
        ("¿Cómo te sientes al trabajar en equipo en proyectos escolares o extracurriculares?", ["Muy cómodo", "Cómodo", "Poco cómodo", "Incómodo"]),
        ("¿Qué rol prefieres asumir cuando trabajas en equipo?", ["Líder", "Facilitador", "Seguidor", "No tengo una preferencia clara"]),
        ("¿Qué tan importante consideras que es la colaboración para el éxito de un proyecto?", ["Muy importante", "Importante", "Poco importante", "No es importante"]),
    ],
    "Resolución de Problemas": [
        ("¿Cómo reaccionas cuando te enfrentas a un problema difícil en tus estudios?", ["Busco soluciones inmediatamente", "Pido ayuda", "Me siento frustrado pero lo intento", "Me rindo fácilmente"]),
        ("¿Con qué frecuencia buscas nuevas maneras de resolver problemas?", ["Muy frecuentemente", "Frecuentemente", "Ocasionalmente", "Raramente"]),
    ],
    "Adaptabilidad": [
        ("¿Qué tan fácil te resulta adaptarte a nuevas situaciones o cambios?", ["Muy fácil", "Fácil", "Difícil", "Muy difícil"]),
        ("¿Cómo te sientes al aprender nuevas herramientas o métodos de estudio?", ["Entusiasmado", "Interesado", "Neutral", "Incómodo"]),
    ],
    "Gestión del Tiempo": [
        ("¿Cómo manejas tu tiempo al realizar tareas o estudiar para exámenes?", ["Planifico con antelación y sigo mi plan", "Intento planificar, pero a veces me retraso", "Trabajo sin mucha planificación", "Suelo procrastinar y hacer todo al último momento"]),
        ("¿Qué tan efectivo consideras que es tu manejo del tiempo?", ["Muy efectivo", "Efectivo", "No muy efectivo", "Poco efectivo"]),
    ],
    "Pensamiento Crítico": [
        ("¿Con qué frecuencia cuestionas la información que recibes antes de aceptarla?", ["Siempre", "Frecuentemente", "Algunas veces"]),
    ]
}

# Respuestas aleatorias
st.header("Cuestionario 2: Las Habilidades Blandas")
responses_2 = {}
for category, questions in form_2_questions.items():
    st.subheader(category)
    for question, options in questions:
        # Seleccionar respuesta aleatoria
        response = random.choice(options)
        responses_2[question] = response
        st.radio(question, options, index=options.index(response))
        # Guardar las respuestas en un CSV

    # Agregar campo de correo electrónico
email = st.text_input("Correo electrónico (opcional)")
wants_contact = st.checkbox("Deseo ser contactado a través de mi correo electrónico")
if st.button("Enviar Respuestas"):
    df = pd.DataFrame(list(responses_2.items()), columns=["Pregunta", "Respuesta"])
    df.to_csv("respuestas_habilidades_blandas.csv", index=False)
    st.write("Respuestas guardadas con éxito.")
    