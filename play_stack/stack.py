from aws_cdk import (
    Stack,
    aws_lambda,
)

from play_stack.python_lambda_function import PythonLambda
from play_stack.python_turbolayer_lambda_function import PythonTurboLayerLambda

from constructs import Construct

class PlayStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        RUNTIME = aws_lambda.Runtime.PYTHON_3_9
        ARCH = aws_lambda.Architecture.ARM_64
        ENTRY = "lambda-function"

        PythonTurboLayerLambda(
            scope=self,
            construct_id='CloudsnorkelTurbolayer',
            entry=ENTRY,
            runtime=RUNTIME,
            architecture=ARCH,
        )

        PythonLambda(
            scope=self,
            construct_id='AwsLambdaPythonAlpha',
            entry=ENTRY,
            runtime=RUNTIME,
            architecture=ARCH,
        )
