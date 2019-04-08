from flask import Flask, render_template, current_app
import yaml
import os


app = Flask(__name__)

def update_process(processes):
	context = []
	for process in processes.keys():
		command = 'pgrep -fx "' + processes[process] + '"'
		context.append({'name': process, 'status': os.system(command) != 256})

	return context



def read_yaml():
	with open("process.yaml", 'r') as stream:
		try:
			return yaml.safe_load(stream)
		except yaml.YAMLError:
			print('YAML error')

@app.route('/')
def hello_world():
	return render_template('status.html', services=update_process(read_yaml()))

if __name__ == '__main__':
	global process
	process = read_yaml()
	print(process)
	app.run()
