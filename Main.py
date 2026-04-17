import time 
import os 
from tarefas import adicionar_tarefa, listar_tarefas

TEMPO = 3

while True:
    print("*****Lista de Tarefas*****")
    print("1- Adicionar Tarefas. ")
    print("2- Listar Tarefas. ")
    print("3- Sair. ")

    opcao = int(input("Escolha uma opção: "))
   
    if opcao == 1:
        descricao = input("Digite uma tarefa: ")
        adicionar_tarefa(descricao)
        
                                    
    elif opcao == 2:
        print("\nSuas Tarefas:")
        listar_tarefas()

    elif opcao == 3:
        print("Saindo do programa...")
        break
        
    else:
        print("Opção inválida, tente novamente.")         
