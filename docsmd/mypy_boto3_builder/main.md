# Main

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](./index.md#mypy-boto3-builder) /
Main

> Auto-generated documentation for [mypy_boto3_builder.main](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py) module.

## generate_product

[Show source in main.py:104](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L104)

Generate a selected product.

#### Arguments

- `product` - Product to generate
- `args` - CLI namespace
- `session` - Boto3 session
- `service_names` - Selected service names
- `master_service_names` - Service names included in master

#### Signature

```python
def generate_product(
    product: Product,
    args: Namespace,
    session: Session,
    service_names: Sequence[ServiceName],
    master_service_names: Sequence[ServiceName],
) -> None:
    ...
```

#### See also

- [Namespace](./cli_parser.md#namespace)
- [Product](./constants.md#product)
- [ServiceName](./service_name.md#servicename)



## get_available_service_names

[Show source in main.py:65](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L65)

Get a list of boto3 supported service names.

#### Arguments

- `session` - Boto3 session

#### Returns

A list of supported services.

#### Signature

```python
def get_available_service_names(session: Session) -> list[ServiceName]:
    ...
```

#### See also

- [ServiceName](./service_name.md#servicename)



## get_generator_cls

[Show source in main.py:87](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L87)

Get Generator class for a product.

#### Raises

- `ValueError` - If product is not supported.

#### Signature

```python
def get_generator_cls(product: Product) -> type[BaseGenerator]:
    ...
```

#### See also

- [BaseGenerator](generators/base_generator.md#basegenerator)
- [Product](./constants.md#product)



## get_selected_service_names

[Show source in main.py:25](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L25)

Get a list of selected service names.

Supports `updated` to select only services updated in currect `boto3` release.
Supports `all` to select all available service names.

#### Arguments

- `selected` - Selected service names as strings.
- `available` - All ServiceNames available in current boto3 release.

#### Returns

A list of selected ServiceNames.

#### Signature

```python
def get_selected_service_names(
    selected: Iterable[str], available: Iterable[ServiceName]
) -> list[ServiceName]:
    ...
```

#### See also

- [ServiceName](./service_name.md#servicename)



## main

[Show source in main.py:135](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L135)

Main entrypoint for builder.

#### Signature

```python
def main() -> None:
    ...
```