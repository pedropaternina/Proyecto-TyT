from db import db
from sqlalchemy import String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Preguntas(db.Model):
    __tablename__ = "preguntas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_tematicas: Mapped[int] = mapped_column(ForeignKey("tematicas.id"))
    enunciado: Mapped[str] = mapped_column(Text, nullable=False)
    context: Mapped[str] = mapped_column(Text, nullable=True)
    context_img: Mapped[str] = mapped_column(String(255), nullable=True) # lo mejor seria pasa un enlace con la imagen, subirla a la base de datos esta hard very hard
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    tematicas: Mapped[list["Tematicas"]] = relationship("Tematicas", back_populates="preguntas") # type: ignore
    opciones_pregunta: Mapped[list["Opciones_pregunta"]] = relationship("Opciones_pregunta", back_populates="preguntas") # type: ignore
    respuestas_usuario_prueba: Mapped[list["Respuestas_usuario_prueba"]] = relationship("Respuestas_usuario_prueba", back_populates="preguntas") # type: ignore