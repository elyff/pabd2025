import sqlite3
from empresa.dao.base_dao import BaseDAO
from empresa.models.funcionario import Funcionario

class FuncionarioDAO(BaseDAO):
    def __init__(self, db):
        self.db = db
        self._ensure()

    def _conn(self):
        return sqlite3.connect(self.db)

    def _ensure(self):
        c = self._conn()
        cur = c.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS funcionario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                salario REAL NOT NULL,
                departamento_id INTEGER,
                FOREIGN KEY(departamento_id) REFERENCES departamento(id)
            )
        """)
        c.commit()
        c.close()

    # ========= OBRIGATÓRIOS DO BaseDAO =========

    # Converte objeto → dicionário
    def to_dict(self, f: Funcionario):
        return {
            "id": f.id,
            "nome": f.nome,
            "salario": f.salario,
            "departamento_id": f.departamento_id
        }

    # Converte dicionário → objeto
    def to_model(self, row):
        return Funcionario(
            id=row[0],
            nome=row[1],
            salario=row[2],
            departamento_id=row[3]
        )

    # =============== CRUD ===============

    def create(self, f: Funcionario):
        c = self._conn()
        cur = c.cursor()
        cur.execute("INSERT INTO funcionario (nome, salario, departamento_id) VALUES (?, ?, ?)",
                    (f.nome, f.salario, f.departamento_id))
        c.commit()
        f.id = cur.lastrowid
        c.close()
        return f

    def read(self, id_):
        c = self._conn()
        cur = c.cursor()
        cur.execute("SELECT id, nome, salario, departamento_id FROM funcionario WHERE id=?", (id_,))
        row = cur.fetchone()
        c.close()
        return self.to_model(row) if row else None

    def update(self, f: Funcionario):
        c = self._conn()
        cur = c.cursor()
        cur.execute("UPDATE funcionario SET nome=?, salario=?, departamento_id=? WHERE id=?",
                    (f.nome, f.salario, f.departamento_id, f.id))
        c.commit()
        c.close()
        return f

    def delete(self, id_):
        c = self._conn()
        cur = c.cursor()
        cur.execute("DELETE FROM funcionario WHERE id=?", (id_,))
        c.commit()
        c.close()