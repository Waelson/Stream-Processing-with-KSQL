from dataclasses import asdict, dataclass, field
import json
import time
import random

import requests
from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient, NewTopic
from faker import Faker


faker = Faker()

BROKER_URL = "PLAINTEXT://localhost:29092"
TOPIC_NAME = "com.mywebsite.streams.clickevents"

TOPIC_PAGE = "com.mywebsite.streams.pages"
TOPIC_EVENT = "com.mywebsite.streams.clickevents"


@dataclass
class Page:
    uri: str = field(default_factory=faker.uri)
    description: str = field(default_factory=faker.uri)
    created: str = field(default_factory=faker.iso8601)


@dataclass
class ClickEvent:
    email: str = field(default_factory=faker.email)
    timestamp: str = field(default_factory=faker.iso8601)
    uri: str = field(default_factory=faker.uri)
    number: int = field(default_factory=lambda: random.randint(0, 999))


def produce():
    """Produces data into the Kafka Topic"""
    p = Producer({"bootstrap.servers": BROKER_URL})

    pages = [Page() for _ in range(500)]
    for page in pages:
        p.produce(
            TOPIC_PAGE,
            value=json.dumps(asdict(page)),
            key=page.uri,
        )

    # Now start simulating clickevents for the pages
    while True:
        page = random.choice(pages)
        click = ClickEvent(uri=page.uri)
        json_str = json.dumps(asdict(click))
        p.produce(
            TOPIC_EVENT,
            value=json_str,
            key=click.uri,
        )
        print(f"Message: {json_str}")
        time.sleep(0.1)


def create_topic(client):
    """Creates the topic with the given topic name"""
    client = AdminClient({"bootstrap.servers": BROKER_URL})
    futures = client.create_topics(
        [NewTopic(topic=TOPIC_NAME, num_partitions=5, replication_factor=1)]
    )
    for _, future in futures.items():
        try:
            future.result()
        except Exception as e:
            pass


def main():
    print(f"Starting application")
    """Checks for topic and creates the topic if it does not exist"""
    # create_topic(TOPIC_NAME)
    try:
        produce()
    except KeyboardInterrupt as e:
        print("shutting down")


if __name__ == "__main__":
    main()
