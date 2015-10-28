from random import sample

def print_menu():
	print ('-' * 30)
	print ("        LOTERICA")
	print ('-' * 30)
	print ("1 - Lotofacil")
	print ("2 - Lotomania")
	print ("3 - Mega Sena")
	print ("4 - 1 numero(MEGA)")
	print ("5 - 4 numeros(Mega Sena)")		
	print ('-' * 30)
	check_choise()
	
def check_choise():
	is_valid = 0
	while is_valid == 0:
		question = int(raw_input("Escolha o tipo de Jogo: [1-3] \n"))
		if (question >= 1 and question <= 5):
			is_valid = 1
		else:
			print ""
			print ('-' * 30)
			print ("       VALOR INVALIDO")
			print ('-' * 30)
			print ""
			print_menu()
	loteria(question)

def loteria(tipo):
	if tipo == 1:
		lst = range(1,26)
		qt = 15		
	elif tipo == 2:
		lst = range(0,100)
		qt = 50
	elif tipo == 3:
		lst = range(1,61)
		qt = 6
	elif tipo == 4:
                lst = range(1,61)
                qt = 1
	else:
                lst = range(1,61)
                qt = 4
	print lst	
	print ordenar(sorteio(lst,qt))

def sorteio(lista, qntNum):
	n = sample(lista,qntNum)	
	return n

def ordenar(lista):
	for j in range(1, len(lista)):
		chave = lista[j]
		i = j - 1
		while i >= 0 and lista[i] > chave:
			lista[i + 1] = lista[i]
			i -= 1
			lista[i + 1] = chave
	return lista

print_menu()
