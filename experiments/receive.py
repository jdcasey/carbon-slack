#!/usr/bin/env python

from carbon_slack.network import Receiver
import sys
import time

TOKEN=sys.argv[1]
CHANNEL = sys.argv[2] if len(sys.argv) > 2 else None

recv = Receiver(TOKEN, CHANNEL)

while True:
	messages = recv.get_messages()
	for m in messages:
		print m

	recv.ack_messages([m['ts'] for m in messages])
	time.sleep(1)

# for c in recv.list_channels():
# 	print "%s (%s)" % (c['name'], c['id'])