import time
import os
from tarefas import adicionar_tarefa, listar_tarefas, carregar_dados, concluir_tarefas, limpar_tela,excluir_tarefa

carregar_dados()

TEMPO = 2

# Cores para deixar o menu elegante
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
CIANO = '\033[96m'
RESET = '\033[0m'

while True:
    limpar_tela()
    print(f"{CIANO}==================================={RESET}")
    print(f"{CIANO}  /// GERENCIADOR DE TAREFAS ///   {RESET}")
    print(f"{CIANO}==================================={RESET}")
    print(f"{VERDE} 1 {RESET}- Adicionar Tarefa")
    print(f"{VERDE} 2 {RESET}- Listar Tarefas")
    print(f"{VERDE} 3 {RESET}- Concluir Tarefa")
    print(f"{VERMELHO} 4 {RESET}- Excluír Tarefa")
    print(f"{VERMELHO} 5 {RESET}- Sair")
    print(f"{CIANO}-----------------------------------{RESET}")
    
    try:
        escolha = input("Escolha uma opção: ")
        
        # Validando se a entrada é vazia para evitar erro visual
        if not escolha:
            continue
            
        opcao = int(escolha)

        if opcao == 1:
            limpar_tela()
            print(f"{AMARELO}>>> NOVA TAREFA <<<{RESET}\n")
            descricao = input("Adicionar Tarefas: ")
            if descricao.strip():
                adicionar_tarefa(descricao)
                print(f"\n{VERDE}Tarefa adicionada com sucesso!{RESET}")
            else:
                print(f"\n{VERMELHO}A descrição não pode estar vazia.{RESET}")
            time.sleep(TEMPO)

        elif opcao == 2: 
            limpar_tela()
            print(f"{AMARELO}>>> SUAS TAREFAS <<<{RESET}")
            listar_tarefas()
            input(f"\n{CIANO}Pressione Enter para voltar ao menu...{RESET}")
            
        elif opcao == 3:
            limpar_tela()
            print(f"{AMARELO}>>> CONCLUIR TAREFA <<<{RESET}\n")
            listar_tarefas()
            try:
                indice = int(input(f"\nDigite o número da tarefa para concluir: "))
                concluir_tarefas(indice)
                print(f"\n{VERDE}Status atualizado!{RESET}")
            except ValueError:
                print(f"\n{VERMELHO}Erro: Digite o número da tarefa.{RESET}")
            time.sleep(TEMPO)
        
        elif opcao == 4:
            limpar_tela()
            print(f"{AMARELO}>>> EXCLUIR TAREFA <<<{RESET}\n")
            listar_tarefas()
            if not listar_tarefas:
                print("\nSua lista está vazia.")
            else:
                try:
                    indice = int(input(f"\nDigite o número da tarefa que deseja APAGAR: "))
                    excluir_tarefa(indice)
                except ValueError:
                    print(f"\n{VERMELHO}Erro: Digite apenas o número da tarefa.{RESET}")
            time.sleep(TEMPO)

        elif opcao == 5:
            limpar_tela()
            print(f"{AMARELO}Salvando dados e saindo... Até logo!{RESET}")
            time.sleep(1)
            break
            
        else:
            print(f"\n{VERMELHO}Opção {opcao} não existe. Tente de 1 a 4.{RESET}")
            time.sleep(TEMPO)

    except ValueError: 
        print(f"\n{VERMELHO}Entrada inválida! Por favor, digite apenas números.{RESET}")
        time.sleep(TEMPO)