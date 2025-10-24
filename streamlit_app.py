<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Rule of Law — Blog</title>
    <!-- Usando el CDN de Tailwind CSS v3 -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Definimos una fuente serif para títulos y una sans para el cuerpo */
        .font-serif {
            font-family: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
        }
        .font-sans {
            font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
        }
        /* Aseguramos que el BODY ocupe todo el espacio visible y maneje el layout flex */
        body {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-900 font-sans">
    
    <!-- Header tipo revista: Fijo y Limpio -->
    <header class="bg-white border-b border-gray-200 shadow-sm sticky top-0 z-40">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center py-5">
                <!-- Logo/Título Principal -->
                <div class="text-4xl font-extrabold text-gray-900 font-serif tracking-tight">Rule of Law</div>
                
                <!-- Navegación principal -->
                <nav class="hidden md:flex space-x-8 text-sm font-medium text-gray-700 uppercase">
                    <a href="#" class="hover:text-blue-700 transition duration-150">Política</a>
                    <a href="#" class="hover:text-blue-700 transition duration-150">Derechos</a>
                    <a href="#" class="hover:text-blue-700 transition duration-150">Justicia</a>
                    <a href="#" class="hover:text-blue-700 transition duration-150">Opinión</a>
                    <a href="#" class="hover:text-blue-700 transition duration-150">Documentos</a>
                </nav>

                <!-- Botón y Suscripción -->
                <div class="flex items-center space-x-4">
                    <button class="bg-blue-800 hover:bg-blue-700 transition duration-150 text-white px-4 py-1.5 rounded-sm text-sm font-semibold shadow-md">Suscríbete</button>
                </div>
            </div>
        </div>
    </header>

    <!-- Área principal del contenido (flex-grow asegura que ocupe el espacio restante) -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 flex-grow">
        
        <!-- Sección Hero y Columna de Artículos (3 columnas) -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-10">
            
            <!-- Artículo Destacado Grande (Columna 1 y 2) -->
            <article class="lg:col-span-2 bg-white rounded-lg shadow-xl hover:shadow-2xl transition duration-300 overflow-hidden">
                <!-- Placeholder de imagen -->
                <img src="https://placehold.co/1200x500/0A3D62/FFFFFF?text=PORTADA" alt="Imagen principal sobre la justicia" class="w-full h-96 object-cover border-b-4 border-blue-600">
                <div class="p-6">
                    <span class="text-xs font-bold uppercase tracking-widest text-blue-600">Política</span>
                    <h1 class="mt-2 text-4xl font-bold leading-tight font-serif text-gray-900">
                        El Equilibrio en Tiempos de Crisis: Análisis del Nuevo Informe de la UE
                    </h1>
                    <p class="mt-4 text-gray-700 text-lg leading-relaxed">
                        Un análisis detallado de las recomendaciones para asegurar la independencia judicial y los derechos fundamentales en el continente europeo. La presión internacional crece.
                    </p>
                    <div class="mt-5 text-sm text-gray-500 border-t pt-4 flex justify-between">
                        <span>Por: <span class="font-semibold text-gray-700">Dr. Helena Robles</span></span>
                        <span>Hace 2 horas</span>
                    </div>
                </div>
            </article>

            <!-- Sidebar (Columna 3) -->
            <aside class="space-y-8">
                
                <!-- Búsqueda y Suscripción -->
                <div class="bg-white p-6 border border-gray-200 rounded-lg shadow">
                    <h4 class="font-bold text-lg mb-3 text-gray-800 font-serif">Buscar Artículos</h4>
                    <input type="text" placeholder="Escribe aquí para buscar..." class="w-full border border-gray-300 rounded-sm px-4 py-2 text-sm focus:ring-blue-500 focus:border-blue-500" />
                    
                    <h4 class="font-bold text-lg mt-6 mb-3 text-gray-800 font-serif">Boletín Exclusivo</h4>
                    <p class="text-sm text-gray-600 mb-3">Recibe nuestro resumen semanal.</p>
                    <button class="w-full bg-blue-600 hover:bg-blue-500 transition duration-150 text-white rounded-sm px-4 py-2 text-sm font-semibold">Regístrate</button>
                </div>
                
                <!-- Artículos Populares -->
                <div class="bg-white p-6 border border-gray-200 rounded-lg shadow">
                    <h4 class="font-bold text-lg mb-4 text-gray-800 border-b pb-2 font-serif">Lo más leído</h4>
                    <ol class="list-decimal pl-5 space-y-3 text-sm text-gray-700">
                        <li class="hover:text-blue-600 transition duration-150 cursor-pointer">
                            <span class="font-semibold">La batalla por el 'Rule of Law' en el TJUE</span>
                            <p class="text-xs text-gray-500 mt-0.5">Opinión | 15 comentarios</p>
                        </li>
                        <li class="hover:text-blue-600 transition duration-150 cursor-pointer">
                            <span class="font-semibold">Desafíos de la inteligencia artificial y los derechos humanos</span>
                            <p class="text-xs text-gray-500 mt-0.5">Tecnología | 8 comentarios</p>
                        </li>
                        <li class="hover:text-blue-600 transition duration-150 cursor-pointer">
                            <span class="font-semibold">Entrevista con el Comisario de Justicia Europeo</span>
                            <p class="text-xs text-gray-500 mt-0.5">Entrevistas | 2 comentarios</p>
                        </li>
                    </ol>
                </div>

            </aside>
        </div>

        <!-- Sección de Artículos Secundarios (Layout de 3 columnas de contenido) -->
        <section class="mt-12">
            <h2 class="text-3xl font-bold font-serif border-b-2 border-gray-300 pb-3 mb-6 text-gray-900">
                Análisis Profundo y Columnas
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                
                <!-- Tarjeta 1 -->
                <article class="bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition duration-300 overflow-hidden">
                    <div class="p-5">
                        <span class="text-xs font-bold uppercase tracking-widest text-red-600">Derechos Humanos</span>
                        <h3 class="mt-2 text-xl font-bold leading-snug font-serif text-gray-900 hover:text-blue-700 cursor-pointer">
                            El impacto de la digitalización en la privacidad de los ciudadanos
                        </h3>
                        <p class="mt-3 text-sm text-gray-700">
                            Un editorial sobre cómo los gobiernos están gestionando el balance entre seguridad y la protección de datos personales.
                        </p>
                        <div class="mt-4 text-xs text-gray-500">
                            <span class="font-semibold">Por: A. López</span> | 18 Oct 2025
                        </div>
                    </div>
                </article>

                <!-- Tarjeta 2 -->
                <article class="bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition duration-300 overflow-hidden">
                    <div class="p-5">
                        <span class="text-xs font-bold uppercase tracking-widest text-green-600">Justicia</span>
                        <h3 class="mt-2 text-xl font-bold leading-snug font-serif text-gray-900 hover:text-blue-700 cursor-pointer">
                            La reforma de los sistemas judiciales en la periferia de la UE
                        </h3>
                        <p class="mt-3 text-sm text-gray-700">
                            Evaluación de los programas de asistencia y la evolución de las instituciones judiciales en los países candidatos.
                        </p>
                        <div class="mt-4 text-xs text-gray-500">
                            <span class="font-semibold">Por: I. Sánchez</span> | 17 Oct 2025
                        </div>
                    </div>
                </article>

                <!-- Tarjeta 3 -->
                <article class="bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition duration-300 overflow-hidden">
                    <div class="p-5">
                        <span class="text-xs font-bold uppercase tracking-widest text-indigo-600">Opinión</span>
                        <h3 class="mt-2 text-xl font-bold leading-snug font-serif text-gray-900 hover:text-blue-700 cursor-pointer">
                            Columna: ¿Es el derecho internacional la respuesta a la guerra?
                        </h3>
                        <p class="mt-3 text-sm text-gray-700">
                            Una perspectiva filosófica sobre la aplicación de las leyes internacionales en conflictos armados actuales.
                        </p>
                        <div class="mt-4 text-xs text-gray-500">
                            <span class="font-semibold">Por: G. Fuentes</span> | 16 Oct 2025
                        </div>
                    </div>
                </article>
                
            </div>
            
            <div class="mt-10 text-center">
                <button class="bg-gray-200 hover:bg-gray-300 text-gray-800 font-semibold py-2 px-6 rounded-sm shadow transition duration-150 text-sm">
                    Ver más artículos antiguos →
                </button>
            </div>
        </section>

    </main>

    <!-- Footer amplio y profesional (mt-auto asegura que se pegue al fondo) -->
    <footer class="bg-gray-900 text-gray-300 mt-16 mt-auto">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 grid grid-cols-2 md:grid-cols-5 gap-8">
            
            <div class="col-span-2">
                <h5 class="font-extrabold text-2xl mb-3 text-white font-serif">Rule of Law</h5>
                <p class="text-sm text-gray-400">El sitio de análisis y debate líder en temas de justicia, democracia y derechos fundamentales.</p>
                <p class="text-xs text-gray-500 mt-4">&copy; 2025 Rule of Law Media</p>
            </div>

            <div>
                <h5 class="font-bold mb-4 text-white uppercase text-sm">Temas</h5>
                <ul class="text-sm text-gray-400 space-y-2">
                    <li><a href="#" class="hover:text-blue-400">Política</a></li>
                    <li><a href="#" class="hover:text-blue-400">Justicia Penal</a></li>
                    <li><a href="#" class="hover:text-blue-400">Derechos Civiles</a></li>
                    <li><a href="#" class="hover:text-blue-400">Internacional</a></li>
                </ul>
            </div>
            
            <div>
                <h5 class="font-bold mb-4 text-white uppercase text-sm">Archivo</h5>
                <ul class="text-sm text-gray-400 space-y-2">
                    <li><a href="#" class="hover:text-blue-400">2025</a></li>
                    <li><a href="#" class="hover:text-blue-400">2024</a></li>
                    <li><a href="#" class="hover:text-blue-400">Especiales</a></li>
                    <li><a href="#" class="hover:text-blue-400">Investigaciones</a></li>
                </ul>
            </div>
            
            <div>
                <h5 class="font-bold mb-4 text-white uppercase text-sm">Legal</h5>
                <ul class="text-sm text-gray-400 space-y-2">
                    <li><a href="#" class="hover:text-blue-400">Aviso Legal</a></li>
                    <li><a href="#" class="hover:text-blue-400">Política de Privacidad</a></li>
                    <li><a href="#" class="hover:text-blue-400">Contacto</a></li>
                </ul>
            </div>
        </div>
        <div class="border-t border-gray-800 text-center py-4 text-sm text-gray-500">
            Desarrollado con pasión.
        </div>
    </footer>
</body>
</html>



