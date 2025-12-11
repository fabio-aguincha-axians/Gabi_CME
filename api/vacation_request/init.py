import azure.functions as func
import azure.durable_functions as df
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(req)
    payload = req.get_json()
    instance_id = client.start_new("vacation_orchestrator", None, payload)

    return func.HttpResponse(
        json.dumps({"instance_id": instance_id}),
        mimetype="application/json"
    )
