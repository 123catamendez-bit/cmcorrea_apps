import streamlit as st

# 🌌 CONFIGURACIÓN GENERAL
st.set_page_config(page_title="🌌 IA Galáctica", layout="wide")

# 🌠 --- FONDO GALÁCTICO ANIMADO ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at bottom, #0b0c28 0%, #05010d 100%);
    position: relative;
    overflow: hidden;
}

/* Fondo animado de estrellas */
#galaxy-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
}

@keyframes moveStars {
    from {transform: translateY(0);}
    to {transform: translateY(-1000px);}
}

.stars, .stars2, .stars3 {
    position: absolute;
    top: 0;
    left: 0;
    width: 200%;
    height: 200%;
    background-repeat: repeat;
    background-size: 1000px 1000px;
    animation: moveStars linear infinite;
}

.stars { background-image: radial-gradient(1px 1px at 10px 20px, white, transparent),
                         radial-gradient(2px 2px at 400px 200px, white, transparent),
                         radial-gradient(1px 1px at 700px 600px, white, transparent);
         animation-duration: 120s; opacity: 0.6; }

.stars2 { background-image: radial-gradient(1px 1px at 30px 50px, #bcdfff, transparent),
                          radial-gradient(2px 2px at 500px 800px, #bcdfff, transparent);
          animation-duration: 240s; opacity: 0.4; }

.stars3 { background-image: radial-gradient(1px 1px at 70px 90px, #ffffff, transparent),
                          radial-gradient(2px 2px at 800px 400px, #ffffff, transparent);
          animation-duration: 360s; opacity: 0.2; }

/* Texto */
h1, h2, h3, p {
    color: #e0e0e0;
    font-family: 'Trebuchet MS', sans-serif;
}

/* Tarjetas galácticas */
.card {
    background-color: rgba(25, 20, 50, 0.85);
    border-radius: 25px;
    padding: 20px;
    margin: 20px 10px;
    box-shadow: 0 0 25px rgba(150, 100, 255, 0.25);
    text-align: center;
    transition: all 0.4s ease;
    border: 1px solid rgba(180, 150, 255, 0.2);
}
.card:hover {
    transform: scale(1.03);
    box-shadow: 0 0 35px rgba(200, 150, 255, 0.4);
}

/* Imágenes dentro del cuadro */
.card img {
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(255,255,255,0.1);
    transition: all 0.3s ease;
}
.card img:hover {
    transform: scale(1.05);
}

/* Botones */
button {
    background: linear-gradient(90deg, #a770ef, #cf8bf3, #fdb99b);
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 12px;
    font-size: 16px;
    cursor: pointer;
    transition: 0.4s;
}
button:hover {
    background: linear-gradient(90deg, #fdb99b, #cf8bf3, #a770ef);
    transform: scale(1.08);
}

/* Contenedor animado */
#galaxy-bg { pointer-events: none; }
</style>

<div id="galaxy-bg">
    <div class="stars"></div>
    <div class="stars2"></div>
    <div class="stars3"></div>
</div>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# 🌟 --- TITULOS PRINCIPALES ---
st.title("🚀 Mis Aplicaciones IA Galácticas")
st.markdown("Explora el universo digital — cada aplicación es un planeta brillante en mi constelación de Inteligencia Artificial.")

with st.sidebar:
    st.subheader("🪐 Panel de Misión")
    st.write("Bienvenido a la **Nave Cata-IA** 🛸. Desde aquí puedes viajar a todos los mundos que he creado en el cosmos digital.")

# --- CONFIGURACIÓN DE COLUMNAS ---
col1, col2, col3 = st.columns(3, gap="large")

# --- PROYECTOS CON IMÁGENES ONLINE ---
proyectos = [
    ("🚀 Mi Primera Misión", "Mi primer lanzamiento hacia el espacio del código.",
     "https://introcata.streamlit.app", "🌌 Lanzar Misión", "al.jpg"),

    ("🌠 Voz Estelar", "Convierte tus pensamientos en ondas sonoras cósmicas.",
     "https://texto-audio-cata.streamlit.app", "🎤 Activar Voz Estelar", "1.jpg"),

    ("💫 Radar de Energía", "Analiza la energía emocional de tus mensajes.",
     "https://txtblobcata.streamlit.app", "💭 Escanear Energía", "2.jpg"),

    ("🖐️ Gestos Cósmicos", "Controla tu nave mediante visión artificial.",
     "https://yolocata.streamlit.app", "🪐 Activar Gestos", "3.jpg"),

    ("🛰️ Visión Orbital", "Sube una imagen y detecta objetos flotando en el espacio.",
     "https://tmcata.streamlit.app", "🔭 Iniciar Visión Orbital", "4.jpg"),

    ("🪶 Traductor de Ecos", "Convierte tus transmisiones de voz en texto interplanetario.",
     "https://traductor-cata.streamlit.app", "🛰️ Abrir Traductor", "5.jpg"),

    ("📡 Escáner Galáctico", "Analiza archivos con IA estelar.",
     "https://tdfesp-cata.streamlit.app", "📄 Analizar Archivo", "6.jpg"),

    ("👁️ Detector Alienígena", "Escanea rostros del cosmos y detecta seres de otra dimensión.",
     "https://ocr-audio-cata.streamlit.app", "👽 Activar Detección", "ali.jpg"),

    ("🔤 OCR Estelar", "Convierte texto desde imágenes espaciales.",
     "https://ocrcata.streamlit.app", "🪞 Iniciar OCR", "7.jpg"),

    ("🗣️ Chat Cósmico con PDF", "Habla con tus archivos y recibe respuestas del universo.",
     "https://chatcata.streamlit.app", "📡 Conectar Chat", "8.jpg"),

    ("🌠 Historias Estelares", "Dibuja algo y deja que la IA cree una historia cósmica.",
     "https://handcata.streamlit.app", "🌟 Crear Historia", "9.jpg"),

    ("🎙️ Control por Voz", "Controla la nave mediante comandos de voz.",
     "https://ctrlvoice-cata.streamlit.app", "🎧 Activar Control", "10.jpg"),

    ("🖌️ Reconocimiento de Dibujo", "La IA intenta descifrar tu figura celeste.",
     "https://hist-infcata.streamlit.app", "🖍️ Reconocer Dibujo", "11.jpg"),

    ("💡 Control de Luz", "Activa sistemas luminosos interestelares.",
     "https://sendcmqtt-cata.streamlit.app", "💫 Encender Luz", "12.jpg"),

    ("📖 Explorador de Textos", "Analiza textos de cualquier idioma con poder cósmico.",
     "https://tf-idfcata.streamlit.app", "📚 Iniciar Exploración", "13.jpg")
]

# --- MOSTRAR TARJETAS EN CUADROS ---
for i, (titulo, texto, link, boton, imagen) in enumerate(proyectos):
    col = [col1, col2, col3][i % 3]
    with col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(imagen, use_container_width=True)
        st.subheader(titulo)
        st.write(texto)
        st.markdown(f"""
            <a href="{link}" target="_blank">
                <button>{boton}</button>
            </a>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
