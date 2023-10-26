from aws_cdk import (
    aws_lambda,
    aws_lambda_python_alpha
)

from constructs import Construct


class PythonLambda(Construct):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        entry: str,
        runtime: aws_lambda.Runtime,
        architecture: aws_lambda.Architecture,
        **kwargs,
    ) -> None:
        
        super().__init__(scope, construct_id, **kwargs)

        aws_lambda_python_alpha.PythonFunction(
            self,
            "Function",
            index="index.py",
            handler='handler',
            entry=entry,
            runtime=runtime,
            architecture=architecture
        )