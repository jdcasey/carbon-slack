#!/usr/bin/env python

import carbon_slack.relay
import carbon_slack.config

cfg=carbon_slack.config.load()
r=carbon_slack.relay.Relay(cfg)
r.run()
