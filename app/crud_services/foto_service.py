

from sqlalchemy.orm import Session
from app.models.models_receita import Receita
from app.schemas.schemas_foto import FotoDelete, FotoCreate
from app.schemas.schemas import ReceitaOut
import os
from pathlib import Path

class FotoService:
    def __init__(self, db: Session):
        self.db = db
        # Pasta uploads dentro da pasta app
        self.uploads_dir = Path(__file__).resolve().parent.parent.parent / "uploads"
        #self.uploads_dir = Path(__file__).resolve().parent.parent / "uploads"
        self.uploads_dir.mkdir(exist_ok=True)


        '''
        self.db = db
        # Criar pasta uploads se não existir
        self.uploads_dir = Path(__file__).parent.parent.parent / "uploads"
        self.uploads_dir.mkdir(exist_ok=True)
        '''

    def adicionar_foto(self, receita_id: int, nome_arquivo: str, conteudo_arquivo: bytes) -> ReceitaOut | None:
        """
        Salva a foto no disco e armazena o nome no banco de dados
        """
        receita = self.db.query(Receita).filter(Receita.id == receita_id).first()
        if not receita:
            return None
        
        try:
            # Limpar nome do arquivo (remover caracteres especiais)
            nome_seguro = "".join(c if c.isalnum() or c in "._- " else "_" for c in nome_arquivo)
            nome_seguro = nome_seguro.replace(" ", "-").lower()
            
            # Caminho completo do arquivo
            caminho_arquivo = self.uploads_dir / nome_seguro
            
            # Salvar arquivo no disco
            with open(caminho_arquivo, 'wb') as f:
                f.write(conteudo_arquivo)
            
            # Armazenar apenas o nome do arquivo no banco
            receita.foto = nome_seguro
            self.db.commit()
            self.db.refresh(receita)
            return ReceitaOut.model_validate(receita)
        
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
            return None

    def deletar_foto(self, dados: FotoDelete) -> bool:
        receita = self.db.query(Receita).filter(Receita.id == dados.receita_id).first()
        if not receita:
            return False
        
        try:
            # Deletar arquivo do disco se existir
            if receita.foto:
                caminho_arquivo = self.uploads_dir / receita.foto
                if caminho_arquivo.exists():
                    caminho_arquivo.unlink()
            
            # Limpar referência no banco
            receita.foto = None
            self.db.commit()
            return True
        except Exception as e:
            print(f"Erro ao deletar arquivo: {e}")
            return False

    def obter_foto(self, receita_id: int) -> str | None:
        receita = self.db.query(Receita).filter(Receita.id == receita_id).first()
        if not receita or not receita.foto:
            return None
        return receita.foto



