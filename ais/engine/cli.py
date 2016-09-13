import os
import click
import importlib.util

@click.group()
def cli():
    pass

SCRIPT_FOLDER = os.path.join(os.path.dirname(__file__), 'scripts')

class ScriptCli(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        for file_ in os.listdir(SCRIPT_FOLDER):
            file_name, file_ext = os.path.splitext(file_)
            if file_ext != '.py' or file_name == '__init__':
                continue
            commands.append(file_name)
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        script_path = os.path.join(SCRIPT_FOLDER, name + '.py')
        spec = importlib.util.spec_from_file_location(name, script_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        main = mod.main
        return main

script_cli = ScriptCli()
cli.add_command(script_cli, name='run')
