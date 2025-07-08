from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProdutoResponse, ProdutoUpdate, ProdutoCreate
from typing import List
from crud import (
    create_produto,
    get_produtos,
    get_produto,
    delete_produto,
    update_produto,
)

router = APIRouter()


@router.post("/produtos/", response_model=ProdutoResponse)
def create_product_route(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return create_produto(db=db, produto=produto)


@router.get("/produtos/", response_model=List[ProdutoResponse])
def read_all_products_route(db: Session = Depends(get_db)):
    products = get_produtos(db)
    return products


@router.get("/produtos/{produto_id}", response_model=ProdutoResponse)
def read_product_route(produto_id: int, db: Session = Depends(get_db)):
    db_product = get_produto(db, produto_id=produto_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_product


@router.delete("/produtos/{produto_id}", response_model=ProdutoResponse)
def detele_product_route(produto_id: int, db: Session = Depends(get_db)):
    db_product = delete_produto(db, produto_id=produto_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_product


@router.put("/produtos/{produto_id}", response_model=ProdutoResponse)
def update_product_route(
    produto_id: int, produto: ProdutoUpdate, db: Session = Depends(get_db)
):
    db_product = update_produto(db, produto_id=produto_id, produto=produto)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_product