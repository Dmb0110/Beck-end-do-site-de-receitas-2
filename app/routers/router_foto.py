

from fastapi import UploadFile, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.crud_services.foto_service import FotoService
from app.schemas.schemas_foto import FotoCreate, FotoDelete
from app.schemas.schemas import ReceitaOut
'''
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

'''



from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.database.session import get_db
from app.crud_services.foto_service import FotoService
from app.schemas.schemas import ReceitaOut
from app.schemas.schemas_foto import FotoCreate, FotoDelete

router = APIRouter()

@router.post("/enviar/{receita_id}", response_model=ReceitaOut)
async def adicionar_foto(receita_id: int, foto: UploadFile = File(...), db: Session = Depends(get_db)):
    service = FotoService(db)
    # Ler o conteúdo do arquivo
    conteudo_arquivo = await foto.read()
    # Passar nome do arquivo e conteúdo
    receita = service.adicionar_foto(receita_id, foto.filename, conteudo_arquivo)
    if not receita:
        return JSONResponse(status_code=404, content={"erro": "Receita não encontrada"})
    return receita

@router.delete("/deletar", response_model=dict)
def deletar_foto(dados: FotoDelete, db: Session = Depends(get_db)):
    service = FotoService(db)
    ok = service.deletar_foto(dados)
    if not ok:
        return JSONResponse(status_code=404, content={"erro": "Receita não encontrada"})
    return {"mensagem": "Foto removida com sucesso"}

@router.get("/receber/{receita_id}", response_model=dict)
def obter_foto(receita_id: int, db: Session = Depends(get_db)):
    service = FotoService(db)
    foto = service.obter_foto(receita_id)
    if not foto:
        return JSONResponse(status_code=404, content={"erro": "Foto não encontrada"})
    return {"foto": foto}
