from flask import request
from flask_restplus import Resource, fields

from App.rest_v2 import swg_api


# from App.ext import api


@swg_api.route('/')
@swg_api.doc(params={'id': 'an Id'})
@swg_api.response(201, "get success")
class HelloWorld(Resource):
    def get(self):
        return "hellow_word"


# api.add_resource(HelloWorld_v2, '/', '/home/', endpoint='todo_ep')

todos = {}
blog_post = swg_api.model('Blog post', {
    'id': fields.Integer(description='The unique identifier of a blog post'),
    'title': fields.String(required=True, description='Article title'),
    'body': fields.String(required=True, description='Article content'),
    'status': fields.String(required=True, enum=['DRAFT', 'PUBLISHED', 'DELETED']),
    'pub_date': fields.DateTime,
})


class TodoSimple_v2(Resource):
    @swg_api.response(201, "get success")
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

    @swg_api.expect(blog_post)
    def post(self):
        return None


swg_api.add_resource(TodoSimple_v2, '/simeple/<string:todo_id>/', endpoint='todo_sim')
