#Speech To Text 
import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('VIHZWLSfwy4ysLXTbGDvBXjM0wexJ8hbV76lxcRRhukA')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/75456471-35c6-4f8d-83f7-77634afd496c')
#if my file isin another location ,provide the entire path with rawinput r
with open(join(dirname(__file__), './.', 'temperature.wav'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/wav'
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))
word=speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
print(word)


#BotSession creation
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('gcx3EhHHs-ajirAWR-8PtUy9457vkppQ1GLOjPPGpw2N')
assistant = AssistantV2(
    version='2020-04-01',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/07ed023e-8467-41f1-a215-e8c04f7d6caa')

response = assistant.create_session(
    assistant_id='73fa32f9-500e-404a-a9bb-758204ba403d'
).get_result()

sessionid=json.dumps(response, indent=2)
print(sessionid)

#Bot user input creation
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('gcx3EhHHs-ajirAWR-8PtUy9457vkppQ1GLOjPPGpw2N')
assistant = AssistantV2(
    version='2020-04-01',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/07ed023e-8467-41f1-a215-e8c04f7d6caa')

response = assistant.message(
    assistant_id='73fa32f9-500e-404a-a9bb-758204ba403d',
    session_id=str(sessionid[19:-3]),
    input={
        'message_type': 'text',
        'text': word
    }
).get_result()

print(json.dumps(response, indent=2))
res=response["output"]["generic"][0]["text"]
print(res)

#Text To Speech
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('c3DisOV0O-w4Be_K9qB9rrFmVST0VaIyNEnkbVmi9DKP')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/138ae418-d901-436b-a8e3-8369793c9601')

with open('output2.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            res,
            voice='en-US_AllisonVoice',
            accept='audio/wav'        
        ).get_result().content)

