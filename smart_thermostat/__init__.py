import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    temp = req.params.get('temp')
    if not temp:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            temp = req_body.get('temp')

    if int(temp) >= 1:
        return func.HttpResponse(
            json.dumps({
                "temperature": temp,
                "environment": "Home"

            })
        )
    else:
        return func.HttpResponse(
            "Please pass a valid temp above 0 on the query string or in the request body",
            status_code=400
        )
