import os
from dotenv import load_dotenv

load_dotenv()            # Carrega as variáveis definidas no arquivo .env para o ambiente do sistema

class Settings:          # Define uma classe chamada 'Settings' para centralizar configurações do projeto

    DATABASE_URL: str = os.getenv('DATABASE_URL')  
    # Cria um atributo chamado 'DATABASE_URL' e atribui o valor da variável de ambiente 'DATABASE_URL'.
    # O ': str' é uma anotação de tipo, indicando que o valor esperado é uma string.
    
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'sua_chave_secreta_deve_estar_em_env')
    # Chave secreta para assinar tokens JWT. Em produção, deve estar em variável de ambiente segura.
    
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'production')
    # Define se está em desenvolvimento ou produção

    def __init__(self):
        if not self.DATABASE_URL:
            raise ValueError(
                "❌ DATABASE_URL não está configurada!\n"
                "Crie um arquivo .env na raiz do projeto com:\n"
                "DATABASE_URL=sua_url_postgresql_aqui\n"
                "SECRET_KEY=sua_chave_secreta_aqui\n"
                "\nPara diagnosticar, execute: python diagnose.py"
            )
        if self.SECRET_KEY == 'sua_chave_secreta_deve_estar_em_env':
            raise ValueError(
                "❌ SECRET_KEY não está configurada ou é o valor padrão!\n"
                "Edite o arquivo .env e defina uma chave segura.\n"
                "\nPara diagnosticar, execute: python diagnose.py"
            )

settings = Settings()    # Instancia a classe 'Settings', criando um objeto com as configurações carregadas
