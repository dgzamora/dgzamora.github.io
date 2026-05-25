import yaml
from weasyprint import HTML

# 1. Leer tus bases de datos .yml de Jekyll
with open('_data/docencia.yml', 'r', encoding='utf-8') as f:
    formacion = yaml.safe_load(f)
with open('_data/investigacion.yml', 'r', encoding='utf-8') as f:
    investigacion = yaml.safe_load(f)
with open('_data/divulgacion.yml', 'r', encoding='utf-8') as f:
    divulgacion = yaml.safe_load(f)

# 2. Diseñar la plantilla HTML del CV (reutilizando tus datos)
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        @page {{ size: A4; margin: 20mm; }}
        body {{ font-family: 'Times New Roman', serif; color: #333; line-height: 1.5; }}
        h1 {{ color: #576e30; border-bottom: 2px solid #576e30; padding-bottom: 5px; }}
        h2 {{ color: #576e30; margin-top: 20px; font-size: 14pt; text-transform: uppercase; }}
        .item {{ margin-bottom: 10px; }}
        .year {{ font-weight: bold; color: #576e30; display: inline-block; width: 60px; }}
    </style>
</head>
<body>
    <h1>Diego García Zamora</h1>
    <p>Profesor Ayudante Doctor | Universidad de Jaén</p>

    <h2>Formación Académica</h2>
"""

# Añadir títulos oficiales
for item in formacion.get('oficial', []):
    html_template += f'<div class="item"><span class="year">{item["anio"]}</span> <strong>{item["titulo"]}</strong> - {item["centro"]}</div>'

html_template += "<h2>Investigación y Publicaciones</h2>"
# Aquí harías lo mismo recorriendo los artículos de investigacion...

html_template += """
</body>
</html>
"""

# 3. Convertir directamente a un PDF local
HTML(string=html_template).write_pdf("CV_Diego_Garcia_Zamora.pdf")
print("¡CV local actualizado en formato PDF!")