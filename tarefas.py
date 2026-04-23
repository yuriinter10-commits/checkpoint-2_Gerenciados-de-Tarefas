import json
import os

lista_tarefas = []
 
def adicionar_tarefa(descricao):
    tarefa = {
            "descricao" : descricao,
            "concluida" : False
        } 
    lista_tarefas.append(tarefa)
    print("tarefa adicinada!")
    salvar_dados()

def limpar_tela(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_tarefas():
    for i, tarefa in enumerate(lista_tarefas, 0):
        if tarefa['concluida']: 
            print(f"{i}. {tarefa['descricao']} ✅")
        else:
            print(f"{i}. {tarefa['descricao']}⚠️❌")

def concluir_tarefas(indice):
   try:
        if lista_tarefas[indice]['concluida']:
            print("Tarefa ja foi Concluida! ")
        
        else: 
            lista_tarefas[indice]['concluida'] = True
            salvar_dados()
            print("Tarefa Concluida com sucesso! ")
   except IndexError:
       print("Erro:⚠️ indice invalido! tarefa não executada. ")     

def salvar_dados():
    with open("dados.json","w") as arquivo:
        json.dump(lista_tarefas, arquivo)   

def carregar_dados():
    global lista_tarefas  
    try:
        with open("dados.json","r") as arquivo:
            lista_tarefas = json.load(arquivo)  


    except FileNotFoundError:
        print("⚠️Erro ao carregar dados...⚠️")
        lista_tarefas = []

