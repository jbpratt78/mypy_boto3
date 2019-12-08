# mypy_boto3

[![PyPI - Handsdown](https://img.shields.io/pypi/v/mypy-boto3.svg?color=blue&style=for-the-badge)](https://pypi.org/project/mypy-boto3)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3.svg?color=blue&style=for-the-badge)](https://pypi.org/project/mypy-boto3)
[![Docs](https://img.shields.io/readthedocs/mypy-boto3.svg?color=blue&style=for-the-badge)](https://mypy-boto3.readthedocs.io/)

`mypy`-friendly type annotations for `boto3`.

Based on [boto3_type_annotations](https://github.com/alliefitter/boto3_type_annotations) by [@alliefitter](https://github.com/alliefitter).

- [mypy_boto3](#mypyboto3)
  - [Installation](#installation)
  - [Latest changes](#latest-changes)
  - [Usage](#usage)
    - [Setup your IDE](#setup-your-ide)
    - [VSCode](#vscode)
    - [PyCharm](#pycharm)
    - [Other IDEs](#other-ides)
    - [Explicit type annotations](#explicit-type-annotations)
    - [Pylint compatibility](#pylint-compatibility)
  - [How to build](#how-to-build)
    - [Locally](#locally)
    - [With Docker image](#with-docker-image)
  - [Differences from boto3-type-annotations](#differences-from-boto3-type-annotations)
  - [Thank you](#thank-you)
  - [Sub-modules](#sub-modules)
    - [Examples](#examples)
    - [List of all sub-modules](#list-of-all-sub-modules)

## Installation

```bash
# install `boto3` type annotations
# for ec2, s3, rds, lambda, sqs, dynamo and cloudformation
# Consumes ~7 MB of space
python -m pip install boto3-stubs[essential]

# or install annotations for services you use
python -m pip install boto3-stubs[acm,apigateway]

# build service index. You should execute this command everytime
# you update boto3-stubs or install/remove services
python -m mypy_boto3
```

## Latest changes

Full changelog can be found in [Releases](https://github.com/vemel/mypy_boto3/releases).

## Usage

- Install [mypy](https://github.com/python/mypy) and optionally enable it in your IDE
- Install [boto3](https://github.com/boto/boto3)
- VSCode: Use explicit types for `boto3.client`, `boto3.session.client`,
  `client.get_waiter` and `client.get_paginator` calls to enjoy code auto-complete and
  correct type hints

```python
import boto3

from mypy_boto3 import s3

# you need explicit type annotatins only if your IDE do not support
# function overloads (e.g. VSCode). FOr PyCHarm anf mypy you do not need
# to set type explicitly
client: s3.Client = boto3.client("s3")

# IDE autocomplete suggests function name and arguments here
client.create_bucket(Bucket="bucket")

# (mypy) error: Missing positional argument "Key" in call to "get_object" of "Client"
client.get_object(Bucket="bucket")

# (mypy) error: Argument "Key" to "get_object" of "Client" has incompatible type "None"; expected "str"
client.get_object(Bucket="bucket", Key=None)

resource: s3.ServiceResource = boto3.Session(region_name="us-west-1").resource("s3")

# IDE autocomplete suggests function name and arguments here
bucket = resource.Bucket("bucket")

# (mypy) error: Unexpected keyword argument "key" for "upload_file" of "Bucket"; did you mean "Key"?
bucket.upload_file(Filename="my.txt", key="my-txt")

# waiters and paginators are annotated as well
waiter: s3.BucketExistsWaiter = client.get_waiter("bucket_exists")
paginator: s3.ListMultipartUploadsPaginator = client.get_paginator(
    "list_multipart_uploads"
)
```

### Setup your IDE

### VSCode

- Install [Official Python extension](https://github.com/microsoft/vscode-python)
- Install [mypy](https://github.com/python/mypy)
- Activate `mypy` checking in settings: `"python.linting.mypyEnabled": true`
- Install `boto3-stubs` with `boto3` services you use
- Run `python -m mypy_boto3`
- Use [explicit type annotations](#explicit-type-annotations) because
  function overload is not fully supported yet

### PyCharm

- Install [mypy plugin](https://plugins.jetbrains.com/plugin/11086-mypy/)
- Install [mypy](https://github.com/python/mypy)
- Set path to `mypy` in `mypy plugin` settings
- Install `boto3-stubs` with `boto3` services you use
- Run `python -m mypy_boto3`

Official `mypy` plugin does not work for some reason for me. If you know
how to setup it correctly, please hep me to update this section.

### Other IDEs

Please help me to extend this section.

### Explicit type annotations

Automatic type discovery is too stressful for PyCharm and does not work in VSCode.
So implicit type annotations support has been removed as it is not useful.

To get full advantage of `boto3-stubs`, you can set types explicitly.

```python
import boto3

from mypy_boto3 import ec2

# covered by boto3-stubs, no explicit type required
session = boto3.session.Session(region_name="us-west-1")

# by default it is botocore.client.BaseClient, but we explicitly
# set it to EC2.Client
ec2_client: ec2.Client = boto3.client("ec2", region_name="us-west-1")

# same for resource
ec2_resource: ec2.ServiceResource = session.resource("ec2")

# PyCharm does not need explicit type annotations here, but VSCode does
bundle_task_complete_waiter: ec2.BundleTaskCompleteWaiter = ec2_client.get_waiter("bundle_task_complete")
describe_volumes_paginator: ec2.DescribeVolumesPaginator = ec2_client.get_paginator("describe_volumes")

# ec2_client, ec2_resource, bundle_task_complete_waiter and describe_volumes_paginator
# now have correct type so IDE autocomplete for methods, arguments and return types
# works as expected. You do not need to specify types explicitly further
```

### Pylint compatibility

It is totally safe to use `TYPE_CHECKING` flag in order to avoid `boto3-stubs`
dependency in production.
However, there is an issue in `pylint` that it complains about undefined
variables. To fix it, set all types to `Any` in non-`TYPE_CHECKING` mode.

```python
import boto3
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3.ec2 import Client, ServiceResource
    from mypy_boto3.ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3.ec2.paginators import DescribeVolumesPaginator
else:
    Client = Any
    ServiceResource = Any
    BundleTaskCompleteWaiter = Any
    DescribeVolumesPaginator = Any

...
```

## How to build

### Locally

`mypy-boto3` is built for the latest version of `boto3`. If you need type annotations for another
version of `boto3`, you can use `mypy-boto3-builder`.

```bash
# Install preferred version of `boto3`
pip install boto3==1.10.18 botocore==1.13.18

# Install `mypy-boto3-builder`
pip install mypy-boto3-builder[black]

# Build all packages
# You can specify required services explicitly like
# ./scripts/build.sh -s ec2 s3
./scripts/build.sh

# Install custom `mypy-boto3` packages
./scripts/install.sh
```

### With Docker image

- Install [Docker](https://docs.docker.com/install/)
- Pull latest `mypy_boto3_builder` version and tag it

```bash
docker pull docker.pkg.github.com/vemel/mypy_boto3/mypy_boto3_builder:latest
docker tag docker.pkg.github.com/vemel/mypy_boto3/mypy_boto3_builder:latest mypy_boto3_builder
```

- Generate stubs in `output` directory

```bash
mkdir output

# generate stubs for all services
docker run -v `pwd`/output:/output -ti mypy_boto3_builder

# generate stubs for s3 service
docker run -v `pwd`/output:/output -ti mypy_boto3_builder -s s3

# generate stubs for a specific boto3 version
docker run -e BOTO3_VERSION=1.10.18 BOTOCORE_VERSION=1.13.18 -v `pwd`/output:/output -ti mypy_boto3_builder
```

- Install packages from `output` directory as described above

## Differences from boto3-type-annotations

- `mypy` compatibility
- Fully type annotated
- No need to set types explicitly (depends on your IDE)
- Generated types for return values and arguments
- Added `ServiceResource` sub-collections
- Support service-specific sub-modules
- Modules documentation
- Type annotations for return structures
- Correct annotations for `client.get_waiter` and `client.get_paginator`
- Helper functions for IDEs with no `overload` support (Hi, VSCode!)

## Thank you

- Guys behind [boto3-type-annotations](https://pypi.org/project/boto3-type-annotations/),
  this package is based on top of their work
- [black](https://github.com/psf/black) developers for awesome formatting tool
- [mypy](https://github.com/python/mypy) for doing all dirty work for us

## Sub-modules

### Examples

You can install any sub-modules using `pip`

```bash
# pip install boto3-stubs[<submodule_name>,...]

# install `boto3` type annotations
# for ec2, s3, rds, lambda, sqs, dynamo and cloudformation
python -m pip install boto3-stubs[essential]

# install ec2, s3 and sqs type annotations
python -m pip install boto3-stubs[s3,ec2,sqs]

# build service index. You should execute this command everytime
# you update boto3-stubs or install/remove services
python -m mypy_boto3
```

### List of all sub-modules

- `essential` - Type annotations for `ec2`, `s3`, `rds`, `lambda`, `sqs`, `dynamodb` and `cloudformation` services.
- `accessanalyzer` - Type annotations for `boto3` [accessanalyzer](https://pypi.org/project/mypy-boto3-accessanalyzer/) service.
- `acm` - Type annotations for `boto3` [acm](https://pypi.org/project/mypy-boto3-acm/) service.
- `acm-pca` - Type annotations for `boto3` [acm-pca](https://pypi.org/project/mypy-boto3-acm-pca/) service.
- `alexaforbusiness` - Type annotations for `boto3` [alexaforbusiness](https://pypi.org/project/mypy-boto3-alexaforbusiness/) service.
- `amplify` - Type annotations for `boto3` [amplify](https://pypi.org/project/mypy-boto3-amplify/) service.
- `apigateway` - Type annotations for `boto3` [apigateway](https://pypi.org/project/mypy-boto3-apigateway/) service.
- `apigatewaymanagementapi` - Type annotations for `boto3` [apigatewaymanagementapi](https://pypi.org/project/mypy-boto3-apigatewaymanagementapi/) service.
- `apigatewayv2` - Type annotations for `boto3` [apigatewayv2](https://pypi.org/project/mypy-boto3-apigatewayv2/) service.
- `appconfig` - Type annotations for `boto3` [appconfig](https://pypi.org/project/mypy-boto3-appconfig/) service.
- `application-autoscaling` - Type annotations for `boto3` [application-autoscaling](https://pypi.org/project/mypy-boto3-application-autoscaling/) service.
- `application-insights` - Type annotations for `boto3` [application-insights](https://pypi.org/project/mypy-boto3-application-insights/) service.
- `appmesh` - Type annotations for `boto3` [appmesh](https://pypi.org/project/mypy-boto3-appmesh/) service.
- `appstream` - Type annotations for `boto3` [appstream](https://pypi.org/project/mypy-boto3-appstream/) service.
- `appsync` - Type annotations for `boto3` [appsync](https://pypi.org/project/mypy-boto3-appsync/) service.
- `athena` - Type annotations for `boto3` [athena](https://pypi.org/project/mypy-boto3-athena/) service.
- `autoscaling` - Type annotations for `boto3` [autoscaling](https://pypi.org/project/mypy-boto3-autoscaling/) service.
- `autoscaling-plans` - Type annotations for `boto3` [autoscaling-plans](https://pypi.org/project/mypy-boto3-autoscaling-plans/) service.
- `backup` - Type annotations for `boto3` [backup](https://pypi.org/project/mypy-boto3-backup/) service.
- `batch` - Type annotations for `boto3` [batch](https://pypi.org/project/mypy-boto3-batch/) service.
- `budgets` - Type annotations for `boto3` [budgets](https://pypi.org/project/mypy-boto3-budgets/) service.
- `ce` - Type annotations for `boto3` [ce](https://pypi.org/project/mypy-boto3-ce/) service.
- `chime` - Type annotations for `boto3` [chime](https://pypi.org/project/mypy-boto3-chime/) service.
- `cloud9` - Type annotations for `boto3` [cloud9](https://pypi.org/project/mypy-boto3-cloud9/) service.
- `clouddirectory` - Type annotations for `boto3` [clouddirectory](https://pypi.org/project/mypy-boto3-clouddirectory/) service.
- `cloudformation` - Type annotations for `boto3` [cloudformation](https://pypi.org/project/mypy-boto3-cloudformation/) service.
- `cloudfront` - Type annotations for `boto3` [cloudfront](https://pypi.org/project/mypy-boto3-cloudfront/) service.
- `cloudhsm` - Type annotations for `boto3` [cloudhsm](https://pypi.org/project/mypy-boto3-cloudhsm/) service.
- `cloudhsmv2` - Type annotations for `boto3` [cloudhsmv2](https://pypi.org/project/mypy-boto3-cloudhsmv2/) service.
- `cloudsearch` - Type annotations for `boto3` [cloudsearch](https://pypi.org/project/mypy-boto3-cloudsearch/) service.
- `cloudsearchdomain` - Type annotations for `boto3` [cloudsearchdomain](https://pypi.org/project/mypy-boto3-cloudsearchdomain/) service.
- `cloudtrail` - Type annotations for `boto3` [cloudtrail](https://pypi.org/project/mypy-boto3-cloudtrail/) service.
- `cloudwatch` - Type annotations for `boto3` [cloudwatch](https://pypi.org/project/mypy-boto3-cloudwatch/) service.
- `codebuild` - Type annotations for `boto3` [codebuild](https://pypi.org/project/mypy-boto3-codebuild/) service.
- `codecommit` - Type annotations for `boto3` [codecommit](https://pypi.org/project/mypy-boto3-codecommit/) service.
- `codedeploy` - Type annotations for `boto3` [codedeploy](https://pypi.org/project/mypy-boto3-codedeploy/) service.
- `codeguru-reviewer` - Type annotations for `boto3` [codeguru-reviewer](https://pypi.org/project/mypy-boto3-codeguru-reviewer/) service.
- `codeguruprofiler` - Type annotations for `boto3` [codeguruprofiler](https://pypi.org/project/mypy-boto3-codeguruprofiler/) service.
- `codepipeline` - Type annotations for `boto3` [codepipeline](https://pypi.org/project/mypy-boto3-codepipeline/) service.
- `codestar` - Type annotations for `boto3` [codestar](https://pypi.org/project/mypy-boto3-codestar/) service.
- `codestar-notifications` - Type annotations for `boto3` [codestar-notifications](https://pypi.org/project/mypy-boto3-codestar-notifications/) service.
- `cognito-identity` - Type annotations for `boto3` [cognito-identity](https://pypi.org/project/mypy-boto3-cognito-identity/) service.
- `cognito-idp` - Type annotations for `boto3` [cognito-idp](https://pypi.org/project/mypy-boto3-cognito-idp/) service.
- `cognito-sync` - Type annotations for `boto3` [cognito-sync](https://pypi.org/project/mypy-boto3-cognito-sync/) service.
- `comprehend` - Type annotations for `boto3` [comprehend](https://pypi.org/project/mypy-boto3-comprehend/) service.
- `comprehendmedical` - Type annotations for `boto3` [comprehendmedical](https://pypi.org/project/mypy-boto3-comprehendmedical/) service.
- `compute-optimizer` - Type annotations for `boto3` [compute-optimizer](https://pypi.org/project/mypy-boto3-compute-optimizer/) service.
- `config` - Type annotations for `boto3` [config](https://pypi.org/project/mypy-boto3-config/) service.
- `connect` - Type annotations for `boto3` [connect](https://pypi.org/project/mypy-boto3-connect/) service.
- `connectparticipant` - Type annotations for `boto3` [connectparticipant](https://pypi.org/project/mypy-boto3-connectparticipant/) service.
- `cur` - Type annotations for `boto3` [cur](https://pypi.org/project/mypy-boto3-cur/) service.
- `dataexchange` - Type annotations for `boto3` [dataexchange](https://pypi.org/project/mypy-boto3-dataexchange/) service.
- `datapipeline` - Type annotations for `boto3` [datapipeline](https://pypi.org/project/mypy-boto3-datapipeline/) service.
- `datasync` - Type annotations for `boto3` [datasync](https://pypi.org/project/mypy-boto3-datasync/) service.
- `dax` - Type annotations for `boto3` [dax](https://pypi.org/project/mypy-boto3-dax/) service.
- `devicefarm` - Type annotations for `boto3` [devicefarm](https://pypi.org/project/mypy-boto3-devicefarm/) service.
- `directconnect` - Type annotations for `boto3` [directconnect](https://pypi.org/project/mypy-boto3-directconnect/) service.
- `discovery` - Type annotations for `boto3` [discovery](https://pypi.org/project/mypy-boto3-discovery/) service.
- `dlm` - Type annotations for `boto3` [dlm](https://pypi.org/project/mypy-boto3-dlm/) service.
- `dms` - Type annotations for `boto3` [dms](https://pypi.org/project/mypy-boto3-dms/) service.
- `docdb` - Type annotations for `boto3` [docdb](https://pypi.org/project/mypy-boto3-docdb/) service.
- `ds` - Type annotations for `boto3` [ds](https://pypi.org/project/mypy-boto3-ds/) service.
- `dynamodb` - Type annotations for `boto3` [dynamodb](https://pypi.org/project/mypy-boto3-dynamodb/) service.
- `dynamodbstreams` - Type annotations for `boto3` [dynamodbstreams](https://pypi.org/project/mypy-boto3-dynamodbstreams/) service.
- `ec2` - Type annotations for `boto3` [ec2](https://pypi.org/project/mypy-boto3-ec2/) service.
- `ec2-instance-connect` - Type annotations for `boto3` [ec2-instance-connect](https://pypi.org/project/mypy-boto3-ec2-instance-connect/) service.
- `ecr` - Type annotations for `boto3` [ecr](https://pypi.org/project/mypy-boto3-ecr/) service.
- `ecs` - Type annotations for `boto3` [ecs](https://pypi.org/project/mypy-boto3-ecs/) service.
- `efs` - Type annotations for `boto3` [efs](https://pypi.org/project/mypy-boto3-efs/) service.
- `eks` - Type annotations for `boto3` [eks](https://pypi.org/project/mypy-boto3-eks/) service.
- `elastic-inference` - Type annotations for `boto3` [elastic-inference](https://pypi.org/project/mypy-boto3-elastic-inference/) service.
- `elasticache` - Type annotations for `boto3` [elasticache](https://pypi.org/project/mypy-boto3-elasticache/) service.
- `elasticbeanstalk` - Type annotations for `boto3` [elasticbeanstalk](https://pypi.org/project/mypy-boto3-elasticbeanstalk/) service.
- `elastictranscoder` - Type annotations for `boto3` [elastictranscoder](https://pypi.org/project/mypy-boto3-elastictranscoder/) service.
- `elb` - Type annotations for `boto3` [elb](https://pypi.org/project/mypy-boto3-elb/) service.
- `elbv2` - Type annotations for `boto3` [elbv2](https://pypi.org/project/mypy-boto3-elbv2/) service.
- `emr` - Type annotations for `boto3` [emr](https://pypi.org/project/mypy-boto3-emr/) service.
- `es` - Type annotations for `boto3` [es](https://pypi.org/project/mypy-boto3-es/) service.
- `events` - Type annotations for `boto3` [events](https://pypi.org/project/mypy-boto3-events/) service.
- `firehose` - Type annotations for `boto3` [firehose](https://pypi.org/project/mypy-boto3-firehose/) service.
- `fms` - Type annotations for `boto3` [fms](https://pypi.org/project/mypy-boto3-fms/) service.
- `forecast` - Type annotations for `boto3` [forecast](https://pypi.org/project/mypy-boto3-forecast/) service.
- `forecastquery` - Type annotations for `boto3` [forecastquery](https://pypi.org/project/mypy-boto3-forecastquery/) service.
- `frauddetector` - Type annotations for `boto3` [frauddetector](https://pypi.org/project/mypy-boto3-frauddetector/) service.
- `fsx` - Type annotations for `boto3` [fsx](https://pypi.org/project/mypy-boto3-fsx/) service.
- `gamelift` - Type annotations for `boto3` [gamelift](https://pypi.org/project/mypy-boto3-gamelift/) service.
- `glacier` - Type annotations for `boto3` [glacier](https://pypi.org/project/mypy-boto3-glacier/) service.
- `globalaccelerator` - Type annotations for `boto3` [globalaccelerator](https://pypi.org/project/mypy-boto3-globalaccelerator/) service.
- `glue` - Type annotations for `boto3` [glue](https://pypi.org/project/mypy-boto3-glue/) service.
- `greengrass` - Type annotations for `boto3` [greengrass](https://pypi.org/project/mypy-boto3-greengrass/) service.
- `groundstation` - Type annotations for `boto3` [groundstation](https://pypi.org/project/mypy-boto3-groundstation/) service.
- `guardduty` - Type annotations for `boto3` [guardduty](https://pypi.org/project/mypy-boto3-guardduty/) service.
- `health` - Type annotations for `boto3` [health](https://pypi.org/project/mypy-boto3-health/) service.
- `iam` - Type annotations for `boto3` [iam](https://pypi.org/project/mypy-boto3-iam/) service.
- `imagebuilder` - Type annotations for `boto3` [imagebuilder](https://pypi.org/project/mypy-boto3-imagebuilder/) service.
- `importexport` - Type annotations for `boto3` [importexport](https://pypi.org/project/mypy-boto3-importexport/) service.
- `inspector` - Type annotations for `boto3` [inspector](https://pypi.org/project/mypy-boto3-inspector/) service.
- `iot` - Type annotations for `boto3` [iot](https://pypi.org/project/mypy-boto3-iot/) service.
- `iot-data` - Type annotations for `boto3` [iot-data](https://pypi.org/project/mypy-boto3-iot-data/) service.
- `iot-jobs-data` - Type annotations for `boto3` [iot-jobs-data](https://pypi.org/project/mypy-boto3-iot-jobs-data/) service.
- `iot1click-devices` - Type annotations for `boto3` [iot1click-devices](https://pypi.org/project/mypy-boto3-iot1click-devices/) service.
- `iot1click-projects` - Type annotations for `boto3` [iot1click-projects](https://pypi.org/project/mypy-boto3-iot1click-projects/) service.
- `iotanalytics` - Type annotations for `boto3` [iotanalytics](https://pypi.org/project/mypy-boto3-iotanalytics/) service.
- `iotevents` - Type annotations for `boto3` [iotevents](https://pypi.org/project/mypy-boto3-iotevents/) service.
- `iotevents-data` - Type annotations for `boto3` [iotevents-data](https://pypi.org/project/mypy-boto3-iotevents-data/) service.
- `iotsecuretunneling` - Type annotations for `boto3` [iotsecuretunneling](https://pypi.org/project/mypy-boto3-iotsecuretunneling/) service.
- `iotthingsgraph` - Type annotations for `boto3` [iotthingsgraph](https://pypi.org/project/mypy-boto3-iotthingsgraph/) service.
- `kafka` - Type annotations for `boto3` [kafka](https://pypi.org/project/mypy-boto3-kafka/) service.
- `kendra` - Type annotations for `boto3` [kendra](https://pypi.org/project/mypy-boto3-kendra/) service.
- `kinesis` - Type annotations for `boto3` [kinesis](https://pypi.org/project/mypy-boto3-kinesis/) service.
- `kinesis-video-archived-media` - Type annotations for `boto3` [kinesis-video-archived-media](https://pypi.org/project/mypy-boto3-kinesis-video-archived-media/) service.
- `kinesis-video-media` - Type annotations for `boto3` [kinesis-video-media](https://pypi.org/project/mypy-boto3-kinesis-video-media/) service.
- `kinesisanalytics` - Type annotations for `boto3` [kinesisanalytics](https://pypi.org/project/mypy-boto3-kinesisanalytics/) service.
- `kinesisanalyticsv2` - Type annotations for `boto3` [kinesisanalyticsv2](https://pypi.org/project/mypy-boto3-kinesisanalyticsv2/) service.
- `kinesisvideo` - Type annotations for `boto3` [kinesisvideo](https://pypi.org/project/mypy-boto3-kinesisvideo/) service.
- `kms` - Type annotations for `boto3` [kms](https://pypi.org/project/mypy-boto3-kms/) service.
- `lakeformation` - Type annotations for `boto3` [lakeformation](https://pypi.org/project/mypy-boto3-lakeformation/) service.
- `lambda` - Type annotations for `boto3` [lambda](https://pypi.org/project/mypy-boto3-lambda/) service.
- `lex-models` - Type annotations for `boto3` [lex-models](https://pypi.org/project/mypy-boto3-lex-models/) service.
- `lex-runtime` - Type annotations for `boto3` [lex-runtime](https://pypi.org/project/mypy-boto3-lex-runtime/) service.
- `license-manager` - Type annotations for `boto3` [license-manager](https://pypi.org/project/mypy-boto3-license-manager/) service.
- `lightsail` - Type annotations for `boto3` [lightsail](https://pypi.org/project/mypy-boto3-lightsail/) service.
- `logs` - Type annotations for `boto3` [logs](https://pypi.org/project/mypy-boto3-logs/) service.
- `machinelearning` - Type annotations for `boto3` [machinelearning](https://pypi.org/project/mypy-boto3-machinelearning/) service.
- `macie` - Type annotations for `boto3` [macie](https://pypi.org/project/mypy-boto3-macie/) service.
- `managedblockchain` - Type annotations for `boto3` [managedblockchain](https://pypi.org/project/mypy-boto3-managedblockchain/) service.
- `marketplace-catalog` - Type annotations for `boto3` [marketplace-catalog](https://pypi.org/project/mypy-boto3-marketplace-catalog/) service.
- `marketplace-entitlement` - Type annotations for `boto3` [marketplace-entitlement](https://pypi.org/project/mypy-boto3-marketplace-entitlement/) service.
- `marketplacecommerceanalytics` - Type annotations for `boto3` [marketplacecommerceanalytics](https://pypi.org/project/mypy-boto3-marketplacecommerceanalytics/) service.
- `mediaconnect` - Type annotations for `boto3` [mediaconnect](https://pypi.org/project/mypy-boto3-mediaconnect/) service.
- `mediaconvert` - Type annotations for `boto3` [mediaconvert](https://pypi.org/project/mypy-boto3-mediaconvert/) service.
- `medialive` - Type annotations for `boto3` [medialive](https://pypi.org/project/mypy-boto3-medialive/) service.
- `mediapackage` - Type annotations for `boto3` [mediapackage](https://pypi.org/project/mypy-boto3-mediapackage/) service.
- `mediapackage-vod` - Type annotations for `boto3` [mediapackage-vod](https://pypi.org/project/mypy-boto3-mediapackage-vod/) service.
- `mediastore` - Type annotations for `boto3` [mediastore](https://pypi.org/project/mypy-boto3-mediastore/) service.
- `mediastore-data` - Type annotations for `boto3` [mediastore-data](https://pypi.org/project/mypy-boto3-mediastore-data/) service.
- `mediatailor` - Type annotations for `boto3` [mediatailor](https://pypi.org/project/mypy-boto3-mediatailor/) service.
- `meteringmarketplace` - Type annotations for `boto3` [meteringmarketplace](https://pypi.org/project/mypy-boto3-meteringmarketplace/) service.
- `mgh` - Type annotations for `boto3` [mgh](https://pypi.org/project/mypy-boto3-mgh/) service.
- `migrationhub-config` - Type annotations for `boto3` [migrationhub-config](https://pypi.org/project/mypy-boto3-migrationhub-config/) service.
- `mobile` - Type annotations for `boto3` [mobile](https://pypi.org/project/mypy-boto3-mobile/) service.
- `mq` - Type annotations for `boto3` [mq](https://pypi.org/project/mypy-boto3-mq/) service.
- `mturk` - Type annotations for `boto3` [mturk](https://pypi.org/project/mypy-boto3-mturk/) service.
- `neptune` - Type annotations for `boto3` [neptune](https://pypi.org/project/mypy-boto3-neptune/) service.
- `networkmanager` - Type annotations for `boto3` [networkmanager](https://pypi.org/project/mypy-boto3-networkmanager/) service.
- `opsworks` - Type annotations for `boto3` [opsworks](https://pypi.org/project/mypy-boto3-opsworks/) service.
- `opsworkscm` - Type annotations for `boto3` [opsworkscm](https://pypi.org/project/mypy-boto3-opsworkscm/) service.
- `organizations` - Type annotations for `boto3` [organizations](https://pypi.org/project/mypy-boto3-organizations/) service.
- `outposts` - Type annotations for `boto3` [outposts](https://pypi.org/project/mypy-boto3-outposts/) service.
- `personalize` - Type annotations for `boto3` [personalize](https://pypi.org/project/mypy-boto3-personalize/) service.
- `personalize-events` - Type annotations for `boto3` [personalize-events](https://pypi.org/project/mypy-boto3-personalize-events/) service.
- `personalize-runtime` - Type annotations for `boto3` [personalize-runtime](https://pypi.org/project/mypy-boto3-personalize-runtime/) service.
- `pi` - Type annotations for `boto3` [pi](https://pypi.org/project/mypy-boto3-pi/) service.
- `pinpoint` - Type annotations for `boto3` [pinpoint](https://pypi.org/project/mypy-boto3-pinpoint/) service.
- `pinpoint-email` - Type annotations for `boto3` [pinpoint-email](https://pypi.org/project/mypy-boto3-pinpoint-email/) service.
- `pinpoint-sms-voice` - Type annotations for `boto3` [pinpoint-sms-voice](https://pypi.org/project/mypy-boto3-pinpoint-sms-voice/) service.
- `polly` - Type annotations for `boto3` [polly](https://pypi.org/project/mypy-boto3-polly/) service.
- `pricing` - Type annotations for `boto3` [pricing](https://pypi.org/project/mypy-boto3-pricing/) service.
- `qldb` - Type annotations for `boto3` [qldb](https://pypi.org/project/mypy-boto3-qldb/) service.
- `qldb-session` - Type annotations for `boto3` [qldb-session](https://pypi.org/project/mypy-boto3-qldb-session/) service.
- `quicksight` - Type annotations for `boto3` [quicksight](https://pypi.org/project/mypy-boto3-quicksight/) service.
- `ram` - Type annotations for `boto3` [ram](https://pypi.org/project/mypy-boto3-ram/) service.
- `rds` - Type annotations for `boto3` [rds](https://pypi.org/project/mypy-boto3-rds/) service.
- `rds-data` - Type annotations for `boto3` [rds-data](https://pypi.org/project/mypy-boto3-rds-data/) service.
- `redshift` - Type annotations for `boto3` [redshift](https://pypi.org/project/mypy-boto3-redshift/) service.
- `rekognition` - Type annotations for `boto3` [rekognition](https://pypi.org/project/mypy-boto3-rekognition/) service.
- `resource-groups` - Type annotations for `boto3` [resource-groups](https://pypi.org/project/mypy-boto3-resource-groups/) service.
- `resourcegroupstaggingapi` - Type annotations for `boto3` [resourcegroupstaggingapi](https://pypi.org/project/mypy-boto3-resourcegroupstaggingapi/) service.
- `robomaker` - Type annotations for `boto3` [robomaker](https://pypi.org/project/mypy-boto3-robomaker/) service.
- `route53` - Type annotations for `boto3` [route53](https://pypi.org/project/mypy-boto3-route53/) service.
- `route53domains` - Type annotations for `boto3` [route53domains](https://pypi.org/project/mypy-boto3-route53domains/) service.
- `route53resolver` - Type annotations for `boto3` [route53resolver](https://pypi.org/project/mypy-boto3-route53resolver/) service.
- `s3` - Type annotations for `boto3` [s3](https://pypi.org/project/mypy-boto3-s3/) service.
- `s3control` - Type annotations for `boto3` [s3control](https://pypi.org/project/mypy-boto3-s3control/) service.
- `sagemaker` - Type annotations for `boto3` [sagemaker](https://pypi.org/project/mypy-boto3-sagemaker/) service.
- `sagemaker-a2i-runtime` - Type annotations for `boto3` [sagemaker-a2i-runtime](https://pypi.org/project/mypy-boto3-sagemaker-a2i-runtime/) service.
- `sagemaker-runtime` - Type annotations for `boto3` [sagemaker-runtime](https://pypi.org/project/mypy-boto3-sagemaker-runtime/) service.
- `savingsplans` - Type annotations for `boto3` [savingsplans](https://pypi.org/project/mypy-boto3-savingsplans/) service.
- `schemas` - Type annotations for `boto3` [schemas](https://pypi.org/project/mypy-boto3-schemas/) service.
- `sdb` - Type annotations for `boto3` [sdb](https://pypi.org/project/mypy-boto3-sdb/) service.
- `secretsmanager` - Type annotations for `boto3` [secretsmanager](https://pypi.org/project/mypy-boto3-secretsmanager/) service.
- `securityhub` - Type annotations for `boto3` [securityhub](https://pypi.org/project/mypy-boto3-securityhub/) service.
- `serverlessrepo` - Type annotations for `boto3` [serverlessrepo](https://pypi.org/project/mypy-boto3-serverlessrepo/) service.
- `service-quotas` - Type annotations for `boto3` [service-quotas](https://pypi.org/project/mypy-boto3-service-quotas/) service.
- `servicecatalog` - Type annotations for `boto3` [servicecatalog](https://pypi.org/project/mypy-boto3-servicecatalog/) service.
- `servicediscovery` - Type annotations for `boto3` [servicediscovery](https://pypi.org/project/mypy-boto3-servicediscovery/) service.
- `ses` - Type annotations for `boto3` [ses](https://pypi.org/project/mypy-boto3-ses/) service.
- `sesv2` - Type annotations for `boto3` [sesv2](https://pypi.org/project/mypy-boto3-sesv2/) service.
- `shield` - Type annotations for `boto3` [shield](https://pypi.org/project/mypy-boto3-shield/) service.
- `signer` - Type annotations for `boto3` [signer](https://pypi.org/project/mypy-boto3-signer/) service.
- `sms` - Type annotations for `boto3` [sms](https://pypi.org/project/mypy-boto3-sms/) service.
- `sms-voice` - Type annotations for `boto3` [sms-voice](https://pypi.org/project/mypy-boto3-sms-voice/) service.
- `snowball` - Type annotations for `boto3` [snowball](https://pypi.org/project/mypy-boto3-snowball/) service.
- `sns` - Type annotations for `boto3` [sns](https://pypi.org/project/mypy-boto3-sns/) service.
- `sqs` - Type annotations for `boto3` [sqs](https://pypi.org/project/mypy-boto3-sqs/) service.
- `ssm` - Type annotations for `boto3` [ssm](https://pypi.org/project/mypy-boto3-ssm/) service.
- `sso` - Type annotations for `boto3` [sso](https://pypi.org/project/mypy-boto3-sso/) service.
- `sso-oidc` - Type annotations for `boto3` [sso-oidc](https://pypi.org/project/mypy-boto3-sso-oidc/) service.
- `stepfunctions` - Type annotations for `boto3` [stepfunctions](https://pypi.org/project/mypy-boto3-stepfunctions/) service.
- `storagegateway` - Type annotations for `boto3` [storagegateway](https://pypi.org/project/mypy-boto3-storagegateway/) service.
- `sts` - Type annotations for `boto3` [sts](https://pypi.org/project/mypy-boto3-sts/) service.
- `support` - Type annotations for `boto3` [support](https://pypi.org/project/mypy-boto3-support/) service.
- `swf` - Type annotations for `boto3` [swf](https://pypi.org/project/mypy-boto3-swf/) service.
- `textract` - Type annotations for `boto3` [textract](https://pypi.org/project/mypy-boto3-textract/) service.
- `transcribe` - Type annotations for `boto3` [transcribe](https://pypi.org/project/mypy-boto3-transcribe/) service.
- `transfer` - Type annotations for `boto3` [transfer](https://pypi.org/project/mypy-boto3-transfer/) service.
- `translate` - Type annotations for `boto3` [translate](https://pypi.org/project/mypy-boto3-translate/) service.
- `waf` - Type annotations for `boto3` [waf](https://pypi.org/project/mypy-boto3-waf/) service.
- `waf-regional` - Type annotations for `boto3` [waf-regional](https://pypi.org/project/mypy-boto3-waf-regional/) service.
- `wafv2` - Type annotations for `boto3` [wafv2](https://pypi.org/project/mypy-boto3-wafv2/) service.
- `workdocs` - Type annotations for `boto3` [workdocs](https://pypi.org/project/mypy-boto3-workdocs/) service.
- `worklink` - Type annotations for `boto3` [worklink](https://pypi.org/project/mypy-boto3-worklink/) service.
- `workmail` - Type annotations for `boto3` [workmail](https://pypi.org/project/mypy-boto3-workmail/) service.
- `workmailmessageflow` - Type annotations for `boto3` [workmailmessageflow](https://pypi.org/project/mypy-boto3-workmailmessageflow/) service.
- `workspaces` - Type annotations for `boto3` [workspaces](https://pypi.org/project/mypy-boto3-workspaces/) service.
- `xray` - Type annotations for `boto3` [xray](https://pypi.org/project/mypy-boto3-xray/) service.
