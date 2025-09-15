from sqlalchemy.orm import Session
from db import get_db
from datetime import datetime
from models import Task, StatusEnum

class TaskService:
  def __init__(self, db: Session):
    self.db = db
    
  def refresh_status(self):
    now = datetime.now()
    tasks = self.db.query(Task).all()
    
    for task in tasks:
      if task.start and now >= task.start and (not task.deadline or now < task.deadline):
        task.status = StatusEnum.pending
      elif task.deadline and now >= task.deadline:
        task.status = StatusEnum.done
      else:
        task.status = StatusEnum.todo
        
    self.db.commit()
    
    
  def add_task(self, title: str, start: datetime, deadline: datetime):
    task = Task(title=title, start=start, deadline=deadline)
    
    self.db.add(task)
    self.db.commit()
    self.db.refresh(task)
    
    return task.to_dict()
    
  def update_task(self, id: int, title: str, start: datetime, deadline: datetime):
    self.refresh_status()
    
    task = self.db.get(Task, id)
    if not task:
      return None
    task.title = title
    task.start = start
    task.deadline = deadline
    
    self.db.commit()
    self.db.refresh(task)
    
    return task.to_dict()
    
  def fetch(self, done: bool):
    self.refresh_status()
    
    if done:     
      tasks = self.db.query(Task).filter(Task.status == StatusEnum.done).all()
    else:
      tasks = self.db.query(Task).all()
    return [task.to_dict() for task in tasks]
    
  def get(self, id: int):
    self.refresh_status()
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