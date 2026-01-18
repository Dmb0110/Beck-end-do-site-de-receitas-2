from sqlalchemy.orm import Session
from app.models.models_receita import Receita  # seu modelo SQLAlchemy
from app.schemas.schemas_foto import FotoDelete
from app.schemas.schemas import ReceitaOut

class FotoService:
    def __init__(self, db: Session):
        self.db = db

    def adicionar_foto(self, receita_id: int, foto_bytes: bytes) -> ReceitaOut | None:
        receita = self.db.query(Receita).filter(Receita.id == receita_id).first()
        if not receita:
            return None
        receita.foto = foto_bytes
        self.db.commit()
        self.db.refresh(receita)
        return ReceitaOut.model_validate(receita)

    def deletar_foto(self, dados: FotoDelete) -> bool:
        receita = self.db.query(Receita).filter(Receita.id == dados.receita_id).first()
        if not receita:
            return False
        receita.foto = None
        self.db.commit()
        return True
