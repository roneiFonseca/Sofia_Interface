import matplotlib.pyplot as plt
import numpy as np
import parametros
import os,sys


# 1 W/ minuto
def plotMode(self,mode):
	os.listdir("/usr/lib/python2.7/dist-packages/PyQt4")
	#os.listdir("/Users/MatiasPedro25/Professional/2016_1/LAB/Software/EVOLUTION/Sofia_Interface/PyQt")
	img = "mode" + str(mode) + ".png"
	# print img
	sentence = [
	"[ -f mode1.png ] && rm mode1.png",
	"[ -f mode2.png ] && rm mode2.png",
	"[ -f mode3.png ] && rm mode3.png"
	]
	# print sentence
	for k in range(len(sentence)):
		os.system(sentence[k])
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
