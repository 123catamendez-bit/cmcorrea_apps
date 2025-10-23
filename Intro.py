import streamlit as st

st.set_page_config(page_title="🌌 IA Galáctica", layout="wide")

# 🌌 --- FONDO GALÁCTICO CON ANIMACIÓN ---
page_bg = """
<style>
/* Fondo base (espacio) */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
    position: relative;
    overflow: hidden;
}

/* Capa principal para estrellas */
#galaxy-bg {
  position: fixed;
  top: 0; left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1;
  overflow: hidden;
}

/* Animación de desplazamiento */
@keyframes moveStars {
  from {transform: translateY(0);}
  to {transform: translateY(-1000px);}
}

/* Diferentes capas de estrellas */
.stars, .stars2, .stars3 {
  position: absolute;
  top: 0; left: 0;
  width: 200%;
  height: 200%;
  background-repeat: repeat;
  background-size: 1000px 1000px;
  animation: moveStars linear infinite;
  opacity: 0.6;
}

.stars {
  background-image: radial-gradient(1px 1px at 10px 20px, white, transparent),
                    radial-gradient(2px 2px at 400px 200px, white, transparent),
                    radial-gradient(1px 1px at 700px 600px, white, transparent);
  animation-duration: 120s;
}
.stars2 {
  background-image: radial-gradient(1px 1px at 30px 50px, #bcdfff, transparent),
                    radial-gradient(2px 2px at 500px 800px, #bcdfff, transparent);
  animation-duration: 240s;
  opacity: 0.4;
}
.stars3 {
  background-image: radial-gradient(1px 1px at 70px 90px, #ffffff, transparent),
                    radial-gradient(2px 2px at 800px 400px, #ffffff, transparent);
  animation-duration: 360s;
  opacity: 0.2;
}

/* Texto */
h1, h2, h3, p {
  color: #e0e0e0;
  text-align: center;
  font-family: 'Trebuchet MS', sans-serif;
}

/* Botones */
a, a:visited, a:hover {
  text-decoration: none;
}
button {
  background-color: #4b56d2;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 10px;
  font-size: 16px;
  cursor: pointer;
  transition: 0.3s;
}
button:hover {
  background-color: #6c72e9;
}
</style>

<div id="galaxy-bg">
  <div class="stars"></div>
  <div class="stars2"></div>
  <div class="stars3"></div>
</div>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- CONTENIDO ---
st.title("🚀 Mis Aplicaciones IA Galácticas")
st.markdown("Explora el universo digital — cada aplicación es un planeta distinto en mi constelación de Inteligencia Artificial.")

with st.sidebar:
    st.subheader("🌠 Panel de Misión")
    st.write("Bienvenido a bordo de la *Nave Cata-IA*. Aquí encontrarás todas mis exploraciones en el cosmos de la Inteligencia Artificial.")

# --- COLUMNAS ---
col1, col2, col3 = st.columns(3, gap="large")

proyectos = [
    ("🚀 Mi Primera Misión", "Mi primer lanzamiento hacia el espacio del código.", "https://introcata.streamlit.app", "🌌 Lanzar Misión"),
    ("🌠 Voz Estelar", "Convierte tus pensamientos en ondas sonoras cósmicas.", "https://texto-audio-cata.streamlit.app", "🎤 Activar Voz Estelar"),
    ("💫 Radar de Energía", "Analiza la energía emocional de tus mensajes.", "https://txtblobcata.streamlit.app", "💭 Escanear Energía"),
    ("🖐️ Gestos Cósmicos", "Controla tu nave espacial mediante visión artificial.", "https://yolocata.streamlit.app", "🪐 Activar Gestos"),
    ("🛰️ Visión Orbital", "Sube una imagen y permite que el radar detecte objetos flotando.", "https://tmcata.streamlit.app", "🔭 Iniciar Visión Orbital"),
    ("🪶 Traductor de Ecos", "Convierte tus transmisiones de voz en texto interplanetario.", "https://traductor-cata.streamlit.app", "🛰️ Abrir Traductor"),
    ("📡 Escáner Galáctico", "Analiza archivos con IA estelar.", "https://textoesp.streamlit.app/", "📄 Analizar Archivo"),
    ("👁️ Detector Alienígena", "Escanea rostros del cosmos.", "https://ocr-isa2.streamlit.app/", "👽 Activar Detección"),
    ("🔤 OCR Estelar", "Convierte texto desde imágenes espaciales.", "https://isavinasco.streamlit.app/", "🪞 Iniciar OCR"),
    ("🗣️ Chat Cósmico con PDF", "Habla con tus archivos y recibe respuestas del universo.", "https://chatpdfejercicioisa.streamlit.app/", "📡 Conectar Chat"),
    ("🌠 Historias Estelares", "Dibuja algo y deja que la IA genere una historia cósmica.", "https://handcata.streamlit.app", "🌟 Crear Historia"),
    ("🎙️ Control por Voz", "Controla la nave mediante comandos de voz.", "https://ctrlvoice-cata.streamlit.app", "🎧 Activar Control"),
    ("🖌️ Reconocimiento de Dibujo", "La IA intenta descifrar tu figura celeste.", "https://reconnocer-el-dibujo.streamlit.app/", "🖍️ Reconocer Dibujo"),
    ("💡 Control de Luz", "Controla sistemas luminosos interestelares.", "https://enviarcmqttisa.streamlit.app/", "💫 Encender Luz"),
    ("📖 Explorador de Textos", "Analiza textos de cualquier idioma.", "https://isabela-vinasco-docs.streamlit.app/", "📚 Iniciar Exploración")
]

# Distribuir en 3 columnas
for i, (titulo, texto, link, boton) in enumerate(proyectos):
    col = [col1, col2, col3][i % 3]
    with col:
        st.subheader(titulo)
        st.write(texto)
        st.markdown(f"""
        <a href="{link}" target="_blank">
            <button>{boton}</button>
        </a>
        """, unsafe_allow_html=True)
