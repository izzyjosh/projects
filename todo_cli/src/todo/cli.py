import click
from rich.console import Console
from rich.table import Table
from rich import print_json
from datetime import datetime
from db import Base, engine, get_db
from service import TaskService

console = Console()

# Setting up table for my task manager
table = Table(title="CLI Task Manager")

table.add_column("id", justify="center")
table.add_column("start date", justify="center", style="cyan")
table.add_column("title", style="magenta")
table.add_column("status", style="green")
table.add_column("deadline", style="red")

@click.group(help="A CLI Task Manager to add, update, fetch, and delete tasks.")
def cli():
    pass
 
Base.metadata.create_all(bind=engine)
  
  
@cli.command("post", help="Create or add a new task")
@click.option("--title","-t", prompt=True, help="title of the task", type=str)
@click.option("--start", "-s", prompt=True,     help="Start date of the task (Format: YYYY-MM-DD HH:MM)", type=click.DateTime(formats=["%Y-%m-%d %H:%M"]))
@click.option("--deadline", "-dl", prompt=True,     help="Deadline of the task (Format: YYYY-MM-DD HH:MM)", type=click.DateTime(formats=["%Y-%m-%d %H:%M"]))
def add(title: str, start: datetime, deadline: datetime):
  
  db = get_db()
  try:
    task_services = TaskService(db)
  
    task = task_services.add_task(title=title, start=start, deadline=deadline)
    print_json(data=task)
    
  finally:
    db.close()
  
 
@cli.command("put", help="Update an existing task")
@click.option("--id", type=int, help="Please always pass the id of the task to be updated")
@click.option("--title", "-t", prompt=True, help="New title",)
@click.option("--start", "-s", prompt=True,     help="Start date of the task (Format: YYYY-MM-DD HH:MM)", type=click.DateTime(formats=["%Y-%m-%d %H:%M"]))
@click.option("--deadline", "-dl", prompt=True, help="New deadline (Format: YYYY-MM-DD HH:MM)", type=click.DateTime(formats=["%Y-%m-%d %H:%M"]))
def update(id: int, title: str,start: datetime, deadline: datetime):
  
  db = get_db()
  
  try:
    task_services = TaskService(db)
    
    task = task_services.update_task(id=id, title=title, start=start, deadline=deadline)
    
    if task is None:
      click.echo("Task does not exist")
    print_json(data=task)
    
  finally:
    db.close()


@cli.command("del", help="Delete a task by Id")
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
  

@cli.command("get", help="Get a particular task by Id and also get all task")
@click.option("--id", type=int, help="Id of the task to be fetched")
@click.option("--done/--not-done", default=False)
def retrieve(id: int, done: bool):
  
  db = get_db()
  try:
    task_services = TaskService(db)
    
    if id:
      task = task_services.get(id=id)
      table.add_row(f"{task['id']}", f"{task['start_date']}", f"{task['title']}", f"{task['status']}", f"{task['deadline']}")
      console.print(table)
      
      if task is None:
        click.echo("Task does not exist")
        
      
    else:
      tasks = task_services.fetch(done=done)
      for task in tasks:
        table.add_row(f"{task['id']}", f"{task['start_date']}", f"{task['title']}", f"{task['status']}", f"{task['deadline']}")
      console.print(table)
  
  finally:
    db.close()