import pandas as pd 
import numpy as np
from sqlalchemy import create_engine
import pymysql
pd.set_option('display.max_columns', None)


def ver_unicos(df):
    print('  ')
    print('VISUALIZACIÓN DE ÚNICOS')
    print('  ')
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].dtype.name in ['string', 'category']:
            print(col)
            print('-----------------------------')
            unicos = df[col].unique()
            print(sorted(unicos, key=lambda x: str(x)))


def extract_data(nombre_df):
    print('INFORMACIÓN SOBRE COLUMNAS')
    print('  ')
    print(nombre_df.info())
    print('--------------------------------------------------')
    print('  ')
    print('DIMENSIONES DATAFRAME')
    print('  ')
    print(nombre_df.shape)
    print('  ')
    print('--------------------------------------------------')
    print('  ')
    print('VISUALIZACIÓN DE DUPLICADOS')
    print('  ')
    print(nombre_df.duplicated().sum())
    print('--------------------------------------------------')
    print('  ')
    print('VISUALIZACIÓN DE NULOS')
    print('  ')
    print(nombre_df.isnull().sum())
    ver_unicos(nombre_df)

    return nombre_df.head()



def porcentaje_nulos(df):
    nulos = df.isnull().sum()/df.shape[0]*100
    nulos = nulos[nulos > 0]
    nulos.sort_values(ascending=False)
    nulos = nulos.to_frame(name='perc_nulos').reset_index()
    return nulos


def borrar_columna(df, lista_col):
    for col in lista_col:
        df.drop(col, axis = 1, inplace = True)
        return df.columns



