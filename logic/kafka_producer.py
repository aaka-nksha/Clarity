import json
try:
    from kafka import KafkaProducer
except ImportError:
    KafkaProducer = None

class ClarityProducer:
    def __init__(self, bootstrap_servers=['localhost:9092']):
        if KafkaProducer:
            try:
                self.producer = KafkaProducer(
                    bootstrap_servers=bootstrap_servers,
                    value_serializer=lambda v: json.dumps(v).encode('utf-8')
                )
            except Exception:
                self.producer = None
        else:
            self.producer = None

    def send_event(self, topic, data):
        """
        Streams events to Kafka for real-time processing.
        """
        if self.producer:
            self.producer.send(topic, data)
            self.producer.flush()
        else:
            print(f"Bypassing Kafka: {data}")
