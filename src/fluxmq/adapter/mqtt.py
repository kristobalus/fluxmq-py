from asyncio import Queue

from fluxmq.message import Message
from fluxmq.status import Status
from fluxmq.topic import Topic
from fluxmq.transport import Transport


class MQTT(Transport):
    async def close(self) -> None:
        pass

    async def connect(self) -> None:
        pass

    async def publish(self, topic: str, payload):
        pass

    async def subscribe(self, topic: str) -> Queue[Message]:
        pass

    async def unsubscribe(self, topic: str):
        pass

    async def request(self, topic: str, payload):
        pass

    async def respond(self, topic: str, response):
        pass


class MQTTTopic(Topic):
    def node_state(self, node_id: str):
        pass

    def start(self, service_id: str):
        pass

    def stop(self, service_id: str):
        pass

    def node_state_request(self, service_id: str):
        pass

    def configuration_request(self, service_id: str):
        pass

    def status_request(self, service_id: str):
        pass

    def request_configuration(self, service_id: str):
        return f""

    def time(self):
        return f"time"

    def control(self, service_id: str):
        return f"service/{service_id}/control"

    def status(self, service_id: str):
        return f"service/{service_id}/status"

    def configuration(self, service_id: str):
        return f"service/{service_id}/configuration"


class MQTTStatus(Status):
    def node_stopped(self, node_id: str):
        pass

    def node_started(self, node_id: str):
        pass

    def up(self):
        return "up"

    def down(self):
        return "down"

    def started(self):
        return "started"

    def stopped(self):
        return "stoppped"
