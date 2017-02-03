import click

@click.command()
@click.option(help='Start flask server')
def rs():
    click.echo('Starting server')
    from app import app
    app.run()

@click.command()
@click.option(help='Create tables in database')
def ct():
    click.echo('Creating tables')
    import models

@click.group()
def cli():
    pass

if __name__=='__main__':
    cli.add_command(ct)
    cli.add_command(rs)


