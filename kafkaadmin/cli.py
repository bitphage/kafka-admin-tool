from pprint import pprint

import click
from kafka.admin import ConfigResource, ConfigResourceType

from kafkaadmin.admin import Admin
from kafkaadmin.options import prefix_option


@click.group()
@click.option("-d", "--debug", default=False, is_flag=True, help="enable debug output")
@click.option(
    "-c", "--config", type=click.File("r"), default="./config.yml", help="specify custom path for config file",
)
@click.pass_context
def main(ctx, debug, config):
    ctx.obj = Admin(config, debug)


@main.command()
@prefix_option
@click.pass_obj
def list_topics(admin, prefix):
    """Display topics, all or matched a prefix."""
    topics_to_show = admin.get_topics_by_prefix(prefix)
    pprint(topics_to_show)


@main.command()
@click.argument("topic")
@click.pass_obj
def describe_topic(admin, topic):
    """Describe a TOPIC."""
    out = admin.admin.describe_topics(topics=[topic])
    pprint(out)


@main.command()
@click.argument("topic")
@click.option("--config_var", help="show specific config variable like retention.ms")
@click.pass_obj
def describe_topic_config(admin, topic, config_var):
    """Show topic config."""
    configs = {}
    if config_var is not None:
        configs = {config_var: True}
    resource = ConfigResource(ConfigResourceType.TOPIC, topic, configs=configs)
    topic_config = admin.admin.describe_configs([resource])
    configuration = topic_config[0].resources[0][4]
    pprint(configuration)


@main.command()
@click.argument("topic")
@click.argument("config_var")
@click.argument("value")
@click.pass_obj
def alter_topic_config(admin, topic, config_var, value):
    """Alter topic config."""
    resource = ConfigResource(ConfigResourceType.TOPIC, topic, configs={config_var: value})
    click.echo(f"setting {config_var}:{value}")
    admin.admin.alter_configs([resource])


@main.command()
@prefix_option
@click.pass_obj
def delete_topics(admin, prefix):
    """Delete all topics starting with prefix."""
    topics = admin.get_topics_by_prefix(prefix)
    click.echo("going to delete following topics:")
    pprint(topics)

    answer = click.prompt("are you sure?", default="n", type=click.Choice(["y", "n"]))
    if answer == "y":
        admin.delete_topics(topics)


if __name__ == "__main__":
    main()