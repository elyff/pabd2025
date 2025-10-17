import os
from supabase import create_client, Client
from dotenv import load_dotenv

#carrega as variaveis de ambiente 
load_dotenv()

class SupabaseConnection:

#Padrao de projeto - Singleton
# Garante que uma classe tenha apenas uma instancia  em toda a aplicação.'''

    _instance = None
    #Type hint
    #Garante o tipo de dado a ser atribuido a um atributo
    _client: Client = None

    #new - cria uma nova instancia da classe
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SupabaseConnection, cls).__new__(cls)
            cls._instance._init_connection()
        return cls._instance
    
    def _init_connection(self):
    supabase_url=os.getenv("SUPABASE_URL")
    supabase_key=os.getenv("SUPABASE_KEY")

    if not supabase_url or not supabase_key:
        raise ValueError("Erro nas variaveis de ambiente.")

    self._client = create_client(supabase_url, supabase_key)
    print("Conexao com o Supabase ✅! ")

    @property
    def client(self) -> Client: # Type hint
        return self._client
    

