# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10proto/user.proto\x12\x05proto\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"J\n\nLoginReply\x12\x0f\n\x07\x63orrect\x18\x01 \x01(\x08\x12\r\n\x05\x63ity1\x18\x02 \x01(\t\x12\r\n\x05\x63ity2\x18\x03 \x01(\t\x12\r\n\x05\x63ity3\x18\x04 \x01(\t\"1\n\x0f\x41\x64\x64ToFavRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\" \n\rAddToFavReply\x12\x0f\n\x07\x63orrect\x18\x01 \x01(\x08\x32w\n\x06Userer\x12\x31\n\x05Login\x12\x13.proto.LoginRequest\x1a\x11.proto.LoginReply\"\x00\x12:\n\x08\x41\x64\x64ToFav\x12\x16.proto.AddToFavRequest\x1a\x14.proto.AddToFavReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LOGINREQUEST']._serialized_start=27
  _globals['_LOGINREQUEST']._serialized_end=77
  _globals['_LOGINREPLY']._serialized_start=79
  _globals['_LOGINREPLY']._serialized_end=153
  _globals['_ADDTOFAVREQUEST']._serialized_start=155
  _globals['_ADDTOFAVREQUEST']._serialized_end=204
  _globals['_ADDTOFAVREPLY']._serialized_start=206
  _globals['_ADDTOFAVREPLY']._serialized_end=238
  _globals['_USERER']._serialized_start=240
  _globals['_USERER']._serialized_end=359
# @@protoc_insertion_point(module_scope)