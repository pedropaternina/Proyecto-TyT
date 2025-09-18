from db import db
from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Respuestas_usuario_prueba(db.Model):
    __tablename__ = "respuestas_usuario_prueba"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_pruebas: Mapped[int] = mapped_column(ForeignKey("pruebas.id"))
    id_preguntas: Mapped[int] = mapped_column(ForeignKey("preguntas.id"))
    id_opciones_pregunta: Mapped[int] = mapped_column(ForeignKey("opciones_pregunta.id"))
    es_correcta: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] =  mapped_column(DateTime, default=datetime.utcnow)

    pruebas: Mapped[list["Pruebas"]] = relationship("Pruebas",back_populates="respuestas_usuario_prueba") # type: ignore
    preguntas: Mapped[list["Preguntas"]] = relationship("Preguntas", back_populates="respuestas_usuario_prueba") # type: ignore
    opciones_pregunta: Mapped[list["Opciones_pregunta"]] = relationship("Opciones_pregunta", back_populates="respuestas_usuario_prueba") # type: ignore
    