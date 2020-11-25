# Streaming Processing with KSQL

This project show how to use KSQL (Streaming SQL Engine for Apache Kafka)

## Enviroment

For you to use this repository you will need the following softwares:

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/engine/install/)
- Zookeeper
- Kafka
- KSQL Server

However, only Docker and Docker Compose need is installed in your machine. All Kafka ecosystem will be embedded via docker images.

## Steps

- Install Docker and Docker Compose
- Load Images
- Create Topics
- Start Simulator

## Install Docker and Docker Compose

This tutorial does not demonstrate the installation process for Docker and Docker Compose. I strongly recommend you to visit the Docker installation link for more informations. [Please click here](https://docs.docker.com/engine/install/).

## Loading Images

```bash
docker-compose up
```

or

```bash
docker-compose up -d
```

## First Interactions

In this tutorial you will be interacting with Kafka software ecosystem ever through 'docker-compose'.

### Creating a Kafka Topic

```bash
docker-compose exec kafka kafka-topics --create --topic com.mywebsite.streams.clickevents --bootstrap-server localhost:9092
```

### Connecting to KSQL Server

```bash
docker-compose exec ksql ksql http://localhost:8088
```

After you connect to KSQL Server you will see below image:

```bash
                  ===========================================
                  =        _  __ _____  ____  _             =
                  =       | |/ // ____|/ __ \| |            =
                  =       | ' /| (___ | |  | | |            =
                  =       |  <  \___ \| |  | | |            =
                  =       | . \ ____) | |__| | |____        =
                  =       |_|\_\_____/ \___\_\______|       =
                  =                                         =
                  =  Streaming SQL Engine for Apache Kafka® =
                  ===========================================

Copyright 2017-2019 Confluent Inc.

CLI v5.4.1, Server v5.4.1 located at http://localhost:8088

Having trouble? Type 'help' (case-insensitive) for a rundown of how things work!

ksql>
```

#### Some Commands

Show all topics

```bash
ksql> SHOW TOPICS;

 Kafka Topic                     | Partitions | Partition Replicas
-------------------------------------------------------------------
 com.mywebsite.streams.clickevents | 1          | 1
-------------------------------------------------------------------
```

Show all streams;

```bash
ksql> SHOW STREAMS;

 Stream Name | Kafka Topic                     | Format
--------------------------------------------------------
 CLICKEVENTS | com.mywebsite.streams.clickevents | JSON
--------------------------------------------------------
```

### Creating a Stream

If you need run it in the background mode.

```bash
CREATE STREAM clickevents
  (email VARCHAR,
  timestamp VARCHAR,
  uri VARCHAR,
  number INTEGER)
WITH (KAFKA_TOPIC='com.mywebsite.streams.clickevents',
  VALUE_FORMAT='JSON');
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
