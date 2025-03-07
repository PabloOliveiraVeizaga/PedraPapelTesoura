from time import sleep
from random import randint

computador = randint(0,2)

print("0 é Pedra, 1 é Papel, 2 é Tesoura")
print("JÓ")
sleep(1)
print("KEN")
sleep(1)
print("PO")

jogador = int(input("Faça a sua escolha: "))
              
if computador == 0:
    if jogador == 0:
        sleep(1)
        print("Eu joguei pedra, foi empate!")
        
    elif jogador == 1:
        sleep(1)
        print("Eu joguei pedra, você venceu...")
        
    elif jogador == 2:
        sleep(1)
        print("Eu joguei pedra, você perdeu!")
        
if computador == 1:
    if jogador == 0:
        sleep(1)
        print("Eu joguei papel, você perdeu!")
    
    elif jogador == 1:
        sleep(1)
        print("Eu joguei papel, foi empate!")
        
    elif jogador == 2:
        sleep(1)
        print("Eu joguei papel, você venceu...")
        
if computador == 2:
    if jogador == 0:
        sleep(1)
        print("Eu joguei tesoura, você venceu...")
    
    elif jogador == 1:
        sleep(1)
        print("Eu joguei tesoura, você perdeu!")
    
    elif jogador == 2:
        sleep(1)
        print("Eu joguei tesoura também, foi empate!")
    

