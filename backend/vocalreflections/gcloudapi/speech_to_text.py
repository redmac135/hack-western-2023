from google.cloud import speech


class SpeechProcessor:
    def __init__(self, audio: bytes):
        self.audio = audio

    def process(self):
        response = self.speech_to_text(
            config=self.get_config(),
            audio=self.get_audio(),
        )
        # getting best result
        return response.results[0].alternatives[0].transcript

    def speech_to_text(
        config: speech.RecognitionConfig,
        audio: speech.RecognitionAudio,
    ) -> speech.RecognizeResponse:
        client = speech.SpeechClient()

        # Synchronous speech recognition request
        response = client.recognize(config=config, audio=audio)

        return response

    def get_config(self):
        return speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )

    def get_audio(self):
        return speech.RecognitionAudio(content=self.audio)
