# coding: utf-8
"""
管理文件
"""
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import Node, Load, User, ShortestPath


app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Node=Node, User=User, Load=Load, ShortestPath=ShortestPath)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()