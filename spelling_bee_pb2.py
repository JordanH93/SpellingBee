# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spelling_bee.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spelling_bee.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12spelling_bee.proto\"\x1a\n\x07GetWord\x12\x0f\n\x07request\x18\x01 \x01(\t\"]\n\x04Word\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x11\n\trand_char\x18\x02 \x01(\t\x12\x11\n\tremaining\x18\x03 \x01(\x05\x12\r\n\x05total\x18\x04 \x01(\x05\x12\x12\n\nsession_id\x18\x05 \x01(\t\"\x1c\n\x07GetGame\x12\x11\n\tselection\x18\x01 \x01(\t\"\x15\n\x04Game\x12\r\n\x05score\x18\x01 \x01(\x05\"\x1b\n\x07SetWord\x12\x10\n\x08set_word\x18\x01 \x01(\t\">\n\x08Response\x12\x10\n\x08response\x18\x01 \x01(\x08\x12\r\n\x05score\x18\x02 \x01(\x05\x12\x11\n\tremaining\x18\x03 \x01(\x05\x32u\n\x12SpellingBeeService\x12 \n\x07setWord\x12\x08.SetWord\x1a\t.Response\"\x00\x12\x1f\n\ncreateGame\x12\x08.GetGame\x1a\x05.Game\"\x00\x12\x1c\n\x07getWord\x12\x08.GetWord\x1a\x05.Word\"\x00\x62\x06proto3'
)




_GETWORD = _descriptor.Descriptor(
  name='GetWord',
  full_name='GetWord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='GetWord.request', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=48,
)


_WORD = _descriptor.Descriptor(
  name='Word',
  full_name='Word',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='Word.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rand_char', full_name='Word.rand_char', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remaining', full_name='Word.remaining', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total', full_name='Word.total', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='Word.session_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=143,
)


_GETGAME = _descriptor.Descriptor(
  name='GetGame',
  full_name='GetGame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='selection', full_name='GetGame.selection', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=173,
)


_GAME = _descriptor.Descriptor(
  name='Game',
  full_name='Game',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='Game.score', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=196,
)


_SETWORD = _descriptor.Descriptor(
  name='SetWord',
  full_name='SetWord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='set_word', full_name='SetWord.set_word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=225,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='Response.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='Response.score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remaining', full_name='Response.remaining', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=289,
)

DESCRIPTOR.message_types_by_name['GetWord'] = _GETWORD
DESCRIPTOR.message_types_by_name['Word'] = _WORD
DESCRIPTOR.message_types_by_name['GetGame'] = _GETGAME
DESCRIPTOR.message_types_by_name['Game'] = _GAME
DESCRIPTOR.message_types_by_name['SetWord'] = _SETWORD
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetWord = _reflection.GeneratedProtocolMessageType('GetWord', (_message.Message,), {
  'DESCRIPTOR' : _GETWORD,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:GetWord)
  })
_sym_db.RegisterMessage(GetWord)

Word = _reflection.GeneratedProtocolMessageType('Word', (_message.Message,), {
  'DESCRIPTOR' : _WORD,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:Word)
  })
_sym_db.RegisterMessage(Word)

GetGame = _reflection.GeneratedProtocolMessageType('GetGame', (_message.Message,), {
  'DESCRIPTOR' : _GETGAME,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:GetGame)
  })
_sym_db.RegisterMessage(GetGame)

Game = _reflection.GeneratedProtocolMessageType('Game', (_message.Message,), {
  'DESCRIPTOR' : _GAME,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:Game)
  })
_sym_db.RegisterMessage(Game)

SetWord = _reflection.GeneratedProtocolMessageType('SetWord', (_message.Message,), {
  'DESCRIPTOR' : _SETWORD,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:SetWord)
  })
_sym_db.RegisterMessage(SetWord)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)



_SPELLINGBEESERVICE = _descriptor.ServiceDescriptor(
  name='SpellingBeeService',
  full_name='SpellingBeeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=291,
  serialized_end=408,
  methods=[
  _descriptor.MethodDescriptor(
    name='setWord',
    full_name='SpellingBeeService.setWord',
    index=0,
    containing_service=None,
    input_type=_SETWORD,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='createGame',
    full_name='SpellingBeeService.createGame',
    index=1,
    containing_service=None,
    input_type=_GETGAME,
    output_type=_GAME,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getWord',
    full_name='SpellingBeeService.getWord',
    index=2,
    containing_service=None,
    input_type=_GETWORD,
    output_type=_WORD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPELLINGBEESERVICE)

DESCRIPTOR.services_by_name['SpellingBeeService'] = _SPELLINGBEESERVICE

# @@protoc_insertion_point(module_scope)
