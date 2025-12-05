class Departamento:
    def __init__(self, id_=None, nome=None):
        self.id=id_; self.nome=nome
    def __repr__(self): return f"<Departamento {self.id} {self.nome}>"

class Funcionario:
    def __init__(self, id_=None, nome=None, salario=0.0, departamento_id=None):
        self.id=id_; self.nome=nome
        self.salario=salario; self.departamento_id=departamento_id
    def __repr__(self): return f"<Funcionario {self.id} {self.nome} {self.salario}>"