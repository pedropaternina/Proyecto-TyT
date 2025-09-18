from db import db
from sqlalchemy import String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Opciones_pregunta(db.Model):
    __tablename__ = "opciones_pregunta"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_preguntas: Mapped[int] = mapped_column(ForeignKey("preguntas.id"))
    texto_opcion: Mapped[str] = mapped_column(String(250), nullable=False)
    es_correcta: Mapped[bool] =  mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    preguntas: Mapped[list["Preguntas"]] = relationship("Preguntas", back_populates="opciones_pregunta") # type: ignore
    respuestas_usuario_prueba: Mapped[list["Respuestas_usuario_prueba"]] = relationship("Respuestas_usuario_prueba", back_populates="opciones_pregunta") # type: ignore
