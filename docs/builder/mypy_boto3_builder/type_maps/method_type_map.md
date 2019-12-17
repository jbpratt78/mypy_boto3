# Method Type Map

> Auto-generated documentation for [builder.mypy_boto3_builder.type_maps.method_type_map](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_maps/method_type_map.py) module.

String to type annotation map that find type annotation by method and argument name.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Maps](index.md#type-maps) / Method Type Map
    - [get_method_type_stub](#get_method_type_stub)

## get_method_type_stub

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_maps/method_type_map.py#L111)

```python
def get_method_type_stub(
    service_name: ServiceName,
    class_name: str,
    method_name: str,
    argument_name: str,
) -> Optional[FakeAnnotation]:
```

Get stub type for method argument.

#### Arguments

- `service_name` - Service name.
- `class_name` - Parent class name.
- `method_name` - Method name.
- `argument_name` - Argument name.

#### Returns

Type annotation or None.
