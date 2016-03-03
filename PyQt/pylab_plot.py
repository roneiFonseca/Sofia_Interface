import matplotlib.pyplot as plt
import numpy as np
import parametros
import os,sys


# 1 W/ minuto
def plotMode(self,mode):
	os.listdir("/Users/MatiasPedro25/Professional/2016_1/LAB/Software/EVOLUTION/Sofia_Interface/PyQt")
	img = "mode" + str(mode) + ".png"
	# print img
	sentence = "rm " + img
	# print sentence
	os.system(sentence)
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

	if mode == 1:
		color = 'blue'
	elif mode == 2:
		color = 'green'
	else:
		color = 'red'

	plt.xticks(x, range(interval+1))
	plt.step(x,y,color)
	plt.ylabel('Potencia (W)')
	plt.xlabel('Tempo (min)')
	plt.grid()
	plt.axis([0, interval, 0, 50])
	plt.savefig(img)
	plt.close()