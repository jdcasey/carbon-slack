#!/usr/bin/env python

from carbon_slack.network import Sender
import sys

TOKEN=sys.argv[1]
CHANNEL=sys.argv[2]

parts = []
while True:
	send = Sender(TOKEN, CHANNEL)

	part = sys.stdin.readline().rstrip()
	if part == '.':
		send.send(parts)
		parts = []
	else:
		parts.append(part)

	