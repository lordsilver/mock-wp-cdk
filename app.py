import aws_cdk as cdk
from stacks.mock_wp_stack import MockWpStack
import os

app = cdk.App()

MockWpStack(
    app, "dev",
    stack_name="MockWpStackdev",
    env=cdk.Environment(
        account=os.environ.get("CDK_ACCOUNT"),
        region=os.environ.get("CDK_REGION")
    )
)

app.synth()
