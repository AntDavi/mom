# protocol.py
REGISTER = "REGISTER"
SEND_USER = "SEND_USER"
SUBSCRIBE = "SUBSCRIBE"
PUBLISH = "PUBLISH"
ADD_QUEUE = "ADD_QUEUE"
ADD_TOPIC = "ADD_TOPIC"
DEL_QUEUE = "DEL_QUEUE"
DEL_TOPIC = "DEL_TOPIC"
LIST = "LIST"
COUNT = "COUNT"

DELIMITER = "::"

def format_message(command, *args):
    return command + DELIMITER + DELIMITER.join(args)

def parse_message(raw_message):
    parts = raw_message.strip().split(DELIMITER)
    return parts[0], parts[1:]
