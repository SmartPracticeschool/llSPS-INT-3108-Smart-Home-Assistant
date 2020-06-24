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
with open(join(dirname(__file__), './.', 'BotAssistent.wav'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/wav'
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))
word=speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
print(word)
