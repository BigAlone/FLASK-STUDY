from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from App import create_app
from App.ext import db
from App.model import User

app = create_app("develop")
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=5000, use_debugger=True))


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)


if __name__ == '__main__':
    manager.run()
