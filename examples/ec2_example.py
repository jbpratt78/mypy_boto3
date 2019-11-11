# install `pip install boto3-stubs[ec2]`

import boto3


def ec2_resource_example() -> None:
    session = boto3.session.Session(region_name="us-west-1")

    resource = session.resource("ec2")

    # (mypy) error: Missing positional argument "Resources" in call
    #   to "create_tags" of "ServiceResource"
    # (mypy) error: Argument "Tags" to "create_tags" of "ServiceResource"
    #   has incompatible type "int"; expected "List[Tag]"
    resource.create_tags(Tags=123)


def ec2_client_example() -> None:
    client = boto3.client("ec2")

    # (mypy) error: Incompatible types (expression has type "int", TypedDict item
    #   "Key" has type "str")
    client.create_tags(Tags=[{"Key": 123}], Resources=[])


def main() -> None:
    ec2_resource_example()
    ec2_client_example()


if __name__ == "__main__":
    main()
