from db import db
from sqlalchemy import String, JSON ,Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Pruebas(db.Model):
    __tablename__ = "pruebas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("users.id"))
    id_tematica: Mapped[int] = mapped_column(ForeignKey("tematicas.id"))
    puntuacion: Mapped[int] = mapped_column(Integer, nullable=False)
    seleccion_usuario: Mapped[dict] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    usuario = relationship("Users", back_populates="pruebas") # type: ignore
    tematicas: Mapped[list["Tematicas"]] = relationship("Tematicas", back_populates="pruebas") # type: ignore
    respuestas_usuario_prueba: Mapped[list["Respuestas_usuario_prueba"]] = relationship("Respuestas_usuario_prueba", back_populates="pruebas") # type: ignore

