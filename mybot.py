#bot user input creation
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from speechtotxt import word
authenticator = IAMAuthenticator('gcx3EhHHs-ajirAWR-8PtUy9457vkppQ1GLOjPPGpw2N')
assistant = AssistantV2(
    version='2020-04-01',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/07ed023e-8467-41f1-a215-e8c04f7d6caa')

response = assistant.message(
    assistant_id='73fa32f9-500e-404a-a9bb-758204ba403d',
    session_id='49d82969-7290-48bc-8d66-4327d6e07ebe',
    input={
        'message_type': 'text',
        'text': word
    }
).get_result()

print(json.dumps(response, indent=2))
res=response["output"]["generic"][0]["text"]
print(res)
