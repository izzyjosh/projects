from sqlalchemy.orm import Session
from db import get_db
from datetime import datetime
from models import Task

class TaskService:
  def __init__(self, db: Session):
    self.db = db
    
  def add_task(self, title: str, deadline: datetime):
    task = Task(title=title, deadline=deadline)
    
    self.db.add(task)
    self.db.commit()
    self.db.refresh(task)
    
    return task.to_dict()
    
  def update_task(self, id: int, title: str, deadline: datetime):
    task = self.db.get(Task, id)
    if not task:
      return None
    task.title = title
    task.deadline = deadline
    
    self.db.commit()
    self.db.refresh(task)
    
    return task.to_dict()
    
  def fetch(self):
    tasks = self.db.query(Task).all()
    return [task.to_dict() for task in tasks]
    
  def get(self, id: int):
    task = self.db.get(Task, id)
    if not task:
      return None
    return task.to_dict()
    
  def delete(self, id: int):
    task = self.db.get(Task, id)
    if not task:
      return None
    self.db.delete(task)
    self.db.commit()
    
    return "task deleted successfully"