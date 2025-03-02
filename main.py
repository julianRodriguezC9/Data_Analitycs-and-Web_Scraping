import requests
import json
import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
from pandasql import sqldf

# Definición de variables globales
URL_COLMO = "https://www.colmo.com.ar/productos/"
USER_AGENT_COLMO = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}
PARAMETRO = {'page': 1, 'limit': 12}

# Lista para almacenar productos
productos = []

# Función para obtener productos de una página
def obtener_productos(pagina):
    """Obtiene productos de una página específica del sitio web."""
    PARAMETRO['page'] = pagina
    response = requests.get(URL_COLMO, headers=USER_AGENT_COLMO, params=PARAMETRO)
    
    # Verificar que la solicitud fue exitosa
    if response.status_code != 200:
        print(f"Error al obtener datos de la página {pagina}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    productos_en_pagina = soup.find_all(class_='js-item-product col-6 col-md-3 item item-product')

    for producto in productos_en_pagina:
        # Verificar si el producto tiene una oferta
        oferta = producto.find(class_='js-offer-label label label-accent') is not None
        producto_data = (
            producto.get('data-product-id'),
            producto.find('a').get('title'),
            json.loads(producto.find('script').string)['offers']['price'],
            oferta
        )
        productos.append(producto_data)

# Función para guardar los productos en un archivo CSV
def guardar_csv(data, archivo):
    """Guarda los datos de productos en un archivo CSV."""
    with open(archivo, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ["id", "descripcion", "precio", "oferta"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Función para realizar consultas SQL sobre un DataFrame
def consulta_sql(query, df):
    """Ejecuta una consulta SQL sobre un DataFrame."""
    return sqldf(query, globals())

# Función para generar gráficos
def generar_graficos(df):
    """Genera y muestra los gráficos para los productos."""
    
    # Histograma de precios
    plt.figure(figsize=(10, 6))
    sns.histplot(df['precio'], kde=True, bins=30)  # Histograma con KDE
    plt.title('Distribución de Precios de los Productos')
    plt.xlabel('Precio')
    plt.ylabel('Frecuencia')
    plt.show()

    # Gráfico de cantidad de productos en oferta vs no oferta
    plt.figure(figsize=(8, 5))
    sns.countplot(x='oferta', data=df)
    plt.title('Productos en Oferta vs No Oferta')
    plt.xlabel('Oferta')
    plt.ylabel('Cantidad de Productos')
    plt.show()

# Obtener productos de las primeras 8 páginas
for pagina in range(1, 9):
    obtener_productos(pagina)

# Construcción del diccionario para el CSV
data = [{"id": p[0], "descripcion": p[1], "precio": p[2], "oferta": p[3]} for p in productos]

# Guardar los datos en un archivo CSV
guardar_csv(data, 'dataProductos.csv')

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('dataProductos.csv')

# Realizar consulta SQL sobre los productos en oferta
consulta = """
SELECT 
    descripcion,
    precio
FROM df
WHERE oferta == True
"""
df_export = consulta_sql(consulta, df)

# Guardar los datos procesados en un nuevo archivo CSV
df_export.to_csv("datosProcesados.csv", index=False)

# Generar los gráficos
generar_graficos(df)
