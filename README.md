# CS3219_Task_D
 
1. Run `docker-compose -f "docker-compose.yml"  up -d `
2. Wait for all the nodes to be up and running
3. Create a topic called "test" via Kafka Tools (or other means).
4. Ensure your python installation has confluent-kafka library installed.
5. Start up the publisher via `python publisher/publisher.py`
6. Start up the subscriber via `python subscriber/subscriber.py`
7. Any messages typed in publisher will now be displayed in the subscriber, showing the functionalities of the pub-sub.
