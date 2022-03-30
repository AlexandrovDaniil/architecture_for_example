import json
import falcon



class MyException(Exception):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("Error Head", "Error")
        resp.status = falcon.HTTP_502
        resp.body = json.dumps({"message": "My custom error"})
