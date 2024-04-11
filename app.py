#!/usr/bin/env python3
import os

import aws_cdk as cdk

from serverless_architecture.serverless_architecture_stack import ServerlessArchitectureStack


app = cdk.App()
ServerlessArchitectureStack(app, "ServerlessArchitectureStack")

app.synth()
