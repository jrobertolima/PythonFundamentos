

def verPalavra(palavra):
    listaLetras=[]    
    for letra in palavra:
        if letra in listaLetras:
            print("\nTem letra repetida! ", letra)
            return
        else:
            listaLetras.append(letra)
            
    print("\nNão tem nenhuma letra repetida!")
    return 
#Ler a palavra
palavra = input('\nInforme a palavra a ser verificada: ')
verPalavra(palavra)

