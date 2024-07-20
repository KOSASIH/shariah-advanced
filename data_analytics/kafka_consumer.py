from kafka import KafkaConsumer

class KafkaConsumer:
    def __init__(self, bootstrap_servers, topic):
        self.consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, group_id="shariah-group")
        self.consumer.subscribe([topic])

    def consume(self):
        for message in self.consumer:
            print(message.value.decode("utf-8"))
