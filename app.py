#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:11:51 2020

@author: guille
"""


import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt
import openpyxl


pd.options.display.max_columns = None
pd.options.display.max_rows = None


add_selectbox = st.sidebar.selectbox(
    'OPCIONES',
    ('Inicio', 'Datos curiosos', 'Estudio COVID-19', 'Valora tu experiencia')
    )

 
if add_selectbox == 'Inicio':

    st.title('Bienvenido a la Enciclopedia Interactiva :earth_americas:')

    st.header('¡Con esta herramienta podrá conocer datos curiosos sobre cualquier punto de la geografía española! :sunglasses:')

    st.markdown("developed by **Guillermo Álvarez Alcoba**")

    datos = pd.read_csv('DatosMunicipios.csv', delimiter=';')
#datos.set_index('Ranking de Población', inplace = True)
    df = pd.DataFrame(datos)
#covidacumulados = pd.read_csv('covidacumulados.csv', delimiter =';')
    image4 = Image.open('learn.jpeg')
    st.image(image4,
             use_column_width=False,
             format='JPEG')

    st.text("")
    st.text("")



elif add_selectbox == 'Datos curiosos':
    st.title('Datos curiosos de la geografía española')
    
    ranking = pd.read_csv('ranking.csv', delimiter=';')
    df = pd.DataFrame(ranking)
    
    datos = pd.read_csv('DatosMunicipios.csv', delimiter=';')
    df = pd.DataFrame(datos)


    st.markdown("**Ranking con la distribución de población por municipios del territorio español**")

    st.dataframe(ranking)

    st.text("")
    st.text("") 
 
    video_file = open('Videopoblacion.mov', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)


    st.text("")
    st.text("")

    option = st.sidebar.selectbox(
        'Selecciona el municipio de tu interés para obtener sus datos',
        datos['Nombre'])

    st.text("")

    data_filter = datos[datos['Nombre'] == option]
    st.markdown("**Ahora entremos a conocer un poco más en detalle los municipios del territorio español** ")
    st.markdown("Selecciona en el desplegable una opción y comienza a investigar")

    st.markdown("**Los datos sobre el municipio que ha seleccionado son:** ")
    st.text("")
    st.write(data_filter)

    st.text("")
    st.markdown("Para conocer la ubicación del municipio en el mapa presta atención a la siguiente imagen")

    st.text("")

    data_filter4 = datos[datos['Nombre'] == option]
    seleccion2 = data_filter4['Provincia'].unique()
    image3 = Image.open('provinciasmapa/{}.jpg'.format(seleccion2[0]))
    st.image(image3, caption='Imagen de la provincia de {}'.format(seleccion2[0]),
             use_column_width=False,
             format='JPEG')



    st.text("")    
    st.text("")
    st.text("")


    image = Image.open('mapafisico.jpeg')
    st.image(image, caption='Mapa físico de España',
             use_column_width=False,
             format='JPEG')


    st.text("")    
    st.text("")
    st.text("")

    st.markdown("Pero...**¿Por qué dejar de aprender?**")
    st.markdown("En esta plataforma podras conocer los siguientes datos del lugar seleccionado: ")
    st.markdown("1)Evolución de la población en cuanto a número de habitantes :family:")
    st.markdown("2)Tener una imagen de la bandera del lugar :checkered_flag:")
    st.markdown("3)Saber cuál es el plato típico (acompañado de una imagen del mismo) :fried_egg:")
    st.markdown("4)Conocer el equipo local, así como su año de fundación :soccer:")

    st.text("")
    st.text("")
    st.markdown("**Selecciona tu municipio en la barra de la izquierda y se mostrará por pantalla el resultado**")
    st.text("")
    st.text("")


    add_selectbox = st.sidebar.selectbox(
        '¿Cuál es la siguiente información que desea conocer sobre el lugar selccionado?',
        ('1. Evolución de la población', '2. Imagen de la bandera del lugar', '3. Conocer el plato típico', '4. Conocer el equipo local')
        )


    poblaciones = pd.read_csv('poblaciones.csv', delimiter=';')
    platos = pd.read_csv('platos.csv', delimiter=';')
    equipos = pd.read_csv('equipos.csv', delimiter=';')
   
 

    if add_selectbox == '1. Evolución de la población':
        
        

        data_filter = poblaciones[poblaciones['Nombre'] == option]
        st.write(data_filter)
        st.text("")
        seleccion2 = data_filter['Nombre'].unique()
        st.markdown("**La evolución de {} en los último 10 años es**".format(seleccion2[0]))
        st.text("")
        data_filter1 = data_filter
        data_filter1 = data_filter1.iloc[:, 1:11]
        data_filter1 = pd.DataFrame(data_filter1.stack())
        
        data_filter1.columns = ['Número de habitantes']
        data_filter1 ['Años'] = [p[1] for p in data_filter1.index]
        data_filter1.index = range(len(data_filter1))
        chart = (
            alt.Chart(data_filter1)
            .mark_bar(size=10)
            .encode(
                x = 'Años:T',
                y = 'Número de habitantes:Q'
                )
            )
            
        st.altair_chart(chart, use_container_width=True)

       
    
        
    
    elif add_selectbox == '2. Imagen de la bandera del lugar':
        data_filter2 = datos[datos['Nombre'] == option]
        seleccion = data_filter2['Provincia'].unique()
        st.markdown("La provincia a la que pertenece el lugar seleccionado es **{}**".format(seleccion[0]))
        image1 = Image.open('banderas/{}.jpg'.format(seleccion[0]))
        st.image(image1, caption='Bandera de la provincia de {}'.format(seleccion[0]),
                 use_column_width=False,
                 format='JPEG')
            

      
    elif add_selectbox == '3. Conocer el plato típico':
        data_filter3 = platos[platos['Nombre'] == option]
        seleccion1 = data_filter3['Plato Típico'].unique()
        st.markdown("Uno de los platos más típicos de la provincia es: **{}**".format(seleccion1[0]))
        image2 = Image.open('platos/{}.jpg'.format(seleccion1[0]))
        st.image(image2, caption='Imagen del plato: {}'.format(seleccion1[0]),
                 use_column_width=False,
                 format='JPEG')

    
    
    
    
    elif add_selectbox == '4. Conocer el equipo local':
        data_filter = equipos[equipos['Nombre'] == option]
        st.write(data_filter)
    

elif add_selectbox == 'Estudio COVID-19':

    st.title('Estudio COVID-19')
    st.markdown("**Comencemos por conocer la situación de España en lo relativo a la crisis del Covid-19 :mask:**")
    st.markdown("Selecciona en el desplegable lo que te interese saber y empecemos a conocer la situación")


    add_selectbox = st.sidebar.selectbox(
        'Seleccione su consulta en relación al Covid-19',
        ('1. Infectados de manera acumulativa', '2. Infectados nuevos diariamente', '3. Fallecidos por día', '4. Fallecidos totales', 
         '5. Recuperados nuevos por día', '6. Recuperados totales acumulado', '7. Estudio completo')
        )

    if add_selectbox == '1. Infectados de manera acumulativa':
        covidacumulados = pd.read_csv('covidacumulados.csv', delimiter =';')
        covidacumulados.set_index('Comunidad', inplace=True)

        Comunidad = st.multiselect(
            'Elige la comunidad', list(covidacumulados.index), ['Comunidad de Madrid', 'Islas Canarias']     
            )
        if not Comunidad:
            st.error('Por favor, seleccione al menos una comunidad')

 

        data = covidacumulados.loc[Comunidad]
        st.write("Crecimiento acumulativo de infectados por Covid-19", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Número de habitantes contagiados"}
            )


        chart1 = (
            alt.Chart(data)
            .mark_area(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Número de habitantes contagiados:Q", stack=None),
                color="Comunidad:N",
                )
            ) 
        st.altair_chart(chart1, use_container_width=True)
    
   

       
    
        
    
    elif add_selectbox == '2. Infectados nuevos diariamente':
        covidnuevos = pd.read_csv('covidnuevos.csv', delimiter =';')
        covidnuevos.set_index('Comunidad', inplace=True)
        
        Comunidad1 = st.multiselect(
            'Elige la comunidad', list(covidnuevos.index), ['Comunidad de Madrid', 'Islas Canarias']     
            )
        if not Comunidad1:
            st.error('Por favor, seleccione al menos una comunidad')



        data1 = covidnuevos.loc[Comunidad1]
        st.write("Evolución diaria de nuevos infectados por Covid-19", data1.sort_index())

        data1 = data1.T.reset_index()
        data1 = pd.melt(data1, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Número de habitantes contagiados"}
            )


        chart2 = (
            alt.Chart(data1)
            .mark_bar(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Número de habitantes contagiados:Q", stack=None),
                color="Comunidad:N",
                )
            )
        st.altair_chart(chart2, use_container_width=True)  

    elif add_selectbox == '3. Fallecidos por día':
        covidfallecidosnuevos = pd.read_csv('covidfallecidosnuevos.csv', delimiter =';')
        covidfallecidosnuevos.set_index('Comunidad', inplace=True)

        Comunidad2 = st.multiselect(
            'Elige la comunidad', list(covidfallecidosnuevos.index), ['Comunidad de Madrid', 'Islas Canarias']     
            )
        if not Comunidad2:
            st.error('Por favor, seleccione al menos una comunidad')



        data2 = covidfallecidosnuevos.loc[Comunidad2]
        st.write("Muertes confirmadas para cada día", data2.sort_index())

        data2 = data2.T.reset_index()
        data2 = pd.melt(data2, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Muertes nuevas diarias"}
            )


        chart3 = (
            alt.Chart(data2)
            .mark_bar(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Muertes nuevas diarias:Q", stack=None),
                color="Comunidad:N",
                )
            )
        st.altair_chart(chart3, use_container_width=True)  
        


    elif add_selectbox == '4. Fallecidos totales':
        covidfallecidosacumulados = pd.read_csv('covidfallecidosacumulados.csv', delimiter =';')
        covidfallecidosacumulados.set_index('Comunidad', inplace=True)
        
        Comunidad3 = st.multiselect(
            'Elige la comunidad', list(covidfallecidosacumulados.index), ['Comunidad de Madrid', 'Islas Canarias']     
            )
        if not Comunidad3:
            st.error('Por favor, seleccione al menos una comunidad')
            


        data3 = covidfallecidosacumulados.loc[Comunidad3]
        st.write("Muertes confirmadas totales", data3.sort_index())
        
        data3 = data3.T.reset_index()
        data3 = pd.melt(data3, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Muertes totales"}
            )


        chart4 = (
            alt.Chart(data3)
            .mark_bar(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Muertes totales:Q", stack=None),
                color="Comunidad:N",
                )
            )
        st.altair_chart(chart4, use_container_width=True)  


    elif add_selectbox == '5. Recuperados nuevos por día':
        covidrecuperadosnuevos = pd.read_csv('covidrecuperadosnuevos.csv', delimiter =';')
        covidrecuperadosnuevos.set_index('Comunidad', inplace=True)

        Comunidad4 = st.multiselect(
            'Elige la comunidad', list(covidrecuperadosnuevos.index), ['Comunidad de Madrid', 'Islas Canarias']     
            )
        if not Comunidad4:
            st.error('Por favor, seleccione al menos una comunidad')



        data4 = covidrecuperadosnuevos.loc[Comunidad4]
        st.write("Números de recuperados diarios", data4.sort_index())
        
        data4 = data4.T.reset_index()
        data4 = pd.melt(data4, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Recuperados diarios"}
            )


        chart5 = (
            alt.Chart(data4)
            .mark_bar(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Recuperados diarios:Q", stack=None),
                color="Comunidad:N",
                )
            )
        st.altair_chart(chart5, use_container_width=True)  


    elif add_selectbox == '6. Recuperados totales acumulado':
        covidrecuperadosacumulados = pd.read_csv('covidrecuperadosacumulados.csv', delimiter =';')
        covidrecuperadosacumulados.set_index('Comunidad', inplace=True)

        Comunidad5 = st.multiselect(
            'Elige la comunidad', list(covidrecuperadosacumulados.index), ['Comunidad de Madrid', 'Islas Canarias']     
            )
        if not Comunidad5:
            st.error('Por favor, seleccione al menos una comunidad')



        data5 = covidrecuperadosacumulados.loc[Comunidad5]
        st.write("Total de pacientes recuperados", data5.sort_index())

        data5 = data5.T.reset_index()
        data5 = pd.melt(data5, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Recuperados totales"}
            )


        chart6 = (
            alt.Chart(data5)
            .mark_bar(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Recuperados totales:Q", stack=None),
                color="Comunidad:N",
                )
            )
        st.altair_chart(chart6, use_container_width=True)  




    elif add_selectbox == '7. Estudio completo':
    
    
        covidacumulados = pd.read_csv('covidacumulados.csv', delimiter =';')
        covidacumulados.set_index('Comunidad', inplace=True)

        Comunidad = st.multiselect(
            'Elige la comunidad', list(covidacumulados.index), ['Comunidad de Madrid', 'Islas Canarias']     
            )
        if not Comunidad:
            st.error('Por favor, seleccione al menos una comunidad')



        data = covidacumulados.loc[Comunidad]
        st.write("Crecimiento acumulativo de infectados por Covid-19", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Número de habitantes contagiados"}
            )


        chart1 = (
            alt.Chart(data)
            .mark_area(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Número de habitantes contagiados:Q", stack=None),
                color="Comunidad:N",
                )
            ) 
        st.altair_chart(chart1, use_container_width=True)
    
    
        covidnuevos = pd.read_csv('covidnuevos.csv', delimiter =';')
        covidnuevos.set_index('Comunidad', inplace=True)

        data1 = covidnuevos.loc[Comunidad]
        st.write("Evolución diaria de nuevos infectados por Covid-19", data1.sort_index())

        data1 = data1.T.reset_index()
        data1 = pd.melt(data1, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Número de habitantes contagiados"}
            )


        chart2 = (
            alt.Chart(data1)
            .mark_bar(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Número de habitantes contagiados:Q", stack=None),
                color="Comunidad:N",
                )
            )
        st.altair_chart(chart2, use_container_width=True)  
    
    
    
    
        covidfallecidosnuevos = pd.read_csv('covidfallecidosnuevos.csv', delimiter =';')
        covidfallecidosnuevos.set_index('Comunidad', inplace=True)

        data2 = covidfallecidosnuevos.loc[Comunidad]
        st.write("Muertes confirmadas para cada día", data2.sort_index())

        data2 = data2.T.reset_index()
        data2 = pd.melt(data2, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Muertes nuevas diarias"}
            )


        chart3 = (
            alt.Chart(data2)
            .mark_bar(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Muertes nuevas diarias:Q", stack=None),
                color="Comunidad:N",
                )
            )
        st.altair_chart(chart3, use_container_width=True)  



        covidfallecidosacumulados = pd.read_csv('covidfallecidosacumulados.csv', delimiter =';')
        covidfallecidosacumulados.set_index('Comunidad', inplace=True)

        data3 = covidfallecidosacumulados.loc[Comunidad]
        st.write("Muertes confirmadas totales", data3.sort_index())

        data3 = data3.T.reset_index()
        data3 = pd.melt(data3, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Muertes totales"}
            )


        chart4 = (
            alt.Chart(data3)
            .mark_bar(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Muertes totales:Q", stack=None),
                color="Comunidad:N",
                )
            )
        st.altair_chart(chart4, use_container_width=True)  


        covidrecuperadosnuevos = pd.read_csv('covidrecuperadosnuevos.csv', delimiter =';')
        covidrecuperadosnuevos.set_index('Comunidad', inplace=True)
        
        data4 = covidrecuperadosnuevos.loc[Comunidad]
        st.write("Números de recuperados diarios", data4.sort_index())

        data4 = data4.T.reset_index()
        data4 = pd.melt(data4, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Recuperados diarios"}
            )


        chart5 = (
            alt.Chart(data4)
            .mark_bar(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Recuperados diarios:Q", stack=None),
                color="Comunidad:N",
                )
            )
        st.altair_chart(chart5, use_container_width=True)  

    
        covidrecuperadosacumulados = pd.read_csv('covidrecuperadosacumulados.csv', delimiter =';')
        covidrecuperadosacumulados.set_index('Comunidad', inplace=True)


        data5 = covidrecuperadosacumulados.loc[Comunidad]
        st.write("Total de pacientes recuperados", data5.sort_index())

        data5 = data5.T.reset_index()
        data5 = pd.melt(data5, id_vars=["index"]).rename(
            columns={"index": "Días", "value": "Recuperados totales"}
            )


        chart6 = (
            alt.Chart(data5)
            .mark_bar(opacity=0.7)
            .encode(
                x=alt.X("Días:O", stack=None),
                y=alt.Y("Recuperados totales:Q", stack=None),
                color="Comunidad:N",
                )
            )
        st.altair_chart(chart6, use_container_width=True)  





    st.text("")



elif add_selectbox == 'Valora tu experiencia':
    
      st.title('¡Ayudanos a mejorar! :pray:')
      st.markdown("**Para nosotros tu opinión es muy importante**")

      st.markdown("Valora tu experiencia con esta herramienta con el único objetivo de ayudarnos a mejorar, cuanto más sincera sea la respuesta **MEJOR**")
    
      st.markdown("**En el siguiente espacio podrá escribir comentarios específicos para tener en cuenta**")
      txt = st.text_area("")  
      
      
      if st.button('Enviar'):
          
          opiniones_df = pd.read_excel('Opiniones.xlsx')
          nueva_opinion = pd.DataFrame({'Opiniones' : [txt] }) 
          opiniones_df = opiniones_df.append(nueva_opinion)
          
          st.write('¡Gracias por tu opinion! :+1:')
          opiniones_df.to_excel("Opiniones.xlsx", "Hoja1")    
    
    
    
      valoracion = st.slider('Califica la utilidad de la herramienta',
                             0, 10, 5)
      if 6 <= valoracion <= 10:
          st.balloons()
          st.success('¡ESTUPENDO!')
          st.markdown("Nos alegra saber que tu experiencia ha sido positiva :smile:")
      elif 0 <= valoracion <= 4:
          st.markdown("Vaya... :pensive:")
          st.markdown("Tomamos nota y trataremos de esforzanos para conseguir que le encuentres utilidad")
      st.text("")
      st.text("")


        
      
  

    


