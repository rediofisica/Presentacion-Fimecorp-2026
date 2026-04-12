# Procedimiento creación presentaciones con slides.com, reveal.js y Markdown

## 1. Crear el directorio de la presentación y hacer un repositorio git 

En cada cambio que se haga se irá haciendo commits para tener copia de seguridad de los contenidos. La mejor opción es abrir el repositorio plantilla "Slides Template Repository" en github y crear el repositorio nuevo a partir de esa plantilla, usando el botón "Use this template->Create a new repository" situado sobre la lista de archivos. Luego clonar el nuevo repositorio a un directorio local, usando vscode. De forma opcional se puede crear un codespace de github para poder trabajar desde el navegador en cualquier dispositivo que no tenga instalado vscode. Para ello, en github, ir al repositorio recién creado, y justo encima de la lista de ficheros, ir a "Code-> Codespaces-> Create codespace on main".

## 2- Escribir la presentación usando Markdown

Se puede usar Visual Studio Code. Así es más fácil hacer los commits. Se ha creado un perfil de Visual Studio Code específico para Markdown. En ese perfil está instalada la extensión "Code Spell Checker" junto con el Add-on para idioma español. Esto permite corregir la ortografía de forma automática. El Add-on de idioma español se puede desactivar para que el idioma reconocido sea el inglés usando el comando "Disable Spanish Spell Checker Dictionary" en la paleta de comandos.

La sintaxis markdown reconocida por Slides.com es la estándar. No reconoce elementos que requieran extensiones de Pandoc, como por ejemplo las matemáticas y las tablas.

### Separación de diapositivas: 

    # Slide one
    ---
    # Slide two

### Atributos de diapositivas:

    <!-- .slide: data-background-color="red" -->
    # This slide has a red background
    ---
    <!-- .slide: data-background-image="https://..." -->
    # Image background
    ---
    <!-- .slide: data-background-video="https://..." -->
    # Video background

    # Heading 1	
    ## Heading 2	
    ### Heading 3
    **Bold**	
    _Italicized_	
    ~~Strikethrough~~	
    See [Slides](https://slides.com)	
    > Block quote
    - List item one
    - List item two	
    1. Ordered item one
    1. Ordered item two

### Matemáticas

El uso de Latex no funciona (no se convierte el texto). Es necesario escribir el código latex en un bloque math dentro de la interfaz gráfica de slides.com:

Inline math: $x^2$

Math block:
$$
\displaystyle
\left( \sum_{k=1}^n a_k b_k \right)^2
\leq
\left( \sum_{k=1}^n a_k^2 \right)
\left( \sum_{k=1}^n b_k^2 \right)
$$

Lo que sí funciona es usar html tags, por ejemplo para un subíndice:

x<sub>0</sub>

### Tablas

Como las tablas markdown requieren una extensión de Pandoc, no funcionan. Sin embargo se pueden crear, convertirlas a html (por ejemplo con el conversor online de Pandoc) y luego copiar el html resultante directamente sobre el archivo markdown.

Por ejemplo, la tabla

  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1

Se convierte a html:

<table>
<thead>
<tr class="header">
<th style="text-align: right;">Right</th>
<th style="text-align: left;">Left</th>
<th style="text-align: center;">Center</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">12</td>
<td style="text-align: left;">12</td>
<td style="text-align: center;">12</td>
<td>12</td>
</tr>
<tr class="even">
<td style="text-align: right;">123</td>
<td style="text-align: left;">123</td>
<td style="text-align: center;">123</td>
<td>123</td>
</tr>
<tr class="odd">
<td style="text-align: right;">1</td>
<td style="text-align: left;">1</td>
<td style="text-align: center;">1</td>
<td>1</td>
</tr>
</tbody>
</table>

y se visualiza correctamente en slides.com

Otros ejemplos de tabla: Tabla multilínea

-------------------------------------------------------------
 Centered   Default           Right Left
  Header    Aligned         Aligned Aligned
----------- ------- --------------- -------------------------
   First    row                12.0 Example of a row that
                                    spans multiple lines.

  Second    row                 5.0 Here's another one. Note
                                    the blank line between
                                    rows.
-------------------------------------------------------------

Grid tables diversas:

+---------------+---------------+--------------------+
| Fruit         | Price         | Advantages         |
+===============+===============+====================+
| Bananas       | $1.34         | - built-in wrapper |
|               |               | - bright color     |
+---------------+---------------+--------------------+
| Oranges       | $2.10         | - cures scurvy     |
|               |               | - tasty            |
+---------------+---------------+--------------------+

+---------------------+----------+
| Property            | Earth    |
+=============+=======+==========+
|             | min   | -89.2 °C |
| Temperature +-------+----------+
| 1961-1990   | mean  | 14 °C    |
|             +-------+----------+
|             | max   | 56.7 °C  |
+-------------+-------+----------+

+---------------------+-----------------------+
| Location            | Temperature 1961-1990 |
|                     | in degree Celsius     |
|                     +-------+-------+-------+
|                     | min   | mean  | max   |
+=====================+=======+=======+=======+
| Antarctica          | -89.2 | N/A   | 19.8  |
+---------------------+-------+-------+-------+
| Earth               | -89.2 | 14    | 56.7  |
+---------------------+-------+-------+-------+

+---------------+---------------+--------------------+
| Right         | Left          | Centered           |
+==============:+:==============+:==================:+
| Bananas       | $1.34         | built-in wrapper   |
+---------------+---------------+--------------------+

Pipe tables:

| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|   12  |  12  |    12   |    12  |
|  123  |  123 |   123   |   123  |
|    1  |    1 |     1   |     1  |

(Nota: también se pueden generar tablas en excel y convertirlas a html)

## 3- Usar la herramienta de importación de Markdown de Slides.com para crear una presentación

Copiar el texto markdown en la herramienta para crear la presentación.

## 4- Exportar la presentación recién creada a reveal.js

Usar la exportación a reveal.js. Cambiar el nombre de la presentación exportada a "export.html".

## 5- Aplicar un script de python para dar formato a la presentación

Ejecutar el script reveal2Slides.py. Este script da el formato deseado a la presentación. El formato está basado en la presentación del grupo de usuarios de Scandidos de Marzo 2023. El script cambia el título de la diapositiva (tipo de encabezado h2) para que esté situado en la parte superior de la diapositiva, texto alineado a la izquierda, tamaño de letra 70%, color azul. El texto de las diapositivas se fija al 75% de tamaño y el texto se alinea a la izquierda. Para un mejor resultado, la presentación en slides.com debería usar el estilo Helvética. 

Se exporta la presentación nueva como modif.html 

## 6- Reimportar la presentación en slides.com 

Una vez reformateada la presentación, se vuelve a a importar en slides.com como si fuera una presentación de reveal.js.


## 7- Añadir imágenes y formato extra a la presentación en slides.com

Se añaden y suben las imágenes a slides.com y se recolocan los elementos usando la interfaz gráfica del mismo.

## 8- Descargar la presentación para usar offline

Se vuelve a usar la exportación a reveal.js. En las opciones de exportación de slid.es, seleccionar "Export to reveal.js". Copiar solo el nodo <div class="reveal"> y pegarlo en el body de la plantilla en blanco "index.html", justo debajo del comienzo del nodo <body>.
Ejecutar el script CreaLista.py, que permite descargar de la nube las imágenes de la presentación, y modifica los enlaces en index.html para que apunten a los ficheros locales. Las imágenes se guardarán en la carpeta images, así como los vídeos y se crea una nueva versión local del index.html llamada new.html. 
Cambiar <meta name="description" content="Título de la presentación"> y <title>Presentación Slides</title>

ATENCIÓN: Las notas de presentación no se exportan. Habría que buscar la forma de exportarlas de forma programática, aunque parece difícil, ya que slides.com no las exporta. En las presentaciones originales de slides.com las notas se encuentran en el nodo <script>, en la variable SLConfig, en el campo "notes". 

## 9- (Opcional) Añadir animaciones avanzadas Lottie o CSS a la presentación offline

slides.com no admite scripts en la presentación. Pero sí los podemos añadir a la presentación offline posteriormente.

## 10- (Opcional) Activar la presentación en github pages

Se puede mostrar la presentación desde github pages. Para ello, simplemente debe estar sincronizado el repositorio github, y ponerlo como público. Después activar la presentación en github pages. El nombre del fichero new.html hay que cambiarlo a index.html.

## 11- (Sólo si se hace el repositorio público) Eliminar los scripts del repositorio público

Eliminar los scripts de python del repositorio.
