import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Nave Cata-IA 🚀", layout="wide")

# --- CSS GALÁCTICO ---
st.markdown("""
<style>
body {
    background: radial-gradient(circle at 20% 20%, #1a002b, #0a0015 80%);
    color: white;
}

h1, h2, h3 {
    text-align: center;
}

.tarjeta {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.08);
}

.tarjeta:hover {
    transform: translateY(-8px);
    box-shadow: 0 0 35px rgba(255, 150, 255, 0.3);
}

.tarjeta img {
    width: 100%;
    border-radius: 12px;
}

.boton-galactico {
    background: linear-gradient(90deg, #6b00b6, #ff0084);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 20px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

.boton-galactico:hover {
    box-shadow: 0 0 15px #ff66c4;
    transform: scale(1.05);
}

.sidebar .sidebar-content {
    background-color: #0d0221;
}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.markdown("""
🌠 **Panel de Misión**

Bienvenida a la **Nave Cata-IA 🚀**
Desde aquí puedes viajar a todos los mundos que has creado en tu cosmos digital.
""")

# --- TÍTULO PRINCIPAL ---
st.title("🚀 Mis Aplicaciones IA Galácticas")
st.markdown("Explora el universo digital — cada aplicación es un planeta brillante en mi constelación de Inteligencia Artificial 🌌")

# --- DATOS DE LAS 15 APLICACIONES ---
apps = [
    {
        "titulo": "Mi Primera Misión",
        "descripcion": "Mi primer lanzamiento hacia el espacio del código.",
        "imagen": "https://i.imgur.com/qIufhof.png",
        "boton": "Lanzar Misión",
        "link": "https://catalinamendezapps.streamlit.app/mi_primera_mision"
    },
    {
        "titulo": "Voz Estelar",
        "descripcion": "Convierte tus pensamientos en ondas sonoras cósmicas.",
        "imagen": "https://i.imgur.com/AvyYtHx.png",
        "boton": "Activar Voz Estelar",
        "link": "https://catalinamendezapps.streamlit.app/voz_estelar"
    },
    {
        "titulo": "Radar de Energía",
        "descripcion": "Analiza la energía emocional de tus mensajes.",
        "imagen": "https://i.imgur.com/VN2c4U2.png",
        "boton": "Escanear Energía",
        "link": "https://catalinamendezapps.streamlit.app/radar_energia"
    },
    # --- Agrega aquí tus otras 12 apps ---
    {
        "titulo": "Planeta Creativo",
        "descripcion": "Explora ideas del universo de la imaginación.",
        "imagen": "https://i.imgur.com/XVqfRrM.png",
        "boton": "Explorar",
        "link": "https://catalinamendezapps.streamlit.app/planeta_creativo"
    },
    {
        "titulo": "Constelación Visual",
        "descripcion": "Transforma tus imágenes en arte espacial.",
        "imagen": "https://i.imgur.com/5HnHn2C.png",
        "boton": "Crear Arte",
        "link": "https://catalinamendezapps.streamlit.app/constelacion_visual"
    },
    {
        "titulo": "Bitácora Galáctica",
        "descripcion": "Registra tus viajes interplanetarios de IA.",
        "imagen": "https://i.imgur.com/8emHuBq.png",
        "boton": "Abrir Bitácora",
        "link": "https://catalinamendezapps.streamlit.app/bitacora_galactica"
    },
    {
        "titulo": "Nave de Traducción",
        "descripcion": "Traduce mensajes a cualquier idioma del cosmos.",
        "imagen": "https://i.imgur.com/kq9S3sF.png",
        "boton": "Traducir",
        "link": "https://catalinamendezapps.streamlit.app/nave_traduccion"
    },
    {
        "titulo": "Mapa de Sentimientos",
        "descripcion": "Explora las emociones del universo con IA.",
        "imagen": "https://i.imgur.com/nwV3bKi.png",
        "boton": "Explorar Mapa",
        "link": "https://catalinamendezapps.streamlit.app/mapa_sentimientos"
    },
    {
        "titulo": "Sistema Solar Creativo",
        "descripcion": "Diseña tu propio sistema de apps con IA.",
        "imagen": "https://i.imgur.com/XyGfQ9E.png",
        "boton": "Diseñar Sistema",
        "link": "https://catalinamendezapps.streamlit.app/sistema_solar"
    },
    {
        "titulo": "Códigos Estelares",
        "descripcion": "Descifra mensajes ocultos del espacio digital.",
        "imagen": "https://i.imgur.com/ypynl5p.png",
        "boton": "Descifrar",
        "link": "https://catalinamendezapps.streamlit.app/codigos_estelares"
    },
    {
        "titulo": "Eco Lunar",
        "descripcion": "Escucha la resonancia emocional de tus textos.",
        "imagen": "https://i.imgur.com/Du8A5GA.png",
        "boton": "Escuchar Eco",
        "link": "https://catalinamendezapps.streamlit.app/eco_lunar"
    },
    {
        "titulo": "Centro de Comando",
        "descripcion": "Administra todas tus misiones IA desde un punto.",
        "imagen": "https://i.imgur.com/zoP4rWh.png",
        "boton": "Entrar al Centro",
        "link": "https://catalinamendezapps.streamlit.app/centro_comando"
    },
    {
        "titulo": "Universo Sonoro",
        "descripcion": "Convierte texto en melodías galácticas.",
        "imagen": "https://i.imgur.com/N2rUxEr.png",
        "boton": "Reproducir",
        "link": "https://catalinamendezapps.streamlit.app/universo_sonoro"
    },
    {
        "titulo": "Pulso Cósmico",
        "descripcion": "Detecta la frecuencia emocional de tus ideas.",
        "imagen": "https://i.imgur.com/yL6cU2g.png",
        "boton": "Medir Pulso",
        "link": "https://catalinamendezapps.streamlit.app/pulso_cosmico"
    },
    {
        "titulo": "Nube de Ideas",
        "descripcion": "Crea lluvias de inspiración artificial.",
        "imagen": "https://i.imgur.com/Vf8h3Ue.png",
        "boton": "Lluvia de Ideas",
        "link": "https://catalinamendezapps.streamlit.app/nube_ideas"
    },
    {
        "titulo": "Portales Interdimensionales",
        "descripcion": "Abre puertas a nuevas realidades digitales.",
        "imagen": "https://i.imgur.com/kKQ6Mfq.png",
        "boton": "Abrir Portal",
        "link": "https://catalinamendezapps.streamlit.app/portales"
    },
]

# --- MOSTRAR LAS TARJETAS EN FILAS DE 3 ---
cols = st.columns(3)
for i, app in enumerate(apps):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="tarjeta">
            <img src="{app['imagen']}" alt="{app['titulo']}">
            <h3>{app['titulo']}</h3>
            <p>{app['descripcion']}</p>
            <a href="{app['link']}" target="_blank">
                <button class="boton-galactico">{app['boton']}</button>
            </a>
        </div>
        """, unsafe_allow_html=True)
        if (i + 1) % 3 == 0:
            st.write("")
