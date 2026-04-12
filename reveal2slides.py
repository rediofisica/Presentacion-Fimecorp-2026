from bs4 import BeautifulSoup

def modificar_html(input_file, output_file):
    # Abrir el archivo HTML de entrada
    with open(input_file, "r", encoding="utf-8") as file:
        html = file.read()

    # Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Encontrar todos los bloques de clase "sl-block"
    for sl_block in soup.find_all("div", class_="sl-block"):
        # Verificar si el bloque contiene un bloque <h2>
        h2_block = sl_block.find("h2")
        if h2_block:
            # Modificar los atributos del bloque "sl-block"
            sl_block["class"] = ["sl-block"]
            sl_block["data-block-type"] = "text"
            #sl_block["data-name"] = "text-c4e0f6"
            sl_block["style"] = "height: auto; width: 960px; left: 0px; top: 19px;"
            #sl_block["data-block-id"] = "5e3838c50727e537f46a0a73208a9556"
            
            # Modificar el atributo del bloque <h2>
            h2_block["style"] = "text-align:left"
            sl_block_content = sl_block.find(class_="sl-block-content")
            if sl_block_content:
                # Cambiar los atributos de la clase "sl-block-content"
                sl_block_content["class"] = ["sl-block-content"]
                sl_block_content["data-placeholder-tag"] = "p"
                sl_block_content["data-placeholder-text"] = "Text"
                sl_block_content["style"] = "z-index: 10; color: rgb(28, 69, 135);font-size: 70%;"

        else:
            # Modificar los atributos del bloque "sl-block-content" si no contiene un bloque <h2>
            sl_block_content = sl_block.find(class_="sl-block-content")
            if sl_block_content:
                sl_block_content["style"] = "font-size: 75%;"
            p_block = sl_block.find("p")
            # Modificar el atributo del bloque <p>
            if p_block:
                p_block["style"] = "text-align:justify"

    # Guardar el HTML modificado en un nuevo archivo
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(str(soup))

# Llamar a la función para modificar el HTML
modificar_html("export.html", "modif.html")
