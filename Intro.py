import streamlit as st
# from PIL import Image  # ← Descomenta cuando tengas las imágenes

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="🌌 IA Galáctica", layout="wide")

# --- FONDO GALÁCTICO ---
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

# --- TÍTULO PRINCIPAL ---
st.title("🚀 Mis Aplicaciones IA Galácticas")
st.markdown("Explora el universo digital — cada aplicación es un planeta distinto en mi constelación de Inteligencia Artificial.")

# --- SIDEBAR ---
with st.sidebar:
    st.subheader("🌠 Panel de Misión")
    st.write("Bienvenido a bordo de la *Nave Cata-IA*. Aquí encontrarás todas mis exploraciones en el cosmos de la Inteligencia Artificial.")
    st.write("Pulsa un botón para iniciar el viaje interplanetario correspondiente a cada proyecto. 🪐")

# --- COLUMNAS PRINCIPALES ---
col1, col2, col3 = st.columns(3, gap="large")

# ======== COLUMNA 1 ========
with col1:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)

    # 1️⃣ Primera misión
    st.subheader("🚀 Mi Primera Misión")
    # st.image('app1.jpg', width=200)
    st.write("Mi primer lanzamiento hacia el espacio del código. Una app sencilla que marcó el inicio de mi viaje galáctico en IA.")
    st.markdown("""
    <a href="https://introcata.streamlit.app" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            🌌 Lanzar Misión
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 2️⃣ Texto a Voz
    st.subheader("🌠 Voz Estelar (Texto a Voz)")
    # st.image('texto_avoz.jpg', width=200)
    st.write("Convierte tus pensamientos en ondas sonoras cósmicas con esta app de texto a voz impulsada por IA.")
    st.markdown("""
    <a href="https://texto-audio-cata.streamlit.app" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            🎤 Activar Voz Estelar
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 3️⃣ Radar de Energía (Sentimientos)
    st.subheader("💫 Radar de Energía (Sentimientos)")
    # st.image('sentimientos.jpg', width=200)
    st.write("Analiza la energía emocional de tus mensajes y descubre si vibras en modo estelar o en eclipse. 🌕")
    st.markdown("""
    <a href="https://txtblobcata.streamlit.app" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            💭 Escanear Energía
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 4️⃣ Gestos Cósmicos
    st.subheader("🖐️ Gestos Cósmicos")
    # st.image('gesto.jpg', width=200)
    st.write("Controla tu nave espacial mediante gestos captados por visión artificial galáctica. ✋")
    st.markdown("""
    <a href="https://yolocata.streamlit.app" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            🪐 Activar Gestos Cósmicos
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 5️⃣ Visión Orbital (Reconocimiento de Objetos)
    st.subheader("🛰️ Visión Orbital (Objetos)")
    # st.image('vision_app.jpg', width=200)
    st.write("Sube una imagen y permite que el radar galáctico detecte los objetos flotando en tu universo visual.")
    st.markdown("""
    <a href="https://tmcata.streamlit.app" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            🔭 Iniciar Visión Orbital
        </button>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ======== COLUMNA 2 ========
with col2:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)

    # 6️⃣ Traductor de Ecos (Audio a Texto)
    st.subheader("🪶 Traductor de Ecos (Audio a Texto)")
    # st.image('audio_atexto.jpg', width=200)
    st.write("Convierte tus transmisiones de voz en texto interplanetario. 📡")
    st.markdown("""
    <a href="https://traductor-cata.streamlit.app" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            🛰️ Abrir Traductor de Ecos
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 7️⃣ Escáner de Documentos Galácticos
    st.subheader("📡 Escáner de Documentos Galácticos")
    # st.image('analisis_texto.jpg', width=200)
    st.write("Analiza archivos de civilizaciones antiguas con el poder de la IA estelar. 📜")
    st.markdown("""
    <a href="https://textoesp.streamlit.app/" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            📄 Analizar Documento Galáctico
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 8️⃣ Detector de Rostros Alienígenas
    st.subheader("👁️ Detector de Rostros Alienígenas")
    # st.image('rostros.jpg', width=200)
    st.write("Escanea el cosmos en busca de rostros conocidos… o desconocidos. 👽")
    st.markdown("""
    <a href="https://ocr-isa2.streamlit.app/" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            👽 Activar Detección Alienígena
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 9️⃣ OCR Estelar
    st.subheader("🔤 OCR Estelar")
    # st.image('ocr_final.jpg', width=200)
    st.write("Convierte texto desde imágenes espaciales, con precisión interestelar. 📖")
    st.markdown("""
    <a href="https://isavinasco.streamlit.app/" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            🪞 Iniciar OCR Estelar
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 🔟 Chat Cósmico con PDF
    st.subheader("🗣️ Chat Cósmico con PDF")
    # st.image('chat_pdf.jpg', width=200)
    st.write("Habla con tus archivos y recibe respuestas del universo digital. 🌌")
    st.markdown("""
    <a href="https://chatpdfejercicioisa.streamlit.app/" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            📡 Conectar Chat Cósmico
        </button>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ======== COLUMNA 3 ========
with col3:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)

    # 11️⃣ Creador de Historias Estelares
    st.subheader("🌠 Creador de Historias Estelares")
    # st.image('historia.jpg', width=200)
    st.write("Dibuja algo y deja que la IA genere una historia cósmica a partir de tu arte. 🎨")
    st.markdown("""
    <a href="https://handcata.streamlit.app" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            🌟 Crear Historia Estelar
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 12️⃣ Control por Voz Galáctico
    st.subheader("🎙️ Control por Voz Galáctico")
    # st.image('voz_control.jpg', width=200)
    st.write("Controla la nave mediante comandos de voz impulsados por IA interplanetaria. 🔊")
    st.markdown("""
    <a href="https://ctrlvoiceisa.streamlit.app/" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            🎧 Activar Control por Voz
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 13️⃣ Reconocimiento de Dibujo Estelar
    st.subheader("🖌️ Reconocimiento de Dibujo Estelar")
    # st.image('dibujo.jpg', width=200)
    st.write("La IA intentará descifrar qué figura celeste has dibujado. 🪶")
    st.markdown("""
    <a href="https://reconnocer-el-dibujo.streamlit.app/" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            🖍️ Reconocer Dibujo
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 14️⃣ Control de Luz Interestelar (IoT)
    st.subheader("💡 Control de Luz Interestelar (IoT)")
    # st.image('control_led.jpg', width=200)
    st.write("Controla sistemas luminosos de la nave mediante tecnología IoT y señales estelares.")
    st.markdown("""
    <a href="https://enviarcmqttisa.streamlit.app/" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            💫 Activar Control Lumínico
        </button>
    </a>
    """, unsafe_allow_html=True)

    # 15️⃣ Explorador de Textos Universales
    st.subheader("📖 Explorador de Textos Universales")
    # st.image('texto_ingles.jpg', width=200)
    st.write("Analiza textos en cualquier idioma y descubre su energía cósmica. 🌍")
    st.markdown("""
    <a href="https://isabela-vinasco-docs.streamlit.app/" target="_blank">
        <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
            📚 Iniciar Exploración Textual
        </button>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
