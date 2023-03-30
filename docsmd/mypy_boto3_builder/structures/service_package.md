# ServicePackage

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
ServicePackage

> Auto-generated documentation for [mypy_boto3_builder.structures.service_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py) module.

## ServicePackage

[Show source in service_package.py:27](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L27)

Parsed Service package.

#### Signature

```python
class ServicePackage(Package):
    def __init__(
        self,
        data: type[BasePackageData],
        service_name: ServiceName,
        client: Client | None = None,
        service_resource: ServiceResource | None = None,
        waiters: Iterable[Waiter] = (),
        paginators: Iterable[Paginator] = (),
        typed_dicts: Iterable[TypeTypedDict] = (),
        literals: Iterable[TypeLiteral] = (),
        helper_functions: Iterable[Function] = (),
    ):
        ...
```

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [Function](./function.md#function)
- [Package](./package.md#package)
- [Paginator](./paginator.md#paginator)
- [ServiceName](../service_name.md#servicename)
- [TypeLiteral](../type_annotations/type_literal.md#typeliteral)
- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)
- [Waiter](./waiter.md#waiter)

### ServicePackage().client

[Show source in service_package.py:56](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L56)

Service Client.

#### Signature

```python
@property
def client(self) -> Client:
    ...
```

#### See also

- [Client](./client.md#client)

### ServicePackage().extract_literals

[Show source in service_package.py:65](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L65)

Extract literals from children.

#### Signature

```python
def extract_literals(self) -> list[TypeLiteral]:
    ...
```

#### See also

- [TypeLiteral](../type_annotations/type_literal.md#typeliteral)

### ServicePackage().extract_typed_dicts

[Show source in service_package.py:119](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L119)

Extract typed dicts from children.

Attempts to resolve circular typed dicts.

#### Signature

```python
def extract_typed_dicts(self) -> list[TypeTypedDict]:
    ...
```

#### See also

- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)

### ServicePackage().get_client_required_import_records

[Show source in service_package.py:191](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L191)

Get import records for `client.py[i]`.

#### Signature

```python
def get_client_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_doc_link

[Show source in service_package.py:309](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L309)

Get link to local docs with anchor.

#### Arguments

- `file` - HTML file name
- `parts` - Anchor parts

#### Signature

```python
def get_doc_link(
    self,
    file: Literal[
        "client", "service_resource", "waiters", "paginators", "type_defs", "literals"
    ],
    *parts: str
) -> str:
    ...
```

### ServicePackage().get_init_all_names

[Show source in service_package.py:174](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L174)

Get `__all__` statement names for `__init__.py[i]`.

#### Signature

```python
def get_init_all_names(self) -> list[str]:
    ...
```

### ServicePackage().get_init_import_records

[Show source in service_package.py:139](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L139)

Get import records for `__init__.py[i]`.

#### Signature

```python
def get_init_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_literals_required_import_records

[Show source in service_package.py:274](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L274)

Get import records for `literals.py[i]`.

#### Signature

```python
def get_literals_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_local_doc_link

[Show source in service_package.py:334](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L334)

Get link to local docs.

#### Signature

```python
def get_local_doc_link(self, service_name: ServiceName | None = None) -> str:
    ...
```

### ServicePackage().get_paginator_required_import_records

[Show source in service_package.py:219](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L219)

Get import records for `paginator.py[i]`.

#### Signature

```python
def get_paginator_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_service_resource_required_import_records

[Show source in service_package.py:204](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L204)

Get import records for `service_resource.py[i]`.

#### Signature

```python
def get_service_resource_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_type_defs_required_import_records

[Show source in service_package.py:247](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L247)

Get import records for `type_defs.py[i]`.

#### Signature

```python
def get_type_defs_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_waiter_required_import_records

[Show source in service_package.py:233](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L233)

Get import records for `waiter.py[i]`.

#### Signature

```python
def get_waiter_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().iterate_types

[Show source in service_package.py:127](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L127)

Iterate over type annotations from Client, ServiceResource, waiters and paginators.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### ServicePackage().validate

[Show source in service_package.py:283](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L283)

Validate parsed module.

Finds duplicated names.
Finds conflicts with reserved Python words.

#### Signature

```python
def validate(self) -> None:
    ...
```