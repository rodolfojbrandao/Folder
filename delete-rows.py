import numpy as np
import pandas as pd
import os

path = '/media/rodolfo/5A0819190818F5AB/DOUTORADO-SIMULACOES-COMPLETAS/PCC-efeito-combinado-tamanho-densidade/08/dados'
os.chdir(path)
data = pd.read_csv('dados0.csv')
data = data.drop(['id', 'f:0', 'f:1', 'f:2', 'omega:0', 'omega:1', 'omega:2'])
data.to_csv('teste.csv')

