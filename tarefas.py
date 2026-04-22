import json

lista_tarefas = []

def adicionar_tarefa(descricao):
    tarefa = {
            "descricao" : descricao,
            "concluida" : False
        } 
    
    lista_tarefas.append(tarefa)
    print("tarefa adicinada!")
    
def listar_tarefas():
    for i, tarefa in enumerate(lista_tarefas, 0):
        if tarefa['concluida']: 
            print(f"{i}. {tarefa['descricao']} ✅")
        else:
            print(f"{i}. {tarefa['descricao']}⚠️❌")

def concluir_tarefas(indice):
   try:
        lista_tarefas[indice]['concluida'] = True
        salvar_dados()
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

