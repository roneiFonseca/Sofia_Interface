import matplotlib.pyplot as plt
import numpy as np
import parametros
import os,sys


# 1 W/ minuto
def plotMode(self,mode):
	os.listdir("/Users/MatiasPedro25/Professional/2016_1/LAB/Software/EVOLUTION/Sofia_Interface/PyQt")
	img = "mode" + str(mode) + ".png"
	print img
	os.system("rm "+str(mode))
	time_step = parametros.todos['tempoStep']
	timeValue = 0 	#Tempo sempre inicia em zero
	potStep = parametros.todos['potenciaStep']
	potValue = parametros.todos['potenciaInicial']
	y = [potValue]
	x=[timeValue]
	interval = parametros.todos['tempo']

	for n in range(interval/time_step):
		potValue += potStep
		y.append(potValue)
		timeValue += time_step
		x.append(timeValue)

	plt.step(x,y)
	plt.ylabel('some numbers')
	plt.grid()
	# plt.show()
	plt.savefig(img)