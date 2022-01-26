from typing import Any, Dict, List, Optional, Type, TypeVar

NOT_SET: object

class NoShapeFoundError(Exception): ...
class InvalidShapeError(Exception): ...
class OperationNotFoundError(Exception): ...
class InvalidShapeReferenceError(Exception): ...

_R = TypeVar("_R")

class ServiceId(str):
    def hyphenize(self) -> str: ...

class Shape:
    SERIALIZED_ATTRS: List[str]
    METADATA_ATTRS: List[str]
    MAP_TYPE: Type[Dict[str, Any]]
    def __init__(
        self,
        shape_name: str,
        shape_model: Dict[str, Any],
        shape_resolver: Optional["ShapeResolver"] = ...,
    ) -> None:
        self.name: str
        self.type_name: str
        self.documentation: str
    @property
    def serialization(self) -> Dict[str, Any]: ...
    @property
    def metadata(self) -> Dict[str, Any]: ...
    @property
    def required_members(self) -> List[Shape]: ...
    @property
    def event_stream_name(self) -> None: ...

class StructureShape(Shape):
    @property
    def members(self) -> Dict[str, Any]: ...
    @property
    def error_code(self) -> str: ...
    @property
    def is_document_type(self) -> bool: ...
    @property
    def is_tagged_union(self) -> bool: ...

class ListShape(Shape):
    @property
    def member(self) -> Shape: ...

class MapShape(Shape):
    @property
    def key(self) -> Shape: ...
    @property
    def value(self) -> Shape: ...

class StringShape(Shape):
    @property
    def enum(self) -> List[str]: ...

class ServiceModel:
    def __init__(
        self, service_description: Dict[str, Any], service_name: Optional[str] = ...
    ) -> None:
        self.metadata: Dict[str, Any]
    def shape_for(
        self, shape_name: str, member_traits: Optional[Dict[str, Any]] = ...
    ) -> Shape: ...
    def shape_for_error_code(self, error_code: int) -> Shape: ...
    def resolve_shape_ref(self, shape_ref: str) -> Shape: ...
    @property
    def shape_names(self) -> List[str]: ...
    @property
    def error_shapes(self) -> List[Shape]: ...
    def operation_model(self, operation_name: str) -> "OperationModel": ...
    @property
    def documentation(self) -> str: ...
    @property
    def operation_names(self) -> List[str]: ...
    @property
    def service_name(self) -> str: ...
    @property
    def service_id(self) -> ServiceId: ...
    @property
    def signing_name(self) -> str: ...
    @property
    def api_version(self) -> str: ...
    @property
    def protocol(self) -> str: ...
    @property
    def endpoint_prefix(self) -> str: ...
    @property
    def endpoint_discovery_operation(self) -> "OperationModel": ...
    @property
    def endpoint_discovery_required(self) -> bool: ...
    @property
    def signature_version(self) -> str: ...
    @signature_version.setter
    def signature_version(self, value: str) -> None: ...

class OperationModel:
    def __init__(
        self,
        operation_model: Dict[str, Any],
        service_model: ServiceModel,
        name: Optional[str] = None,
    ) -> None:
        self.metadata: Dict[str, Any]
        self.http: Dict[str, Any]
    @property
    def name(self) -> str: ...
    @property
    def wire_name(self) -> str: ...
    @property
    def service_model(self) -> ServiceModel: ...
    @property
    def documentation(self) -> str: ...
    @property
    def deprecated(self) -> bool: ...
    @property
    def endpoint_discovery(self) -> Optional["OperationModel"]: ...
    @property
    def is_endpoint_discovery_operation(self) -> bool: ...
    @property
    def input_shape(self) -> StructureShape: ...
    @property
    def output_shape(self) -> StructureShape: ...
    @property
    def idempotent_members(self) -> List[str]: ...
    @property
    def auth_type(self) -> Optional[str]: ...
    @property
    def error_shapes(self) -> List[Shape]: ...
    @property
    def endpoint(self) -> Optional[str]: ...
    @property
    def http_checksum_required(self) -> bool: ...
    @property
    def has_event_stream_input(self) -> bool: ...
    @property
    def has_event_stream_output(self) -> bool: ...
    def get_event_stream_input(self) -> Optional[Shape]: ...
    def get_event_stream_output(self) -> Optional[Shape]: ...
    @property
    def has_streaming_input(self) -> bool: ...
    @property
    def has_streaming_output(self) -> bool: ...
    def get_streaming_input(self) -> Optional[Shape]: ...
    def get_streaming_output(self) -> Optional[Shape]: ...

class ShapeResolver:
    SHAPE_CLASSES: Dict[str, Shape]
    def __init__(self, shape_map: Dict[str, Shape]) -> None: ...
    def get_shape_by_name(
        self, shape_name: str, member_traits: Optional[Dict[str, Any]] = ...
    ) -> Shape: ...
    def resolve_shape_ref(self, shape_ref: Dict[str, Any]) -> Shape: ...

class UnresolvableShapeMap:
    def get_shape_by_name(
        self, shape_name: str, member_traits: Optional[Dict[str, Any]] = ...
    ) -> Shape: ...
    def resolve_shape_ref(self, shape_ref: Dict[str, Any]) -> Shape: ...

class DenormalizedStructureBuilder:
    def __init__(self, name: Optional[str] = ...) -> None:
        self.name: str
        self.members: Dict[str, Any]
    def with_members(self: _R, members: Dict[str, Any]) -> _R: ...
    def build_model(self) -> StructureShape: ...

class ShapeNameGenerator:
    def __init__(self) -> None: ...
    def new_shape_name(self, type_name: str) -> str: ...
