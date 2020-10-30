#GRÁFICO DE LINHA 

import matplotlib.pyplot as plt 

x = [15, 70, 80, 90, 100, 150]
y = [100, 200, 300, 400, 500, 600]
#Título
plt.title("Gráfico De Linhas")
#Eixos
plt.xlabel("EIXO-x")
plt.ylabel("EIXO-y")





plt.plot(x, y, color="red", marker="*",)
plt.plot(x, y, color='k')
plt.show()
