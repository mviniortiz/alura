#Este outro exercício pede para eu criar um programa onde uma pessoa seguidora deve forncer o número de participantes do sorteio e devolver para ela o número sorteado. 
#A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes.


from random import randint
n = int(input("Digite o nº de participantes do sorteio: "))
print(f"O número sorteado foi {randint(1, n)}")
