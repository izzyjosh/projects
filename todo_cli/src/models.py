from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Enum, Date

import enum
from datetime import date
from db import Base

class StatusEnum(enum.Enum):
  pending = "pending"
  done = "done"
  
class Task(Base):
  __tablename__ = "task"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(30))
  status: Mapped[StatusEnum] = mapped_column(Enum(StatusEnum), default=StatusEnum.pending)
  created_at: Mapped[date] = mapped_column(Date, default = date.today)
  deadline: Mapped[date] = mapped_column(Date, nullable=True)
  
  def __repr__(self):
    return f"{self.title} -> {self.status}"
  
  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "status": self.status,
      "created_at": self.created_at.isoformat(),
      "deadline": self.deadline.isoformat() if self.deadline else None
    }
  
  