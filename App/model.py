from App.ext import db


class example(db.Model):
    __tablename__ = "table_name"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(20))


class User(db.Model):
    __tablename__ = "user_table"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))


class Post(db.Model):
    __tablename__ = "user_post"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))


class projectLog(db.Model):
    __tablename__ = "project_log"
    id = db.Column(db.Integer, primary_key=True)
