from google.cloud import speech


class SpeechProcessor:
    def __init__(self, audio_path: bytes):
        print(audio_path)
        with open(audio_path, "rb") as audio_file:
            self.audio = speech.RecognitionAudio(content=audio_file.read())
        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
            sample_rate_hertz=48000,
            language_code="en-US",
        )

    def process(self):
        response = self.speech_to_text()
        # getting best result
        return response.results[0].alternatives[0].transcript

    def speech_to_text(self) -> speech.RecognizeResponse:
        client = speech.SpeechClient()

        # Synchronous speech recognition request
        response = client.recognize(config=self.config, audio=self.audio)

        return response
