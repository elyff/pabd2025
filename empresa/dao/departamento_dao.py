import sqlite3
from empresa.dao.base_dao import BaseDAO
from empresa.models.departamento import Departamento

class DepartamentoDAO(BaseDAO):
    def __init__(self, db):
        self.db=db; self._ensure()
    def _conn(self): return sqlite3.connect(self.db)
    def _ensure(self):
        c=self._conn(); cur=c.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS departamento(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL)""")
        c.commit(); c.close()
    def create(self, d:Departamento):
        c=self._conn(); cur=c.cursor()
        cur.execute("INSERT INTO departamento(nome) VALUES(?)",(d.nome,))
        c.commit(); d.id=cur.lastrowid; c.close(); return d
    def read(self,id_):
        c=self._conn(); cur=c.cursor()
        cur.execute("SELECT id,nome FROM departamento WHERE id=?",(id_,))
        r=cur.fetchone(); c.close()
        return Departamento(r[0],r[1]) if r else None
    def update(self,d:Departamento):
        c=self._conn(); cur=c.cursor()
        cur.execute("UPDATE departamento SET nome=? WHERE id=?",(d.nome,d.id))
        c.commit(); c.close(); return d
    def delete(self,id_):
        c=self._conn(); cur=c.cursor()
        cur.execute("DELETE FROM departamento WHERE id=?",(id_,))
        c.commit(); c.close()