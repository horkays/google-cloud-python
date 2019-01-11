# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/scheduler_v1beta1/proto/target.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/scheduler_v1beta1/proto/target.proto",
    package="google.cloud.scheduler.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        '\n"com.google.cloud.scheduler.v1beta1B\013TargetProtoP\001ZGgoogle.golang.org/genproto/googleapis/cloud/scheduler/v1beta1;scheduler'
    ),
    serialized_pb=_b(
        '\n1google/cloud/scheduler_v1beta1/proto/target.proto\x12\x1egoogle.cloud.scheduler.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto"\xe2\x01\n\nHttpTarget\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12?\n\x0bhttp_method\x18\x02 \x01(\x0e\x32*.google.cloud.scheduler.v1beta1.HttpMethod\x12H\n\x07headers\x18\x03 \x03(\x0b\x32\x37.google.cloud.scheduler.v1beta1.HttpTarget.HeadersEntry\x12\x0c\n\x04\x62ody\x18\x04 \x01(\x0c\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xcb\x02\n\x13\x41ppEngineHttpTarget\x12?\n\x0bhttp_method\x18\x01 \x01(\x0e\x32*.google.cloud.scheduler.v1beta1.HttpMethod\x12L\n\x12\x61pp_engine_routing\x18\x02 \x01(\x0b\x32\x30.google.cloud.scheduler.v1beta1.AppEngineRouting\x12\x14\n\x0crelative_uri\x18\x03 \x01(\t\x12Q\n\x07headers\x18\x04 \x03(\x0b\x32@.google.cloud.scheduler.v1beta1.AppEngineHttpTarget.HeadersEntry\x12\x0c\n\x04\x62ody\x18\x05 \x01(\x0c\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xb5\x01\n\x0cPubsubTarget\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12P\n\nattributes\x18\x04 \x03(\x0b\x32<.google.cloud.scheduler.v1beta1.PubsubTarget.AttributesEntry\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"T\n\x10\x41ppEngineRouting\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08instance\x18\x03 \x01(\t\x12\x0c\n\x04host\x18\x04 \x01(\t*s\n\nHttpMethod\x12\x1b\n\x17HTTP_METHOD_UNSPECIFIED\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x07\n\x03GET\x10\x02\x12\x08\n\x04HEAD\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06\x44\x45LETE\x10\x05\x12\t\n\x05PATCH\x10\x06\x12\x0b\n\x07OPTIONS\x10\x07\x42|\n"com.google.cloud.scheduler.v1beta1B\x0bTargetProtoP\x01ZGgoogle.golang.org/genproto/googleapis/cloud/scheduler/v1beta1;schedulerb\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
    ],
)

_HTTPMETHOD = _descriptor.EnumDescriptor(
    name="HttpMethod",
    full_name="google.cloud.scheduler.v1beta1.HttpMethod",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="HTTP_METHOD_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="POST", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="GET", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="HEAD", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PUT", index=4, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DELETE", index=5, number=5, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PATCH", index=6, number=6, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="OPTIONS", index=7, number=7, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=975,
    serialized_end=1090,
)
_sym_db.RegisterEnumDescriptor(_HTTPMETHOD)

HttpMethod = enum_type_wrapper.EnumTypeWrapper(_HTTPMETHOD)
HTTP_METHOD_UNSPECIFIED = 0
POST = 1
GET = 2
HEAD = 3
PUT = 4
DELETE = 5
PATCH = 6
OPTIONS = 7


_HTTPTARGET_HEADERSENTRY = _descriptor.Descriptor(
    name="HeadersEntry",
    full_name="google.cloud.scheduler.v1beta1.HttpTarget.HeadersEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.scheduler.v1beta1.HttpTarget.HeadersEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.scheduler.v1beta1.HttpTarget.HeadersEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=323,
    serialized_end=369,
)

_HTTPTARGET = _descriptor.Descriptor(
    name="HttpTarget",
    full_name="google.cloud.scheduler.v1beta1.HttpTarget",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="uri",
            full_name="google.cloud.scheduler.v1beta1.HttpTarget.uri",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="http_method",
            full_name="google.cloud.scheduler.v1beta1.HttpTarget.http_method",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="headers",
            full_name="google.cloud.scheduler.v1beta1.HttpTarget.headers",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="body",
            full_name="google.cloud.scheduler.v1beta1.HttpTarget.body",
            index=3,
            number=4,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_HTTPTARGET_HEADERSENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=143,
    serialized_end=369,
)


_APPENGINEHTTPTARGET_HEADERSENTRY = _descriptor.Descriptor(
    name="HeadersEntry",
    full_name="google.cloud.scheduler.v1beta1.AppEngineHttpTarget.HeadersEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.scheduler.v1beta1.AppEngineHttpTarget.HeadersEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.scheduler.v1beta1.AppEngineHttpTarget.HeadersEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=323,
    serialized_end=369,
)

_APPENGINEHTTPTARGET = _descriptor.Descriptor(
    name="AppEngineHttpTarget",
    full_name="google.cloud.scheduler.v1beta1.AppEngineHttpTarget",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="http_method",
            full_name="google.cloud.scheduler.v1beta1.AppEngineHttpTarget.http_method",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="app_engine_routing",
            full_name="google.cloud.scheduler.v1beta1.AppEngineHttpTarget.app_engine_routing",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="relative_uri",
            full_name="google.cloud.scheduler.v1beta1.AppEngineHttpTarget.relative_uri",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="headers",
            full_name="google.cloud.scheduler.v1beta1.AppEngineHttpTarget.headers",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="body",
            full_name="google.cloud.scheduler.v1beta1.AppEngineHttpTarget.body",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_APPENGINEHTTPTARGET_HEADERSENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=372,
    serialized_end=703,
)


_PUBSUBTARGET_ATTRIBUTESENTRY = _descriptor.Descriptor(
    name="AttributesEntry",
    full_name="google.cloud.scheduler.v1beta1.PubsubTarget.AttributesEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.scheduler.v1beta1.PubsubTarget.AttributesEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.scheduler.v1beta1.PubsubTarget.AttributesEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=838,
    serialized_end=887,
)

_PUBSUBTARGET = _descriptor.Descriptor(
    name="PubsubTarget",
    full_name="google.cloud.scheduler.v1beta1.PubsubTarget",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="topic_name",
            full_name="google.cloud.scheduler.v1beta1.PubsubTarget.topic_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="google.cloud.scheduler.v1beta1.PubsubTarget.data",
            index=1,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="attributes",
            full_name="google.cloud.scheduler.v1beta1.PubsubTarget.attributes",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_PUBSUBTARGET_ATTRIBUTESENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=706,
    serialized_end=887,
)


_APPENGINEROUTING = _descriptor.Descriptor(
    name="AppEngineRouting",
    full_name="google.cloud.scheduler.v1beta1.AppEngineRouting",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="service",
            full_name="google.cloud.scheduler.v1beta1.AppEngineRouting.service",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="google.cloud.scheduler.v1beta1.AppEngineRouting.version",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="instance",
            full_name="google.cloud.scheduler.v1beta1.AppEngineRouting.instance",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="host",
            full_name="google.cloud.scheduler.v1beta1.AppEngineRouting.host",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=889,
    serialized_end=973,
)

_HTTPTARGET_HEADERSENTRY.containing_type = _HTTPTARGET
_HTTPTARGET.fields_by_name["http_method"].enum_type = _HTTPMETHOD
_HTTPTARGET.fields_by_name["headers"].message_type = _HTTPTARGET_HEADERSENTRY
_APPENGINEHTTPTARGET_HEADERSENTRY.containing_type = _APPENGINEHTTPTARGET
_APPENGINEHTTPTARGET.fields_by_name["http_method"].enum_type = _HTTPMETHOD
_APPENGINEHTTPTARGET.fields_by_name[
    "app_engine_routing"
].message_type = _APPENGINEROUTING
_APPENGINEHTTPTARGET.fields_by_name[
    "headers"
].message_type = _APPENGINEHTTPTARGET_HEADERSENTRY
_PUBSUBTARGET_ATTRIBUTESENTRY.containing_type = _PUBSUBTARGET
_PUBSUBTARGET.fields_by_name["attributes"].message_type = _PUBSUBTARGET_ATTRIBUTESENTRY
DESCRIPTOR.message_types_by_name["HttpTarget"] = _HTTPTARGET
DESCRIPTOR.message_types_by_name["AppEngineHttpTarget"] = _APPENGINEHTTPTARGET
DESCRIPTOR.message_types_by_name["PubsubTarget"] = _PUBSUBTARGET
DESCRIPTOR.message_types_by_name["AppEngineRouting"] = _APPENGINEROUTING
DESCRIPTOR.enum_types_by_name["HttpMethod"] = _HTTPMETHOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HttpTarget = _reflection.GeneratedProtocolMessageType(
    "HttpTarget",
    (_message.Message,),
    dict(
        HeadersEntry=_reflection.GeneratedProtocolMessageType(
            "HeadersEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_HTTPTARGET_HEADERSENTRY,
                __module__="google.cloud.scheduler_v1beta1.proto.target_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1beta1.HttpTarget.HeadersEntry)
            ),
        ),
        DESCRIPTOR=_HTTPTARGET,
        __module__="google.cloud.scheduler_v1beta1.proto.target_pb2",
        __doc__="""Http target. The job will be pushed to the job handler by means of an
  HTTP request via an
  [http\_method][google.cloud.scheduler.v1beta1.HttpTarget.http\_method]
  such as HTTP POST, HTTP GET, etc. The job is acknowledged by means of an
  HTTP response code in the range [200 - 299]. A failure to receive a
  response constitutes a failed execution. For a redirected request, the
  response returned by the redirected request is considered.
  
  
  Attributes:
      uri:
          Required.  The full URI path that the request will be sent to.
          This string must begin with either "http://" or "https://".
          Some examples of valid values for
          [uri][google.cloud.scheduler.v1beta1.HttpTarget.uri] are:
          ``http://acme.com`` and ``https://acme.com/sales:8080``. Cloud
          Scheduler will encode some characters for safety and
          compatibility. The maximum allowed URL length is 2083
          characters after encoding.
      http_method:
          Which HTTP method to use for the request.
      headers:
          The user can specify HTTP request headers to send with the
          job's HTTP request. This map contains the header field names
          and values. Repeated headers are not supported, but a header
          value can contain commas. These headers represent a subset of
          the headers that will accompany the job's HTTP request. Some
          HTTP request headers will be ignored or replaced. A partial
          list of headers that will be ignored or replaced is below: -
          Host: This will be computed by Cloud Scheduler and derived
          from [uri][google.cloud.scheduler.v1beta1.HttpTarget.uri]. \*
          ``Content-Length``: This will be computed by Cloud Scheduler.
          \* ``User-Agent``: This will be set to ``"Google-Cloud-
          Scheduler"``. \* ``X-Google-*``: Google internal use only. \*
          ``X-AppEngine-*``: Google internal use only.  The total size
          of headers must be less than 80KB.
      body:
          HTTP request body. A request body is allowed only if the HTTP
          method is POST, PUT, or PATCH. It is an error to set body on a
          job with an incompatible
          [HttpMethod][google.cloud.scheduler.v1beta1.HttpMethod].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1beta1.HttpTarget)
    ),
)
_sym_db.RegisterMessage(HttpTarget)
_sym_db.RegisterMessage(HttpTarget.HeadersEntry)

AppEngineHttpTarget = _reflection.GeneratedProtocolMessageType(
    "AppEngineHttpTarget",
    (_message.Message,),
    dict(
        HeadersEntry=_reflection.GeneratedProtocolMessageType(
            "HeadersEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_APPENGINEHTTPTARGET_HEADERSENTRY,
                __module__="google.cloud.scheduler_v1beta1.proto.target_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1beta1.AppEngineHttpTarget.HeadersEntry)
            ),
        ),
        DESCRIPTOR=_APPENGINEHTTPTARGET,
        __module__="google.cloud.scheduler_v1beta1.proto.target_pb2",
        __doc__="""App Engine target. The job will be pushed to a job handler by means of
  an HTTP request via an
  [http\_method][google.cloud.scheduler.v1beta1.AppEngineHttpTarget.http\_method]
  such as HTTP POST, HTTP GET, etc. The job is acknowledged by means of an
  HTTP response code in the range [200 - 299]. Error 503 is considered an
  App Engine system error instead of an application error. Requests
  returning error 503 will be retried regardless of retry configuration
  and not counted against retry counts. Any other response code, or a
  failure to receive a response before the deadline, constitutes a failed
  attempt.
  
  
  Attributes:
      http_method:
          The HTTP method to use for the request. PATCH and OPTIONS are
          not permitted.
      app_engine_routing:
          App Engine Routing setting for the job.
      relative_uri:
          The relative URI.  The relative URL must begin with "/" and
          must be a valid HTTP relative URL. It can contain a path,
          query string arguments, and ``#`` fragments. If the relative
          URL is empty, then the root path "/" will be used. No spaces
          are allowed, and the maximum length allowed is 2083
          characters.
      headers:
          HTTP request headers.  This map contains the header field
          names and values. Headers can be set when the job is created.
          Cloud Scheduler sets some headers to default values:  -
          ``User-Agent``: By default, this header is    ``"AppEngine-
          Google; (+http://code.google.com/appengine)"``. This    header
          can be modified, but Cloud Scheduler will append
          ``"AppEngine-Google; (+http://code.google.com/appengine)"`` to
          the    modified ``User-Agent``.  If the job has an [body][goog
          le.cloud.scheduler.v1beta1.AppEngineHttpTarget.body], Cloud
          Scheduler sets the following headers:  -  ``Content-Type``: By
          default, the ``Content-Type`` header is set to
          ``"application/octet-stream"``. The default can be overridden
          by    explictly setting ``Content-Type`` to a particular media
          type when    the job is created. For example, ``Content-Type``
          can be set to    ``"application/json"``. -  ``Content-
          Length``: This is computed by Cloud Scheduler. This value
          is output only. It cannot be changed.  The headers below are
          output only. They cannot be set or overridden:  -
          ``X-Google-*``: For Google internal use only. -
          ``X-AppEngine-*``: For Google internal use only. See `Reading
          request    headers <https://cloud.google.com/appengine/docs/py
          thon/taskqueue/push/creating-
          handlers#reading_request_headers>`__.  In addition, some App
          Engine headers, which contain job-specific information, are
          also be sent to the job handler; see `request headers <https:/
          /cloud.google.com/appengine/docs/standard/python/config/cron#s
          ecuring_urls_for_cron>`__.
      body:
          Body.  HTTP request body. A request body is allowed only if
          the HTTP method is POST or PUT. It will result in invalid
          argument error to set a body on a job with an incompatible
          [HttpMethod][google.cloud.scheduler.v1beta1.HttpMethod].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1beta1.AppEngineHttpTarget)
    ),
)
_sym_db.RegisterMessage(AppEngineHttpTarget)
_sym_db.RegisterMessage(AppEngineHttpTarget.HeadersEntry)

PubsubTarget = _reflection.GeneratedProtocolMessageType(
    "PubsubTarget",
    (_message.Message,),
    dict(
        AttributesEntry=_reflection.GeneratedProtocolMessageType(
            "AttributesEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_PUBSUBTARGET_ATTRIBUTESENTRY,
                __module__="google.cloud.scheduler_v1beta1.proto.target_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1beta1.PubsubTarget.AttributesEntry)
            ),
        ),
        DESCRIPTOR=_PUBSUBTARGET,
        __module__="google.cloud.scheduler_v1beta1.proto.target_pb2",
        __doc__="""Pub/Sub target. The job will be delivered by publishing a message to the
  given Pub/Sub topic.
  
  
  Attributes:
      topic_name:
          Required.  The name of the Cloud Pub/Sub topic to which
          messages will be published when a job is delivered. The topic
          name must be in the same format as required by PubSub's
          `PublishRequest.name <https://cloud.google.com/pubsub/docs/ref
          erence/rpc/google.pubsub.v1#publishrequest>`__, for example
          ``projects/PROJECT_ID/topics/TOPIC_ID``.  The topic must be in
          the same project as the Cloud Scheduler job.
      data:
          The message payload for PubsubMessage.  Pubsub message must
          contain either non-empty data, or at least one attribute.
      attributes:
          Attributes for PubsubMessage.  Pubsub message must contain
          either non-empty data, or at least one attribute.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1beta1.PubsubTarget)
    ),
)
_sym_db.RegisterMessage(PubsubTarget)
_sym_db.RegisterMessage(PubsubTarget.AttributesEntry)

AppEngineRouting = _reflection.GeneratedProtocolMessageType(
    "AppEngineRouting",
    (_message.Message,),
    dict(
        DESCRIPTOR=_APPENGINEROUTING,
        __module__="google.cloud.scheduler_v1beta1.proto.target_pb2",
        __doc__="""App Engine Routing.
  
  For more information about services, versions, and instances see `An
  Overview of App
  Engine <https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine>`__,
  `Microservices Architecture on Google App
  Engine <https://cloud.google.com/appengine/docs/python/microservices-on-app-engine>`__,
  `App Engine Standard request
  routing <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__,
  and `App Engine Flex request
  routing <https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed>`__.
  
  
  Attributes:
      service:
          App service.  By default, the job is sent to the service which
          is the default service when the job is attempted.
      version:
          App version.  By default, the job is sent to the version which
          is the default version when the job is attempted.
      instance:
          App instance.  By default, the job is sent to an instance
          which is available when the job is attempted.  Requests can
          only be sent to a specific instance if `manual scaling is used
          in App Engine Standard
          <https://cloud.google.com/appengine/docs/python/an-overview-
          of-app-engine?hl=en_US#scaling_types_and_instance_classes>`__.
          App Engine Flex does not support instances. For more
          information, see `App Engine Standard request routing
          <https://cloud.google.com/appengine/docs/standard/python/how-
          requests-are-routed>`__ and `App Engine Flex request routing
          <https://cloud.google.com/appengine/docs/flexible/python/how-
          requests-are-routed>`__.
      host:
          Output only. The host that the job is sent to.  For more
          information about how App Engine requests are routed, see
          `here
          <https://cloud.google.com/appengine/docs/standard/python/how-
          requests-are-routed>`__.  The host is constructed as:  -
          ``host = [application_domain_name]``\     ``| [service] + '.'
          + [application_domain_name]``\     ``| [version] + '.' +
          [application_domain_name]``\     ``| [version_dot_service]+
          '.' + [application_domain_name]``\     ``| [instance] + '.' +
          [application_domain_name]``\     ``| [instance_dot_service] +
          '.' + [application_domain_name]``\     ``|
          [instance_dot_version] + '.' + [application_domain_name]``\
          ``| [instance_dot_version_dot_service] + '.' +
          [application_domain_name]``  -  ``application_domain_name`` =
          The domain name of the app, for example    .appspot.com, which
          is associated with the job's project ID.  -  ``service =``    
          [service][google.cloud.scheduler.v1beta1.AppEngineRouting.serv
          ice]  -  ``version =``    [version][google.cloud.scheduler.v1b
          eta1.AppEngineRouting.version]  -  ``version_dot_service =``
          [version][google.cloud.scheduler.v1beta1.AppEngineRouting.vers
          ion]    ``+ '.' +``    [service][google.cloud.scheduler.v1beta
          1.AppEngineRouting.service]  -  ``instance =``    [instance][g
          oogle.cloud.scheduler.v1beta1.AppEngineRouting.instance]  -
          ``instance_dot_service =``    [instance][google.cloud.schedule
          r.v1beta1.AppEngineRouting.instance]    ``+ '.' +``    [servic
          e][google.cloud.scheduler.v1beta1.AppEngineRouting.service]  -
          ``instance_dot_version =``    [instance][google.cloud.schedule
          r.v1beta1.AppEngineRouting.instance]    ``+ '.' +``    [versio
          n][google.cloud.scheduler.v1beta1.AppEngineRouting.version]  -
          ``instance_dot_version_dot_service =``    [instance][google.cl
          oud.scheduler.v1beta1.AppEngineRouting.instance]    ``+ '.'
          +``    [version][google.cloud.scheduler.v1beta1.AppEngineRouti
          ng.version]    ``+ '.' +``    [service][google.cloud.scheduler
          .v1beta1.AppEngineRouting.service]  If [service][google.cloud.
          scheduler.v1beta1.AppEngineRouting.service] is empty, then the
          job will be sent to the service which is the default service
          when the job is attempted.  If [version][google.cloud.schedule
          r.v1beta1.AppEngineRouting.version] is empty, then the job
          will be sent to the version which is the default version when
          the job is attempted.  If [instance][google.cloud.scheduler.v1
          beta1.AppEngineRouting.instance] is empty, then the job will
          be sent to an instance which is available when the job is
          attempted.  If [service][google.cloud.scheduler.v1beta1.AppEng
          ineRouting.service], [version][google.cloud.scheduler.v1beta1.
          AppEngineRouting.version], or [instance][google.cloud.schedule
          r.v1beta1.AppEngineRouting.instance] is invalid, then the job
          will be sent to the default version of the default service
          when the job is attempted.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1beta1.AppEngineRouting)
    ),
)
_sym_db.RegisterMessage(AppEngineRouting)


DESCRIPTOR._options = None
_HTTPTARGET_HEADERSENTRY._options = None
_APPENGINEHTTPTARGET_HEADERSENTRY._options = None
_PUBSUBTARGET_ATTRIBUTESENTRY._options = None
# @@protoc_insertion_point(module_scope)
