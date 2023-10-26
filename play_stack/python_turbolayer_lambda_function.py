from aws_cdk import (
    aws_lambda,
)

from cloudsnorkel.cdk_turbo_layers import (
    PythonDependencyPackager,
    DependencyPackagerType,
)

from constructs import Construct


class PythonTurboLayerLambda(Construct):
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

        packager = PythonDependencyPackager(
            self,
            "Package",
            runtime=runtime,
            type=DependencyPackagerType.LAMBDA,
            architecture=architecture,
        )

        turbo_package_layer = packager.layer_from_requirements_txt(
            "Package", entry
        )

        aws_lambda.Function(
            self,
            "Function",
            code=aws_lambda.Code.from_asset(entry),
            handler="index.handler",
            runtime=runtime,
            layers=[turbo_package_layer],
            architecture=architecture,
        )