import logging
from typing import List, Optional, Set

import yaml
from kafka import KafkaAdminClient, KafkaConsumer

log = logging.getLogger(__name__)


class Admin:
    def __init__(self, config: str, debug: bool):
        self.set_debug(debug)
        self.config = yaml.safe_load(config)

        self.admin = KafkaAdminClient(bootstrap_servers=self.config["bootstrap_servers"])
        self.consumer = KafkaConsumer(bootstrap_servers=self.config["bootstrap_servers"])

    @staticmethod
    def set_debug(debug: bool) -> None:
        if debug is True:
            log.setLevel(logging.DEBUG)
        else:
            log.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        log.addHandler(handler)

    def get_topics_by_prefix(self, prefix: Optional[str] = None) -> List[str]:
        """Return all topics matched prefix."""
        all_topics: Set[str] = self.consumer.topics()
        if not prefix:
            return list(all_topics)

        topics: List[str] = [topic for topic in all_topics if topic.startswith(prefix)]
        return topics
