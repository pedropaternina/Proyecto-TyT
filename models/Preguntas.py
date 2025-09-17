from db import db
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Preguntas(db.Model):
    __tablename__ = "preguntas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_tematicas: Mapped[int] = mapped_column(ForeignKey("tematicas.id"))
    enunciado: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    tematicas: Mapped[list["Tematicas"]] = relationship(back_populates="preguntas") # type: ignore
    opciones_pregunta: Mapped[list["Opciones_pregunta"]] = relationship(back_populates="opciones_pregunta") # type: ignore
    respuestas_usuario_prueba: Mapped[list["Respuestas_usuario_prueba"]] = relationship(back_populates="respuestas_usuario_prueba") # type: ignore