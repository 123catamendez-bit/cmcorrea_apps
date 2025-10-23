import streamlit as st

st.set_page_config(page_title="🌌 IA Galáctica", layout="wide")

# 🌌 --- FONDO GALÁCTICO CON ANIMACIÓN ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at bottom, #0a0118 0%, #000010 100%);
    position: relative;
    overflow: hidden;
    color: #e8e6ff;
}

/* ✨ Animación de estrellas */
@keyframes moveStars {
  from {transform: translateY(0);}
  to {transform: translateY(-1000px);}
}

.stars, .stars2, .stars3 {
  position: fixed;
  top: 0; left: 0;
  width: 200%;
  height: 200%;
  background-repeat: repeat;
  background-size: 1000px 1000px;
  animation: moveStars linear infinite;
  z-index: -1;
}

.stars {
  background-image: radial-gradient(1px 1px at 10px 20px, white, transparent),
                    radial-gradient(2px 2px at 400px 200px, white, transparent),
                    radial-gradient(1px 1px at 700px 600px, white, transparent);
  animation-duration: 160s;
}
.stars2 {
  background-image: radial-gradient(1px 1px at 30px 50px, #bcdfff, transparent),
                    radial-gradient(2px 2px at 500px 800px, #bcdfff, transparent);
  animation-duration: 300s;
  opacity: 0.4;
}
.stars3 {
  background-image: radial-gradient(1px 1px at 70px 90px, #ffffff, transparent),
                    radial-gradient(2px 2px at 800px 400px, #ffffff, transparent);
  animation-duration: 500s;
  opacity: 0.2;
}

/* 🌠 Títulos y texto */
h1, h2, h3, p {
  text-align: center;
  color: #e0e0ff;
  font-family: 'Trebuchet MS', sans-serif;
}
h1 {
  text-shadow: 0 0 20px #a56dff, 0 0 40px #6b36ff;
  font-size: 3rem;
}

/* 🪐 Tarjetas */
.card {
  background: rgba(40, 0, 80, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 20px;
  box-shadow: 0 0 20px rgba(160, 100, 255, 0.3);
  padding: 20px;
  margin-bottom: 40px;
  transition: all 0.3s ease-in-out;
  backdrop-filter: blur(8px);
}
.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 0 40px rgba(220, 150, 255, 0.7);
}

/* 🌌 Imagen de tarjeta (MISMO TAMAÑO PARA TODAS) */
.card img {
  width: 100%;
  height: 200px; /* Ajusta este valor si quieres más alto/bajo */
  object-fit: cover;
  object-position: center;
  border-radius: 15px;
  box-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
  margin-bottom: 15px;
  transition: transform 0.4s ease, box-shadow 0.4s ease;
}
.card img:hover {
  transform: scale(1.05);
  box-shadow: 0 0 30px rgba(200, 160, 255, 0.6);
}

/* 🚀 Botón */
button {
  background: linear-gradient(90deg, #6b36ff, #c04dff);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 12px;
  font-size: 15px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.3s;
  width: 100%;
}
button:hover {
  transform: scale(1.05);
  box-shadow: 0 0 25px #dba6ff;
}
</style>

<div class="stars"></div>
<div class="stars2"></div>
<div class="stars3"></div>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- CONTENIDO PRINCIPAL ---
st.title("🚀 Mis Aplicaciones IA Galácticas")
st.markdown("Explora el **universo digital** — cada aplicación es un planeta brillante en mi constelación de Inteligencia Artificial 🌠.")

with st.sidebar:
    st.subheader("🪐 Panel de Misión")
    st.write("Bienvenido a la *Nave Cata-IA*. Aquí puedes visitar todos los mundos que he creado con IA en el cosmos digital.")

# --- LISTA DE PROYECTOS CON IMÁGENES ---
proyectos = [
    ("🚀 Mi Primera Misión", "Mi primer lanzamiento hacia el espacio del código.", "https://introcata.streamlit.app", "🌌 Lanzar Misión", "al.jpg"),
    ("🌠 Voz Estelar", "Convierte tus pensamientos en ondas sonoras cósmicas.", "https://texto-audio-cata.streamlit.app", "🎤 Activar Voz Estelar", "2.jpg"),
    ("💫 Radar de Energía", "Analiza la energía emocional de tus mensajes.", "https://txtblobcata.streamlit.app", "💭 Escanear Energía", "3.jpg"),
    ("🖐️ Gestos Cósmicos", "Controla tu nave espacial mediante visión artificial.", "https://yolocata.streamlit.app", "🪐 Activar Gestos", "4.jpg"),
    ("🛰️ Visión Orbital", "Sube una imagen y permite que el radar detecte objetos flotando.", "https://tmcata.streamlit.app", "🔭 Iniciar Visión Orbital", "5.jpg"),
    ("🪶 Traductor de Ecos", "Convierte tus transmisiones de voz en texto interplanetario.", "https://traductor-cata.streamlit.app", "🛰️ Abrir Traductor", "6.jpg"),
    ("📡 Escáner Galáctico", "Analiza archivos con IA estelar.", "https://tdfesp-cata.streamlit.app", "📄 Analizar Archivo", "7.jpg"),
    ("👁️ Detector Alienígena", "Escanea rostros del cosmos.", "https://ocr-audio-cata.streamlit.app", "👽 Activar Detección", "ali.jpg"),
    ("🔤 OCR Estelar", "Convierte texto desde imágenes espaciales.", "https://ocrcata.streamlit.app", "🪞 Iniciar OCR", "9.jpg"),
    ("🗣️ Chat Cósmico con PDF", "Habla con tus archivos y recibe respuestas del universo.", "https://chatcata.streamlit.app", "📡 Conectar Chat", "10.jpg"),
    ("🌠 Historias Estelares", "Dibuja algo y deja que la IA genere una historia cósmica.", "https://handcata.streamlit.app", "🌟 Crear Historia", "11.jpg"),
    ("🎙️ Control por Voz", "Controla la nave mediante comandos de voz.", "https://ctrlvoice-cata.streamlit.app", "🎧 Activar Control", "12.jpg"),
    ("🖌️ Reconocimiento de Dibujo", "La IA intenta descifrar tu figura celeste.", "https://hist-infcata.streamlit.app", "🖍️ Reconocer Dibujo", "13.jpg"),
    ("💡 Control de Luz", "Controla sistemas luminosos interestelares.", "https://sendcmqtt-cata.streamlit.app", "💫 Encender Luz", "8.jpg"),
    ("📖 Explorador de Textos", "Analiza textos de cualquier idioma.", "https://tf-idfcata.streamlit.app", "📚 Iniciar Exploración", "1.jpg")
]

# --- DISTRIBUCIÓN EN 3 COLUMNAS ---
col1, col2, col3 = st.columns(3, gap="large")

for i, (titulo, texto, link, boton, imagen) in enumerate(proyectos):
    col = [col1, col2, col3][i % 3]
    with col:
        st.markdown(f"""
        <div class="card">
            <img src="{imagen}" alt="{titulo}">
            <h3>{titulo}</h3>
            <p>{texto}</p>
            <a href="{link}" target="_blank">
                <button>{boton}</button>
            </a>
        </div>
        """, unsafe_allow_html=True)
