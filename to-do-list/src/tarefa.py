class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def atualizar(self, novo_titulo, nova_descricao):
        self.titulo = novo_titulo
        self.descricao = nova_descricao

    def __repr__(self):
        status = "✅" if self.concluida else "❌"
        return f"{status} {self.titulo} - {self.descricao}"


def filtrar_concluidas(lista_tarefas):
    return [t for t in lista_tarefas if t.concluida]
