import pandas as pd

dict_sim = ['Sim', 'sim', 'S','y','True', True, '1', 1]
dict_nao = ['Não', 'não', 'N', 'nao', 'False', False, '0', 0]

def corrigir_tipos_nulos_aco(row):
    tipoA300 = row['tipo_do_aço_A300']
    tipoA400 = row['tipo_do_aço_A400']
        
    if pd.isna(tipoA400):
        if tipoA300 in dict_sim:
            tipoA400 = 0
        elif tipoA300 in dict_nao:
            tipoA400 = 1
        
    if pd.isna(tipoA300) or tipoA300 == '-':
        if tipoA400 in dict_sim:
            tipoA300 = 0
        elif tipoA400 in dict_nao:
            tipoA300 = 1

    return pd.Series([tipoA300, tipoA400])

def corrigir_tipos(row):
    tipoA300 = row['tipo_do_aço_A300']
    tipoA400 = row['tipo_do_aço_A400']
        
    if tipoA300 in dict_sim:
         tipoA300 = 1
    elif tipoA300 in dict_nao:
         tipoA300 = 0
        
    if tipoA400 in dict_sim:
        tipoA400 = 1
    elif tipoA400 in dict_nao:
        tipoA400 = 0

    return pd.Series([tipoA300, tipoA400])

def corrigir_falhas(df):
    cols_falhas = ['falha_1', 'falha_2', 'falha_3', 'falha_4', 'falha_5', 'falha_6', 'falha_outros']
    df[cols_falhas] = df[cols_falhas].replace(
        {val: 0 for val in dict_nao} | {val: 1 for val in dict_sim}
    )
    return df

def preencher_com_mediana(df):
    cols = ['x_maximo', 'soma_da_luminosidade', 'maximo_da_luminosidade', 
            'espessura_da_chapa_de_aço', 'index_quadrado', 
            'indice_global_externo','indice_de_luminosidade']
    df[cols] = df[cols].fillna(df[cols].median())
    return df

