import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import os


# ============================================================
# SPORT CHAT V2.4
# ============================================================

COLOR_FONDO = "#0B1320"
COLOR_PANEL = "#111C2E"
COLOR_PANEL_2 = "#17253A"
COLOR_TEXTO = "#F5F7FA"
COLOR_SECUNDARIO = "#AAB7C4"
COLOR_ACENTO = "#00D4FF"
COLOR_ACENTO_2 = "#7C4DFF"

RUTA_CBUM = "cbum.jpg"

imagen_actual = None


# ============================================================
# BASE DE DATOS
# ============================================================

PERFILES = {

    # ===================== FÚTBOL ============================

    "messi": {
        "datos": (
            "Lionel Messi",
            "Argentina",
            "Inter Miami",
            "Fútbol",
            "Delantero",
            "24/06/1987",
            "Activo"
        ),
        "stats": (
            "⚽ Goles: 800+\n"
            "🎯 Asistencias: 350+\n"
            "🏆 Balones de Oro: 8\n"
            "🌎 Mundial: 1"
        )
    },

    "cristiano": {
        "datos": (
            "Cristiano Ronaldo",
            "Portugal",
            "Al-Nassr",
            "Fútbol",
            "Delantero",
            "05/02/1985",
            "Activo"
        ),
        "stats": (
            "⚽ Goles: 900+\n"
            "🎯 Asistencias: 250+\n"
            "🏆 Balones de Oro: 5\n"
            "🏆 Champions League: 5"
        )
    },

    "haaland": {
        "datos": (
            "Erling Haaland",
            "Noruega",
            "Manchester City",
            "Fútbol",
            "Delantero",
            "21/07/2000",
            "Activo"
        ),
        "stats": (
            "⚽ Goles: 300+\n"
            "🎯 Asistencias: 70+\n"
            "🏆 Champions League: 1\n"
            "🏆 Premier League: 2+"
        )
    },

    "mbappe": {
        "datos": (
            "Kylian Mbappé",
            "Francia",
            "Real Madrid",
            "Fútbol",
            "Delantero",
            "20/12/1998",
            "Activo"
        ),
        "stats": (
            "⚽ Goles: 400+\n"
            "🎯 Asistencias: 130+\n"
            "🌎 Mundial: 1\n"
            "🏆 Ligue 1: 6+"
        )
    },

    "neymar": {
        "datos": (
            "Neymar Jr.",
            "Brasil",
            "Santos",
            "Fútbol",
            "Delantero",
            "05/02/1992",
            "Activo"
        ),
        "stats": (
            "⚽ Goles: 450+\n"
            "🎯 Asistencias: 250+\n"
            "🏆 Champions League: 1\n"
            "🌎 Copa Libertadores: 1"
        )
    },

    "salah": {
        "datos": (
            "Mohamed Salah",
            "Egipto",
            "Liverpool",
            "Fútbol",
            "Delantero",
            "15/06/1992",
            "Activo"
        ),
        "stats": (
            "⚽ Goles: 350+\n"
            "🎯 Asistencias: 150+\n"
            "🏆 Champions League: 1\n"
            "🏆 Premier League: 1+"
        )
    },

    "de bruyne": {
        "datos": (
            "Kevin De Bruyne",
            "Bélgica",
            "Manchester City",
            "Fútbol",
            "Mediocampista",
            "28/06/1991",
            "Activo"
        ),
        "stats": (
            "⚽ Goles: 150+\n"
            "🎯 Asistencias: 250+\n"
            "🏆 Champions League: 1\n"
            "🏆 Premier League: 6"
        )
    },

    "yamal": {
        "datos": (
            "Lamine Yamal",
            "España",
            "FC Barcelona",
            "Fútbol",
            "Extremo",
            "13/07/2007",
            "Activo"
        ),
        "stats": (
            "⚽ Goles: 30+\n"
            "🎯 Asistencias: 30+\n"
            "🏆 Eurocopa: 1\n"
            "⭐ Joven talento"
        )
    },

    "julian": {
        "datos": (
            "Julián Álvarez",
            "Argentina",
            "Atlético de Madrid",
            "Fútbol",
            "Delantero",
            "31/01/2000",
            "Activo"
        ),
        "stats": (
            "⚽ Goles: 150+\n"
            "🎯 Asistencias: 50+\n"
            "🌎 Mundial: 1\n"
            "🏆 Champions League: 1"
        )
    },

    # ===================== BÁSQUETBOL ========================

    "lebron": {
        "datos": (
            "LeBron James",
            "Estados Unidos",
            "Los Angeles Lakers",
            "Básquetbol",
            "Alero",
            "30/12/1984",
            "Activo"
        ),
        "stats": (
            "🏀 Puntos: 40.000+\n"
            "🎯 Asistencias: 11.000+\n"
            "🏆 NBA: 4\n"
            "⭐ MVP: 4"
        )
    },

    "curry": {
        "datos": (
            "Stephen Curry",
            "Estados Unidos",
            "Golden State Warriors",
            "Básquetbol",
            "Base",
            "14/03/1988",
            "Activo"
        ),
        "stats": (
            "🏀 Puntos: 25.000+\n"
            "🎯 Triples: 4.000+\n"
            "🏆 NBA: 4\n"
            "⭐ MVP: 2"
        )
    },

    "jordan": {
        "datos": (
            "Michael Jordan",
            "Estados Unidos",
            "Chicago Bulls",
            "Básquetbol",
            "Escolta",
            "17/02/1963",
            "Retirado"
        ),
        "stats": (
            "🏀 Puntos: 32.292\n"
            "🏆 NBA: 6\n"
            "⭐ MVP: 5\n"
            "🏅 MVP Finales: 6"
        )
    },

    # ===================== TENIS =============================

    "djokovic": {
        "datos": (
            "Novak Djokovic",
            "Serbia",
            "ATP",
            "Tenis",
            "Jugador",
            "22/05/1987",
            "Activo"
        ),
        "stats": (
            "🎾 Grand Slams: 24\n"
            "🏆 Australian Open: 10\n"
            "🏆 Wimbledon: 7\n"
            "🥇 Oro olímpico: 1"
        )
    },

    "alcaraz": {
        "datos": (
            "Carlos Alcaraz",
            "España",
            "ATP",
            "Tenis",
            "Jugador",
            "05/05/2003",
            "Activo"
        ),
        "stats": (
            "🎾 Grand Slams: 4+\n"
            "🏆 Roland Garros: 1+\n"
            "🏆 Wimbledon: 1+\n"
            "⭐ Ex número 1"
        )
    },

    "nadal": {
        "datos": (
            "Rafael Nadal",
            "España",
            "ATP",
            "Tenis",
            "Jugador",
            "03/06/1986",
            "Retirado"
        ),
        "stats": (
            "🎾 Grand Slams: 22\n"
            "🏆 Roland Garros: 14\n"
            "🏆 US Open: 4\n"
            "🥇 Oro olímpico"
        )
    },

    # ===================== BOXEO =============================

    "canelo": {
        "datos": (
            "Saúl Canelo Álvarez",
            "México",
            "Boxeo profesional",
            "Boxeo",
            "Peso supermediano",
            "18/07/1990",
            "Activo"
        ),
        "stats": (
            "🥊 Victorias: 60+\n"
            "🥊 KO: 39+\n"
            "🏆 Campeón mundial\n"
            "⭐ Múltiples divisiones"
        )
    },

    "tyson": {
        "datos": (
            "Mike Tyson",
            "Estados Unidos",
            "Boxeo profesional",
            "Boxeo",
            "Peso pesado",
            "30/06/1966",
            "Retirado"
        ),
        "stats": (
            "🥊 Victorias: 50\n"
            "🥊 KO: 44\n"
            "🏆 Campeón mundial\n"
            "⚡ KO más joven"
        )
    },

    "ali": {
        "datos": (
            "Muhammad Ali",
            "Estados Unidos",
            "Boxeo profesional",
            "Boxeo",
            "Peso pesado",
            "17/01/1942",
            "Fallecido"
        ),
        "stats": (
            "🥊 Victorias: 56\n"
            "🥊 KO: 37\n"
            "🏆 Campeón mundial\n"
            "🥇 Oro olímpico"
        )
    },

    # ===================== FÓRMULA 1 =========================

    "verstappen": {
        "datos": (
            "Max Verstappen",
            "Países Bajos",
            "Red Bull Racing",
            "Fórmula 1",
            "Piloto",
            "30/09/1997",
            "Activo"
        ),
        "stats": (
            "🏎️ Victorias: 60+\n"
            "🏆 Mundiales: 4+\n"
            "🥇 Pole positions: 40+\n"
            "⚡ Red Bull Racing"
        )
    },

    "hamilton": {
        "datos": (
            "Lewis Hamilton",
            "Reino Unido",
            "Ferrari",
            "Fórmula 1",
            "Piloto",
            "07/01/1985",
            "Activo"
        ),
        "stats": (
            "🏎️ Victorias: 100+\n"
            "🏆 Mundiales: 7\n"
            "🥇 Pole positions: 100+\n"
            "⭐ Récords históricos"
        )
    },

    "alonso": {
        "datos": (
            "Fernando Alonso",
            "España",
            "Aston Martin",
            "Fórmula 1",
            "Piloto",
            "29/07/1981",
            "Activo"
        ),
        "stats": (
            "🏎️ Victorias: 30+\n"
            "🏆 Mundiales: 2\n"
            "🥇 Podios: 100+\n"
            "⭐ Campeón del mundo"
        )
    },

    # ===================== CULTURISMO =========================

    "arnold": {
        "datos": (
            "Arnold Schwarzenegger",
            "Austria",
            "Culturismo",
            "Culturismo",
            "Fisicoculturista",
            "30/07/1947",
            "Retirado"
        ),
        "stats": (
            "💪 Mr. Olympia: 7\n"
            "🏆 Mr. Universe\n"
            "⭐ Leyenda del culturismo\n"
            "🎬 Actor"
        )
    },

    "ronnie": {
        "datos": (
            "Ronnie Coleman",
            "Estados Unidos",
            "Culturismo",
            "Culturismo",
            "Fisicoculturista",
            "13/05/1964",
            "Retirado"
        ),
        "stats": (
            "💪 Mr. Olympia: 8\n"
            "🏆 8 títulos consecutivos\n"
            "⭐ Leyenda del culturismo\n"
            "🔥 Big Ron"
        )
    },

    "cbum": {
        "datos": (
            "Chris Bumstead",
            "Canadá",
            "Culturismo",
            "Culturismo",
            "Classic Physique",
            "02/02/1995",
            "Retirado"
        ),
        "stats": (
            "💪 Classic Physique Olympia: 6\n"
            "🏆 6 títulos consecutivos\n"
            "⭐ CBum\n"
            "🔥 Classic Physique"
        )
    }
}


# ============================================================
# ALIAS
# ============================================================

ALIAS = {
    "cr7": "cristiano",
    "cristiano ronaldo": "cristiano",

    "erling": "haaland",
    "erling haaland": "haaland",

    "kylian": "mbappe",
    "kylian mbappe": "mbappe",
    "kylian mbappé": "mbappe",

    "neymar jr": "neymar",
    "neymar jr.": "neymar",

    "mohamed salah": "salah",

    "kevin de bruyne": "de bruyne",

    "lamine": "yamal",
    "lamine yamal": "yamal",

    "julian alvarez": "julian",
    "julian álvarez": "julian",
    "julián álvarez": "julian",

    "lebron james": "lebron",
    "stephen curry": "curry",
    "michael jordan": "jordan",

    "novak djokovic": "djokovic",
    "carlos alcaraz": "alcaraz",
    "rafael nadal": "nadal",

    "canelo alvarez": "canelo",
    "saul canelo alvarez": "canelo",

    "mike tyson": "tyson",
    "muhammad ali": "ali",

    "max verstappen": "verstappen",
    "lewis hamilton": "hamilton",
    "fernando alonso": "alonso",

    "arnold schwarzenegger": "arnold",
    "ronnie coleman": "ronnie",
    "chris bumstead": "cbum"
}


# ============================================================
# FUNCIONES DE PERFIL
# ============================================================

def obtener_perfil(nombre):
    nombre = nombre.lower().strip()

    if nombre in PERFILES:
        return PERFILES[nombre]

    if nombre in ALIAS:
        return PERFILES.get(ALIAS[nombre])

    return None


def obtener_clave(nombre):
    nombre = nombre.lower().strip()

    if nombre in PERFILES:
        return nombre

    if nombre in ALIAS:
        return ALIAS[nombre]

    return None


# ============================================================
# LISTAR DEPORTISTAS POR DEPORTE
# ============================================================

def obtener_deportistas_por_deporte(deporte):
    resultado = []

    for clave, perfil in PERFILES.items():
        if perfil["datos"][3] == deporte:
            resultado.append(
                perfil["datos"][0]
            )

    return sorted(resultado)


def actualizar_deportistas(event=None):
    deporte = deporte_var.get()

    lista = obtener_deportistas_por_deporte(
        deporte
    )

    combo_deportista["values"] = lista
    combo_deportista.set("")

    estado.config(
        text=f"🏅 {len(lista)} deportistas disponibles en {deporte}"
    )


# ============================================================
# API THE SPORTS DB
# ============================================================

def buscar_en_api(nombre):
    url = (
        "https://www.thesportsdb.com/"
        "api/v1/json/123/searchplayers.php"
    )

    try:
        respuesta = requests.get(
            url,
            params={"p": nombre},
            timeout=8
        )

        respuesta.raise_for_status()

        datos = respuesta.json()

        jugadores = datos.get("player")

        if jugadores:
            return jugadores[0]

    except Exception as error:
        print(
            "Error TheSportsDB:",
            error
        )

    return None


# ============================================================
# DESCARGAR IMAGEN
# ============================================================

def descargar_imagen(url):
    try:
        respuesta = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) SportChat/2.4"
            }
        )

        respuesta.raise_for_status()

        imagen = Image.open(
            BytesIO(respuesta.content)
        ).convert("RGB")

        imagen.load()

        return imagen

    except Exception as error:
        print(
            "Error descargando imagen:",
            error
        )

        return None


# ============================================================
# API WIKIPEDIA - FOTO
# ============================================================

def buscar_foto_wikipedia(nombre):

    nombres_wikipedia = {

        "Lionel Messi": "Lionel Messi",
        "Cristiano Ronaldo": "Cristiano Ronaldo",
        "Erling Haaland": "Erling Haaland",
        "Kylian Mbappé": "Kylian Mbappé",
        "Neymar Jr.": "Neymar",
        "Mohamed Salah": "Mohamed Salah",
        "Kevin De Bruyne": "Kevin De Bruyne",
        "Lamine Yamal": "Lamine Yamal",
        "Julián Álvarez": "Julián Álvarez",

        "LeBron James": "LeBron James",
        "Stephen Curry": "Stephen Curry",
        "Michael Jordan": "Michael Jordan",

        "Novak Djokovic": "Novak Djokovic",
        "Carlos Alcaraz": "Carlos Alcaraz",
        "Rafael Nadal": "Rafael Nadal",

        "Saúl Canelo Álvarez": "Canelo Álvarez",
        "Mike Tyson": "Mike Tyson",
        "Muhammad Ali": "Muhammad Ali",

        "Max Verstappen": "Max Verstappen",
        "Lewis Hamilton": "Lewis Hamilton",
        "Fernando Alonso": "Fernando Alonso",

        "Arnold Schwarzenegger": "Arnold Schwarzenegger",
        "Ronnie Coleman": "Ronnie Coleman",
        "Chris Bumstead": "Chris Bumstead"
    }

    nombre_wiki = nombres_wikipedia.get(
        nombre,
        nombre
    )

    try:

        url = "https://en.wikipedia.org/w/api.php"

        parametros = {
            "action": "query",
            "format": "json",
            "prop": "pageimages",
            "piprop": "thumbnail",
            "pithumbsize": "500",
            "redirects": "1",
            "titles": nombre_wiki
        }

        respuesta = requests.get(
            url,
            params=parametros,
            timeout=10,
            headers={
                "User-Agent":
                "Mozilla/5.0 SportChat/2.4"
            }
        )

        respuesta.raise_for_status()

        datos = respuesta.json()

        paginas = (
            datos
            .get("query", {})
            .get("pages", {})
        )

        for pagina in paginas.values():

            thumbnail = pagina.get(
                "thumbnail"
            )

            if thumbnail:

                imagen_url = thumbnail.get(
                    "source"
                )

                if imagen_url:
                    return imagen_url

    except Exception as error:

        print(
            "Error Wikipedia:",
            error
        )

    return None


# ============================================================
# BUSCAR FOTO
# ============================================================

def buscar_foto(nombre):

    # --------------------------------------------------------
    # 1. CBUM LOCAL
    # --------------------------------------------------------

    if nombre.lower() in (
        "cbum",
        "chris bumstead"
    ):

        try:

            ruta = os.path.join(
                os.path.dirname(
                    os.path.abspath(__file__)
                ),
                RUTA_CBUM
            )

            imagen = Image.open(
                ruta
            ).convert("RGB")

            return imagen

        except Exception as error:

            print(
                "Error cbum.jpg:",
                error
            )

    # --------------------------------------------------------
    # 2. WIKIPEDIA
    # --------------------------------------------------------

    foto_wiki = buscar_foto_wikipedia(
        nombre
    )

    if foto_wiki:

        imagen = descargar_imagen(
            foto_wiki
        )

        if imagen:
            return imagen

    # --------------------------------------------------------
    # 3. THE SPORTS DB
    # --------------------------------------------------------

    jugador = buscar_en_api(
        nombre
    )

    if jugador:

        fotos = [
            jugador.get("strThumb"),
            jugador.get("strCutout"),
            jugador.get("strRender")
        ]

        for foto in fotos:

            if not foto:
                continue

            imagen = descargar_imagen(
                foto
            )

            if imagen:
                return imagen

    return None


# ============================================================
# MOSTRAR FOTO INDIVIDUAL
# ============================================================

def mostrar_foto(nombre):

    global imagen_actual

    # Limpiar imagen anterior
    etiqueta_imagen.config(
        image="",
        text="⏳",
        font=("Arial", 32),
        fg=COLOR_SECUNDARIO
    )

    etiqueta_imagen.image = None
    imagen_actual = None

    ventana.update_idletasks()

    imagen = buscar_foto(
        nombre
    )

    if imagen is None:

        etiqueta_imagen.config(
            image="",
            text="📷",
            font=("Arial", 42),
            fg=COLOR_SECUNDARIO
        )

        etiqueta_imagen.image = None
        imagen_actual = None

        return

    try:

        imagen = imagen.copy()

        # ====================================================
        # FOTO INDIVIDUAL
        # ====================================================

        imagen.thumbnail(
            (200, 200),
            Image.Resampling.LANCZOS
        )

        imagen_actual = ImageTk.PhotoImage(
            imagen
        )

        # Mantener referencia para Tkinter
        etiqueta_imagen.image = imagen_actual

        etiqueta_imagen.config(
            image=imagen_actual,
            text=""
        )

        ventana.update_idletasks()

        print(
            f"Foto individual cargada: {nombre}"
        )

    except Exception as error:

        print(
            "Error mostrando foto:",
            error
        )

        etiqueta_imagen.config(
            image="",
            text="📷",
            font=("Arial", 42),
            fg=COLOR_SECUNDARIO
        )

        etiqueta_imagen.image = None
        imagen_actual = None


# ============================================================
# MOSTRAR PERFIL
# ============================================================

def mostrar_perfil(perfil, clave):

    datos = perfil["datos"]

    etiqueta_datos.config(
        text=(
            f"👤 {datos[0]}\n"
            f"🌎 {datos[1]}\n"
            f"🏟️ {datos[2]}\n"
            f"🏅 {datos[3]}\n"
            f"📍 {datos[4]}\n"
            f"🎂 {datos[5]}\n"
            f"🔵 {datos[6]}"
        )
    )

    etiqueta_stats.config(
        text=perfil["stats"]
    )

    estado.config(
        text=f"📸 Cargando foto de {datos[0]}..."
    )

    ventana.update_idletasks()

    mostrar_foto(
        datos[0]
    )

    estado.config(
        text=f"✅ {datos[0]} seleccionado"
    )


# ============================================================
# SELECCIONAR DEPORTISTA DESDE LISTA
# ============================================================

def seleccionar_deportista(event=None):

    nombre = combo_deportista.get()

    if not nombre:
        return

    buscar_deportista_por_nombre(
        nombre
    )


# ============================================================
# BÚSQUEDA GENERAL
# ============================================================

def buscar_deportista():

    nombre = entrada_busqueda.get().strip()

    if not nombre:

        estado.config(
            text="⚠️ Escribe un deportista."
        )

        return

    if nombre.lower() == "ej: messi, haaland...":

        entrada_busqueda.delete(
            0,
            tk.END
        )

        estado.config(
            text="⚠️ Escribe un nombre."
        )

        return

    buscar_deportista_por_nombre(
        nombre
    )


def buscar_deportista_por_nombre(nombre):

    clave = obtener_clave(
        nombre
    )

    perfil = obtener_perfil(
        nombre
    )

    if perfil:

        mostrar_perfil(
            perfil,
            clave
        )

        entrada_busqueda.delete(
            0,
            tk.END
        )

        entrada_busqueda.insert(
            0,
            perfil["datos"][0]
        )

        agregar_al_chat(
            f"🔎 {perfil['datos'][0]}\n"
            f"🏅 {perfil['datos'][3]}\n"
            f"🏟️ {perfil['datos'][2]}"
        )

        return

    jugador = buscar_en_api(
        nombre
    )

    if jugador:

        nombre_api = jugador.get(
            "strPlayer",
            nombre
        )

        perfil_api = {

            "datos": (
                nombre_api,

                jugador.get(
                    "strNationality",
                    "No disponible"
                ),

                jugador.get(
                    "strTeam",
                    "No disponible"
                ),

                jugador.get(
                    "strSport",
                    "No disponible"
                ),

                jugador.get(
                    "strPosition",
                    "No disponible"
                ),

                jugador.get(
                    "dateBorn",
                    "No disponible"
                ),

                "Activo"
            ),

            "stats": (
                "📊 Información obtenida "
                "desde TheSportsDB"
            )
        }

        mostrar_perfil(
            perfil_api,
            ""
        )

        agregar_al_chat(
            f"🌐 API: {nombre_api}"
        )

        return

    estado.config(
        text=f"❌ No encontré: {nombre}"
    )

    agregar_al_chat(
        f"❌ No encontré resultados "
        f"para: {nombre}"
    )


# ============================================================
# HISTORIAL
# ============================================================

def agregar_al_chat(texto):

    chat.config(
        state="normal"
    )

    chat.insert(
        tk.END,
        texto + "\n\n"
    )

    chat.config(
        state="disabled"
    )

    chat.see(
        tk.END
    )


def limpiar_chat():

    chat.config(
        state="normal"
    )

    chat.delete(
        "1.0",
        tk.END
    )

    chat.config(
        state="disabled"
    )

    estado.config(
        text="🧹 Historial limpiado"
    )


# ============================================================
# COMPARADOR
# ============================================================

def cargar_foto_comparacion(etiqueta, nombre):

    imagen = buscar_foto(
        nombre
    )

    if imagen is None:

        etiqueta.config(
            image="",
            text="📷"
        )

        etiqueta.image = None

        return

    try:

        imagen = imagen.copy()

        imagen.thumbnail(
            (120, 120),
            Image.Resampling.LANCZOS
        )

        foto = ImageTk.PhotoImage(
            imagen
        )

        etiqueta.config(
            image=foto,
            text=""
        )

        etiqueta.image = foto

    except Exception as error:

        print(
            "Error mostrando foto comparación:",
            error
        )


def comparar_jugadores():

    nombre_1 = (
        entrada_comparar_1
        .get()
        .strip()
    )

    nombre_2 = (
        entrada_comparar_2
        .get()
        .strip()
    )

    perfil_1 = obtener_perfil(
        nombre_1
    )

    perfil_2 = obtener_perfil(
        nombre_2
    )

    if not perfil_1:

        messagebox.showerror(
            "Jugador no encontrado",
            f"No encontré:\n\n{nombre_1}"
        )

        return

    if not perfil_2:

        messagebox.showerror(
            "Jugador no encontrado",
            f"No encontré:\n\n{nombre_2}"
        )

        return

    datos_1 = perfil_1["datos"]
    datos_2 = perfil_2["datos"]

    agregar_al_chat(
        f"🆚 COMPARACIÓN\n"
        f"{datos_1[0]} VS {datos_2[0]}"
    )

    comparacion = tk.Toplevel(
        ventana
    )

    comparacion.title(
        f"🆚 {datos_1[0]} vs {datos_2[0]}"
    )

    comparacion.geometry(
        "900x600"
    )

    comparacion.minsize(
        750,
        500
    )

    comparacion.resizable(
        True,
        True
    )

    comparacion.configure(
        bg=COLOR_FONDO
    )

    tk.Label(
        comparacion,
        text="🆚 COMPARACIÓN",
        font=("Arial", 22, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_ACENTO
    ).pack(
        pady=(20, 5)
    )

    tk.Label(
        comparacion,
        text=(
            f"{datos_1[0]}    VS    "
            f"{datos_2[0]}"
        ),
        font=("Arial", 17, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    ).pack(
        pady=(0, 15)
    )

    contenedor = tk.Frame(
        comparacion,
        bg=COLOR_FONDO
    )

    contenedor.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=5
    )

    # ========================================================
    # PANEL 1
    # ========================================================

    panel1 = tk.Frame(
        contenedor,
        bg=COLOR_PANEL
    )

    panel1.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 10)
    )

    tk.Label(
        panel1,
        text=f"👤 {datos_1[0]}",
        font=("Arial", 17, "bold"),
        bg=COLOR_PANEL,
        fg=COLOR_ACENTO
    ).pack(
        pady=15
    )

    foto1 = tk.Label(
        panel1,
        text="📷",
        font=("Arial", 35),
        bg=COLOR_PANEL,
        fg=COLOR_SECUNDARIO
    )

    foto1.pack(
        pady=5
    )

    cargar_foto_comparacion(
        foto1,
        datos_1[0]
    )

    tk.Label(
        panel1,
        text=(
            f"🌎 {datos_1[1]}\n"
            f"🏟️ {datos_1[2]}\n"
            f"🏅 {datos_1[3]}\n"
            f"📍 {datos_1[4]}\n"
            f"🎂 {datos_1[5]}\n"
            f"🔵 {datos_1[6]}"
        ),
        font=("Arial", 10),
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO,
        justify="center"
    ).pack(
        pady=5
    )

    tk.Label(
        panel1,
        text="📊 ESTADÍSTICAS",
        font=("Arial", 13, "bold"),
        bg=COLOR_PANEL,
        fg=COLOR_ACENTO_2
    ).pack(
        pady=(10, 5)
    )

    tk.Label(
        panel1,
        text=perfil_1["stats"],
        font=("Arial", 10),
        bg=COLOR_PANEL,
        fg=COLOR_SECUNDARIO,
        justify="center"
    ).pack()

    # ========================================================
    # VS
    # ========================================================

    tk.Label(
        contenedor,
        text="VS",
        font=("Arial", 22, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_ACENTO_2
    ).pack(
        side="left",
        padx=15
    )

    # ========================================================
    # PANEL 2
    # ========================================================

    panel2 = tk.Frame(
        contenedor,
        bg=COLOR_PANEL
    )

    panel2.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(10, 0)
    )

    tk.Label(
        panel2,
        text=f"👤 {datos_2[0]}",
        font=("Arial", 17, "bold"),
        bg=COLOR_PANEL,
        fg=COLOR_ACENTO
    ).pack(
        pady=15
    )

    foto2 = tk.Label(
        panel2,
        text="📷",
        font=("Arial", 35),
        bg=COLOR_PANEL,
        fg=COLOR_SECUNDARIO
    )

    foto2.pack(
        pady=5
    )

    cargar_foto_comparacion(
        foto2,
        datos_2[0]
    )

    tk.Label(
        panel2,
        text=(
            f"🌎 {datos_2[1]}\n"
            f"🏟️ {datos_2[2]}\n"
            f"🏅 {datos_2[3]}\n"
            f"📍 {datos_2[4]}\n"
            f"🎂 {datos_2[5]}\n"
            f"🔵 {datos_2[6]}"
        ),
        font=("Arial", 10),
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO,
        justify="center"
    ).pack(
        pady=5
    )

    tk.Label(
        panel2,
        text="📊 ESTADÍSTICAS",
        font=("Arial", 13, "bold"),
        bg=COLOR_PANEL,
        fg=COLOR_ACENTO_2
    ).pack(
        pady=(10, 5)
    )

    tk.Label(
        panel2,
        text=perfil_2["stats"],
        font=("Arial", 10),
        bg=COLOR_PANEL,
        fg=COLOR_SECUNDARIO,
        justify="center"
    ).pack()

    tk.Button(
        comparacion,
        text="✖ CERRAR",
        command=comparacion.destroy,
        bg=COLOR_PANEL_2,
        fg=COLOR_TEXTO,
        activebackground=COLOR_ACENTO,
        activeforeground=COLOR_FONDO,
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=30,
        pady=8,
        cursor="hand2"
    ).pack(
        pady=15
    )


# ============================================================
# VENTANA
# ============================================================

ventana = tk.Tk()

ventana.title(
    "⚽ SPORT CHAT V2.4"
)

ventana.geometry(
    "600x850"
)

ventana.minsize(
    500,
    650
)

ventana.resizable(
    True,
    True
)

ventana.configure(
    bg=COLOR_FONDO
)


# ============================================================
# CABECERA
# ============================================================

tk.Label(
    ventana,
    text="⚽ SPORT CHAT",
    font=("Arial", 24, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_ACENTO
).pack(
    pady=(10, 0)
)

tk.Label(
    ventana,
    text="Buscador y comparador deportivo",
    font=("Arial", 10),
    bg=COLOR_FONDO,
    fg=COLOR_SECUNDARIO
).pack(
    pady=(0, 7)
)


# ============================================================
# BUSCADOR
# ============================================================

panel_busqueda = tk.Frame(
    ventana,
    bg=COLOR_PANEL
)

panel_busqueda.pack(
    fill="x",
    padx=10,
    pady=4
)

entrada_busqueda = tk.Entry(
    panel_busqueda,
    font=("Arial", 11),
    bg=COLOR_PANEL_2,
    fg=COLOR_TEXTO,
    insertbackground=COLOR_TEXTO,
    relief="flat"
)

entrada_busqueda.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(10, 5),
    pady=8,
    ipady=5
)

entrada_busqueda.insert(
    0,
    "Ej: Messi, Haaland..."
)

tk.Button(
    panel_busqueda,
    text="🔎 BUSCAR",
    command=buscar_deportista,
    bg=COLOR_ACENTO,
    fg=COLOR_FONDO,
    activebackground=COLOR_TEXTO,
    font=("Arial", 9, "bold"),
    relief="flat",
    padx=12,
    pady=7,
    cursor="hand2"
).pack(
    side="right",
    padx=(5, 10)
)


# ============================================================
# DEPORTE + LISTA DE DEPORTISTAS
# ============================================================

panel_filtro = tk.Frame(
    ventana,
    bg=COLOR_PANEL
)

panel_filtro.pack(
    fill="x",
    padx=10,
    pady=4
)

tk.Label(
    panel_filtro,
    text="🏅 Deporte:",
    font=("Arial", 9, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO
).pack(
    side="left",
    padx=(10, 5),
    pady=8
)

deporte_var = tk.StringVar(
    value="Fútbol"
)

combo_deporte = ttk.Combobox(
    panel_filtro,
    textvariable=deporte_var,
    values=[
        "Fútbol",
        "Básquetbol",
        "Tenis",
        "Boxeo",
        "Fórmula 1",
        "Culturismo"
    ],
    state="readonly",
    width=16
)

combo_deporte.pack(
    side="left",
    padx=5
)

tk.Label(
    panel_filtro,
    text="👤 Deportista:",
    font=("Arial", 9, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO
).pack(
    side="left",
    padx=(10, 5)
)

combo_deportista = ttk.Combobox(
    panel_filtro,
    state="readonly",
    width=20
)

combo_deportista.pack(
    side="left",
    padx=5
)

combo_deporte.bind(
    "<<ComboboxSelected>>",
    actualizar_deportistas
)

combo_deportista.bind(
    "<<ComboboxSelected>>",
    seleccionar_deportista
)


# ============================================================
# COMPARADOR
# ============================================================

panel_comparador = tk.Frame(
    ventana,
    bg=COLOR_PANEL
)

panel_comparador.pack(
    fill="x",
    padx=10,
    pady=4
)

tk.Label(
    panel_comparador,
    text="🆚 COMPARAR DEPORTISTAS",
    font=("Arial", 9, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_ACENTO
).pack(
    pady=(6, 4)
)

fila_comparador = tk.Frame(
    panel_comparador,
    bg=COLOR_PANEL
)

fila_comparador.pack(
    fill="x",
    padx=8,
    pady=(0, 7)
)

entrada_comparar_1 = tk.Entry(
    fila_comparador,
    font=("Arial", 10),
    bg=COLOR_PANEL_2,
    fg=COLOR_TEXTO,
    insertbackground=COLOR_TEXTO,
    relief="flat"
)

entrada_comparar_1.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=5
)

entrada_comparar_1.insert(
    0,
    "Messi"
)

tk.Label(
    fila_comparador,
    text=" VS ",
    font=("Arial", 10, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_ACENTO_2
).pack(
    side="left"
)

entrada_comparar_2 = tk.Entry(
    fila_comparador,
    font=("Arial", 10),
    bg=COLOR_PANEL_2,
    fg=COLOR_TEXTO,
    insertbackground=COLOR_TEXTO,
    relief="flat"
)

entrada_comparar_2.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=5
)

entrada_comparar_2.insert(
    0,
    "Haaland"
)

tk.Button(
    fila_comparador,
    text="🆚 COMPARAR",
    command=comparar_jugadores,
    bg=COLOR_ACENTO_2,
    fg=COLOR_TEXTO,
    activebackground=COLOR_ACENTO,
    activeforeground=COLOR_FONDO,
    font=("Arial", 9, "bold"),
    relief="flat",
    padx=10,
    pady=6,
    cursor="hand2"
).pack(
    side="left",
    padx=(7, 0)
)


# ============================================================
# PERFIL
# ============================================================

panel_perfil = tk.Frame(
    ventana,
    bg=COLOR_PANEL
)

panel_perfil.pack(
    fill="x",
    padx=10,
    pady=4
)


# ============================================================
# FOTO INDIVIDUAL
# ============================================================

etiqueta_imagen = tk.Label(
    panel_perfil,
    text="📷",
    font=("Arial", 38),
    bg=COLOR_PANEL,
    fg=COLOR_SECUNDARIO
)

etiqueta_imagen.pack(
    side="left",
    padx=8,
    pady=6
)


panel_datos = tk.Frame(
    panel_perfil,
    bg=COLOR_PANEL
)

panel_datos.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5,
    pady=6
)

etiqueta_datos = tk.Label(
    panel_datos,
    text="Selecciona un deportista",
    font=("Arial", 9),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    justify="left",
    anchor="w"
)

etiqueta_datos.pack(
    fill="x"
)

etiqueta_stats = tk.Label(
    panel_datos,
    text="📊 Estadísticas aparecerán aquí",
    font=("Arial", 8),
    bg=COLOR_PANEL,
    fg=COLOR_SECUNDARIO,
    justify="left",
    anchor="w"
)

etiqueta_stats.pack(
    fill="x",
    pady=(3, 0)
)


# ============================================================
# ESTADO
# ============================================================

estado = tk.Label(
    ventana,
    text="🟢 SPORT CHAT listo",
    font=("Arial", 8),
    bg=COLOR_FONDO,
    fg=COLOR_SECUNDARIO
)

estado.pack(
    pady=2
)


# ============================================================
# BOTÓN LIMPIAR
# ============================================================

panel_botones = tk.Frame(
    ventana,
    bg=COLOR_FONDO
)

panel_botones.pack(
    side="bottom",
    fill="x",
    padx=10,
    pady=7
)

tk.Button(
    panel_botones,
    text="🧹 LIMPIAR HISTORIAL",
    command=limpiar_chat,
    bg=COLOR_PANEL_2,
    fg=COLOR_TEXTO,
    activebackground=COLOR_ACENTO,
    activeforeground=COLOR_FONDO,
    font=("Arial", 9, "bold"),
    relief="flat",
    padx=25,
    pady=7,
    cursor="hand2"
).pack(
    side="right"
)


# ============================================================
# HISTORIAL
# ============================================================

panel_chat = tk.Frame(
    ventana,
    bg=COLOR_FONDO
)

panel_chat.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=(2, 2)
)

scroll_chat = tk.Scrollbar(
    panel_chat,
    orient="vertical"
)

scroll_chat.pack(
    side="right",
    fill="y"
)

chat = tk.Text(
    panel_chat,
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    font=("Consolas", 9),
    relief="flat",
    wrap="word",
    yscrollcommand=scroll_chat.set
)

chat.pack(
    side="left",
    fill="both",
    expand=True
)

scroll_chat.config(
    command=chat.yview
)

chat.config(
    state="disabled"
)


# ============================================================
# ENTER
# ============================================================

entrada_busqueda.bind(
    "<Return>",
    lambda event: buscar_deportista()
)

entrada_comparar_1.bind(
    "<Return>",
    lambda event: entrada_comparar_2.focus()
)

entrada_comparar_2.bind(
    "<Return>",
    lambda event: comparar_jugadores()
)


# ============================================================
# QUITAR PLACEHOLDER AL HACER CLICK
# ============================================================

def limpiar_placeholder(event):

    if entrada_busqueda.get() == "Ej: Messi, Haaland...":

        entrada_busqueda.delete(
            0,
            tk.END
        )


entrada_busqueda.bind(
    "<FocusIn>",
    limpiar_placeholder
)


# ============================================================
# INICIO
# ============================================================

actualizar_deportistas()

agregar_al_chat(
    "👋 Bienvenido a SPORT CHAT\n\n"
    "🏅 Selecciona un deporte para ver sus deportistas.\n"
    "👤 Selecciona un deportista de la lista.\n"
    "🔎 También puedes escribir un nombre.\n"
    "🆚 Usa el comparador para enfrentar dos deportistas."
)


# ============================================================
# INICIAR
# ============================================================

ventana.mainloop()
