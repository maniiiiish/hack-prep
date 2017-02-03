import click

@click.command()
def rs():
    click.echo('Starting server')
    from app import app
    app.run()

@click.command()
def ct():
    click.echo('Creating tables')
    from models import db
    from app import db
    db.create_all()

@click.group()
def cli():
    pass

if __name__=='__main__':
    cli.add_command(ct)
    cli.add_command(rs)
    cli()


