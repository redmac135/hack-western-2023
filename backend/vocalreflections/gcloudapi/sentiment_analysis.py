from google.cloud import language


class SentimentProcessor:
    def __init__(self, text: str):
        self.text = text

    def process(self):
        response = self.analyze_text_sentiment()
        return self.summarize_text_sentiment(response)

    def analyze_text_sentiment(self) -> language.AnalyzeSentimentResponse:
        client = language.LanguageServiceClient()
        document = language.Document(
            content=self.text,
            type_=language.Document.Type.PLAIN_TEXT,
        )
        return client.analyze_sentiment(document=document)

    def summarize_text_sentiment(self, response: language.AnalyzeSentimentResponse):
        sentiment = response.document_sentiment
        return {
            "score": sentiment.score,
            "magnitude": sentiment.magnitude,
            "language": response.language,
        }
