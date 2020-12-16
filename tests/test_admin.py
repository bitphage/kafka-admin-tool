from typing import List, Union

import pytest
from kafka.admin.new_topic import NewTopic

from kafkaadmin.admin import Admin


@pytest.fixture()
def admin(kafka):
    config = {"bootstrap_servers": [f"localhost:{kafka.broker.service_port}"]}
    admin = Admin(config, False)
    return admin


@pytest.fixture()
def create_topic(admin):
    """Factory fixture to create new topics."""

    def _create_topic(topic_names: Union[str, List[str]]) -> None:
        if not isinstance(topic_names, list):
            topic_names = [topic_names]

        new_topics = [NewTopic(name, 1, 1) for name in topic_names]
        admin.admin.create_topics(new_topics)

    return _create_topic


def test_get_topics_by_prefix(admin, create_topic):
    create_topic(["foo-1", "foo-2", "bar-1"])
    topics = admin.get_topics_by_prefix("foo")
    assert set(topics) == {"foo-1", "foo-2"}
