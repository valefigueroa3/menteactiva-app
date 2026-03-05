# =============================================================
# MenteActiva - Generador de Ejercicios Cognitivos
# Para adultos mayores
# Ejecutar con: streamlit run app.py
# =============================================================

import streamlit as st
import random

# ---------------------------------------------------------------
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# ---------------------------------------------------------------
st.set_page_config(
    page_title="MenteActiva",
    page_icon=None,
    layout="centered"
)

# ---------------------------------------------------------------
# ESTILOS CSS — PALETA CÁLIDA Y DISEÑO AMIGABLE
# Paleta: azul pizarra + terracota + crema
# ---------------------------------------------------------------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap');

        /* ---- BASE ---- */
        html, body, [class*="css"] {
            font-family: 'Montserrat', sans-serif;
            font-size: 18px !important;
            background-color: #FAF7F2 !important;
            color: #2D2D2D;
        }

        /* Fondo general de la app */
        .stApp {
            background-color: #FAF7F2;
        }

        /* ---- BANNER SUPERIOR ---- */
        .banner {
            background: linear-gradient(135deg, #3D5A80 0%, #5B84B1 60%, #7FA9D4 100%);
            border-radius: 16px;
            padding: 2.2rem 2rem 1.8rem 2rem;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(61,90,128,0.18);
        }
        .banner h1 {
            font-family: 'Montserrat', sans-serif;
            font-size: 2rem !important;
            color: #FFFFFF !important;
            margin: 0 0 0.3rem 0;
            letter-spacing: 1px;
            text-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }
        .banner p {
            font-size: 0.95rem;
            color: #D9E8F5;
            margin: 0;
            font-weight: 300;
        }

        /* ---- SECCIÓN DEL FORMULARIO ---- */
        .form-box {
            background: #FFFFFF;
            border-radius: 16px;
            padding: 1.8rem 2rem;
            box-shadow: 0 2px 16px rgba(0,0,0,0.07);
            margin-bottom: 1.8rem;
        }
        .form-box h2 {
            font-family: 'Montserrat', sans-serif;
            font-size: 1.6rem !important;
            color: #3D5A80 !important;
            margin-top: 0;
            border-bottom: 2px solid #E8EEF5;
            padding-bottom: 0.6rem;
            margin-bottom: 1.2rem;
        }

        /* Títulos generales */
        h2 {
            font-size: 1.7rem !important;
            color: #3D5A80;
        }
        h3 {
            font-size: 1.35rem !important;
            color: #3D5A80;
        }

        /* Etiquetas de campos */
        label, .stSelectbox label, .stNumberInput label, .stSlider label {
            font-size: 1.1rem !important;
            font-weight: 700;
            color: #3D5A80 !important;
        }

        /* Campos de entrada */
        .stSelectbox > div > div,
        .stNumberInput > div > div > input {
            border-radius: 8px !important;
            border: 1.5px solid #C5D5E8 !important;
            background-color: #F5F8FC !important;
            font-size: 1.05rem !important;
        }

        /* Texto visible en selectbox — corrige letra blanca en móvil */
        .stSelectbox > div > div > div,
        .stSelectbox > div > div > div *,
        .stSelectbox span,
        .stSelectbox p,
        [data-baseweb="select"] *,
        [data-baseweb="select"] span,
        [data-baseweb="select"] div,
        [data-baseweb="popover"] li,
        [data-baseweb="popover"] span,
        [data-baseweb="menu"] li,
        [data-baseweb="menu"] span {
            color: #2D2D2D !important;
        }

        /* Fondo del menú desplegable — fuerza blanco y letra oscura */
        [data-baseweb="popover"],
        [data-baseweb="popover"] > div,
        [data-baseweb="menu"],
        [data-baseweb="menu"] > ul,
        [data-baseweb="menu"] li,
        ul[role="listbox"],
        ul[role="listbox"] li,
        div[role="option"],
        div[role="listbox"] {
            background-color: #FFFFFF !important;
            color: #2D2D2D !important;
        }

        /* Todo el texto dentro del desplegable */
        [data-baseweb="popover"] *,
        [data-baseweb="menu"] *,
        ul[role="listbox"] *,
        div[role="option"] * {
            color: #2D2D2D !important;
            background-color: transparent !important;
        }

        /* Opción seleccionada dentro del menú */
        [data-baseweb="menu"] [aria-selected="true"],
        div[role="option"][aria-selected="true"] {
            background-color: #E8F0F9 !important;
            color: #3D5A80 !important;
        }

        /* Hover sobre opciones */
        [data-baseweb="menu"] li:hover,
        div[role="option"]:hover {
            background-color: #F0F5FA !important;
        }

        /* Slider */
        .stSlider > div > div > div > div {
            background-color: #3D5A80 !important;
        }

        /* ---- BOTÓN PRINCIPAL ---- */
        .stButton > button {
            background: linear-gradient(135deg, #E07A5F, #C85A3F);
            color: white;
            font-size: 1.2rem !important;
            font-weight: 700;
            font-family: 'Montserrat', sans-serif;
            padding: 0.75rem 2rem;
            border-radius: 50px;
            border: none;
            width: 100%;
            box-shadow: 0 4px 14px rgba(224,122,95,0.35);
            transition: all 0.2s ease;
            letter-spacing: 0.5px;
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, #C85A3F, #A84030);
            box-shadow: 0 6px 18px rgba(224,122,95,0.45);
            transform: translateY(-1px);
        }

        /* ---- TARJETAS DE EJERCICIOS ---- */
        .ejercicio-card {
            background: #FFFFFF;
            border-radius: 16px;
            padding: 1.6rem 1.8rem;
            margin-bottom: 1.6rem;
            font-size: 1.1rem;
            box-shadow: 0 3px 18px rgba(0,0,0,0.08);
            border-top: 5px solid #3D5A80;
            transition: box-shadow 0.2s ease;
        }
        .ejercicio-card:hover {
            box-shadow: 0 6px 24px rgba(0,0,0,0.13);
        }
        .ejercicio-card h3 {
            font-family: 'Montserrat', sans-serif;
            color: #3D5A80 !important;
            margin-top: 0;
        }
        /* Colores por tipo de ejercicio */
        .tipo-memoria    { border-top-color: #5B84B1; }
        .tipo-razonamiento { border-top-color: #E07A5F; }
        .tipo-verbal     { border-top-color: #6BAE9B; }
        .tipo-atencion   { border-top-color: #9B7DC8; }

        /* Badge de tipo */
        .badge {
            display: inline-block;
            padding: 0.25rem 0.85rem;
            border-radius: 50px;
            font-size: 0.9rem;
            font-weight: 700;
            margin-bottom: 0.8rem;
            letter-spacing: 0.4px;
        }
        .badge-memoria     { background: #E8F0F9; color: #3D5A80; }
        .badge-razonamiento{ background: #FCEEE9; color: #C85A3F; }
        .badge-verbal      { background: #E8F5F2; color: #3D8A7A; }
        .badge-atencion    { background: #F2EDF8; color: #7B5CA8; }

        /* Línea divisoria dentro de tarjeta */
        .ejercicio-card hr {
            border: none;
            border-top: 1.5px solid #F0F0F0;
            margin: 1rem 0;
        }

        /* ---- PIE DE PÁGINA ---- */
        .footer {
            text-align: center;
            padding: 1.2rem;
            margin-top: 1rem;
            font-size: 0.9rem;
            color: #AAAAAA;
            border-top: 1px solid #ECECEC;
        }

        /* ---- MENSAJE MOTIVACIONAL ---- */
        .motivacion {
            background: linear-gradient(135deg, #EEF4FB, #E8F5F0);
            border-radius: 12px;
            padding: 1.2rem 1.6rem;
            text-align: center;
            font-size: 1.15rem;
            color: #3D5A80;
            font-weight: 600;
            margin-top: 1rem;
            border: 1.5px solid #C5D5E8;
        }
    </style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------
# BANCO DE EJERCICIOS COGNITIVOS
# Cada ejercicio tiene: título, instrucciones, habilidad, 
# dificultad (bajo/medio/alto), tiempo mínimo (minutos)
# ---------------------------------------------------------------
EJERCICIOS = [

    # === MEMORIA ===
    {
        "tipo": "memoria",
        "titulo": "Lista de palabras",
        "instrucciones": (
            "Lee despacio la siguiente lista de 5 palabras: "
            "CASA, PERRO, ÁRBOL, LUNA, PAN. "
            "Cierra los ojos durante 30 segundos. "
            "Luego intenta escribirlas o decirlas en voz alta, "
            "en el orden que recuerdes."
        ),
        "habilidad": "Memoria a corto plazo",
        "dificultad": "bajo",
        "tiempo": 5,
    },
    {
        "tipo": "memoria",
        "titulo": "Recuerda los colores",
        "instrucciones": (
            "Observa esta secuencia de colores durante 20 segundos: "
            "ROJO — AZUL — VERDE — AMARILLO — BLANCO. "
            "Cubre la pantalla y espera 1 minuto. "
            "Escribe los colores en el mismo orden que aparecían."
        ),
        "habilidad": "Memoria visual y secuencial",
        "dificultad": "bajo",
        "tiempo": 5,
    },
    {
        "tipo": "memoria",
        "titulo": "Historia breve",
        "instrucciones": (
            "Lee este párrafo una sola vez, con calma: "
            "'María fue al mercado el martes por la mañana. "
            "Compró 3 manzanas, un kilo de arroz y una botella de aceite. "
            "Al regresar, se encontró con su vecina Rosa y tomaron un café.' "
            "Sin releer, responde: ¿Qué día fue María? ¿Cuántas manzanas compró? "
            "¿Con quién se encontró?"
        ),
        "habilidad": "Memoria episódica y comprensión lectora",
        "dificultad": "medio",
        "tiempo": 8,
    },
    {
        "tipo": "memoria",
        "titulo": "Números al revés",
        "instrucciones": (
            "Lee estos números UNA vez: 7 — 4 — 2 — 9 — 5. "
            "Ahora repítelos en orden INVERSO (de último a primero) "
            "en voz alta o escríbelos. "
            "Intenta hacerlo sin volver a mirarlos."
        ),
        "habilidad": "Memoria de trabajo",
        "dificultad": "alto",
        "tiempo": 10,
    },

    # === RAZONAMIENTO LÓGICO ===
    {
        "tipo": "razonamiento",
        "titulo": "¿Qué sigue?",
        "instrucciones": (
            "Observa la siguiente secuencia y decide qué número continúa: "
            "2 — 4 — 6 — 8 — ___. "
            "Ahora intenta esta otra: 1 — 3 — 6 — 10 — ___. "
            "Piensa en la regla que siguen los números antes de responder."
        ),
        "habilidad": "Razonamiento lógico y reconocimiento de patrones",
        "dificultad": "bajo",
        "tiempo": 5,
    },
    {
        "tipo": "razonamiento",
        "titulo": "El intruso",
        "instrucciones": (
            "En cada grupo, encuentra la palabra que NO pertenece y explica por qué: \n"
            "1. Perro — Gato — Mesa — Caballo \n"
            "2. Manzana — Naranja — Zanahoria — Pera \n"
            "3. Rojo — Azul — Verde — Cuadrado \n"
            "No hay respuestas únicas: lo importante es tu razonamiento."
        ),
        "habilidad": "Clasificación y razonamiento categorial",
        "dificultad": "bajo",
        "tiempo": 7,
    },
    {
        "tipo": "razonamiento",
        "titulo": "Acertijo sencillo",
        "instrucciones": (
            "Lee con calma y piensa la respuesta: \n"
            "'Tengo ciudades, pero no casas. "
            "Tengo montañas, pero no árboles. "
            "Tengo agua, pero no peces. "
            "Tengo caminos, pero no autos. ¿Qué soy?' \n\n"
            "Tómate el tiempo que necesites. La respuesta es: UN MAPA."
        ),
        "habilidad": "Razonamiento abstracto",
        "dificultad": "medio",
        "tiempo": 8,
    },
    {
        "tipo": "razonamiento",
        "titulo": "Problema cotidiano",
        "instrucciones": (
            "Resuelve este problema paso a paso: \n"
            "Ana tiene $500. Compra una bolsa de pan por $120 "
            "y dos litros de leche a $90 cada uno. "
            "¿Cuánto dinero le queda? \n\n"
            "Intenta hacerlo mentalmente antes de usar papel."
        ),
        "habilidad": "Razonamiento numérico y aritmética mental",
        "dificultad": "medio",
        "tiempo": 8,
    },
    {
        "tipo": "razonamiento",
        "titulo": "Rompecabezas de lógica",
        "instrucciones": (
            "Lee el siguiente problema: \n"
            "'Luis es más alto que Pedro. Pedro es más alto que Juan. "
            "Juan es más alto que Carlos.' \n"
            "Responde sin volver a leer: "
            "¿Quién es el más alto? ¿Quién es el más bajo? "
            "¿Pedro es más alto que Carlos?"
        ),
        "habilidad": "Razonamiento deductivo",
        "dificultad": "alto",
        "tiempo": 10,
    },

    # === FLUIDEZ VERBAL ===
    {
        "tipo": "verbal",
        "titulo": "Palabras con letra",
        "instrucciones": (
            "Durante 2 minutos, escribe o di en voz alta todas las palabras "
            "que se te ocurran que comiencen con la letra M. "
            "No vale repetir palabras. "
            "Intenta llegar a 10 palabras."
        ),
        "habilidad": "Fluidez verbal fonológica",
        "dificultad": "bajo",
        "tiempo": 5,
    },
    {
        "tipo": "verbal",
        "titulo": "Animales del campo",
        "instrucciones": (
            "En 2 minutos, nombra todos los animales que viven en el campo "
            "que puedas recordar. "
            "Dícelos en voz alta o escríbelos. "
            "Meta sugerida: 12 animales distintos."
        ),
        "habilidad": "Fluidez verbal semántica",
        "dificultad": "bajo",
        "tiempo": 5,
    },
    {
        "tipo": "verbal",
        "titulo": "Completa el refrán",
        "instrucciones": (
            "Completa estos refranes populares con la palabra que falta: \n"
            "1. 'A caballo regalado, no le mires el ___.' \n"
            "2. 'Más vale tarde que ___.' \n"
            "3. 'El que mucho abarca, poco ___.' \n"
            "Luego explica con tus palabras qué significa uno de ellos."
        ),
        "habilidad": "Memoria semántica y fluidez verbal",
        "dificultad": "medio",
        "tiempo": 7,
    },
    {
        "tipo": "verbal",
        "titulo": "Cuento en cadena",
        "instrucciones": (
            "Inventa una historia corta (al menos 5 oraciones) "
            "usando obligatoriamente estas 4 palabras: "
            "PUENTE — NIÑO — LLUVIA — SOMBRERO. \n"
            "Puedes escribirla o contarla en voz alta. "
            "No hay respuestas incorrectas, ¡sé creativo!"
        ),
        "habilidad": "Fluidez verbal y creatividad",
        "dificultad": "alto",
        "tiempo": 12,
    },

    # === ATENCIÓN ===
    {
        "tipo": "atencion",
        "titulo": "Cuenta regresiva",
        "instrucciones": (
            "Cuenta hacia atrás desde 50 hasta 1, "
            "de uno en uno, en voz alta o por escrito. "
            "Hazlo despacio y sin saltarte ningún número. "
            "Si te equivocas, vuelve a empezar desde donde cometiste el error."
        ),
        "habilidad": "Atención sostenida y concentración",
        "dificultad": "bajo",
        "tiempo": 5,
    },
    {
        "tipo": "atencion",
        "titulo": "Busca la letra",
        "instrucciones": (
            "Lee este texto lentamente y rodea con un círculo "
            "(o cuenta mentalmente) todas las letras A que encuentres: \n\n"
            "'La abuela Ana amaba los árboles del jardín. "
            "Cada mañana salía a regar las plantas antes de almorzar.' \n\n"
            "¿Cuántas letras A encontraste? (Respuesta: 14)"
        ),
        "habilidad": "Atención selectiva",
        "dificultad": "bajo",
        "tiempo": 5,
    },
    {
        "tipo": "atencion",
        "titulo": "Doble tarea",
        "instrucciones": (
            "Realiza estas dos actividades al mismo tiempo: \n"
            "1. Golpea suavemente la mesa con tu mano derecha al ritmo de 1 por segundo. \n"
            "2. Mientras tanto, nombra en voz alta frutas: una fruta por cada golpe. \n"
            "Intenta mantener el ritmo durante 1 minuto sin repetir frutas."
        ),
        "habilidad": "Atención dividida",
        "dificultad": "medio",
        "tiempo": 8,
    },
    {
        "tipo": "atencion",
        "titulo": "Resta mental",
        "instrucciones": (
            "Comienza en 100 y resta 7 de forma continua: "
            "100, 93, 86, 79... y así sucesivamente. \n"
            "Hazlo en voz alta o por escrito, sin usar calculadora. \n"
            "Intenta llegar hasta 0 o lo más lejos que puedas."
        ),
        "habilidad": "Atención concentrada y aritmética mental",
        "dificultad": "alto",
        "tiempo": 10,
    },
]


# ---------------------------------------------------------------
# FUNCIÓN PRINCIPAL: SELECCIÓN DE EJERCICIOS PERSONALIZADOS
# Filtra y elige ejercicios según el perfil del usuario
# ---------------------------------------------------------------
def seleccionar_ejercicios(dificultad, tiempo_disponible, nivel_memoria):
    """
    Selecciona 3 ejercicios cognitivos adaptados al perfil del usuario.

    Parámetros:
        dificultad      (str): "bajo", "medio" o "alto"
        tiempo_disponible (int): minutos disponibles
        nivel_memoria   (str): "bajo", "medio" o "alto"

    Retorna:
        Lista de 3 diccionarios de ejercicios
    """

    # Mapa de dificultad: si el usuario eligió "medio",
    # incluimos ejercicios de nivel bajo y medio
    niveles_aceptados = {
        "bajo": ["bajo"],
        "medio": ["bajo", "medio"],
        "alto":  ["bajo", "medio", "alto"],
    }
    niveles = niveles_aceptados.get(dificultad, ["bajo"])

    # Si el nivel de memoria es bajo, priorizamos ejercicios de memoria
    if nivel_memoria == "bajo":
        tipos_prioritarios = ["memoria", "atencion"]
    elif nivel_memoria == "medio":
        tipos_prioritarios = ["memoria", "razonamiento", "verbal", "atencion"]
    else:
        tipos_prioritarios = ["razonamiento", "verbal", "atencion", "memoria"]

    # Filtrar ejercicios que cumplan con dificultad y tiempo
    candidatos = [
        e for e in EJERCICIOS
        if e["dificultad"] in niveles
        and e["tiempo"] <= tiempo_disponible
    ]

    # Si quedan muy pocos candidatos, ampliaremos el filtro de tiempo
    if len(candidatos) < 3:
        candidatos = [
            e for e in EJERCICIOS
            if e["dificultad"] in niveles
        ]

    # Si aún así no hay suficientes, usamos todos
    if len(candidatos) < 3:
        candidatos = EJERCICIOS.copy()

    # Intentar incluir variedad de tipos cognitivos
    seleccionados = []
    tipos_usados = []

    # Primera pasada: priorizar tipos recomendados con variedad
    random.shuffle(candidatos)
    for ejercicio in candidatos:
        if len(seleccionados) >= 3:
            break
        if ejercicio["tipo"] not in tipos_usados:
            seleccionados.append(ejercicio)
            tipos_usados.append(ejercicio["tipo"])

    # Segunda pasada: completar si faltan ejercicios
    for ejercicio in candidatos:
        if len(seleccionados) >= 3:
            break
        if ejercicio not in seleccionados:
            seleccionados.append(ejercicio)

    return seleccionados[:3]


# ---------------------------------------------------------------
# ENCABEZADO DE LA APLICACIÓN
# ---------------------------------------------------------------
st.markdown("""
    <div class="banner">
        <h1>MenteActiva</h1>
        <p>Ejercicios cognitivos personalizados para mantener tu mente activa</p>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# FORMULARIO DE DATOS DEL USUARIO
# ---------------------------------------------------------------
st.markdown("""
    <div class="form-box">
        <h2>Cuentanos sobre ti</h2>
        <p style="color:#666; font-size:1.05rem;">Completa los siguientes datos para recibir ejercicios adaptados a ti.</p>
    </div>
""", unsafe_allow_html=True)

# Organizar campos en dos columnas para mejor aprovechamiento del espacio
col1, col2 = st.columns(2)

with col1:
    edad = st.number_input(
        "¿Cuántos años tienes?",
        min_value=50,
        max_value=100,
        value=65,
        step=1,
        help="Ingresa tu edad actual"
    )

    nivel_memoria = st.selectbox(
        "¿Cómo sientes tu memoria últimamente?",
        options=["bajo", "medio", "alto"],
        index=1,
        format_func=lambda x: {"bajo": "Baja — Me cuesta recordar cosas",
                                "medio": "Media — A veces olvido cosas",
                                "alto": "Alta — Recuerdo bien"}[x],
        help="Selecciona cómo percibes tu memoria"
    )

    nivel_educativo = st.selectbox(
        "¿Cuál es tu nivel educativo?",
        options=["primaria", "secundaria", "universidad"],
        index=1,
        format_func=lambda x: {"primaria": "Primaria",
                                "secundaria": "Secundaria / Bachillerato",
                                "universidad": "Universidad o más"}[x]
    )

with col2:
    tiempo_disponible = st.slider(
        "¿Cuántos minutos tienes disponibles?",
        min_value=5,
        max_value=60,
        value=15,
        step=5,
        help="Selecciona el tiempo que puedes dedicar a los ejercicios"
    )

    dificultad = st.selectbox(
        "¿Qué nivel de dificultad prefieres?",
        options=["bajo", "medio", "alto"],
        index=1,
        format_func=lambda x: {"bajo": "Bajo — Quiero algo tranquilo",
                                "medio": "Medio — Un poco de desafío",
                                "alto": "Alto — Quiero desafiarme"}[x]
    )

st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# BOTÓN PARA GENERAR EJERCICIOS
# ---------------------------------------------------------------
generar = st.button("Generar mis ejercicios")

# ---------------------------------------------------------------
# MOSTRAR LOS EJERCICIOS GENERADOS
# ---------------------------------------------------------------
if generar:

    # Seleccionar ejercicios según el perfil ingresado
    ejercicios = seleccionar_ejercicios(dificultad, tiempo_disponible, nivel_memoria)

    # Mensaje de bienvenida personalizado
    st.markdown(
        f"""<div style='background:#EEF4FB; border-radius:12px; padding:1.2rem 1.6rem;
                        margin-bottom:1.5rem; border-left: 5px solid #3D5A80;'>
            <h2 style='color:#3D5A80; margin:0 0 0.4rem 0; font-size:1.6rem;'>Tus ejercicios de hoy</h2>
            <p style='color:#555; margin:0; font-size:1.05rem;'>Preparados para ti con nivel
            <strong style='color:#E07A5F;'>{dificultad}</strong> y
            {tiempo_disponible} minutos disponibles.</p>
        </div>""",
        unsafe_allow_html=True
    )

    # Etiquetas y clases por tipo de ejercicio
    tipos_info = {
        "memoria":       {"label": "Memoria",            "badge": "badge-memoria",      "card": "tipo-memoria"},
        "razonamiento":  {"label": "Razonamiento logico", "badge": "badge-razonamiento", "card": "tipo-razonamiento"},
        "verbal":        {"label": "Fluidez verbal",      "badge": "badge-verbal",       "card": "tipo-verbal"},
        "atencion":      {"label": "Atencion",            "badge": "badge-atencion",     "card": "tipo-atencion"},
    }

    # Mostrar cada ejercicio como una tarjeta visual
    for i, ejercicio in enumerate(ejercicios, start=1):

        info = tipos_info.get(ejercicio["tipo"], {"label": ejercicio["tipo"].capitalize(), "badge": "", "card": ""})

        # Tarjeta del ejercicio con HTML personalizado
        st.markdown(
            f"""
            <div class="ejercicio-card {info['card']}">
                <span class="badge {info['badge']}">{info['label']}</span>
                <h3>Ejercicio {i} — {ejercicio['titulo']}</h3>
                <p style="color:#555; margin:0.2rem 0;">
                    <strong style="color:#3D5A80;">Habilidad que estimula:</strong>
                    {ejercicio['habilidad']}
                </p>
                <p style="color:#555; margin:0.2rem 0 0.8rem 0;">
                    <strong style="color:#3D5A80;">Tiempo estimado:</strong>
                    {ejercicio['tiempo']} minutos
                </p>
                <hr/>
                <p style="font-weight:700; color:#3D5A80; margin-bottom:0.4rem;">Instrucciones:</p>
                <p style="font-size:1.12rem; line-height:1.8; color:#333;">{ejercicio['instrucciones']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Mensaje de cierre motivacional
    st.markdown(
        "<div class='motivacion'>"
        "Recuerda que ejercitar la mente cada dia hace la diferencia."
        " Tomatelo con calma y disfruta cada ejercicio."
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center; font-size:0.95rem; color:#aaa; margin-top:0.8rem;'>"
        "Presiona el boton nuevamente para obtener otros ejercicios.</p>",
        unsafe_allow_html=True
    )

# ---------------------------------------------------------------
# PIE DE PÁGINA
# ---------------------------------------------------------------
st.markdown(
    "<div class='footer'>MenteActiva &mdash; Cuida tu mente, vive mejor</div>",
    unsafe_allow_html=True
)
