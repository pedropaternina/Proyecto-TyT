from db import db
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Pruebas(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("users.id"))
    id_tematica: Mapped[int] = mapped_column(ForeignKey("tematicas.id"))
    puntuacion: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    users: Mapped[list["Users"]] = relationship(back_populates="users") # type: ignore
    tematicas: Mapped[list["Tematicas"]] = relationship(back_populates="tematicas") # type: ignore
    respuestas_usuario_prueba: Mapped[list["Respuestas_usuario_prueba"]] = relationship(back_populates="respuestas_usuario_prueba") # type: ignore

