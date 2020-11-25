# Streaming Processing with KSQL

This project show how to use KSQL (Streaming SQL Engine for Apache Kafka)

## Enviroment

For you to use this repository you will need the following softwares:

- [Python](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/engine/install/)
- Zookeeper
- Kafka
- KSQL Server

However, only Docker and Docker Compose need is installed in your machine. All Kafka ecosystem will be embedded via docker images.

## Steps

1. Install Python and Pip
2. Install Docker and Docker Compose
3. Load Images
4. Create Topics
5. Start Simulator

### 1 - Install Python and Pip

The installation process of the Python and Pip is very easy, so this tutorial dont't will cover this steps. I recommend you look for more information in [www.python.org](https://www.python.org/downloads/) and [pip.pypa.io](https://pip.pypa.io/en/stable/installing/).

### 2 - Install Docker and Docker Compose

This tutorial does not demonstrate the installation process for Docker and Docker Compose. I strongly recommend you to visit the Docker installation link for more informations. [Please click here](https://docs.docker.com/engine/install/).

### 3 - Loading Images

```bash
docker-compose up
```

or

```bash
docker-compose up -d
```

The last command allow you to run <code>docker-compose</code> in the background.

### 4 - Create Topics

```bash
docker-compose exec kafka kafka-topics --create --topic com.mywebsite.streams.pages --bootstrap-server localhost:9092
```

```bash
docker-compose exec kafka kafka-topics --create --topic com.udacity.streams.clickevents --bootstrap-server localhost:9092
```

### 5 - Start Simulator

```bash
python click_simulator.py
```

## Connecting to KSQL Server

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

 Kafka Topic                       | Partitions | Partition Replicas
---------------------------------------------------------------------
 com.mywebsite.streams.clickevents | 5          | 1
 com.mywebsite.streams.pages       | 1          | 1
---------------------------------------------------------------------
```

Show all streams

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
