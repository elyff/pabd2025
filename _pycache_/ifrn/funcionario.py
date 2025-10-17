class funcionario(pessoa):
    def __init__(self, nome, cpf, siape):
        super().__init__(nome, idade)
        self.sia

    def mostrar_dados(self):
        dados_pessoa = super().mostrar_dados()
        return f"{dados_pessoa}, Salário: {self.salario}"
    