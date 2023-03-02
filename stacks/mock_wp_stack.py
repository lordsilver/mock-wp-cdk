from constructs import Construct
from aws_cdk import (
    Stack, RemovalPolicy,
    aws_route53 as route53,
    aws_ecs as ecs,
)
from cloudcomponents.cdk_wordpress import Wordpress
import os

WP_DOMAIN = account=os.environ.get("WP_DOMAIN")
WP_CONTAINER_IMAGE = account=os.environ.get("WP_CONTAINER_IMAGE")

class MockWpStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hosted_zone = route53.PublicHostedZone.from_lookup(
            self, "HostedZone", 
            domain_name=WP_DOMAIN
        )

        Wordpress(
            self, "Wordpress",
            domain_name=f"blog.{WP_DOMAIN}",
            domain_zone=hosted_zone,
            image=ecs.ContainerImage.from_registry(WP_CONTAINER_IMAGE),
            removal_policy=RemovalPolicy.DESTROY,
            offload_static_content=True, # Support for plugin e.g. `WP Offload Media for Amazon S3
        )