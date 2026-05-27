import random
print("--------------------------------------------------------------------")
print()
print("                          MEGASENA                                  ")
print()
print("--------------------------------------------------------------------")
print()
print()
qtdjogos = int(input("Quantos jogos você deseja fazer? : "))
print()


def gerador (jogos):
    objeto = {}
    for i in range(jogos):
        lista = []
        jogo = 0
        while (jogo < 6):
            numero_aleatorio = random.randint(1, 60)
            lista.append(numero_aleatorio)
            jogo += 1
        if (len(lista) == 6) :   
            objeto[i +1] = lista
            lista = []
    return objeto
 
sorteios = gerador(qtdjogos)
print("os jogos sorteados foram:")
for i in sorteios:
    print(sorteios[i])
print()

input("Pressione Enter para sair...")