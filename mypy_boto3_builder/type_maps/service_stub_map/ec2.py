"""
EC2 service injected methods.
"""


from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.typed_dicts import ec2_tag_type

create_tags_method = Method(
    "create_tags",
    [
        Argument("self", None),
        Argument.kwflag(),
        Argument("Resources", TypeSubscript(Type.Sequence, [Type.str])),
        Argument("Tags", TypeSubscript(Type.Sequence, [ec2_tag_type])),
        Argument("DryRun", Type.bool, Type.Ellipsis),
    ],
    Type.none,
)

delete_tags_method = Method(
    "delete_tags",
    [
        Argument("self", None),
        Argument.kwflag(),
        Argument("Resources", TypeSubscript(Type.Sequence, [Type.str])),
        Argument("Tags", TypeSubscript(Type.Sequence, [ec2_tag_type]), Type.Ellipsis),
        Argument("DryRun", Type.bool, Type.Ellipsis),
    ],
    Type.none,
)

CLIENT_METHODS = [
    create_tags_method.copy(),
    delete_tags_method.copy(),
]
INSTANCE_METHODS = [
    create_tags_method.copy().remove_argument("Resources"),
    delete_tags_method.copy().remove_argument("Resources"),
]
COMMON_METHODS = [
    create_tags_method.copy().remove_argument("Resources"),
]
