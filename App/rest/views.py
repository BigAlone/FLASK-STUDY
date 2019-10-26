import random
import datetime

from App.rest import api, logger
from flask_restful import Resource, marshal_with, fields, marshal


class HelloWorld(Resource):
    def get(self):
        logger.info('logged by current_app.logger')
        logger.warning('logged by current_app.logger')
        return 'Hello World!'


api.add_resource(HelloWorld, '/', '/home')


class Task(object):
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def __repr__(self):
        return self.title


task_list = []
for task in range(1, 3):
    task_list.append(Task(id=task, title=f"章节{task}", content=f"内容{task}"))
resource_fields = {
    'id': fields.Integer(),
    'title': fields.String(default="未录入"),
    'content': fields.String(default="无内容")
}


class TaskListAPI(Resource):
    @marshal_with(resource_fields)
    # def get(self, task_id):
    #     task = list(filter(lambda t: t.id == task_id, task_list))
    #     print(task)
    #     return abort(404) if len(task) == 0 else task
    def get(self):
        # print(task_list)
        logger.info('this is a test')
        return task_list


api.add_resource(TaskListAPI, '/tasks')


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
    # @marshal_with(Insurance_fields)
    # def get(self, task_id):
    #     task = list(filter(lambda t: t.id == task_id, task_list))
    #     print(task)
    #     return abort(404) if len(task) == 0 else task
    def get(self):
        data = {
            "code": 0,
            "messsage": "success",
            "result": marshal(Insurance_list, Insurance_fields)
            # "result": Insurance_list
        }
        logger.error("this is a error")
        return data


api.add_resource(InsuranceListAPI, '/insurance')
