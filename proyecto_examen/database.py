from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///vehiculos.db")

def inicializar_bd():
    SQLModel.metadata.create_all(engine)