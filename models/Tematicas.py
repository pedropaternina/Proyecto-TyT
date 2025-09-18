from db import db
from datetime import datetime
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Tematicas(db.Model):
    __tablename__ = "tematicas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    nombre_tematica: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    preguntas: Mapped[list["Preguntas"]] = relationship("Preguntas", back_populates="tematicas") # type: ignore
    pruebas: Mapped[list["Pruebas"]] = relationship("Pruebas",back_populates="tematicas") # type: ignore
    