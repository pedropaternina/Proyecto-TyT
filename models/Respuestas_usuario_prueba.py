from db import db
from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Respuestas_usuario_prueba(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_pruebas: Mapped[int] = mapped_column(ForeignKey("pruebas"))
    id_preguntas: Mapped[int] = mapped_column(ForeignKey("preguntas"))
    id_opciones_pregunta: Mapped[int] = mapped_column(ForeignKey("opciones_pregunta"))
    es_correcta: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] =  mapped_column(DateTime, default=datetime.utcnow)

    pruebas: Mapped[list["Pruebas"]] = relationship(back_populates="pruebas") # type: ignore
    preguntas: Mapped[list["Preguntas"]] = relationship(back_populates="Preguntas") # type: ignore
    opciones_pregunta: Mapped[list["Opciones_pregunta"]] = relationship(back_populates="opciones_pregunta") # type: ignore
    