import sys
import click
import carbon_slack.config as config
import carbon_slack.relay as relay
import carbon_slack.slack as slack
import time
import datetime.datetime as dt

@click.command()
def init(args):
	print config.serialized_sample()

@click.command()
@click.option('--config', '-c', help='Alternative config YAML')
def relay(args, config=None):
    cfg = config.load(config)

    client = relay.Relay(cfg)
	try:
	    while True:
	    	client.run()
	    	time.sleep(10)
	except KeyboardInterrupt:
	    if client is not None:
	        try:
	            client.close()
	        finally:
	            print "attempted to close relay"

	    sys.stderr.write("\nExiting\n")
	    sys.exit(0)

@click.command()
@click.option('--config', '-c', help='Alternative config YAML')
def recv(args, config=None):
    cfg = config.load(config)

    recv = slack.Receiver(cfg)
	messages = recv.get_messages()
	for m in messages:
		username = recv.find_user(m['user'])
		m['username'] = username
		m['datestamp'] = dt.fromtimestamp(m['ts'])
		print "%(datestamp)s  %(username)s: %(text)s" % m

@click.command()
@click.argument('metric_name')
@click.argument('metric_value')
@click.option('--config', '-c', help='Alternative config YAML')
def send(args, config=None):
    cfg = config.load()

    sender = slack.Sender(cfg)
    now = int(time.time())
    sender.send("%s %s %s" % (args.metric_name, args.metric_value, now))
