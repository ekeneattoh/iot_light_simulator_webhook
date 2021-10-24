import logging
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
        return func.HttpResponse({
            "data": {
                "light_status": "Light is ON",
                "environment": "Work"
            }
        })
    elif command == "off":
        return func.HttpResponse({
            "data": "Light is OFF",
            "environment": "Work"
        })
    else:
        return func.HttpResponse(
            "Please pass a valid command on/off on the query string or in the request body",
            status_code=400
        )
