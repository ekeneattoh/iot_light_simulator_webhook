import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    command = req.params.get("command")
    if not command:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            command = req_body.get("command")

    if command == "on":
        return func.HttpResponse(json.dumps({
            "data": "Door is LOCKED",
            "environment": "Home"
        }))
    elif command == "off":
        return func.HttpResponse(json.dumps({
            "data": "Door is OPENED",
            "environment": "Home"
        }))
    else:
        return func.HttpResponse(
            "Please pass a valid command on/off on the query string or in the request body",
            status_code=400
        )
