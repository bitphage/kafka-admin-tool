#!/usr/bin/env python

from pprint import pprint
from typing import Set

import click
from kafka import KafkaAdminClient, KafkaConsumer

from kafkaadmin.functions import config_option, logging_option


@click.command()
@config_option
@logging_option
@click.argument("topic_prefix")
@click.pass_context
def main(ctx, topic_prefix):
    """Delete all topics starting with prefix."""
    consumer = KafkaConsumer(bootstrap_servers=ctx.config["bootstrap_servers"])
    admin = KafkaAdminClient(bootstrap_servers=ctx.config["bootstrap_servers"])
    topics: Set[str] = consumer.topics()
    topics_to_delete = []
    for topic in topics:
        if topic.startswith(topic_prefix):
            topics_to_delete.append(topic)

    print("going to delete following topics:")
    pprint(topics_to_delete)
    answer = click.prompt("are you sure?", default="n", type=click.Choice(["y", "n"]))
    if answer == "y":
        admin.delete_topics(topics_to_delete)


if __name__ == "__main__":
    main()
