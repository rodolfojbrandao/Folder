import os
import numpy as np
import pandas as pd

path = '/media/rodolfo/5A0819190818F5AB/DOUTORADO-SIMULACOES-COMPLETAS/PCC-efeito-combinado-tamanho-densidade/17/dados'
os.chdir(path)

for i in range(0,491):
    data = pd.read_csv('dados.{}.csv'.format(i))
    data = data.drop(['id', 'f:0', 'f:1', 'f:2', 'omega:0', 'omega:1', 'omega:2'], axis = 1)
    data.to_csv('dados.{}.csv'.format(i))