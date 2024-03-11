from gpiozero import Button
from time import sleep
from picamera import PiCamera
from signal import pause
from google.oauth2 import service_account
import vertexai
from vertexai.vision_models import ImageTextModel, Image
from pydub import AudioSegment
from pydub.playback import play 
from google.cloud import texttospeech
SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
SERVICE_ACCOUNT_FILE = 'keys.json'
PROJECT_ID = 'groovy-height-411217' # @param {type:"string"}
LOCATION = 'us-central1'  # @param {type:"string"}

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
vertexai.init(project=PROJECT_ID, location=LOCATION,credentials=credentials,)
model = ImageTextModel.from_pretrained("imagetext@001")
audio_config = texttospeech.AudioConfig(
	    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
	    speaking_rate=1)
print("Initialized")

button2 = Button(2)
button27 = Button(27)
camera=PiCamera()
camera.start_preview(alpha=192)


def getDesc():
	print("Button clicked")
	#camera.capture('pic.jpg')

	source_image = Image.load_from_file(location='./pic.jpg')
	print("Request sent")
	captions = model.get_captions(
	    image=source_image,
	    # Optional:
	    number_of_results=1,
	    language="hi",
	)
	print(captions)
	"""Synthesizes speech from the input string of text."""


	client = texttospeech.TextToSpeechClient(credentials=credentials)

	input_text = texttospeech.SynthesisInput(text=captions[0])

	# Note: the voice can also be specified by name.
	# Names of voices can be retrieved with client.list_voices().
	voice = texttospeech.VoiceSelectionParams(
	    language_code="hi-in",
	    name="hi-IN-Neural2-A",
	)

	audio_config = texttospeech.AudioConfig(
	    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
	    speaking_rate=1
	)

	response = client.synthesize_speech(
	    request={"input": input_text, "voice": voice, "audio_config": audio_config}
	)

	# The response's audio_content is binary.
	with open("output.mp3", "wb") as out:
	    out.write(response.audio_content)
	    print('Audio content written to file "output.mp3"')

	song = AudioSegment.from_wav("output.mp3") 
	play(song)

def getQnA():
	print("Button 27 clicked");
	source_image = Image.load_from_file(location='./pic.jpg');
	answers = model.ask_question(
        image=source_image,
        question="Is the sky black?",
        # Optional parameters
        number_of_results=1,
    )
	print(answers)
	client = texttospeech.TextToSpeechClient(credentials=credentials)

	input_text = texttospeech.SynthesisInput(text=answers[0])

	# Note: the voice can also be specified by name.
	# Names of voices can be retrieved with client.list_voices().
	voice = texttospeech.VoiceSelectionParams(
	    language_code="hi-in",
	    name="hi-IN-Neural2-A",
	)

	response = client.synthesize_speech(
	    request={"input": input_text, "voice": voice, "audio_config": audio_config}
	)

	with open("output.mp3", "wb") as out:
		out.write(response.audio_content)
		print('Audio content written to file "output.mp3"')
	song = AudioSegment.from_wav("output.mp3") 
		play(song)

button2.when_pressed=getDesc
button27.when_pressed=getQnA
pause()
