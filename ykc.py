# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import array
import struct
import zlib
from enum import Enum
from pkg_resources import parse_version

from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Ykc(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.magic = self._io.ensure_fixed_contents(struct.pack('8b', 89, 75, 67, 48, 48, 49, 0, 0))
        self.magic2 = self._io.ensure_fixed_contents(struct.pack('8b', 24, 0, 0, 0, 0, 0, 0, 0))
        self.header_ofs = self._io.read_u4le()
        self.header_len = self._io.read_u4le()

    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.entries = []
            while not self._io.is_eof():
                self.entries.append(self._root.FileEntry(self._io, self, self._root))



    class FileEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.filename_ofs = self._io.read_u4le()
            self.filename_len = self._io.read_u4le()
            self.body_ofs = self._io.read_u4le()
            self.body_len = self._io.read_u4le()
            self.unknown5 = self._io.read_u4le()

        @property
        def filename(self):
            if hasattr(self, '_m_filename'):
                return self._m_filename if hasattr(self, '_m_filename') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.filename_ofs)
            self._m_filename = (KaitaiStream.bytes_terminate(io.read_bytes(self.filename_len), 0, False)).decode(u"SJIS")
            io.seek(_pos)
            return self._m_filename if hasattr(self, '_m_filename') else None

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body if hasattr(self, '_m_body') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.body_ofs)
            self._m_body = io.read_bytes(self.body_len)
            io.seek(_pos)
            return self._m_body if hasattr(self, '_m_body') else None


    @property
    def header(self):
        if hasattr(self, '_m_header'):
            return self._m_header if hasattr(self, '_m_header') else None

        _pos = self._io.pos()
        self._io.seek(self.header_ofs)
        self._raw__m_header = self._io.read_bytes(self.header_len)
        io = KaitaiStream(BytesIO(self._raw__m_header))
        self._m_header = self._root.Header(io, self, self._root)
        self._io.seek(_pos)
        return self._m_header if hasattr(self, '_m_header') else None


