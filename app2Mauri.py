import streamlit as st
import pandas as pd
import plotly.express as px

df_dcomplejo = pd.read_csv('demo_data.csv')

st.sidebar.header('Filtros')
filtro_producto = st.sidebar.multiselect('Selecciona Productos:', df_dcomplejo['Producto'].unique())
filtro_region = st.sidebar.multiselect('Selecciona Región:', df_dcomplejo['Region'].unique())
filtro_mes = st.sidebar.multiselect('Selecciona Mes:', df_dcomplejo['Mes'].unique())

tab1, tab2, tab3 = st.tabs(["Líneas", "Dispersión", "Barras"])

df_filtrado = df_dcomplejo.copy()

if filtro_producto:
    df_filtrado = df_filtrado[df_filtrado['Producto'].isin(filtro_producto)]

if filtro_region:
    df_filtrado = df_filtrado[df_filtrado['Region'].isin(filtro_region)]

if filtro_mes:
    df_filtrado = df_filtrado[df_filtrado['Mes'].isin(filtro_mes)]

with tab1:
    st.header("Gráfico de líneas")
    fig1 = px.line(df_filtrado, x='Mes', y='Cantidad', color='Producto', title='Ventas por Mes')
    st.plotly_chart(fig1)
with tab2:
    st.header("Gráfico de dispersión")
    fig2 = px.scatter(df_filtrado, x='Precio', y='Cantidad', color='Producto', title='Precio vs Cantidad Vendida')
    st.plotly_chart(fig2)
with tab3:
    st.header("Gráfico de barras")
    df_fig3 = df_filtrado.groupby('Producto').agg({'Cantidad' : 'sum'}).reset_index()
    fig3 = px.bar(df_fig3, x='Producto', y='Cantidad', color='Producto', title='Total de Ventas por Producto')
    st.plotly_chart(fig3)