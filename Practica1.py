import kaggle
import os

def get_csv_kaggle ():
  print('Descargando DataSet...')
  kaggle.api.authenticate()
  kaggle.api.dataset_download_files('carolzhangdc/imdb-5000-movie-dataset', path=os.path.join(os.getcwd(), "dataSet"), unzip=True)

get_csv_kaggle()