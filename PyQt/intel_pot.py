pot_init = 0.0
pot_fin = 25.0
tempo = 15.0
tempo_div=[]
w_div=[]
w = pot_fin - pot_init
#verificando divisores de tempo
for n in range(2,int(tempo)):
	if tempo % n == 0: 
		tempo_div.append(n)
print tempo_div
for m in tempo_div:
	result = w/(tempo/m)
	# if result.is_integer():
	w_div.append(result)

print w_div
