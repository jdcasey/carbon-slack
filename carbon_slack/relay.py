import time
import socket
from carbon_slack.slack import Receiver
from carbon_slack.carbon import PlaintextSender

class Relay(object):
    def __init__(self, config, last_message=0):
        """Initialize the Relay using a config dict and an optional last-message timestamp (in unix seconds).
        """
        self.recv = Receiver(config, last_message)
        self.send = PlaintextSender(config)
        self.config = config

    def close(self):
        """If a socket is open in the sender at the time when the user kills this script, try to close it 
        gracefully.
        """
        self.send.close()

    def run(self):
        """Receive any available messages from the Slack channel and assume they are metrics triplets (key, value, tstamp).
        Messages can be multi-line, with a triplet per line. For each message that we can parse in this way,
        add the message 'ts' value to an acks array, which will be used to delete those messages from the 
        Slack channel to reduce the possibility of duplicate processing.

        For each triplet we can parse, send a new metric data point over a socket that we open to the Carbon
        daemon for this purpose, using newline-delimited plaintext.
        """
        messages = self.recv.get_messages()
        if len(messages) < 1:
            print "No metrics to report"
            return

        print "Sending stats..."

        acks = []
        metrics = []
        for m in messages:
            lines = [l.rstrip() for l in m['text'].splitlines()]
            for line in lines:
                parts = line.split(' ')
                if len(parts) < 3:
                    continue

                metrics.append("%s %s %s\n" % (parts[0], parts[1], parts[2]))
            acks.append(m['ts'])

        self.sender.send_metrics(metrics)

        if len(acks) > 0:
            self.recv.ack_messages(acks)
