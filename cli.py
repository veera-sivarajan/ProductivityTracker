import click

@click.command()
#@click.argument('task', default = 'nothing', type = str)
#@click.argument('time', default = 0, type = float) 
#@click.promt('Enter activity:')
#@click.promt('Enter time spent:')
def cli():
	task = click.prompt('Enter activity:')
	time = click.prompt('Enter time spent:')

	print(task, time)

cli()
