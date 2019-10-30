import datetime
import random

from flask import request
from flask_restful import Resource, fields, marshal

from App.rest import api, consolelog


class HelloWorld(Resource):
    def get(self):
        # streamlogger.info('logged by current_app.logger')
        # streamlogger.warning('logged by current_app.logger')
        return {'Hello': ' World!'}


api.add_resource(HelloWorld, '/', '/home/', endpoint='todo_ep')


class Insurance(object):
    def __init__(self, insurance_number, insurance_type, amount, user, user_type, adress, insurance_range, date,
                 status):
        self.insurance_number = insurance_number
        self.insurance_type = insurance_type
        self.insurance_range = insurance_range
        self.amount = amount
        self.user = user
        self.user_type = user_type
        self.adress = adress
        self.date = date
        self.status = status

    def __repr__(self):
        return self.insurance_number


Insurance_list = []

for insurance in range(1, 100):
    year = random.randint(2000, 2019)
    month = random.randint(1, 13)
    day = random.randint(1, 29)
    amount = random.randint(0, 100)
    insurance_range = f"{year}-{month}-{day}~{year + 2}-{month}-{day}"
    Insurance_list.append(
        Insurance(insurance_number=insurance, insurance_type=f"出租方案一", insurance_range=insurance_range, amount=amount,
                  user=insurance, user_type=random.randint(1, 4), adress=f"上海市长宁区虹桥路188弄{insurance}号",
                  date=datetime.date.today(),
                  status=random.randint(1, 4)))
Insurance_fields = {
    'insurance_number': fields.Integer(),
    'code': fields.Integer(),
    'message': fields.String(),
    'insurance_type': fields.String(default="出租方案一"),
    'insurance_range': fields.String(default="2017-08-01~2019-08-01"),
    'amount': fields.Integer(),
    'user': fields.Integer(),
    'user_type': fields.Integer(),
    'adress': fields.String(default="未录入"),
    'date': fields.String(),
    'status': fields.Integer()
}


class InsuranceListAPI(Resource):
    def get(self):
        try:
            data = {
                "code": 0,
                "messsage": "success",
                "result": marshal(Insurance_list, Insurance_fields)
                # "result": Insurance_list
            }
            return data
        except:
            consolelog.info("需要处理异常")
            # abort(404)

    def post(self):
        try:
            form_data = request.get_data()
            consolelog.info(form_data)
            Insurance(insurance_number=insurance, insurance_type=f"出租方案一", insurance_range=insurance_range,
                      amount=amount,
                      user=insurance, user_type=random.randint(1, 4), adress=f"上海市长宁区虹桥路188弄{insurance}号",
                      date=datetime.date.today(),
                      status=random.randint(1, 4))
        except:
            pass


api.add_resource(InsuranceListAPI, '/insurance/')

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}



api.add_resource(TodoSimple, '/simeple/<string:todo_id>/', endpoint='todo_sim')

