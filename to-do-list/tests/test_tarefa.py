from src.tarefa import Tarefa, filtrar_concluidas

def test_criar_tarefa():
    tarefa = Tarefa("Estudar", "Revisar conteúdo de Python")
    assert tarefa.titulo == "Estudar"
    assert not tarefa.concluida

def test_concluir_tarefa():
    tarefa = Tarefa("Exercício", "Fazer teste automatizado")
    tarefa.concluir()
    assert tarefa.concluida is True

def test_atualizar_tarefa():
    tarefa = Tarefa("Antigo", "Descrição antiga")
    tarefa.atualizar("Novo", "Nova descrição")
    assert tarefa.titulo == "Novo"

def test_filtrar_concluidas():
    t1 = Tarefa("A", "Desc"); t2 = Tarefa("B", "Desc")
    t2.concluir()
    lista = [t1, t2]
    filtradas = filtrar_concluidas(lista)
    assert len(filtradas) == 1 and filtradas[0].titulo == "B"
