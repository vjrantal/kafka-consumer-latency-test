# kafka-consumer-latency-test

## Introduction

This repository contains code that compares the latency with different amount
of Kafka consumer per consumer group.

## Running

* Create Event Hub with 2 partitions
* Set the following environment variables:
  * BOOTSTRAP_SERVERS=`<event-hub-name>`.servicebus.windows.net:9093
  * SASL_PLAIN_PASSWORD=`<event-hubs-connection-string>`
  * KAFKA_TOPIC_NAME=`<event-hub-name>`
* Run main.py with python >= 3.9
