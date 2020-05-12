# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.escondida = []
		#inicializando escondida para mascarar word
		for i in range(len(word)):
			self.escondida.append('_')
		self.erradas = " "
		self.corretas = " "
		self.game_status = 0 
		self.print_game_status()

	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word:
			self.corretas = self.corretas + " " + letter
		else:
			self.erradas = self.erradas + " "+ letter
			self.game_status += 1

		self.hide_word(letter)

		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return (self.game_status >= 6)
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		return ("".join(self.escondida) == self.word) 		
		
	# Método para não mostrar a letra no board
	def hide_word(self, letter):
		for ind, char in enumerate(self.word):
			if char == letter:
				self.escondida[ind] = letter
		

	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[self.game_status])
		print("\n\nPalavra: " + "".join(self.escondida)) 
		print("\n\nLetras erradas: "+ self.erradas)
		print("\n\nLetras corretas: "+ self.corretas)

		return (self.hangman_won() or self.hangman_over())
		

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
            bank = f.readlines()

        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	fim = False
	while not fim:
		letra = input("\n\nIndique uma letra -> ")
		game.guess(letra)
	# Verifica o status do jogo
		fim = game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
