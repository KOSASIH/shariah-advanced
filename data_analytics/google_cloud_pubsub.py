from google.cloud import pubsub

class GoogleCloudPubSub:
    def __init__(self, project_id, topic_name):
        self.publisher = pubsub.PublisherClient()
        self.topic_name = f"projects/{project_id}/topics/{topic_name}"

    def publish_message(self, message):
        self.publisher.publish(self.topic_name, message.encode("utf-8"))

    def create_subscription(self, subscription_name):
        self.publisher.create_subscription(self.topic_name, subscription_name)

    def pull_messages(self, subscription_name):
        subscriber = pubsub.SubscriberClient()
        subscription_path = f"projects/{self.project_id}/subscriptions/{subscription_name}"
        response = subscriber.pull(subscription_path, max_messages=10)
        messages = []
        for msg in response.received_messages:
            messages.append(msg.message.data.decode("utf-8"))
        return messages
