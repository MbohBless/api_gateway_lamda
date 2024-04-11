from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct


class ServerlessArchitectureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lamda = _lambda.Function(
            self, "Test Lambda",
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset("lambda"),
            handler="handler_1.handler",
        )
        
        apigw.LambdaRestApi(
            self, "Practice Rest Endpoint",
            handler=my_lamda,
            # proxy=False
        )
        # create an endpoint
        # create a lambda
        