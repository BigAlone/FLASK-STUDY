from flask import request
from flask_restplus import Resource

from App.rest_v3 import swg_api



@swg_api.route('/')
class HelloWorld_v3(Resource):
    def get(self):
        # streamlogger.info('logged by current_app.logger')
        # streamlogger.warning('logged by current_app.logger')
        return "hellow_word"


# api.add_resource(HelloWorld_v2, '/', '/home/', endpoint='todo_ep')

todos = {}


class TodoSimple_v3(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


swg_api.add_resource(TodoSimple_v3, '/simeple/<string:todo_id>/', endpoint='todo_sim_v3')
