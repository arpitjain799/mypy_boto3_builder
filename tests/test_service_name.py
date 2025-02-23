import pytest

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog


class TestServiceName:
    def test_init(self) -> None:
        service_name = ServiceName("my-service", "MyService")
        assert service_name.name == "my-service"
        assert service_name.import_name == "my_service"
        assert service_name.class_name == "MyService"
        assert service_name.boto3_version == "latest"
        assert service_name.boto3_name == "my-service"
        assert service_name.extras_name == "my-service"
        assert (
            service_name.boto3_doc_link
            == "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/my-service.html#MyService"
        )

    def test_special_name(self) -> None:
        assert ServiceName("lambda", "MyService").import_name == "lambda_"

    def test_is_essential(self) -> None:
        assert not ServiceName("my-service", "MyService").is_essential()
        assert ServiceName("lambda", "MyService").is_essential()

    def test_is_custom_resource(self) -> None:
        assert ServiceName("dynamodb", "DynamoDB").is_custom_resource("Table")
        assert ServiceName("dynamodb", "DynamoDB").is_custom_resource("ServiceResource")
        assert not ServiceName("dynamodb", "DynamoDB").is_custom_resource("Condition")
        assert not ServiceName("ec2", "EC2").is_custom_resource("ServiceResource")


class TestServiceNameCatalog:
    def test_add(self) -> None:
        assert ServiceNameCatalog.add("test", "Test").name == "test"
        assert ServiceNameCatalog.add("test", "Test").name == "test"
