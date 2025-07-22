import pandas as pd
import numpy as np


def borrar_duplicados(df):
    df.drop_duplicates(inplace = True)
    print(df.duplicated().sum())

def minusculas_celdas (df):
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].dtype.name == 'string':
            df[col] = df[col].str.lower()
            df[col] = df[col].str.rstrip()
            df[col] = df[col].str.replace(r'\.$', '', regex=True)

    return df

def puntos_por_barra(df):
    nuevas_columnas = {}
    for col in df.columns:
        nuevas_columnas[col] = col.lower().replace(".", "_")

    df.rename(columns = nuevas_columnas, inplace = True)
    df.columns

def limpieza_divisas (df, col, tipo):
    df[col] = df[col].str.replace('$', "")
    df[col] = df[col].str.replace('.', "")
    df[col] = df[col].str.replace(',', ".")
    df[col] = df[col].astype(tipo)



def minusculas(df):
    nuevas_columnas = {}
    for col in df.columns:
        nuevas_columnas[col] = col.lower()

    df.rename(columns = nuevas_columnas, inplace = True)
    df.columns    

def cambio_tipo(df, col, tipo):
    df[col] = df[col].astype(tipo)
    print(df.info()) 


def tipo_fecha(df, col):
    df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')
    print(df[df[col].isna()]) 
    return df     


def cambiar_a_entero(df, col):
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convierte a numérico (float si hay decimales o NaN)
    df[col] = df[col].astype('Int64')  #convierte a entero permitiendo NaNs (Int64 de pandas, no int normal)
    df.info()

   

def cambiar_objeto(df, col):
    df[col] = df[col].astype(str)
    df.info()


def si_no(df, col):
    df[col] = df[col].replace({'1': 'si', '0': 'no'})
    return df


def meses(df, col):
    diccionario_mapa = {1: "enero", 2: "febrero", 3: "marzo",  4: "abril",  5: "mayo",  6: "junio",  7: "julio",  8: "agosto",  9: "septiembre",  10: "octubre",  11: "noviembre",  12: "diciembre",} 
    for item in col:
        df[item] = df[item].map(diccionario_mapa)


def dividir_col (df, col_original, col_nueva1, col_nueva2):
    df[[col_nueva1, col_nueva2]] = df[col_original].str.split("-", expand = True).get([1,2])


#NULOS
 

# Cambiar nulo por nueva categoría
def objeto_categoria (df, col):
    df[col] = df[col].fillna('Unknown')
# Cambiar nulo por moda
def objeto_moda(df, col):
    moda= df[col].mode()[0] 
    df[col] = df[col].fillna(moda)
    return moda
# Cambiar nulo por mediana
def mediana_num(df, col):
    mediana= df[col].median()
    df[col] = df[col].fillna(mediana)   
    nulos= df.isnull().sum().sort_values(ascending= False)
    return nulos




 