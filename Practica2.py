import pandas as pd
import os

#IMPORTACION DEL DATASET
data = pd.read_csv('dataSet\movie_metadata.csv')

# ELIMINACION DE LAS SIGUIENTES COLUMNAS:
def delete_columns(df: pd.DataFrame)->pd.DataFrame:
    df = df.drop('color', axis=1)
    df = df.drop('director_facebook_likes', axis=1)
    df = df.drop('actor_3_facebook_likes', axis=1)
    df = df.drop('actor_1_facebook_likes', axis=1)
    df = df.drop('movie_imdb_link', axis=1)
    df = df.drop('num_user_for_reviews', axis=1)
    df = df.drop('actor_2_facebook_likes', axis=1)
    df = df.drop('aspect_ratio', axis=1)
    df = df.drop('movie_facebook_likes', axis=1)
    df = df.drop('actor_2_name', axis=1)
    df = df.drop('actor_1_name', axis=1)
    df = df.drop('actor_3_name', axis=1)
    df = df.drop('facenumber_in_poster', axis=1)
    df = df.drop('cast_total_facebook_likes', axis=1)
    return df

data = delete_columns(data)

# Se guardan los datos limpios
data.to_csv(os.path.join(os.getcwd(), "dataSet", 'MoviesDataSet.csv'), index=False)