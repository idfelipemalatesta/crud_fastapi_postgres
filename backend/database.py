from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://myuser:mypassword@postgres/mydatabase"

# Cria o motor do banco de dados, e o conecta ao banco de dados PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão de banco de dados, é que vai executar as queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos
Base = declarative_base()


# Fecha a sessão do banco de dados após o uso
# Isso garante que a conexão seja liberada corretamente
# e evita vazamentos de recursos.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
