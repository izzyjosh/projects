import click
from datetime import datetime

@click.group()
def cli():
  pass
  
@cli.command()
@click.option("--title","-t", help="title of the task", type=str)
@click.option("--dead-line", "-dl", help="Deadline of the task (Format: YYYY-MM-DD)", type=click.DateTime(formats=["%Y-%m-%d"]))
def add(title: str, dead_line: datetime):
  pass
  
 
@cli.commamd()
@click.option("--title", "-t", help="New title",)
@click.option("--deadline", "-dl", help="New deadline (Format: YYYY-MM-DD)", type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option("")
def update(title: str, dead_line: datetime):
  pass