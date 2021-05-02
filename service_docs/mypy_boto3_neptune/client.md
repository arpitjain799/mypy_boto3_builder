# NeptuneClient for boto3 Neptune module

> [Index](../index.md) > [Neptune](./index.md) > NeptuneClient

Auto-generated documentation for [Neptune](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune)
type annotations stubs module [mypy_boto3_neptune](https://pypi.org/project/mypy-boto3-neptune/).

- [NeptuneClient for boto3 Neptune module](#neptuneclient-for-boto3-neptune-module)
  - [NeptuneClient](#neptuneclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_role_to_db_cluster](#add_role_to_db_cluster)
    - [add_source_identifier_to_subscription](#add_source_identifier_to_subscription)
    - [add_tags_to_resource](#add_tags_to_resource)
    - [apply_pending_maintenance_action](#apply_pending_maintenance_action)
    - [can_paginate](#can_paginate)
    - [copy_db_cluster_parameter_group](#copy_db_cluster_parameter_group)
    - [copy_db_cluster_snapshot](#copy_db_cluster_snapshot)
    - [copy_db_parameter_group](#copy_db_parameter_group)
    - [create_db_cluster](#create_db_cluster)
    - [create_db_cluster_endpoint](#create_db_cluster_endpoint)
    - [create_db_cluster_parameter_group](#create_db_cluster_parameter_group)
    - [create_db_cluster_snapshot](#create_db_cluster_snapshot)
    - [create_db_instance](#create_db_instance)
    - [create_db_parameter_group](#create_db_parameter_group)
    - [create_db_subnet_group](#create_db_subnet_group)
    - [create_event_subscription](#create_event_subscription)
    - [delete_db_cluster](#delete_db_cluster)
    - [delete_db_cluster_endpoint](#delete_db_cluster_endpoint)
    - [delete_db_cluster_parameter_group](#delete_db_cluster_parameter_group)
    - [delete_db_cluster_snapshot](#delete_db_cluster_snapshot)
    - [delete_db_instance](#delete_db_instance)
    - [delete_db_parameter_group](#delete_db_parameter_group)
    - [delete_db_subnet_group](#delete_db_subnet_group)
    - [delete_event_subscription](#delete_event_subscription)
    - [describe_db_cluster_endpoints](#describe_db_cluster_endpoints)
    - [describe_db_cluster_parameter_groups](#describe_db_cluster_parameter_groups)
    - [describe_db_cluster_parameters](#describe_db_cluster_parameters)
    - [describe_db_cluster_snapshot_attributes](#describe_db_cluster_snapshot_attributes)
    - [describe_db_cluster_snapshots](#describe_db_cluster_snapshots)
    - [describe_db_clusters](#describe_db_clusters)
    - [describe_db_engine_versions](#describe_db_engine_versions)
    - [describe_db_instances](#describe_db_instances)
    - [describe_db_parameter_groups](#describe_db_parameter_groups)
    - [describe_db_parameters](#describe_db_parameters)
    - [describe_db_subnet_groups](#describe_db_subnet_groups)
    - [describe_engine_default_cluster_parameters](#describe_engine_default_cluster_parameters)
    - [describe_engine_default_parameters](#describe_engine_default_parameters)
    - [describe_event_categories](#describe_event_categories)
    - [describe_event_subscriptions](#describe_event_subscriptions)
    - [describe_events](#describe_events)
    - [describe_orderable_db_instance_options](#describe_orderable_db_instance_options)
    - [describe_pending_maintenance_actions](#describe_pending_maintenance_actions)
    - [describe_valid_db_instance_modifications](#describe_valid_db_instance_modifications)
    - [failover_db_cluster](#failover_db_cluster)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [modify_db_cluster](#modify_db_cluster)
    - [modify_db_cluster_endpoint](#modify_db_cluster_endpoint)
    - [modify_db_cluster_parameter_group](#modify_db_cluster_parameter_group)
    - [modify_db_cluster_snapshot_attribute](#modify_db_cluster_snapshot_attribute)
    - [modify_db_instance](#modify_db_instance)
    - [modify_db_parameter_group](#modify_db_parameter_group)
    - [modify_db_subnet_group](#modify_db_subnet_group)
    - [modify_event_subscription](#modify_event_subscription)
    - [promote_read_replica_db_cluster](#promote_read_replica_db_cluster)
    - [reboot_db_instance](#reboot_db_instance)
    - [remove_role_from_db_cluster](#remove_role_from_db_cluster)
    - [remove_source_identifier_from_subscription](#remove_source_identifier_from_subscription)
    - [remove_tags_from_resource](#remove_tags_from_resource)
    - [reset_db_cluster_parameter_group](#reset_db_cluster_parameter_group)
    - [reset_db_parameter_group](#reset_db_parameter_group)
    - [restore_db_cluster_from_snapshot](#restore_db_cluster_from_snapshot)
    - [restore_db_cluster_to_point_in_time](#restore_db_cluster_to_point_in_time)
    - [start_db_cluster](#start_db_cluster)
    - [stop_db_cluster](#stop_db_cluster)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)
    - [get_paginator](#get_paginator-13)
    - [get_paginator](#get_paginator-14)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)

## NeptuneClient

Type annotations for `boto3.client("neptune")`

Can be used directly:

```python
from mypy_boto3_neptune.client import NeptuneClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_neptune.client import Exceptions

def handle_error(exc: Exceptions.AuthorizationNotFoundFault) -> None:
    ...
```


Exceptions:

- `Exceptions.AuthorizationNotFoundFault`
- `Exceptions.CertificateNotFoundFault`
- `Exceptions.ClientError`
- `Exceptions.DBClusterAlreadyExistsFault`
- `Exceptions.DBClusterEndpointAlreadyExistsFault`
- `Exceptions.DBClusterEndpointNotFoundFault`
- `Exceptions.DBClusterEndpointQuotaExceededFault`
- `Exceptions.DBClusterNotFoundFault`
- `Exceptions.DBClusterParameterGroupNotFoundFault`
- `Exceptions.DBClusterQuotaExceededFault`
- `Exceptions.DBClusterRoleAlreadyExistsFault`
- `Exceptions.DBClusterRoleNotFoundFault`
- `Exceptions.DBClusterRoleQuotaExceededFault`
- `Exceptions.DBClusterSnapshotAlreadyExistsFault`
- `Exceptions.DBClusterSnapshotNotFoundFault`
- `Exceptions.DBInstanceAlreadyExistsFault`
- `Exceptions.DBInstanceNotFoundFault`
- `Exceptions.DBParameterGroupAlreadyExistsFault`
- `Exceptions.DBParameterGroupNotFoundFault`
- `Exceptions.DBParameterGroupQuotaExceededFault`
- `Exceptions.DBSecurityGroupNotFoundFault`
- `Exceptions.DBSnapshotAlreadyExistsFault`
- `Exceptions.DBSnapshotNotFoundFault`
- `Exceptions.DBSubnetGroupAlreadyExistsFault`
- `Exceptions.DBSubnetGroupDoesNotCoverEnoughAZs`
- `Exceptions.DBSubnetGroupNotFoundFault`
- `Exceptions.DBSubnetGroupQuotaExceededFault`
- `Exceptions.DBSubnetQuotaExceededFault`
- `Exceptions.DBUpgradeDependencyFailureFault`
- `Exceptions.DomainNotFoundFault`
- `Exceptions.EventSubscriptionQuotaExceededFault`
- `Exceptions.InstanceQuotaExceededFault`
- `Exceptions.InsufficientDBClusterCapacityFault`
- `Exceptions.InsufficientDBInstanceCapacityFault`
- `Exceptions.InsufficientStorageClusterCapacityFault`
- `Exceptions.InvalidDBClusterEndpointStateFault`
- `Exceptions.InvalidDBClusterSnapshotStateFault`
- `Exceptions.InvalidDBClusterStateFault`
- `Exceptions.InvalidDBInstanceStateFault`
- `Exceptions.InvalidDBParameterGroupStateFault`
- `Exceptions.InvalidDBSecurityGroupStateFault`
- `Exceptions.InvalidDBSnapshotStateFault`
- `Exceptions.InvalidDBSubnetGroupStateFault`
- `Exceptions.InvalidDBSubnetStateFault`
- `Exceptions.InvalidEventSubscriptionStateFault`
- `Exceptions.InvalidRestoreFault`
- `Exceptions.InvalidSubnet`
- `Exceptions.InvalidVPCNetworkStateFault`
- `Exceptions.KMSKeyNotAccessibleFault`
- `Exceptions.OptionGroupNotFoundFault`
- `Exceptions.ProvisionedIopsNotAvailableInAZFault`
- `Exceptions.ResourceNotFoundFault`
- `Exceptions.SNSInvalidTopicFault`
- `Exceptions.SNSNoAuthorizationFault`
- `Exceptions.SNSTopicArnNotFoundFault`
- `Exceptions.SharedSnapshotQuotaExceededFault`
- `Exceptions.SnapshotQuotaExceededFault`
- `Exceptions.SourceNotFoundFault`
- `Exceptions.StorageQuotaExceededFault`
- `Exceptions.StorageTypeNotSupportedFault`
- `Exceptions.SubnetAlreadyInUse`
- `Exceptions.SubscriptionAlreadyExistFault`
- `Exceptions.SubscriptionCategoryNotFoundFault`
- `Exceptions.SubscriptionNotFoundFault`


## Methods


### add_role_to_db_cluster

Type annotations for `boto3.client("neptune").add_role_to_db_cluster` method.

[Client.add_role_to_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.add_role_to_db_cluster)

```python
def add_role_to_db_cluster(
    self,
    DBClusterIdentifier: str,
    RoleArn: str,
    FeatureName: str = None
) -> None:
    pass
```

### add_source_identifier_to_subscription

Type annotations for `boto3.client("neptune").add_source_identifier_to_subscription` method.

[Client.add_source_identifier_to_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.add_source_identifier_to_subscription)

```python
def add_source_identifier_to_subscription(
    self,
    SubscriptionName: str,
    SourceIdentifier: str
) -> AddSourceIdentifierToSubscriptionResultTypeDef:
    pass
```

### add_tags_to_resource

Type annotations for `boto3.client("neptune").add_tags_to_resource` method.

[Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.add_tags_to_resource)

```python
def add_tags_to_resource(
    self,
    ResourceName: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### apply_pending_maintenance_action

Type annotations for `boto3.client("neptune").apply_pending_maintenance_action` method.

[Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.apply_pending_maintenance_action)

```python
def apply_pending_maintenance_action(
    self,
    ResourceIdentifier: str,
    ApplyAction: str,
    OptInType: str
) -> ApplyPendingMaintenanceActionResultTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("neptune").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### copy_db_cluster_parameter_group

Type annotations for `boto3.client("neptune").copy_db_cluster_parameter_group` method.

[Client.copy_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.copy_db_cluster_parameter_group)

```python
def copy_db_cluster_parameter_group(
    self,
    SourceDBClusterParameterGroupIdentifier: str,
    TargetDBClusterParameterGroupIdentifier: str,
    TargetDBClusterParameterGroupDescription: str,
    Tags: List["TagTypeDef"] = None
) -> CopyDBClusterParameterGroupResultTypeDef:
    pass
```

### copy_db_cluster_snapshot

Type annotations for `boto3.client("neptune").copy_db_cluster_snapshot` method.

[Client.copy_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.copy_db_cluster_snapshot)

```python
def copy_db_cluster_snapshot(
    self,
    SourceDBClusterSnapshotIdentifier: str,
    TargetDBClusterSnapshotIdentifier: str,
    KmsKeyId: str = None,
    PreSignedUrl: str = None,
    CopyTags: bool = None,
    Tags: List["TagTypeDef"] = None,
    SourceRegion: str = None
) -> CopyDBClusterSnapshotResultTypeDef:
    pass
```

### copy_db_parameter_group

Type annotations for `boto3.client("neptune").copy_db_parameter_group` method.

[Client.copy_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.copy_db_parameter_group)

```python
def copy_db_parameter_group(
    self,
    SourceDBParameterGroupIdentifier: str,
    TargetDBParameterGroupIdentifier: str,
    TargetDBParameterGroupDescription: str,
    Tags: List["TagTypeDef"] = None
) -> CopyDBParameterGroupResultTypeDef:
    pass
```

### create_db_cluster

Type annotations for `boto3.client("neptune").create_db_cluster` method.

[Client.create_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.create_db_cluster)

```python
def create_db_cluster(
    self,
    DBClusterIdentifier: str,
    Engine: str,
    AvailabilityZones: List[str] = None,
    BackupRetentionPeriod: int = None,
    CharacterSetName: str = None,
    DatabaseName: str = None,
    DBClusterParameterGroupName: str = None,
    VpcSecurityGroupIds: List[str] = None,
    DBSubnetGroupName: str = None,
    EngineVersion: str = None,
    Port: int = None,
    MasterUsername: str = None,
    MasterUserPassword: str = None,
    OptionGroupName: str = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    ReplicationSourceIdentifier: str = None,
    Tags: List["TagTypeDef"] = None,
    StorageEncrypted: bool = None,
    KmsKeyId: str = None,
    PreSignedUrl: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnableCloudwatchLogsExports: List[str] = None,
    DeletionProtection: bool = None,
    SourceRegion: str = None
) -> CreateDBClusterResultTypeDef:
    pass
```

### create_db_cluster_endpoint

Type annotations for `boto3.client("neptune").create_db_cluster_endpoint` method.

[Client.create_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.create_db_cluster_endpoint)

```python
def create_db_cluster_endpoint(
    self,
    DBClusterIdentifier: str,
    DBClusterEndpointIdentifier: str,
    EndpointType: str,
    StaticMembers: List[str] = None,
    ExcludedMembers: List[str] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDBClusterEndpointOutputTypeDef:
    pass
```

### create_db_cluster_parameter_group

Type annotations for `boto3.client("neptune").create_db_cluster_parameter_group` method.

[Client.create_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.create_db_cluster_parameter_group)

```python
def create_db_cluster_parameter_group(
    self,
    DBClusterParameterGroupName: str,
    DBParameterGroupFamily: str,
    Description: str,
    Tags: List["TagTypeDef"] = None
) -> CreateDBClusterParameterGroupResultTypeDef:
    pass
```

### create_db_cluster_snapshot

Type annotations for `boto3.client("neptune").create_db_cluster_snapshot` method.

[Client.create_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.create_db_cluster_snapshot)

```python
def create_db_cluster_snapshot(
    self,
    DBClusterSnapshotIdentifier: str,
    DBClusterIdentifier: str,
    Tags: List["TagTypeDef"] = None
) -> CreateDBClusterSnapshotResultTypeDef:
    pass
```

### create_db_instance

Type annotations for `boto3.client("neptune").create_db_instance` method.

[Client.create_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.create_db_instance)

```python
def create_db_instance(
    self,
    DBInstanceIdentifier: str,
    DBInstanceClass: str,
    Engine: str,
    DBName: str = None,
    AllocatedStorage: int = None,
    MasterUsername: str = None,
    MasterUserPassword: str = None,
    DBSecurityGroups: List[str] = None,
    VpcSecurityGroupIds: List[str] = None,
    AvailabilityZone: str = None,
    DBSubnetGroupName: str = None,
    PreferredMaintenanceWindow: str = None,
    DBParameterGroupName: str = None,
    BackupRetentionPeriod: int = None,
    PreferredBackupWindow: str = None,
    Port: int = None,
    MultiAZ: bool = None,
    EngineVersion: str = None,
    AutoMinorVersionUpgrade: bool = None,
    LicenseModel: str = None,
    Iops: int = None,
    OptionGroupName: str = None,
    CharacterSetName: str = None,
    PubliclyAccessible: bool = None,
    Tags: List["TagTypeDef"] = None,
    DBClusterIdentifier: str = None,
    StorageType: str = None,
    TdeCredentialArn: str = None,
    TdeCredentialPassword: str = None,
    StorageEncrypted: bool = None,
    KmsKeyId: str = None,
    Domain: str = None,
    CopyTagsToSnapshot: bool = None,
    MonitoringInterval: int = None,
    MonitoringRoleArn: str = None,
    DomainIAMRoleName: str = None,
    PromotionTier: int = None,
    Timezone: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnablePerformanceInsights: bool = None,
    PerformanceInsightsKMSKeyId: str = None,
    EnableCloudwatchLogsExports: List[str] = None,
    DeletionProtection: bool = None
) -> CreateDBInstanceResultTypeDef:
    pass
```

### create_db_parameter_group

Type annotations for `boto3.client("neptune").create_db_parameter_group` method.

[Client.create_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.create_db_parameter_group)

```python
def create_db_parameter_group(
    self,
    DBParameterGroupName: str,
    DBParameterGroupFamily: str,
    Description: str,
    Tags: List["TagTypeDef"] = None
) -> CreateDBParameterGroupResultTypeDef:
    pass
```

### create_db_subnet_group

Type annotations for `boto3.client("neptune").create_db_subnet_group` method.

[Client.create_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.create_db_subnet_group)

```python
def create_db_subnet_group(
    self,
    DBSubnetGroupName: str,
    DBSubnetGroupDescription: str,
    SubnetIds: List[str],
    Tags: List["TagTypeDef"] = None
) -> CreateDBSubnetGroupResultTypeDef:
    pass
```

### create_event_subscription

Type annotations for `boto3.client("neptune").create_event_subscription` method.

[Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.create_event_subscription)

```python
def create_event_subscription(
    self,
    SubscriptionName: str,
    SnsTopicArn: str,
    SourceType: str = None,
    EventCategories: List[str] = None,
    SourceIds: List[str] = None,
    Enabled: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateEventSubscriptionResultTypeDef:
    pass
```

### delete_db_cluster

Type annotations for `boto3.client("neptune").delete_db_cluster` method.

[Client.delete_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.delete_db_cluster)

```python
def delete_db_cluster(
    self,
    DBClusterIdentifier: str,
    SkipFinalSnapshot: bool = None,
    FinalDBSnapshotIdentifier: str = None
) -> DeleteDBClusterResultTypeDef:
    pass
```

### delete_db_cluster_endpoint

Type annotations for `boto3.client("neptune").delete_db_cluster_endpoint` method.

[Client.delete_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.delete_db_cluster_endpoint)

```python
def delete_db_cluster_endpoint(
    self,
    DBClusterEndpointIdentifier: str
) -> DeleteDBClusterEndpointOutputTypeDef:
    pass
```

### delete_db_cluster_parameter_group

Type annotations for `boto3.client("neptune").delete_db_cluster_parameter_group` method.

[Client.delete_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.delete_db_cluster_parameter_group)

```python
def delete_db_cluster_parameter_group(
    self,
    DBClusterParameterGroupName: str
) -> None:
    pass
```

### delete_db_cluster_snapshot

Type annotations for `boto3.client("neptune").delete_db_cluster_snapshot` method.

[Client.delete_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.delete_db_cluster_snapshot)

```python
def delete_db_cluster_snapshot(
    self,
    DBClusterSnapshotIdentifier: str
) -> DeleteDBClusterSnapshotResultTypeDef:
    pass
```

### delete_db_instance

Type annotations for `boto3.client("neptune").delete_db_instance` method.

[Client.delete_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.delete_db_instance)

```python
def delete_db_instance(
    self,
    DBInstanceIdentifier: str,
    SkipFinalSnapshot: bool = None,
    FinalDBSnapshotIdentifier: str = None
) -> DeleteDBInstanceResultTypeDef:
    pass
```

### delete_db_parameter_group

Type annotations for `boto3.client("neptune").delete_db_parameter_group` method.

[Client.delete_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.delete_db_parameter_group)

```python
def delete_db_parameter_group(
    self,
    DBParameterGroupName: str
) -> None:
    pass
```

### delete_db_subnet_group

Type annotations for `boto3.client("neptune").delete_db_subnet_group` method.

[Client.delete_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.delete_db_subnet_group)

```python
def delete_db_subnet_group(
    self,
    DBSubnetGroupName: str
) -> None:
    pass
```

### delete_event_subscription

Type annotations for `boto3.client("neptune").delete_event_subscription` method.

[Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.delete_event_subscription)

```python
def delete_event_subscription(
    self,
    SubscriptionName: str
) -> DeleteEventSubscriptionResultTypeDef:
    pass
```

### describe_db_cluster_endpoints

Type annotations for `boto3.client("neptune").describe_db_cluster_endpoints` method.

[Client.describe_db_cluster_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_db_cluster_endpoints)

```python
def describe_db_cluster_endpoints(
    self,
    DBClusterIdentifier: str = None,
    DBClusterEndpointIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBClusterEndpointMessageTypeDef:
    pass
```

### describe_db_cluster_parameter_groups

Type annotations for `boto3.client("neptune").describe_db_cluster_parameter_groups` method.

[Client.describe_db_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_db_cluster_parameter_groups)

```python
def describe_db_cluster_parameter_groups(
    self,
    DBClusterParameterGroupName: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBClusterParameterGroupsMessageTypeDef:
    pass
```

### describe_db_cluster_parameters

Type annotations for `boto3.client("neptune").describe_db_cluster_parameters` method.

[Client.describe_db_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_db_cluster_parameters)

```python
def describe_db_cluster_parameters(
    self,
    DBClusterParameterGroupName: str,
    Source: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBClusterParameterGroupDetailsTypeDef:
    pass
```

### describe_db_cluster_snapshot_attributes

Type annotations for `boto3.client("neptune").describe_db_cluster_snapshot_attributes` method.

[Client.describe_db_cluster_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_db_cluster_snapshot_attributes)

```python
def describe_db_cluster_snapshot_attributes(
    self,
    DBClusterSnapshotIdentifier: str
) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
    pass
```

### describe_db_cluster_snapshots

Type annotations for `boto3.client("neptune").describe_db_cluster_snapshots` method.

[Client.describe_db_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_db_cluster_snapshots)

```python
def describe_db_cluster_snapshots(
    self,
    DBClusterIdentifier: str = None,
    DBClusterSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None
) -> DBClusterSnapshotMessageTypeDef:
    pass
```

### describe_db_clusters

Type annotations for `boto3.client("neptune").describe_db_clusters` method.

[Client.describe_db_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_db_clusters)

```python
def describe_db_clusters(
    self,
    DBClusterIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBClusterMessageTypeDef:
    pass
```

### describe_db_engine_versions

Type annotations for `boto3.client("neptune").describe_db_engine_versions` method.

[Client.describe_db_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_db_engine_versions)

```python
def describe_db_engine_versions(
    self,
    Engine: str = None,
    EngineVersion: str = None,
    DBParameterGroupFamily: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None,
    DefaultOnly: bool = None,
    ListSupportedCharacterSets: bool = None,
    ListSupportedTimezones: bool = None
) -> DBEngineVersionMessageTypeDef:
    pass
```

### describe_db_instances

Type annotations for `boto3.client("neptune").describe_db_instances` method.

[Client.describe_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_db_instances)

```python
def describe_db_instances(
    self,
    DBInstanceIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBInstanceMessageTypeDef:
    pass
```

### describe_db_parameter_groups

Type annotations for `boto3.client("neptune").describe_db_parameter_groups` method.

[Client.describe_db_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_db_parameter_groups)

```python
def describe_db_parameter_groups(
    self,
    DBParameterGroupName: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBParameterGroupsMessageTypeDef:
    pass
```

### describe_db_parameters

Type annotations for `boto3.client("neptune").describe_db_parameters` method.

[Client.describe_db_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_db_parameters)

```python
def describe_db_parameters(
    self,
    DBParameterGroupName: str,
    Source: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBParameterGroupDetailsTypeDef:
    pass
```

### describe_db_subnet_groups

Type annotations for `boto3.client("neptune").describe_db_subnet_groups` method.

[Client.describe_db_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_db_subnet_groups)

```python
def describe_db_subnet_groups(
    self,
    DBSubnetGroupName: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DBSubnetGroupMessageTypeDef:
    pass
```

### describe_engine_default_cluster_parameters

Type annotations for `boto3.client("neptune").describe_engine_default_cluster_parameters` method.

[Client.describe_engine_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_engine_default_cluster_parameters)

```python
def describe_engine_default_cluster_parameters(
    self,
    DBParameterGroupFamily: str,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeEngineDefaultClusterParametersResultTypeDef:
    pass
```

### describe_engine_default_parameters

Type annotations for `boto3.client("neptune").describe_engine_default_parameters` method.

[Client.describe_engine_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_engine_default_parameters)

```python
def describe_engine_default_parameters(
    self,
    DBParameterGroupFamily: str,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeEngineDefaultParametersResultTypeDef:
    pass
```

### describe_event_categories

Type annotations for `boto3.client("neptune").describe_event_categories` method.

[Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_event_categories)

```python
def describe_event_categories(
    self,
    SourceType: str = None,
    Filters: List[FilterTypeDef] = None
) -> EventCategoriesMessageTypeDef:
    pass
```

### describe_event_subscriptions

Type annotations for `boto3.client("neptune").describe_event_subscriptions` method.

[Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_event_subscriptions)

```python
def describe_event_subscriptions(
    self,
    SubscriptionName: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> EventSubscriptionsMessageTypeDef:
    pass
```

### describe_events

Type annotations for `boto3.client("neptune").describe_events` method.

[Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_events)

```python
def describe_events(
    self,
    SourceIdentifier: str = None,
    SourceType: SourceType = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Duration: int = None,
    EventCategories: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> EventsMessageTypeDef:
    pass
```

### describe_orderable_db_instance_options

Type annotations for `boto3.client("neptune").describe_orderable_db_instance_options` method.

[Client.describe_orderable_db_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_orderable_db_instance_options)

```python
def describe_orderable_db_instance_options(
    self,
    Engine: str,
    EngineVersion: str = None,
    DBInstanceClass: str = None,
    LicenseModel: str = None,
    Vpc: bool = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> OrderableDBInstanceOptionsMessageTypeDef:
    pass
```

### describe_pending_maintenance_actions

Type annotations for `boto3.client("neptune").describe_pending_maintenance_actions` method.

[Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_pending_maintenance_actions)

```python
def describe_pending_maintenance_actions(
    self,
    ResourceIdentifier: str = None,
    Filters: List[FilterTypeDef] = None,
    Marker: str = None,
    MaxRecords: int = None
) -> PendingMaintenanceActionsMessageTypeDef:
    pass
```

### describe_valid_db_instance_modifications

Type annotations for `boto3.client("neptune").describe_valid_db_instance_modifications` method.

[Client.describe_valid_db_instance_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.describe_valid_db_instance_modifications)

```python
def describe_valid_db_instance_modifications(
    self,
    DBInstanceIdentifier: str
) -> DescribeValidDBInstanceModificationsResultTypeDef:
    pass
```

### failover_db_cluster

Type annotations for `boto3.client("neptune").failover_db_cluster` method.

[Client.failover_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.failover_db_cluster)

```python
def failover_db_cluster(
    self,
    DBClusterIdentifier: str = None,
    TargetDBInstanceIdentifier: str = None
) -> FailoverDBClusterResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("neptune").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("neptune").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceName: str,
    Filters: List[FilterTypeDef] = None
) -> TagListMessageTypeDef:
    pass
```

### modify_db_cluster

Type annotations for `boto3.client("neptune").modify_db_cluster` method.

[Client.modify_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.modify_db_cluster)

```python
def modify_db_cluster(
    self,
    DBClusterIdentifier: str,
    NewDBClusterIdentifier: str = None,
    ApplyImmediately: bool = None,
    BackupRetentionPeriod: int = None,
    DBClusterParameterGroupName: str = None,
    VpcSecurityGroupIds: List[str] = None,
    Port: int = None,
    MasterUserPassword: str = None,
    OptionGroupName: str = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
    EngineVersion: str = None,
    DeletionProtection: bool = None
) -> ModifyDBClusterResultTypeDef:
    pass
```

### modify_db_cluster_endpoint

Type annotations for `boto3.client("neptune").modify_db_cluster_endpoint` method.

[Client.modify_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.modify_db_cluster_endpoint)

```python
def modify_db_cluster_endpoint(
    self,
    DBClusterEndpointIdentifier: str,
    EndpointType: str = None,
    StaticMembers: List[str] = None,
    ExcludedMembers: List[str] = None
) -> ModifyDBClusterEndpointOutputTypeDef:
    pass
```

### modify_db_cluster_parameter_group

Type annotations for `boto3.client("neptune").modify_db_cluster_parameter_group` method.

[Client.modify_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.modify_db_cluster_parameter_group)

```python
def modify_db_cluster_parameter_group(
    self,
    DBClusterParameterGroupName: str,
    Parameters: List["ParameterTypeDef"]
) -> DBClusterParameterGroupNameMessageTypeDef:
    pass
```

### modify_db_cluster_snapshot_attribute

Type annotations for `boto3.client("neptune").modify_db_cluster_snapshot_attribute` method.

[Client.modify_db_cluster_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.modify_db_cluster_snapshot_attribute)

```python
def modify_db_cluster_snapshot_attribute(
    self,
    DBClusterSnapshotIdentifier: str,
    AttributeName: str,
    ValuesToAdd: List[str] = None,
    ValuesToRemove: List[str] = None
) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
    pass
```

### modify_db_instance

Type annotations for `boto3.client("neptune").modify_db_instance` method.

[Client.modify_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.modify_db_instance)

```python
def modify_db_instance(
    self,
    DBInstanceIdentifier: str,
    AllocatedStorage: int = None,
    DBInstanceClass: str = None,
    DBSubnetGroupName: str = None,
    DBSecurityGroups: List[str] = None,
    VpcSecurityGroupIds: List[str] = None,
    ApplyImmediately: bool = None,
    MasterUserPassword: str = None,
    DBParameterGroupName: str = None,
    BackupRetentionPeriod: int = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    MultiAZ: bool = None,
    EngineVersion: str = None,
    AllowMajorVersionUpgrade: bool = None,
    AutoMinorVersionUpgrade: bool = None,
    LicenseModel: str = None,
    Iops: int = None,
    OptionGroupName: str = None,
    NewDBInstanceIdentifier: str = None,
    StorageType: str = None,
    TdeCredentialArn: str = None,
    TdeCredentialPassword: str = None,
    CACertificateIdentifier: str = None,
    Domain: str = None,
    CopyTagsToSnapshot: bool = None,
    MonitoringInterval: int = None,
    DBPortNumber: int = None,
    PubliclyAccessible: bool = None,
    MonitoringRoleArn: str = None,
    DomainIAMRoleName: str = None,
    PromotionTier: int = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnablePerformanceInsights: bool = None,
    PerformanceInsightsKMSKeyId: str = None,
    CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
    DeletionProtection: bool = None
) -> ModifyDBInstanceResultTypeDef:
    pass
```

### modify_db_parameter_group

Type annotations for `boto3.client("neptune").modify_db_parameter_group` method.

[Client.modify_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.modify_db_parameter_group)

```python
def modify_db_parameter_group(
    self,
    DBParameterGroupName: str,
    Parameters: List["ParameterTypeDef"]
) -> DBParameterGroupNameMessageTypeDef:
    pass
```

### modify_db_subnet_group

Type annotations for `boto3.client("neptune").modify_db_subnet_group` method.

[Client.modify_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.modify_db_subnet_group)

```python
def modify_db_subnet_group(
    self,
    DBSubnetGroupName: str,
    SubnetIds: List[str],
    DBSubnetGroupDescription: str = None
) -> ModifyDBSubnetGroupResultTypeDef:
    pass
```

### modify_event_subscription

Type annotations for `boto3.client("neptune").modify_event_subscription` method.

[Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.modify_event_subscription)

```python
def modify_event_subscription(
    self,
    SubscriptionName: str,
    SnsTopicArn: str = None,
    SourceType: str = None,
    EventCategories: List[str] = None,
    Enabled: bool = None
) -> ModifyEventSubscriptionResultTypeDef:
    pass
```

### promote_read_replica_db_cluster

Type annotations for `boto3.client("neptune").promote_read_replica_db_cluster` method.

[Client.promote_read_replica_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.promote_read_replica_db_cluster)

```python
def promote_read_replica_db_cluster(
    self,
    DBClusterIdentifier: str
) -> PromoteReadReplicaDBClusterResultTypeDef:
    pass
```

### reboot_db_instance

Type annotations for `boto3.client("neptune").reboot_db_instance` method.

[Client.reboot_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.reboot_db_instance)

```python
def reboot_db_instance(
    self,
    DBInstanceIdentifier: str,
    ForceFailover: bool = None
) -> RebootDBInstanceResultTypeDef:
    pass
```

### remove_role_from_db_cluster

Type annotations for `boto3.client("neptune").remove_role_from_db_cluster` method.

[Client.remove_role_from_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.remove_role_from_db_cluster)

```python
def remove_role_from_db_cluster(
    self,
    DBClusterIdentifier: str,
    RoleArn: str,
    FeatureName: str = None
) -> None:
    pass
```

### remove_source_identifier_from_subscription

Type annotations for `boto3.client("neptune").remove_source_identifier_from_subscription` method.

[Client.remove_source_identifier_from_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.remove_source_identifier_from_subscription)

```python
def remove_source_identifier_from_subscription(
    self,
    SubscriptionName: str,
    SourceIdentifier: str
) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
    pass
```

### remove_tags_from_resource

Type annotations for `boto3.client("neptune").remove_tags_from_resource` method.

[Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.remove_tags_from_resource)

```python
def remove_tags_from_resource(
    self,
    ResourceName: str,
    TagKeys: List[str]
) -> None:
    pass
```

### reset_db_cluster_parameter_group

Type annotations for `boto3.client("neptune").reset_db_cluster_parameter_group` method.

[Client.reset_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.reset_db_cluster_parameter_group)

```python
def reset_db_cluster_parameter_group(
    self,
    DBClusterParameterGroupName: str,
    ResetAllParameters: bool = None,
    Parameters: List["ParameterTypeDef"] = None
) -> DBClusterParameterGroupNameMessageTypeDef:
    pass
```

### reset_db_parameter_group

Type annotations for `boto3.client("neptune").reset_db_parameter_group` method.

[Client.reset_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.reset_db_parameter_group)

```python
def reset_db_parameter_group(
    self,
    DBParameterGroupName: str,
    ResetAllParameters: bool = None,
    Parameters: List["ParameterTypeDef"] = None
) -> DBParameterGroupNameMessageTypeDef:
    pass
```

### restore_db_cluster_from_snapshot

Type annotations for `boto3.client("neptune").restore_db_cluster_from_snapshot` method.

[Client.restore_db_cluster_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.restore_db_cluster_from_snapshot)

```python
def restore_db_cluster_from_snapshot(
    self,
    DBClusterIdentifier: str,
    SnapshotIdentifier: str,
    Engine: str,
    AvailabilityZones: List[str] = None,
    EngineVersion: str = None,
    Port: int = None,
    DBSubnetGroupName: str = None,
    DatabaseName: str = None,
    OptionGroupName: str = None,
    VpcSecurityGroupIds: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    KmsKeyId: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnableCloudwatchLogsExports: List[str] = None,
    DBClusterParameterGroupName: str = None,
    DeletionProtection: bool = None
) -> RestoreDBClusterFromSnapshotResultTypeDef:
    pass
```

### restore_db_cluster_to_point_in_time

Type annotations for `boto3.client("neptune").restore_db_cluster_to_point_in_time` method.

[Client.restore_db_cluster_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.restore_db_cluster_to_point_in_time)

```python
def restore_db_cluster_to_point_in_time(
    self,
    DBClusterIdentifier: str,
    SourceDBClusterIdentifier: str,
    RestoreType: str = None,
    RestoreToTime: datetime = None,
    UseLatestRestorableTime: bool = None,
    Port: int = None,
    DBSubnetGroupName: str = None,
    OptionGroupName: str = None,
    VpcSecurityGroupIds: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    KmsKeyId: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnableCloudwatchLogsExports: List[str] = None,
    DBClusterParameterGroupName: str = None,
    DeletionProtection: bool = None
) -> RestoreDBClusterToPointInTimeResultTypeDef:
    pass
```

### start_db_cluster

Type annotations for `boto3.client("neptune").start_db_cluster` method.

[Client.start_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.start_db_cluster)

```python
def start_db_cluster(
    self,
    DBClusterIdentifier: str
) -> StartDBClusterResultTypeDef:
    pass
```

### stop_db_cluster

Type annotations for `boto3.client("neptune").stop_db_cluster` method.

[Client.stop_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client.stop_db_cluster)

```python
def stop_db_cluster(
    self,
    DBClusterIdentifier: str
) -> StopDBClusterResultTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeDBClusterEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterEndpoints)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDBClusterEndpointsPaginatorName
) -> DescribeDBClusterEndpointsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeDBClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameterGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDBClusterParameterGroupsPaginatorName
) -> DescribeDBClusterParameterGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeDBClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDBClusterParametersPaginatorName
) -> DescribeDBClusterParametersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeDBClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterSnapshots)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDBClusterSnapshotsPaginatorName
) -> DescribeDBClusterSnapshotsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDBClustersPaginatorName
) -> DescribeDBClustersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBEngineVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDBEngineVersionsPaginatorName
) -> DescribeDBEngineVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDBInstancesPaginatorName
) -> DescribeDBInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeDBParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameterGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDBParameterGroupsPaginatorName
) -> DescribeDBParameterGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeDBParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDBParametersPaginatorName
) -> DescribeDBParametersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBSubnetGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDBSubnetGroupsPaginatorName
) -> DescribeDBSubnetGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeEngineDefaultParameters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEngineDefaultParametersPaginatorName
) -> DescribeEngineDefaultParametersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeEventSubscriptions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventSubscriptionsPaginatorName
) -> DescribeEventSubscriptionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventsPaginatorName
) -> DescribeEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeOrderableDBInstanceOptions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeOrderableDBInstanceOptionsPaginatorName
) -> DescribeOrderableDBInstanceOptionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("neptune").get_paginator` method.

[Paginator.DescribePendingMaintenanceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribePendingMaintenanceActions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribePendingMaintenanceActionsPaginatorName
) -> DescribePendingMaintenanceActionsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("neptune").get_waiter` method.

[Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Waiter.DBInstanceAvailable)

```python
@overload
def get_waiter(
    self,
    waiter_name: DBInstanceAvailableWaiterName
) -> DBInstanceAvailableWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("neptune").get_waiter` method.

[Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Waiter.DBInstanceDeleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: DBInstanceDeletedWaiterName
) -> DBInstanceDeletedWaiter:
    pass
```