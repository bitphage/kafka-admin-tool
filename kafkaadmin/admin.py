import logging
from typing import List, Optional, Set

import yaml
from kafka import KafkaAdminClient, KafkaConsumer

from kafkaadmin.functions import set_debug

log = logging.getLogger(__name__)


class Admin:
    def __init__(self, config: str, debug: bool):
        set_debug(log, debug)
        self.config = yaml.safe_load(config)

        self.admin = KafkaAdminClient(bootstrap_servers=self.config["bootstrap_servers"])
        self.consumer = KafkaConsumer(bootstrap_servers=self.config["bootstrap_servers"])

    def get_topics_by_prefix(self, prefix: Optional[str] = None) -> List[str]:
        """Return all topics matched prefix."""
        all_topics: Set[str] = self.consumer.topics()
        if not prefix:
            return list(all_topics)

        topics: List[str] = [topic for topic in all_topics if topic.startswith(prefix)]
        return topics
