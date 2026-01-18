from fastapi import UploadFile, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.crud_services.foto_service import FotoService
from app.schemas.schemas_foto import FotoCreate, FotoDelete
from app.schemas.schemas import ReceitaOut

router = APIRouter()

# Rota para adicionar foto
@router.post(
        "/criar/{receita_id}", 
        response_model=ReceitaOut
    )
async def adicionar_foto(receita_id: int, foto: UploadFile, db: Session = Depends(get_db)):
    service = FotoService(db)
    foto_bytes = await foto.read()  # lê o arquivo como binário
    receita = service.adicionar_foto(receita_id, foto_bytes)
    if not receita:
        return {"erro": "Receita não encontrada"}
    return receita

# Rota para deletar foto
@router.delete(
        "/deletar"
    )
def deletar_foto(dados: FotoDelete, db: Session = Depends(get_db)):
    service = FotoService(db)
    ok = service.deletar_foto(dados)
    if not ok:
        return {"erro": "Receita não encontrada"}
    return {"mensagem": "Foto removida com sucesso"}
