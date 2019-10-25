from flask_migrate import MigrateCommand
from App import create_app
from flask_script import Manager, Server

app = create_app("develop")
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=5000, use_debugger=True))

if __name__ == '__main__':
    manager.run()
