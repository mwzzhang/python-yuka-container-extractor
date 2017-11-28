meta:
  id: ykc
  application: Yuka Engine
  endian: le

seq:
  - id: magic
    contents: ["YKC001", 0, 0]
  - id: magic2
    contents: [0x18, 0, 0, 0, 0, 0, 0, 0]
  - id: header_ofs
    type: u4
  - id: header_len
    type: u4

instances:
  header:
    pos: header_ofs
    size: header_len
    type: header

types:
  header:
    seq:
      - id: entries
        repeat: eos
        type: file_entry
  file_entry:
    seq:
      - id: filename_ofs
        type: u4
      - id: filename_len
        type: u4
      - id: body_ofs
        type: u4
      - id: body_len
        type: u4
      - id: unknown5
        type: u4
    instances:
      filename:
        pos: filename_ofs
        size: filename_len
        type: strz
        encoding: SJIS
        io: _root._io
      body:
        pos: body_ofs
        size: body_len
        io: _root._io
