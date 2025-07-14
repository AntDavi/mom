from queue import Queue
from collections import defaultdict

class MessageBroker:
    def __init__(self):
        self.users = {}  # nome: Queue
        self.topics = defaultdict(set)  # nome_topico: set(nomes_usuarios)

    def register_user(self, name):
        if name in self.users:
            return False
        self.users[name] = Queue()
        return True

    def add_topic(self, topic):
        self.topics[topic] = set()

    def subscribe_user_to_topic(self, user, topic):
        self.topics[topic].add(user)

    def send_user_message(self, to_user, msg):
        if to_user in self.users:
            self.users[to_user].put(msg)
            return True
        return False

    def publish_to_topic(self, topic, msg):
        if topic in self.topics:
            for user in self.topics[topic]:
                self.send_user_message(user, f"[TOPIC:{topic}] {msg}")
            return True
        return False

    def get_messages(self, user):
        msgs = []
        while not self.users[user].empty():
            msgs.append(self.users[user].get())
        return msgs

    def list_queues(self):
        return list(self.users.keys())

    def list_topics(self):
        return list(self.topics.keys())

    def count_queue_messages(self, user):
        return self.users[user].qsize() if user in self.users else 0
