# Data_Analytics y Web Scraping

## **Descripción**

### Resumen

En este proyecto se utilizan herramientas de web scraping, análisis HTML y tecnologías SQL para extraer datos de una tienda online de ropa. El objetivo es identificar y extraer información clave que pueda ser utilizada para análisis posteriores. Este proyecto aplica técnicas para obtener, limpiar, transformar y visualizar datos desde una página web, permitiendo obtener información relevante de los datos recopilados.

### Objetivos

El objetivo principal es aprender y aplicar técnicas de web scraping, así como adquirir habilidades en limpieza, transformación y visualización de datos. Esto ayudará a desarrollar un entendimiento integral del proceso de extracción y tratamiento de datos provenientes de la web.

## **Abstract**

This project focuses on the use of web scraping tools, HTML analysis, and SQL technologies to extract relevant data from an online clothing store. The goal is to identify key information, such as product details, prices, and availability, for further analysis. The project also aims to improve skills in data cleaning, transformation, and visualization to effectively handle and process the data extracted from the website.

## **Tecnologías Utilizadas**

- **Python**: Lenguaje de programación principal para el proyecto.
- **BeautifulSoup**: Librería de Python para analizar HTML y realizar scraping.
- **Requests**: Librería de Python para realizar solicitudes HTTP y obtener páginas web.
- **SQL**: Lenguaje utilizado para gestionar y consultar bases de datos.
- **SQLite**: Base de datos ligera utilizada para almacenar los datos obtenidos del scraping.
- **Pandas**: Librería de Python para la manipulación y análisis de datos.
- **Jupyter Notebooks**: Entorno interactivo para analizar y visualizar datos.
- **DevTools del Navegador**: Herramientas para analizar el tráfico de red del sitio web objetivo.

## **Desarrollo**
El proyecto comenzó con la instalación de todas las herramientas y librerías necesarias a través del símbolo del sistema de Windows, ya que el proyecto fue desarrollado en este sistema operativo. Una vez completada la instalación, se procedió a analizar la página web objetivo para entender su estructura y diseño HTML. Se enviaron solicitudes HTTP a la página para obtener la información requerida.

El objetivo específico del proyecto fue recopilar detalles de todos los productos a la venta, incluyendo sus nombres, precios y si tenían descuentos. Los datos recopilados se almacenaron inicialmente en formato CSV y luego se transfirieron a una base de datos SQL para realizar un análisis más profundo. La manipulación, filtrado y almacenamiento de los datos se realizó dentro de la base de datos SQL.

## **Conclusiones, dificultades y mejoras**
Una de las principales dificultades del proyecto fue entender por qué, al realizar el web scraping de los productos en la página web, solo se obtenían doce productos en lugar de todos los disponibles. Este problema se solucionó al analizar el tráfico de la página y descubrir que la carga de productos era dinámica. Es decir, al desplazarse hacia abajo, la página realizaba solicitudes adicionales para cargar más productos.

Una vez comprendido este proceso, la solución consistió en simular esas mismas solicitudes dinámicas para obtener todos los productos disponibles, de manera que el scraping pudiera acceder a toda la información de forma completa.

El web scraping demostró ser una herramienta poderosa para analizar páginas web con grandes cantidades de datos. A través de este proyecto, fue posible aprender y aplicar técnicas clave de extracción de datos y vincularlos eficientemente a una base de datos SQL para su posterior análisis.

En resumen, el proyecto fue un éxito. Se siguieron los procesos adecuados, se utilizaron herramientas y tecnologías relevantes para el web scraping, y se empleó SQL para almacenar los datos en una base de datos, lo que permitió manipular y consultar la información de forma más eficiente.

Como próximo paso, se planea expandir el alcance del proyecto obteniendo datos de múltiples páginas web relacionadas, lo que permitirá realizar análisis más completos y comparativos entre diferentes fuentes de información. La idea es automatizar la recolección de datos de diversas plataformas y cruzarlos entre sí para obtener conclusiones más precisas y enriquecidas.

Además, se incorporará Power BI como herramienta para la visualización de los datos obtenidos, lo que permitirá crear dashboards interactivos y gráficos dinámicos que facilitarán la comprensión y el análisis de grandes volúmenes de información. Esto permitirá presentar los datos de manera más clara y accesible, brindando una mejor perspectiva de las tendencias y patrones identificados.

Con la integración de más fuentes de datos y la visualización avanzada con Power BI, se abriría la posibilidad de realizar análisis más profundos, como la comparación de precios, disponibilidad de productos y tendencias de mercado a través de diferentes tiendas en línea. Además, la integración de múltiples fuentes de datos podría facilitar la construcción de modelos predictivos y análisis más complejos, mejorando la capacidad para tomar decisiones informadas basadas en datos extraídos de diversas páginas web.
