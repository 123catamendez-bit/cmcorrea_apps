import streamlit as st

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="🌌 IA Galáctica", layout="wide")

# --- FONDO ANIMADO GALÁCTICO ---
page_bg = """
<style>
/* Fondo del universo */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
    overflow: hidden;
    position: relative;
}

/* Estrellas animadas */
@keyframes moveStars {
  from {transform: translateY(0);}
  to {transform: translateY(-1000px);}
}

.stars, .stars2, .stars3 {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-repeat: repeat;
  background-size: contain;
  animation: moveStars linear infinite;
  z-index: -1;
}

/* Capas de estrellas (diferentes tamaños y velocidades) */
.stars {
  background-image: radial-gradient(2px 2px at 20px 20px, white, transparent),
                    radial-gradient(1px 1px at 60px 80px, white, transparent),
                    radial-gradient(1.5px 1.5px at 130px 40px, white, transparent);
  animation-duration: 100s;
  opacity: 0.6;
}
.stars2 {
  background-image: radial-gradient(1px 1px at 10px 10px, #bcdfff, transparent),
                    radial-gradient(2px 2px at 80px 120px, #bcdfff, transparent);
  animation-duration: 200s;
  opacity: 0.4;
}
.stars3 {
  background-image: radial-gradient(1.2px 1.2px at 40px 60px, #ffffff, transparent),
                    radial-gradient(1px 1px at 90px 100px, #ffffff, transparent);
  animation-duration: 300s;
  opacity: 0.2;
}

/* Textos */
h1, h2, h3, p {
    color: #e0e0e0;
    text-align: center;
    font-family: 'Trebuchet MS', sans-serif;
}

/* Botones */
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

<div class="stars"></div>
<div class="stars2"></div>
<div class="stars3"></div>
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

# --- COLUMNAS ---
col1, col2, col3 = st.columns(3, gap="large")

# ======== COLUMNA 1 ========
with col1:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    proyectos_col1 = [
        ("🚀 Mi Primera Misión", "Mi primer lanzamiento hacia el espacio del código. Una app sencilla que marcó el inicio de mi viaje galáctico en IA.", "https://introcata.streamlit.app", "🌌 Lanzar Misión"),
        ("🌠 Voz Estelar (Texto a Voz)", "Convierte tus pensamientos en ondas sonoras cósmicas con esta app de texto a voz impulsada por IA.", "https://texto-audio-cata.streamlit.app", "🎤 Activar Voz Estelar"),
        ("💫 Radar de Energía (Sentimientos)", "Analiza la energía emocional de tus mensajes y descubre si vibras en modo estelar o en eclipse.", "https://txtblobcata.streamlit.app", "💭 Escanear Energía"),
        ("🖐️ Gestos Cósmicos", "Controla tu nave espacial mediante gestos captados por visión artificial galáctica.", "https://yolocata.streamlit.app", "🪐 Activar Gestos Cósmicos"),
        ("🛰️ Visión Orbital (Objetos)", "Sube una imagen y permite que el radar galáctico detecte los objetos flotando en tu universo visual.", "https://tmcata.streamlit.app", "🔭 Iniciar Visión Orbital"),
    ]
    for titulo, texto, link, boton in proyectos_col1:
        st.subheader(titulo)
        st.write(texto)
        st.markdown(f"""
        <a href="{link}" target="_blank">
            <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
                {boton}
            </button>
        </a>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ======== COLUMNA 2 ========
with col2:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    proyectos_col2 = [
        ("🪶 Traductor de Ecos (Audio a Texto)", "Convierte tus transmisiones de voz en texto interplanetario.", "https://traductor-cata.streamlit.app", "🛰️ Abrir Traductor de Ecos"),
        ("📡 Escáner de Documentos Galácticos", "Analiza archivos de civilizaciones antiguas con el poder de la IA estelar.", "https://textoesp.streamlit.app/", "📄 Analizar Documento Galáctico"),
        ("👁️ Detector de Rostros Alienígenas", "Escanea el cosmos en busca de rostros conocidos… o desconocidos.", "https://ocr-isa2.streamlit.app/", "👽 Activar Detección Alienígena"),
        ("🔤 OCR Estelar", "Convierte texto desde imágenes espaciales, con precisión interestelar.", "https://isavinasco.streamlit.app/", "🪞 Iniciar OCR Estelar"),
        ("🗣️ Chat Cósmico con PDF", "Habla con tus archivos y recibe respuestas del universo digital.", "https://chatpdfejercicioisa.streamlit.app/", "📡 Conectar Chat Cósmico"),
    ]
    for titulo, texto, link, boton in proyectos_col2:
        st.subheader(titulo)
        st.write(texto)
        st.markdown(f"""
        <a href="{link}" target="_blank">
            <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
                {boton}
            </button>
        </a>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ======== COLUMNA 3 ========
with col3:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    proyectos_col3 = [
        ("🌠 Creador de Historias Estelares", "Dibuja algo y deja que la IA genere una historia cósmica a partir de tu arte.", "https://handcata.streamlit.app", "🌟 Crear Historia Estelar"),
        ("🎙️ Control por Voz Galáctico", "Controla la nave mediante comandos de voz impulsados por IA interplanetaria.", "https://ctrlvoiceisa.streamlit.app/", "🎧 Activar Control por Voz"),
        ("🖌️ Reconocimiento de Dibujo Estelar", "La IA intentará descifrar qué figura celeste has dibujado.", "https://reconnocer-el-dibujo.streamlit.app/", "🖍️ Reconocer Dibujo"),
        ("💡 Control de Luz Interestelar (IoT)", "Controla sistemas luminosos de la nave mediante tecnología IoT y señales estelares.", "https://enviarcmqttisa.streamlit.app/", "💫 Activar Control Lumínico"),
        ("📖 Explorador de Textos Universales", "Analiza textos en cualquier idioma y descubre su energía cósmica.", "https://isabela-vinasco-docs.streamlit.app/", "📚 Iniciar Exploración Textual"),
    ]
    for titulo, texto, link, boton in proyectos_col3:
        st.subheader(titulo)
        st.write(texto)
        st.markdown(f"""
        <a href="{link}" target="_blank">
            <button style="background-color:#4b56d2;color:white;border:none;padding:12px 24px;border-radius:8px;font-size:16px;cursor:pointer;">
                {boton}
            </button>
        </a>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
