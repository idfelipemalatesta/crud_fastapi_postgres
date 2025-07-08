from fastapi import FastAPI
from database import engine
import models
from routes import router


app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(router)