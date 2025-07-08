from sqlalchemy.orm import Session
from schemas import ProdutoUpdate, ProdutoCreate
from models import ProdutoModel

def get_produto(db: Session, produto_id: int):
    """
    Função que recebe um ID de produto e retorna o produto correspondente
    do banco de dados.
    """
    return db.query(ProdutoModel).filter(ProdutoModel.id == produto_id).first()


def get_produtos(db: Session):
    """
    Função que retorna todos os produtos do banco.
    """
    return db.query(ProdutoModel).all()


def create_produto(db: Session, produto: ProdutoCreate):
    """
    Função que recebe um objeto ProdutoCreate e cria um novo produto no banco.
    """
    db_produto = ProdutoModel(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto


def delete_produto(db: Session, produto_id: int):
    """
    Função que recebe um ID de produto e remove o produto correspondente
    """
    db_produto = db.query(ProdutoModel).filter(ProdutoModel.id == produto_id).first()
    db.delete(db_produto)
    db.commit()
    return db_produto


def update_produto(db: Session, produto_id: int, produto: ProdutoUpdate):
    """
    Função que recebe um ID de produto e um objeto ProdutoUpdate e atualiza
    o produto correspondente no banco.
    """
    db_produto = db.query(ProdutoModel).filter(ProdutoModel.id == produto_id).first()
    
    if db_produto is None:
        return None

    if produto.nome is not None:
        db_produto.nome = produto.nome
    if produto.descricao is not None:
        db_produto.descricao = produto.descricao
    if produto.preco is not None:
        db_produto.preco = produto.preco
    if produto.categoria is not None:
        db_produto.categoria = produto.categoria
    if produto.email_fornecedor is not None:
        db_produto.email_fornecedor = produto.email_fornecedor

    """ Alternativamente, você pode usar o seguinte código para atualizar
    # todos os atributos que foram passados no objeto produto, ignorando os não definidos.
    
    for attr, value in produto.model_dump(exclude_unset=True).items():
        setattr(db_produto, attr, value)
    """

    db.commit()
    return db_produto
