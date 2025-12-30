import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

 
# Configuración de la página
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")
st.title("📊 Análisis de Anuncios de Venta de Coches")

# Cargar los datos con manejo de errores
try:
    car_data = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("No se encontró el archivo 'vehicles_us.csv'. Verifica que esté en la misma carpeta.")
    st.stop()

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Cuando el usuario hace clic en el botón
    # Mensaje informativo
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    st.write('Relación entre el **kilometraje** (odómetro) y el **precio** del vehículo.')

    # Limpieza básica de datos (recomendado para evitar puntos erróneos)
    data_clean = car_data[['price', 'odometer']].dropna()  # Eliminar filas con valores nulos
    data_clean = data_clean[(data_clean['price'] > 0) & (data_clean['odometer'] >= 0)]  # Precios y km positivos

    # Crear el gráfico de dispersión
    fig = px.scatter(
        data_clean,
        x="odometer",
        y="price",
        title="Precio vs. Kilometraje",
        labels={"odometer": "Kilometraje (millas)", "price": "Precio ($)"},
        opacity=0.6,                  # Puntos semi-transparentes para ver densidad
        color_discrete_sequence=['#636EFA']
    )

    # Mejoras visuales
    fig.update_traces(marker=dict(size=6))
    fig.update_layout(
        xaxis_title="Kilometraje (millas)",
        yaxis_title="Precio ($)",
        showlegend=False
    )

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)