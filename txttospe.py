from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from mybot import res
authenticator = IAMAuthenticator('c3DisOV0O-w4Be_K9qB9rrFmVST0VaIyNEnkbVmi9DKP')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/138ae418-d901-436b-a8e3-8369793c9601')

with open('output.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            res,
            voice='en-US_AllisonVoice',
            accept='audio/wav'        
        ).get_result().content)

