import streamlit as st
# from PIL import Image   # ← Descomenta esto cuando ya tengas las imágenes

# --- Configuración general ---
st.set_page_config(page_title="IA Galáctica 🚀", layout="wide")

# --- Fondo galáctico ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0b0f1a;
    background-image: radial-gradient(circle at 20% 20%, #16213e, #0b0f1a);
}
[data-testid="stSidebar"] {
    background-color: #1a1f2e;
}
h1, h2, h3, p {
    color: #e0e0e0;
    text-align: center;
    font-family: 'Trebuchet MS', sans-serif;
}
button {
    display: block;
    margin: 0 auto;
}
a, a:visited, a:hover, a:active {
    text-decoration: none !important;
    outline: none !important;
    box-shadow: none !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Título principal ---
st.title("🌌 IA Galáctica")
st.markdown("Explora el universo de la Inteligencia Artificial — cada aplicación es un nuevo planeta por descubrir.")

# --- Sidebar ---
with st.sidebar:
    st.subheader("Panel de Misión 👩‍🚀")
    st.write("Bienvenido a bordo. Estas son mis exploraciones a través del cosmos digital con IA. Pulsa un botón y despega hacia una nueva experiencia.")

# --- Aplicación 1 ---
st.subheader("🪐 Mi Primera Misión")

# image = Image.open('app1.jpg')  # ← Agrega tu imagen aquí más adelante
# st.image(image, width=200)

st.write("Mi primer lanzamiento al espacio del código. Una app sencilla, pero el inicio de un viaje intergaláctico hacia la Inteligencia Artificial.")
st.markdown(
    """
    <a href="https://miprimeraappisa.streamlit.app/" target="_blank">
        <button style="
            background-color:#4b56d2;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🚀 Lanzar Primera Misión
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# --- Columnas ---
col1, col2, col3 = st.columns([1, 1, 1], gap="large")

with col1:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)

    st.subheader("🌠 Voz Estelar (Texto a Voz)")
    # image = Image.open('texto_avoz.jpg')
    # st.image(image, width=190)
    st.write("Convierte tus pensamientos en voz galáctica. Ideal para explorar nuevos idiomas del universo digital.")
    st.markdown(
        """
        <a href="https://intro3-cv4kbcjgxbiveh8ph2kmyp.streamlit.app/" target="_blank">
            <button style="
                background-color:#4b56d2;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:8px;
                font-size:16px;
                cursor:pointer;
            ">
                🎤 Activar Voz Estelar
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.subheader("💫 Radar de Emociones")
    # image = Image.open('sentimientos.jpg')
    # st.image(image, width=200)
    st.write("Analiza las emociones ocultas en tus mensajes. ¿Estás orbitando la alegría, la calma o el caos?")
    st.markdown(
    """
    <a href="https://isabelavinasco.streamlit.app/" target="_blank">
        <button style="
            background-color:#4b56d2;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            💭 Escanear Emociones
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("🖐️ Gestos Cósmicos")
    # image = Image.open('gesto.jpg')
    # st.image(image, width=200)
    st.write("Deja que tus movimientos hablen por ti. Controla la nave con gestos captados por visión espacial de IA.")
    st.markdown(
    """
    <a href="https://yolov5-isa.streamlit.app/" target="_blank">
        <button style="
            background-color:#4b56d2;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ✋ Activar Gestos Cósmicos
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("🛰️ Visión Orbital (Reconocimiento de Objetos)")
    # image = Image.open('vision_app.jpg')
    # st.image(image, width=200)
    st.write("Sube una imagen y deja que el radar de IA detecte qué objetos flotan en tu universo visual.")
    st.markdown(
    """
    <a href="https://visionapp-isa-lpq3fitf2jwnkastes8odi.streamlit.app/" target="_blank">
        <button style="
            background-color:#4b56d2;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🪞 Iniciar Visión Orbital
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


with col2:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)

    st.subheader("🪶 Traductor de Ecos (Audio a Texto)")
    # image = Image.open('audio_atexto.jpg')
    # st.image(image, width=200)
    st.write("Convierte mensajes de audio en texto estelar. Ideal para descifrar transmisiones interplanetarias.")
    st.markdown(
    """
    <a href="https://intro2-fojj4mqk3pvfuy4gb5twvg.streamlit.app/" target="_blank">
        <button style="
            background-color:#4b56d2;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🛰️ Abrir Traductor de Ecos
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("📡 Escáner de Documentos Galácticos")
    # image = Image.open('analisis_texto.jpg')
    # st.image(image, width=200)
    st.write("Explora documentos antiguos de civilizaciones digitales y descubre sus secretos con IA avanzada.")
    st.markdown(
    """
    <a href="https://textoesp.streamlit.app/" target="_blank">
        <button style="
            background-color:#4b56d2;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            📄 Analizar Documento Galáctico
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("👁️ Detector de Rostros Alienígenas")
    # image = Image.open('OCR.jpg')
    # st.image(image, width=200)
    st.write("Escanea imágenes en busca de rostros conocidos (o desconocidos) por la IA interplanetaria.")
    st.markdown(
    """
    <a href="https://ocr-isa2.streamlit.app/" target="_blank">
        <button style="
            background-color:#4b56d2;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            👽 Activar Detección Alienígena
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


with col3:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)

    st.subheader("🔤 OCR Estelar")
    # image = Image.open('ocr_final.jpg')
    # st.image(image, width=200)
    st.write("Convierte imágenes en texto legible desde cualquier rincón de la galaxia. Rápido, preciso y futurista.")
    st.markdown(
    """
    <a href="https://isavinasco.streamlit.app/" target="_blank">
        <button style="
            background-color:#4b56d2;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🔭 Iniciar OCR Estelar
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("🗣️ Chat Cósmico con PDF")
    # image = Image.open('chat_pdf.jpg')
    # st.image(image, width=200)
    st.write("Habla con los archivos de tu nave. La IA interpreta tus documentos y responde como un copiloto digital.")
    st.markdown(
    """
    <a href="https://chatpdfejercicioisa.streamlit.app/" target="_blank">
        <button style="
            background-color:#4b56d2;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            📡 Conectar Chat Cósmico
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("🌌 Creador de Historias Estelares")
    # image = Image.open('historia.jpg')
    # st.image(image, width=200)
    st.write("Dibuja algo y deja que la IA cree una historia galáctica basada en tu arte. Donde cada trazo genera una nueva aventura.")
    st.markdown(
    """
    <a href="https://historia-infantil.streamlit.app/" target="_blank">
        <button style="
            background-color:#4b56d2;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            🌠 Crear Historia Estelar
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)
