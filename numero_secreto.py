def dificuldade(grau):
	for rodada in range(1, grau):
    		print('Tentativa {} de {}'.format(rodada,grau))
    		chute = int(input('Digite um número: '))
    		print('Voce digitou {}'.format(chute))
    		acertou = numero_secreto == chute
    		maior = chute > numero_secreto
    		menor = chute < numero_secreto
    		if acertou:
    	    		print('Voce acertou')
    	    		menu()
    	    		break
    		elif maior:
            		print('Voce errou! O seu chute foi maior doque o numero secreto ')
            		if rodada == grau -1:
            			print('Tente Novamente')
            			menu()
    		elif menor:
            		print('Voce errou! O seu chute foi menor doque o numero secreto')
            		if rodada == grau -1 :
            			print('Tente Novamente')
            			menu()

def menu():
	
	nivel = input('Que nivel preferes: Facil, Medio, Dificil? Digite --> ')
	if nivel == 'facil' or nivel == 'Facil' or  nivel == 'FACIL':
    		dificuldade(facil)
	elif nivel == 'medio' or nivel == 'Medio' or nivel == 'MEDIO':
		dificuldade(medio)
	elif nivel == 'dificil' or nivel == 'Dificil' or nivel == 'DIFICIL':
    		dificuldade(dificil)
	else:
    		print('Fim do jogo')
    		
numero_secreto = 42
facil = 12
medio = 7
dificil = 5
menu()
