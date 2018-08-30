import os
import numpy as np
import pandas as pd
from multiprocessing import Pool

path='/home/hp/Desktop'
os.chdir(path)
#constantes
raio1 = 0.003
raio2 = 0.0003
rx = 5
ry = 5
rz = 10
celulas = rx*ry*rz
dt = 499
size = (celulas,dt)

#vetores alocados
contador_tipo1 = np.zeros(size)
contador_tipo2 = np.zeros(size)
velocidade_tipo1 = np.zeros(size)
velocidade_tipo2 = np.zeros(size)


dados = pd.read_csv(f'dados.0.csv')