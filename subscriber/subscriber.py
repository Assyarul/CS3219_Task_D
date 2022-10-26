from confluent_kafka import Consumer

conf = {'bootstrap.servers' : "localhost:9092,localhost:9093,localhost:9094",
        'group.id': "test",
        'auto.offset.reset': "smallest"}

c = Consumer(conf)
c.subscribe(["test"])
if __name__ == "__main__":
    print("Apache Kafka Consumer:")
    while 1:
        msg = c.poll(timeout=1.0)
        if msg is None: continue

        else:
            print(msg.value().decode('utf-8'))
    c.close()