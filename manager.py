#!/usr/bin/env python3

# @FileName : manager.py
# @作者 : Liu
# @日期 : 2019年05月10日
# @时间 : 11时29分
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand, upgrade, migrate
from app import init_app, db

app = init_app('production')
manger = Manager(app)
migrates = Migrate(app, db=db)
manger.add_command('db', MigrateCommand)


@manger.command
def dev():
    from livereload import Server
    liver_server = Server(app.wsgi_app)
    liver_server.watch('**/*.*')
    liver_server.serve(open_url_delay=True)


@manger.command
def test():
    pass


@manger.command
def update_db():
    migrate()
    from app.model import Role
    Role.seed()


@manger.command
def adddata():
    db.drop_all()
    db.create_all()
    from app.model import Role
    Role.seed()
    # migrate()


@manger.command
def deploy():
    from app.model import Role
    upgrade()
    Role.seed()


if __name__ == '__main__':
    manger.run()
