import logging
from typing import Any, Dict, List, Optional, Set

from kafka import KafkaAdminClient, KafkaConsumer

from kafkaadmin.functions import set_debug

log = logging.getLogger(__name__)


class Admin:
    def __init__(self, config: Dict[str, Any], debug: bool):
        set_debug(log, debug)
        self.config = config
        self.admin = KafkaAdminClient(bootstrap_servers=self.config["bootstrap_servers"])
        self.consumer = KafkaConsumer(bootstrap_servers=self.config["bootstrap_servers"])

    @staticmethod
    def generate_topics_move(topics: List[str]) -> Dict[str, Any]:
        jsonified_topics: List[Dict[str, str]] = [{"topic": t} for t in topics]
        generated = {"topics": jsonified_topics, "version": 1}
        return generated

    def get_topics_by_prefix(self, prefix: Optional[str] = None) -> List[str]:
        """Return all topics matched prefix."""
        all_topics: Set[str] = self.consumer.topics()
        if not prefix:
            return list(all_topics)

        topics: List[str] = [topic for topic in all_topics if topic.startswith(prefix)]
        return topics
