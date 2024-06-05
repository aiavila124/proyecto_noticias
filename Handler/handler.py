from Utils.decorators import http
from Class.response import Response
from Helpers.basic_helper import get_data
from Class.users_class import UsersClass

@http
def create_user(event, context):
    body = get_data(event["body"])
    model = UsersClass()
    model.create_user(body)

    return Response("OK")

@http
def get_filter_users(event, context):
    body = get_data(event["body"])
    model = UsersClass()
    data = model.get_filter_users(body)
    return Response("OK", data = data)

@http
def get_token(event, context):
    body = get_data(event["body"])
    model = UsersClass()
    data = model.get_token(body)

    print("aaa", data)
    return Response("OK", data = data)

