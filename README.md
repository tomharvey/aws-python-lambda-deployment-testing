# Deploy python packages

Testing why a package won't deploy to ARM based lambda and to find a workaround.

I was seeing:

```
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested
```

When running `cdk deploy` and could see it installing the x86 version of the package.

I was on a M2 (ARM) Mac and was specifying `aws_lambda.Architecture.ARM_64` as my lambda arch.

But, here it is, compiling packages for x86! How disappointing.

### Repo

This is mainly a CDK bootstrapped project.

The stack is defined in play_stack.stack and calls 2 constructs:

1. The aws_lambda_python_alpha approach to building a python function.
2. The turbolayers approach to building a python function.

Compare these 2 constrcuts to see how the approach differs.

Deploy and you can test them.


### Turbolayers

I have used https://github.com/CloudSnorkel/cdk-turbo-layers for some projects recently
and this makes the deploy a lot faster by running the package installation on a remote lambda
and then you access them all through a layer.

This means that you don't compile your packages on each deploy. Check the package docs for more.

It also means that even for locally triggered `deploy` I won't be building my dependancies locally.

And, that solved the issue - as well as bringing faster deploys.

