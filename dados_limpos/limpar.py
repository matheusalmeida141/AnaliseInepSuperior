import pandas as pd

############ TRATA O ARQUIVO DAS COLUNAS ################
colunas = open('colunas')

colunas = colunas.readlines()

cols = []
for i in colunas:
    cols.append(i[:len(i) - 1])

cols.append('NO_CINE_ROTULO')

del colunas

############ FILTRA AS COLUNAS DOS DADOS BRUTOS ###################
for i in range(10, 25):
    
    arquivo = f"../dados_brutos/20{i}/dados/MICRODADOS_CADASTRO_CURSOS_20{i}.CSV"

    df = pd.read_csv(arquivo, sep=';', usecols=cols, encoding='latin1', low_memory=False)

#print(df.head())

    del arquivo

    ######### REMOVER DEMAIS CURSOS ####################################

    lic = df[ (df['TP_GRAU_ACADEMICO'] == 2)  & (df['NO_CINE_ROTULO'].str.startswith('Matemática', na=False)) ]
    del df

    lic.to_csv(f'./dados/20{i}.csv')

    del lic
    
    print(i)