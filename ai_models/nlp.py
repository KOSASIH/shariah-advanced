import spacy
from transformers import BertTokenizer, BertModel

class NLP:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.model = BertModel.from_pretrained("bert-base-uncased")

    def process_text(self, text):
        doc = self.nlp(text)
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        return entities

    def sentiment_analysis(self, text):
        inputs = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=512,
            return_attention_mask=True,
            return_tensors="pt",
        )
        outputs = self.model(inputs["input_ids"], attention_mask=inputs["attention_mask"])
        sentiment = torch.nn.functional.softmax(outputs.last_hidden_state[:, 0, :], dim=1)
        return sentiment

    def topic_modeling(self, texts):
        topics = []
        for text in texts:
            inputs = self.tokenizer.encode_plus(
                text,
                add_special_tokens=True,
                max_length=512,
                return_attention_mask=True,
                return_tensors="pt",
            )
            outputs = self.model(inputs["input_ids"], attention_mask=inputs["attention_mask"])
            topic = torch.nn.functional.softmax(outputs.last_hidden_state[:, 0, :], dim=1)
            topics.append(topic)
        return topics
