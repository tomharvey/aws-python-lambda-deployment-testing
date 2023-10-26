#!/usr/bin/env python3

import aws_cdk as cdk

from play_stack.stack import PlayStack


app = cdk.App()
PlayStack(app, "PlayStack")

app.synth()
