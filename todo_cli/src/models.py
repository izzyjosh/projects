from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Enum, DateTime

import enum
from datetime import datetime
from db import Base

class StatusEnum(enum.Enum):
  todo = "todo"
  pending = "pending"
  done = "done"
  
class Task(Base):
  __tablename__ = "task"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(30))
  status: Mapped[StatusEnum] = mapped_column(Enum(StatusEnum), default=StatusEnum.todo)
  start: Mapped[datetime] = mapped_column(DateTime)
  created_at: Mapped[datetime] = mapped_column(DateTime, default = datetime.now())
  deadline: Mapped[datetime] = mapped_column(DateTime, nullable=True)
  
  def __repr__(self):
    return f"{self.title} -> {self.status}"
  
  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "status": self.status.value,
      "start_date": self.start.strftime("%Y-%m-%d %H:%M"),
      "created_at": self.created_at.strftime("%Y-%m-%d %H:%M"),
      "deadline": self.deadline.strftime("%Y-%m-%d %H:%M") if self.deadline else None
    }
  
  
