import click
from fileman.command import (create, remove, rename, del_file, create_file)

@click.group()
def cli() -> None:
    """
    DESCRIPTION: This is a file manager command line app. It performs various functions which can be accessed from the help function.
    """
    pass

# Define all sub commands here
@cli.command(name="mkdir")
@click.argument("name", nargs=-1)
def mkdir(name: str) -> None:
    """Make a new directory"""
    create(name)


@cli.command(name="rmdir")
@click.argument("name")
def rmdir(name: str) -> None:
    """Remove an existing directory"""
    remove(name)


@cli.command(name="mv")
@click.argument("src")
@click.argument("dst")
def move(src, dst) -> None:
    """Move a file or directory to another path"""
    rename(src, dst)


@cli.command(name="del")
@click.argument("filename")
def delete(filename) -> None:
    """Delete a file or directory"""
    del_file(filename)

@cli.command(name="search")
def search() -> None:
    """Search for a particular file or directory if it exist"""
    pass

@cli.command(name="touch")
@click.argument("filename")
def touch(filename) -> None:
    """Create a new file in the current directory"""
    create_file(filename)

