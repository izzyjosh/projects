import click
from datetime import datetime
from db import Base, engine, get_db
from service import TaskService

@click.group()
def cli():
  pass
 
Base.metadata.create_all(bind=engine)
  
  
@cli.command("post")
@click.option("--title","-t", prompt=True, help="title of the task", type=str)
@click.option("--deadline", "-dl", prompt=True,     help="Deadline of the task (Format: YYYY-MM-DD)", type=click.DateTime(formats=["%Y-%m-%d"]))
def add(title: str, deadline: datetime):
  
  db = get_db()
  try:
    task_services = TaskService(db)
  
    task = task_services.add_task(title=title, deadline=deadline)
    click.echo(f"{task}")
  finally:
    db.close()
  
 
@cli.command("put")
@click.option("--id", type=int, help="Please always pass the id of the task to be updated")
@click.option("--title", "-t", prompt=True, help="New title",)
@click.option("--deadline", "-dl", prompt=True, help="New deadline (Format: YYYY-MM-DD)", type=click.DateTime(formats=["%Y-%m-%d"]))
def update(id: int, title: str, deadline: datetime):
  
  db = get_db()
  
  try:
    task_services = TaskService(db)
    
    task = task_services.update_task(id=id, title=title, deadline=deadline)
    
    if task is None:
      click.echo("Task does not exist")
    click.echo(f"{task}")
  finally:
    db.close()


@cli.command("del")
@click.option("--id", type=int, help="Id of the task to be deleted")
def delete(id: int):
  
  db = get_db()
  try:
    task_services = TaskService(db)
    
    message = task_services.delete(id=id)
    
    if message is None:
      click.echo("Task does not exist")
    click.echo(f"{message}")
  finally:
    db.close()
  

@cli.command("get")
@click.option("--id", type=int, help="Id of the task to be fetched")
def retriev(id: int):
  
  db = get_db()
  try:
    task_services = TaskService(db)
    
    if id:
      task = task_services.get(id=id)
      
      if task is None:
        click.echo("Task does not exist")
      click.echo(f"{task}")
      
    else:
      task = task_services.fetch()
      click.echo(f"{task}")
  finally:
    db.close()