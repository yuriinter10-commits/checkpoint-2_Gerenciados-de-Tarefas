import time 
import os 
from tarefas import adicionar_tarefa, listar_tarefas,carregar_dados,concluir_tarefas

carregar_dados()

TEMPO = 3

while True:
    print("*****Lista de Tarefas*****")
    print("1- Adicionar Tarefas. ")
    print("2- Listar Tarefas. ")
    print("3-Concluir Tarefas. ")
    print("4- Sair. ")

    opcao = int(input("Escolha uma opção: "))
   
    if opcao == 1:
        descricao = input("Digite uma tarefa: ")
        adicionar_tarefa(descricao)
        
                                    
    elif opcao == 2:
        print("\nSuas Tarefas:")
        listar_tarefas()
    
    elif opcao == 3:
        input = (int("Digite um numero de tarefas! ")) 
    
    elif opcao == 4:
        print("Saindo do programa...")
       
        break
        
    else:
        print("Opção inválida, tente novamente.")         
