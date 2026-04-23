import time 
import os

from tarefas import adicionar_tarefa, listar_tarefas,carregar_dados,concluir_tarefas, limpar_tela

carregar_dados()
limpar_tela()

TEMPO = 3

while True:
    limpar_tela()
    print("=====GERENCIADOR DE TAREFAS=====")
    print("1- Adicionar Tarefas. ")
    print("______________________")
    print("2- Listar Tarefas. ")
    print("______________________")
    print("3-Concluir Tarefas. ")
    print("______________________")
    print("4- Sair. ")
    
    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            limpar_tela()
            descricao = input("Digite uma tarefa: ")
            adicionar_tarefa(descricao)
            time.sleep(TEMPO)

        elif opcao == 2: 
            
            limpar_tela()
            print("\nSuas Tarefas:")
            listar_tarefas()
            time.sleep(TEMPO)
            
        elif opcao == 3:
            limpar_tela()
            listar_tarefas()
            tarefa = int(input("Qual tarefa deseja concluir? "))
            concluir_tarefas(tarefa) 

            time.sleep(TEMPO)
    
        elif opcao == 4:
            limpar_tela()
            time.sleep(TEMPO)
            print("Saindo do programa...")
            break
            
        else:
            limpar_tela()
            time.sleep(TEMPO)
            print("Opção inválida, tente novamente.")         

    except ValueError: 
        print("Erro: Digite apenas numeros")
        time.sleep(TEMPO)