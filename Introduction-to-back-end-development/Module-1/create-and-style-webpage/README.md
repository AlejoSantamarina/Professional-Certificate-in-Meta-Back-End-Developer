Instrucciones del laboratorio: Crear y dar estilo a una página web

En este ejercicio, practicarás la construcción de tu propia página web utilizando HTML y CSS.


    Consejos: Antes de comenzar
    Para ver tu código y las instrucciones lado a lado, selecciona lo siguiente en la barra de herramientas de VSCode:

        View (Ver) -> Editor Layout (Diseño del editor) -> Two Columns (Dos columnas)

        Para ver este archivo en modo de vista previa, haz clic derecho en este archivo README.md y selecciona Open Preview (Abrir vista previa).

        Selecciona tu archivo de código en el árbol de archivos, lo cual lo abrirá en una nueva pestaña de VSCode.

        Arrastra tus archivos de código hacia la segunda columna.

        ¡Buen trabajo! Ahora puedes ver las instrucciones y el código al mismo tiempo.


Tarea 1: Crear el archivo HTML.
Objetivos

    Añadir photo.jpg a la página web.

    Añadir tu nombre como un encabezado en la página web.

    Añadir una lista desordenada de tus cinco artistas musicales favoritos.

    Añadir una lista ordenada de tus cinco películas favoritas.

    Añadir un hipervínculo a tu perfil de Facebook o a meta.com.

Sigue las instrucciones paso a paso a continuación:

    Abre el archivo index.html y configura la siguiente estructura básica de un documento HTML:
    HTML

    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>
    </body>
    </html>

    Establece el título del documento HTML con tu nombre:
    HTML

    <!DOCTYPE html>
    <html>
    <head>
        <title>tu nombre</title>
    </head>
    <body>
    </body>
    </html>

    Enlaza el archivo styles.css dentro del elemento head.

    Añade cinco elementos de división (div) dentro del elemento body.

    Añade un encabezado de nivel 1 (h1) en el primer elemento de división que muestre tu nombre.

    Añade la imagen photo.jpg usando un elemento img en el segundo elemento de división.

    Añade un atributo id con el valor photo al elemento de imagen.

    Añade un encabezado de nivel 2 (h2) con el texto "Favorite Music Artists" en el tercer elemento de división. En esa misma división, añade una lista desordenada (ul) con tus 5 artistas favoritos.

    Añade un encabezado de nivel 2 (h2) con el texto "Favorite Films" en el cuarto elemento de división. En esa misma división, añade una lista ordenada (ol) con tus 5 películas favoritas.

    Añade un hipervínculo a tu página de perfil de Facebook en el último elemento de división. Alternativamente, añade un hipervínculo a https://www.meta.com/. Como paso final, añade "My Profile" como el texto descriptivo de la etiqueta <a>.

Tarea 2: Dar estilo a la página web usando CSS.
Objetivos

    Dar estilo a la página web mediante CSS.

Sigue las instrucciones paso a paso a continuación:

    Abre el archivo styles.css.

    Añade una regla CSS para tu imagen que establezca la propiedad border (borde) con un ancho de 2 píxeles, de tipo solid (sólido) y color blue (azul).

    Añade una regla CSS para el encabezado 1 (h1) que contiene tu nombre y cambia su color a blue (azul).

    Añade una regla CSS para todos los encabezados <h2> y cambia su color a grey (gris).

    Añade una regla CSS que aplique un margin (margen) de 4 píxeles a los elementos de división (div).

Paso final: ¡Enviemos tu código!

¡Buen trabajo! Para completar esta evaluación:

    Guarda tu archivo a través de File (Archivo) -> Save (Guardar).

    Selecciona "Submit Assignment" (Enviar tarea) en tu barra de herramientas del laboratorio.

Tu código será calificado automáticamente y recibirás comentarios en breve en la pestaña "Grades" (Calificaciones). También puedes ver tu puntuación en la pestaña "My Submission" (Mi envío) de tu tarea de programación.


Consejos

    Asegúrate de que las etiquetas HTML estén cerradas correctamente.

    Usa un tipo de encabezado diferente para tu nombre.

    Recuerda el modelo de caja (box model).

    Repasa las lecciones Creación de un documento HTML, Adición de imágenes, Selección y estilo, y Diferentes tipos de selectores.