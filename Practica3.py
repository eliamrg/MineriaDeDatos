import pandas as pd
import os

#IMPORTACION DEL DATASET
data = pd.read_csv('dataSet\MoviesDataSet.csv')

def Analisis_Calificacion_por_Año():
    # SE OBTINEN LOS DATOS A MOSTRAR COMO LA MEDIA, LA SUMA, EL MAXIMO Y MINIMO
    df_Analisis_Calificacion_por_Año = data.groupby(['title_year']).agg({'imdb_score': ['sum', 'count', 'mean', 'min', 'max']}).reset_index()
    # SE RENOMBRAN LAS COLUMNAS
    df_Analisis_Calificacion_por_Año.columns = [ 'Año', 'Suma_Calificacion', 'Conteo_Calificaciones', 'Promedio_Calificacion', 'Calificacion_Minima', 'Calificacion_Maxima']
    # EXPORTACION DE CSV
    df_Analisis_Calificacion_por_Año.to_csv(os.path.join(os.getcwd(), "dataSet", 'Analisis_de_calificaciones_anio.csv'), index=False)

def Analisis_Ganancia_por_Año():
    # SE OBTINEN LOS DATOS A MOSTRAR COMO LA MEDIA, LA SUMA, EL MAXIMO Y MINIMO
    df_Analisis_Ganancia_por_Año = data.groupby(['title_year']).agg({'gross': ['sum', 'count', 'mean', 'min', 'max']}).reset_index()
    # SE RENOMBRAN LAS COLUMNAS
    df_Analisis_Ganancia_por_Año.columns = [ 'Año', 'Suma_Ganancias', 'Conteo_Ganancias', 'Promedio_Ganancias', 'Ganancia_Minima', 'Ganancia_Maxima']
    # EXPORTACION DE CSV
    df_Analisis_Ganancia_por_Año.to_csv(os.path.join(os.getcwd(), "dataSet", 'Analisis_de_ganancias_anio.csv'), index=False)

Analisis_Calificacion_por_Año()
Analisis_Ganancia_por_Año()