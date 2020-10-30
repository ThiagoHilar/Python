#GRÁFICO SCATTERPLOT

import matplotlib.pyplot as plt 

x = [15, 70, 80, 90, 100, 150]
y = [100, 200, 300, 400, 500, 600]

TITULO = "GRÁFICO SCATTERPLOT"
eixox = "eixo x"
eixoy = "eixo y"
	#Legendas
plt.title(TITULO)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, color='grey', s=100, marker="o")
plt.plot(x, y)
plt.legend()
plt.legend()

plt.show()

