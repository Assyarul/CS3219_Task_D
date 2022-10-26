from confluent_kafka import Producer
import socket


conf = {'bootstrap.servers' : "localhost:9092,localhost:9093,localhost:9094",
        'client.id': socket.gethostname()}

p = Producer(conf)


if __name__ == "__main__":
    inputstring = ""
    print("Apache Kafka Producer:")
    while inputstring != "exit":
        inputstring = input('>')
        p.produce("test",key="key",value=inputstring)
    
    p.flush()