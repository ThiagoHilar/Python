#GRÁFICO DE BARRAS

import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 20, 30, 40, 50, 60, 70, 80]
TITULO = "GRÁFICO DE BARRAS"
eixox = "eixo x"
eixoy = "eixo y"
	#Legendas
plt.title(TITULO)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.bar(x, y, color="orange")
plt.legend("10")
plt.show()
