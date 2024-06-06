from Utils.decorators import http
from Class.response import Response
from Helpers.basic_helper import get_data
from Class.users_class import UsersClass
from Class.functions_class import FunctionClass

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

    return Response("OK", data = data)

@http
def create_function(event, context):
    body = get_data(event["body"])
    model = FunctionClass()
    data = model.create_function(body)

    return Response("OK", data = data)

@http
def create_profile(event, context):
    body = get_data(event["body"])
    model = FunctionClass()
    data = model.create_profile(body)

    return Response("OK", data = data)

@http
def create_role_permission(event, context):
    body = get_data(event["body"])
    model = FunctionClass()
    model.create_role_permission(body)

    return Response("OK")

@http
def get_functions(event, context):
    id_ = event["queryStringParameters"]["function_id"] \
            if event["queryStringParameters"] else None
    
    model = FunctionClass()
    data = model.get_functions(id_)

    return Response("OK", data = data)

@http
def get_profile(event, context):
    id_ = event["queryStringParameters"]["id"] \
            if event["queryStringParameters"] else None
    
    model = FunctionClass()
    data = model.get_profile(id_)

    return Response("OK", data = data)

@http
def get_role_permission(event, context):
    id_ = event["queryStringParameters"]["id"] \
            if event["queryStringParameters"] else None
    
    model = FunctionClass()
    data = model.get_role_permission(id_)

    return Response("OK", data = data)