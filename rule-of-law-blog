import streamlit as st

# 1. Configuración de la página
# Establece el título y el layout en "wide" para aprovechar el espacio.
st.set_page_config(
    page_title="Rule of Law Blog",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. El contenido HTML completo
# Se utiliza la sintaxis de triple comilla para manejar el contenido HTML multilinea.
# Nota: La etiqueta <script src="https://cdn.tailwindcss.com"></script> se utiliza para cargar Tailwind CSS.
# Los marcadores de posición de imagen ('placehold.co') se usan para asegurar la visualización inmediata.
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Rule of Law — Blog | Estado de Derecho, Democracia y Derechos Humanos</title>
  <!-- Usando el CDN de Tailwind CSS v3 para mejor compatibilidad -->
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    /* Usando la fuente Inter para un look moderno */
    body {
      font-family: 'Inter', sans-serif;
    }
    /* Estilos adicionales para simular un periódico moderno */
    .marquee {
      white-space: nowrap;
      overflow: hidden;
    }
    .marquee div {
      display: inline-block;
      padding-left: 100%;
      animation: marquee 18s linear infinite;
    }
    @keyframes marquee {
      0% { transform: translate(0, 0); }
      100% { transform: translate(-100%, 0); }
    }
  </style>
</head>
<body class="bg-gray-100 text-gray-900 font-sans">
  <!-- Cabecera principal -->
  <header class="bg-white shadow-md sticky top-0 z-40 border-t-4 border-blue-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center py-4">
        <div class="flex items-center space-x-4">
          <div class="text-3xl font-extrabold text-blue-900 tracking-tight">Rule of Law</div>
          <div class="hidden md:flex items-center text-sm text-gray-600 space-x-4">
            <a href="#" class="hover:text-blue-800 transition duration-150">Política</a>
            <a href="#" class="hover:text-blue-800 transition duration-150">Derechos</a>
            <a href="#" class="hover:text-blue-800 transition duration-150">Justicia</a>
            <a href="#" class="hover:text-blue-800 transition duration-150">Opinión</a>
          </div>
        </div>
        <div class="flex items-center space-x-4">
          <form class="hidden sm:block">
            <input aria-label="Buscar" placeholder="Buscar..." class="border rounded-full px-4 py-1 text-sm focus:ring-2 focus:ring-blue-500 transition duration-150" />
          </form>
          <button class="bg-blue-800 hover:bg-blue-700 transition duration-150 text-white px-4 py-1.5 rounded-full text-sm font-semibold shadow-md">Suscríbete</button>
        </div>
      </div>
    </div>
    <!-- Ticker de últimas noticias -->
    <div class="bg-blue-900 text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="marquee py-2 text-sm font-medium">
          <div>&bull; Última hora: Informe sobre Estado de Derecho en la UE &bull; Nueva resolución del Parlamento Europeo &bull; Debate sobre independencia judicial en curso &bull; Eventos: seminario sobre derechos humanos (inscríbete) &bull;</div>
        </div>
      </div>
    </div>
  </header>

  <!-- Área principal tipo periódico: hero + columnas -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div class="grid grid-cols-1 lg:grid-cols-4 gap-8">
      <!-- Columnón principal (col-span 3) -->
      <div class="lg:col-span-3 space-y-8">
        <!-- Hero principal (imagen grande) -->
        <article class="bg-white rounded-xl shadow-lg hover:shadow-xl transition duration-300 overflow-hidden">
          <div class="md:flex">
            <div class="md:w-2/3">
              <!-- Marcador de posición de imagen -->
              <img src="https://placehold.co/800x400/0A3D62/FFFFFF?text=Estado+de+Derecho" alt="Comisión Europea" class="w-full h-80 object-cover">
            </div>
            <div class="md:w-1/3 p-6 flex flex-col justify-between">
              <div>
                <span class="text-xs font-semibold uppercase tracking-wider text-blue-600 bg-blue-100 px-2 py-0.5 rounded">Política · Bruselas</span>
                <h2 class="mt-3 text-2xl font-bold leading-snug">La situación del Estado de Derecho en la Unión Europea: nuevo informe</h2>
                <p class="mt-3 text-gray-700 text-sm leading-relaxed">Un análisis exhaustivo sobre la independencia judicial y las recomendaciones para reforzar las instituciones democráticas en los Estados miembros.</p>
            </div>
              <div class="mt-4 text-sm text-gray-600 border-t pt-3">Por: <span class="font-medium">Equipo Rule of Law</span> · 24 oct 2025</div>
            </div>
          </div>
        </article>

        <!-- Grid de artículos destacados -->
        <section class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <article class="bg-white rounded-xl shadow-lg hover:shadow-xl transition duration-300 overflow-hidden">
            <!-- Marcador de posición de imagen -->
            <img src="https://placehold.co/400x250/1C508C/FFFFFF?text=Noticia" alt="miniatura" class="w-full h-44 object-cover">
            <div class="p-5">
              <span class="text-xs font-semibold uppercase tracking-wider text-green-600">Opinión</span>
              <h3 class="mt-2 font-bold text-xl leading-tight">¿Cómo proteger la independencia judicial?</h3>
              <p class="text-sm text-gray-700 mt-2">Columnas de expertos sobre medidas prácticas y reformas legales necesarias para garantizar tribunales imparciales.</p>
            </div>
          </article>

          <article class="bg-white rounded-xl shadow-lg hover:shadow-xl transition duration-300 overflow-hidden">
            <!-- Marcador de posición de imagen -->
            <img src="https://placehold.co/400x250/1C508C/FFFFFF?text=Eventos" alt="miniatura" class="w-full h-44 object-cover">
            <div class="p-5">
              <span class="text-xs font-semibold uppercase tracking-wider text-orange-600">Eventos</span>
              <h3 class="mt-2 font-bold text-xl leading-tight">Seminario: Democracia y participación ciudadana</h3>
              <p class="text-sm text-gray-700 mt-2">Un repaso a los próximos encuentros en varias capitales europeas.</p>
            </div>
          </article>
        </section>

        <!-- Lista de artículos recientes estilo periódico -->
        <section class="bg-white rounded-xl shadow-lg p-6">
          <h3 class="text-2xl font-extrabold border-b pb-3 mb-4 text-blue-900">Últimas noticias</h3>
          <ul class="divide-y divide-gray-200">
            <li class="py-4">
              <a href="#" class="flex items-start space-x-4 hover:bg-gray-50 p-2 -m-2 rounded transition duration-150">
                <!-- Marcador de posición de imagen -->
                <img src="https://placehold.co/96x64/3472A8/FFFFFF?text=Thumb" alt="thumb" class="w-24 h-16 object-cover rounded">
                <div class="flex-1">
                  <h4 class="font-semibold text-lg">La Comisión presenta medidas para salvaguardar el Estado de Derecho</h4>
                  <p class="text-sm text-gray-600 mt-1">La propuesta incluye un mecanismo de seguimiento y ayudas condicionadas.</p>
                </div>
              </a>
            </li>
            <li class="py-4">
              <a href="#" class="flex items-start space-x-4 hover:bg-gray-50 p-2 -m-2 rounded transition duration-150">
                <!-- Marcador de posición de imagen -->
                <img src="https://placehold.co/96x64/3472A8/FFFFFF?text=Thumb" alt="thumb" class="w-24 h-16 object-cover rounded">
                <div class="flex-1">
                  <h4 class="font-semibold text-lg">Debate en el Parlamento Europeo sobre derechos fundamentales</h4>
                  <p class="text-sm text-gray-600 mt-1">Representantes discuten el balance entre seguridad y libertades civiles.</p>
                </div>
              </a>
            </li>
            <li class="py-4">
              <a href="#" class="flex items-start space-x-4 hover:bg-gray-50 p-2 -m-2 rounded transition duration-150">
                <!-- Marcador de posición de imagen -->
                <img src="https://placehold.co/96x64/3472A8/FFFFFF?text=Thumb" alt="thumb" class="w-24 h-16 object-cover rounded">
                <div class="flex-1">
                  <h4 class="font-semibold text-lg">Análisis de la nueva sentencia del TJUE sobre protección de datos</h4>
                  <p class="text-sm text-gray-600 mt-1">Una mirada a las implicaciones para las empresas y los ciudadanos.</p>
                </div>
              </a>
            </li>
          </ul>
        </section>
      </div>

      <!-- Barra lateral (sidebar) -->
      <aside class="space-y-6">
        <div class="bg-white rounded-xl shadow-lg p-6">
          <h4 class="font-bold text-xl mb-3 text-blue-900">Suscríbete a nuestro boletín</h4>
          <p class="text-sm text-gray-600 mb-4">Recibe boletines con lo más relevante sobre Estado de Derecho y derechos humanos.</p>
          <form class="space-y-3">
            <input type="email" placeholder="Correo electrónico" class="w-full border border-gray-300 rounded-lg px-4 py-2 text-sm focus:ring-blue-500 focus:border-blue-500" required />
            <button class="w-full bg-blue-800 hover:bg-blue-700 transition duration-150 text-white rounded-lg px-4 py-2 text-sm font-semibold shadow-md">Suscribirse</button>
          </form>
        </div>

        <div class="bg-white rounded-xl shadow-lg p-6">
          <h4 class="font-bold text-xl mb-4 text-blue-900">Tendencias</h4>
          <ol class="list-none text-sm space-y-3 text-gray-700">
            <li class="flex items-start">
              <span class="text-blue-800 font-bold mr-2 text-lg">1.</span>
              <a href="#" class="hover:text-blue-600 transition duration-150">Independencia judicial en Polonia y el TUE</a>
            </li>
            <li class="flex items-start">
              <span class="text-blue-800 font-bold mr-2 text-lg">2.</span>
              <a href="#" class="hover:text-blue-600 transition duration-150">Informe anual sobre el estado de los derechos humanos en el mundo</a>
            </li>
            <li class="flex items-start">
              <span class="text-blue-800 font-bold mr-2 text-lg">3.</span>
              <a href="#" class="hover:text-blue-600 transition duration-150">Sentencia clave del Tribunal de Justicia de la UE</a>
            </li>
          </ol>
        </div>

        <div class="bg-white rounded-xl shadow-lg p-6">
          <h4 class="font-bold text-xl mb-4 text-blue-900">Opiniones destacadas</h4>
          <div class="space-y-3 text-sm text-gray-700">
            <a href="#" class="block hover:text-blue-600 hover:underline transition duration-150 border-b border-gray-100 pb-2">La defensa de las libertades en tiempos difíciles</a>
            <a href="#" class="block hover:text-blue-600 hover:underline transition duration-150 border-b border-gray-100 pb-2">El papel de la sociedad civil y su impacto en la justicia</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- Sección de blog / columnas secundarias -->
    <section class="mt-12 grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2 space-y-4">
        <h3 class="text-2xl font-extrabold text-blue-900 mb-4 border-b pb-3">Publicaciones recientes</h3>
        <article class="bg-white rounded-xl shadow hover:shadow-lg p-5 transition duration-300">
          <h4 class="font-bold text-lg">Nuevo estudio sobre participación ciudadana y Estado de Derecho</h4>
          <p class="text-sm text-gray-700 mt-2">Resumen del estudio con enlaces para descargar el informe completo y materiales complementarios.</p>
          <div class="text-xs text-gray-500 mt-2">Derechos | 23 Octubre</div>
        </article>

        <article class="bg-white rounded-xl shadow hover:shadow-lg p-5 transition duration-300">
          <h4 class="font-bold text-lg">Columna de opinión: Sociedad y justicia en el siglo XXI</h4>
          <p class="text-sm text-gray-700 mt-2">Reflexión de una experta en derecho constitucional sobre los desafíos actuales.</p>
          <div class="text-xs text-gray-500 mt-2">Opinión | 22 Octubre</div>
        </article>
      </div>

      <aside class="space-y-6">
        <div class="bg-white rounded-xl shadow-lg p-6">
          <h4 class="font-bold text-xl text-blue-900 mb-4">Eventos próximos</h4>
          <ul class="text-sm text-gray-700 space-y-3">
            <li class="border-b border-gray-100 pb-2">
              <span class="font-semibold text-blue-600">12 Nov:</span> Seminario en Bruselas (Independencia)
            </li>
            <li class="border-b border-gray-100 pb-2">
              <span class="font-semibold text-blue-600">5 Dic:</span> Foro internacional de derechos humanos
            </li>
          </ul>
        </div>

        <div class="bg-white rounded-xl shadow-lg p-6">
          <h4 class="font-bold text-xl text-blue-900 mb-4">Archivo</h4>
          <select class="w-full border border-gray-300 rounded-lg px-4 py-2 text-sm focus:ring-blue-500 focus:border-blue-500">
            <option>Octubre 2025</option>
            <option>Septiembre 2025</option>
            <option>Agosto 2025</option>
          </select>
        </div>
      </aside>
    </section>
  </main>

  <!-- Pie de página tipo periódico -->
  <footer class="bg-gray-900 text-gray-200 mt-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 grid grid-cols-2 md:grid-cols-4 gap-8">
      <div class="col-span-2 md:col-span-1">
        <h5 class="font-extrabold text-xl mb-3 text-white">Rule of Law</h5>
        <p class="text-sm text-gray-400">Blog especializado en democracia, Estado de Derecho y derechos humanos en la Unión Europea.</p>
      </div>
      <div>
        <h5 class="font-bold mb-3 text-white">Secciones</h5>
        <ul class="text-sm text-gray-400 space-y-2">
          <li><a href="#" class="hover:text-blue-400">Política</a></li>
          <li><a href="#" class="hover:text-blue-400">Derechos</a></li>
          <li><a href="#" class="hover:text-blue-400">Justicia</a></li>
          <li><a href="#" class="hover:text-blue-400">Opinión</a></li>
        </ul>
      </div>
      <div>
        <h5 class="font-bold mb-3 text-white">Sobre nosotros</h5>
        <ul class="text-sm text-gray-400 space-y-2">
          <li><a href="#" class="hover:text-blue-400">Miembros</a></li>
          <li><a href="#" class="hover:text-blue-400">Actividades</a></li>
          <li><a href="#" class="hover:text-blue-400">Publicaciones</a></li>
        </ul>
      </div>
      <div>
        <h5 class="font-bold mb-3 text-white">Contacto</h5>
        <p class="text-sm text-gray-400">contacto@ruleoflaw.eu</p>
        <p class="text-sm text-gray-400 mt-4">Redes sociales:</p>
        <!-- Placeholder para iconos de redes sociales (no visibles sin librerías externas) -->
        <div class="flex space-x-3 mt-1">
          <a href="#" class="text-gray-500 hover:text-blue-400">X</a>
          <a href="#" class="text-gray-500 hover:text-blue-400">FB</a>
          <a href="#" class="text-gray-500 hover:text-blue-400">LI</a>
        </div>
      </div>
    </div>
    <div class="border-t border-gray-800 text-center py-4 text-sm text-gray-500">
      &copy; 2025 Rule of Law · Todos los derechos reservados
    </div>
  </footer>
</body>
</html>
"""
# 3. Muestra el contenido HTML usando Markdown con la opción para permitir HTML no seguro.
# Esto incrusta todo el diseño Tailwind/CSS directamente en la aplicación Streamlit.
st.markdown(html_content, unsafe_allow_html=True)
