from Utils.decorators import http
from Class.response import Response
from Helpers.basic_helper import get_data
from Class.news_class import NewsClass

@http
def create_news(event, context):
    token = event["headers"]["authorization"].split(" ")[1]
    body = get_data(event["body"])
    model = NewsClass(token)
    model.create_news(body)

    return Response("OK")



