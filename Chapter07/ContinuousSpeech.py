import azure.cognitiveservices.speech as speechsdk
import time

speech_key, service_region = "9a0fbf205ecb407abe0ba8c7d86cb1ab", "westus2"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
speech_recognizer.session_stopped.connect(lambda evt: print('\nSESSION STOPPED {}'.format(evt)))
speech_recognizer.recognized.connect(lambda evt: print('\n{}'.format(evt.result.text)))
print('Say a few words')
try:
    while True:
        speech_recognizer.start_continuous_recognition()
        time.sleep(10)
        speech_recognizer.stop_continuous_recognition()
except KeyboardInterrupt:
        speech_recognizer.session_started.disconnect_all()
        speech_recognizer.recognized.disconnect_all()
        speech_recognizer.session_stopped.disconnect_all()
