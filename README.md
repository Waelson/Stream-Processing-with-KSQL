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

After you install Python and Pip run the command below to install all dependencies need to execute <code>click_simulator.py</code>.

```bash
pip install -r requirements.txt
```

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

If you executed all steps correctly. You will see an image similar that below.

```bash
Starting application
Message: {"email": "anoble@yahoo.com", "timestamp": "1986-03-10T16:38:40", "uri": "https://mitchell.info/login.php", "number": 358}
Message: {"email": "leonardpatrick@mason-clark.info", "timestamp": "1971-04-25T10:09:26", "uri": "https://www.bailey.com/search/about/", "number": 431}
Message: {"email": "morriskatie@villarreal-villa.biz", "timestamp": "1996-11-22T00:12:20", "uri": "http://www.woodard.info/terms.php", "number": 838}
Message: {"email": "kenneth79@rogers.info", "timestamp": "2005-10-24T22:16:59", "uri": "http://www.king.com/wp-content/blog/blog/index/", "number": 793}
Message: {"email": "wbailey@wu-martinez.net", "timestamp": "1995-06-20T12:44:44", "uri": "https://www.smith-neal.com/categories/login/", "number": 509}
Message: {"email": "tkennedy@hall-wolfe.org", "timestamp": "2009-01-27T14:04:20", "uri": "https://www.marshall-holmes.info/", "number": 336}
Message: {"email": "steven15@yahoo.com", "timestamp": "2019-12-13T16:09:11", "uri": "https://www.sims.net/main.html", "number": 263}
Message: {"email": "hobbsmario@hotmail.com", "timestamp": "1990-08-16T05:09:04", "uri": "http://www.smith.com/search/tags/explore/about.jsp", "number": 61}
...
```

## Connecting to KSQL Server

```bash
docker-compose exec ksql ksql http://localhost:8088
```

After you connect to KSQL Server you will see the image below:

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
