lista_tarefas = []

def adicionar_tarefa(descricao):
    tarefa = {
            "descricao" : descricao,
            "concluída" : False
        } 
    
    lista_tarefas.append(tarefa)
    print("tarefa adicinada!")
    
def listar_tarefas():
    for i, tarefa in enumerate(lista_tarefas, 1):
        print(f"{i}. {tarefa['descricao']}")