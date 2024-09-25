# -*- coding: utf-8 -*-
"""Grafico de doações no mês de Julho.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZVtbrD7lWya0c76E1m8vfZgaxUcXcLgJ
"""

import matplotlib.pyplot as plt
import numpy as np

### Criar eixos e a figura
fig, ax = plt.subplots()
nomefig = 'graficosdoações.png'
xlab = 'Datas do mes de Julho'
ylab = 'Numero de Doacoes'
fsize, lsize = 14, 12
## eixo x
Data = np.array ([1,6,7,12,21,25,30])
print(Data)
### eixo y
Doacoes = np.array([0,1,1,2,1,1,1])
## Plotar dados
ax.plot(Data, Doacoes, marker = 'o', lw = 2, ls= '-')
### configurar
ax.set_xlabel(xlab, fontsize = fsize)
ax.set_ylabel(ylab, fontsize = fsize)
ax.tick_params (labelsize = lsize, width = 2)
ax.grid(ls = '--', color = 'grey')
### Salvar
fig.savefig ( 'nome.png')
plt.show()

