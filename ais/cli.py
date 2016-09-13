import click
from ais.engine.cli import cli as engine_cli

@click.group()
def cli():
    pass

cli.add_command(engine_cli, name='engine')
