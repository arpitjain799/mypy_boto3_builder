# Structures for boto3 S3Outposts module

> [Index](../index.md) > [S3Outposts](./index.md) > Structures

Auto-generated documentation for [S3Outposts](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts)
type annotations stubs module [mypy_boto3_s3outposts](https://pypi.org/project/mypy-boto3-s3outposts/).

- [Structures for boto3 S3Outposts module](#structures-for-boto3-s3outposts-module)
  - [EndpointTypeDef](#endpointtypedef)
  - [NetworkInterfaceTypeDef](#networkinterfacetypedef)
  - [CreateEndpointResultTypeDef](#createendpointresulttypedef)
  - [ListEndpointsResultTypeDef](#listendpointsresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## EndpointTypeDef

```python
from mypy_boto3_s3outposts.type_defs import EndpointTypeDef
```




Optional fields:
- `EndpointArn`: `str`
- `OutpostsId`: `str`
- `CidrBlock`: `str`
- `Status`: `EndpointStatus`
- `CreationTime`: `datetime`
- `NetworkInterfaces`: `List["NetworkInterfaceTypeDef"]`


## NetworkInterfaceTypeDef

```python
from mypy_boto3_s3outposts.type_defs import NetworkInterfaceTypeDef
```




Optional fields:
- `NetworkInterfaceId`: `str`


## CreateEndpointResultTypeDef

```python
from mypy_boto3_s3outposts.type_defs import CreateEndpointResultTypeDef
```




Optional fields:
- `EndpointArn`: `str`


## ListEndpointsResultTypeDef

```python
from mypy_boto3_s3outposts.type_defs import ListEndpointsResultTypeDef
```




Optional fields:
- `Endpoints`: `List["EndpointTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_s3outposts.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`
