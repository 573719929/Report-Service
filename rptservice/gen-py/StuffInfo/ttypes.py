#
# Autogenerated by Thrift Compiler (0.8.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException
import Shared.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class StuffInfo:
  """
  Attributes:
   - stuff_id
   - name
   - uid
   - adid
   - width
   - height
   - type
   - title
   - desc
   - addr
   - thumb
   - crop
   - landing_page
   - enabled
   - ctime
   - mtime
   - size
   - media_name
   - version
   - verified_or_not
   - group_id
   - plan_id
   - group_name
   - plan_name
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'stuff_id', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.I32, 'uid', None, None, ), # 3
    (4, TType.I32, 'adid', None, None, ), # 4
    (5, TType.I32, 'width', None, None, ), # 5
    (6, TType.I32, 'height', None, None, ), # 6
    (7, TType.I32, 'type', None,     1, ), # 7
    (8, TType.STRING, 'title', None, None, ), # 8
    (9, TType.STRING, 'desc', None, None, ), # 9
    (10, TType.STRING, 'addr', None, None, ), # 10
    (11, TType.STRING, 'thumb', None, None, ), # 11
    (12, TType.STRING, 'crop', None, None, ), # 12
    (13, TType.STRING, 'landing_page', None, None, ), # 13
    (14, TType.I32, 'enabled', None,     1, ), # 14
    (15, TType.I32, 'ctime', None, None, ), # 15
    (16, TType.I32, 'mtime', None, None, ), # 16
    (17, TType.I32, 'size', None, None, ), # 17
    (18, TType.STRING, 'media_name', None, None, ), # 18
    (19, TType.I32, 'version', None, None, ), # 19
    (20, TType.I32, 'verified_or_not', None, None, ), # 20
    (21, TType.I32, 'group_id', None, None, ), # 21
    (22, TType.I32, 'plan_id', None, None, ), # 22
    (23, TType.STRING, 'group_name', None, None, ), # 23
    (24, TType.STRING, 'plan_name', None, None, ), # 24
  )

  def __init__(self, stuff_id=None, name=None, uid=None, adid=None, width=None, height=None, type=thrift_spec[7][4], title=None, desc=None, addr=None, thumb=None, crop=None, landing_page=None, enabled=thrift_spec[14][4], ctime=None, mtime=None, size=None, media_name=None, version=None, verified_or_not=None, group_id=None, plan_id=None, group_name=None, plan_name=None,):
    self.stuff_id = stuff_id
    self.name = name
    self.uid = uid
    self.adid = adid
    self.width = width
    self.height = height
    self.type = type
    self.title = title
    self.desc = desc
    self.addr = addr
    self.thumb = thumb
    self.crop = crop
    self.landing_page = landing_page
    self.enabled = enabled
    self.ctime = ctime
    self.mtime = mtime
    self.size = size
    self.media_name = media_name
    self.version = version
    self.verified_or_not = verified_or_not
    self.group_id = group_id
    self.plan_id = plan_id
    self.group_name = group_name
    self.plan_name = plan_name

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.stuff_id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.uid = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.adid = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.width = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.height = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.title = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.desc = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.addr = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.STRING:
          self.thumb = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.STRING:
          self.crop = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.STRING:
          self.landing_page = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.I32:
          self.enabled = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.I32:
          self.ctime = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 16:
        if ftype == TType.I32:
          self.mtime = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 17:
        if ftype == TType.I32:
          self.size = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 18:
        if ftype == TType.STRING:
          self.media_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 19:
        if ftype == TType.I32:
          self.version = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 20:
        if ftype == TType.I32:
          self.verified_or_not = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 21:
        if ftype == TType.I32:
          self.group_id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 22:
        if ftype == TType.I32:
          self.plan_id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 23:
        if ftype == TType.STRING:
          self.group_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 24:
        if ftype == TType.STRING:
          self.plan_name = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('StuffInfo')
    if self.stuff_id is not None:
      oprot.writeFieldBegin('stuff_id', TType.I32, 1)
      oprot.writeI32(self.stuff_id)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.uid is not None:
      oprot.writeFieldBegin('uid', TType.I32, 3)
      oprot.writeI32(self.uid)
      oprot.writeFieldEnd()
    if self.adid is not None:
      oprot.writeFieldBegin('adid', TType.I32, 4)
      oprot.writeI32(self.adid)
      oprot.writeFieldEnd()
    if self.width is not None:
      oprot.writeFieldBegin('width', TType.I32, 5)
      oprot.writeI32(self.width)
      oprot.writeFieldEnd()
    if self.height is not None:
      oprot.writeFieldBegin('height', TType.I32, 6)
      oprot.writeI32(self.height)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 7)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.title is not None:
      oprot.writeFieldBegin('title', TType.STRING, 8)
      oprot.writeString(self.title)
      oprot.writeFieldEnd()
    if self.desc is not None:
      oprot.writeFieldBegin('desc', TType.STRING, 9)
      oprot.writeString(self.desc)
      oprot.writeFieldEnd()
    if self.addr is not None:
      oprot.writeFieldBegin('addr', TType.STRING, 10)
      oprot.writeString(self.addr)
      oprot.writeFieldEnd()
    if self.thumb is not None:
      oprot.writeFieldBegin('thumb', TType.STRING, 11)
      oprot.writeString(self.thumb)
      oprot.writeFieldEnd()
    if self.crop is not None:
      oprot.writeFieldBegin('crop', TType.STRING, 12)
      oprot.writeString(self.crop)
      oprot.writeFieldEnd()
    if self.landing_page is not None:
      oprot.writeFieldBegin('landing_page', TType.STRING, 13)
      oprot.writeString(self.landing_page)
      oprot.writeFieldEnd()
    if self.enabled is not None:
      oprot.writeFieldBegin('enabled', TType.I32, 14)
      oprot.writeI32(self.enabled)
      oprot.writeFieldEnd()
    if self.ctime is not None:
      oprot.writeFieldBegin('ctime', TType.I32, 15)
      oprot.writeI32(self.ctime)
      oprot.writeFieldEnd()
    if self.mtime is not None:
      oprot.writeFieldBegin('mtime', TType.I32, 16)
      oprot.writeI32(self.mtime)
      oprot.writeFieldEnd()
    if self.size is not None:
      oprot.writeFieldBegin('size', TType.I32, 17)
      oprot.writeI32(self.size)
      oprot.writeFieldEnd()
    if self.media_name is not None:
      oprot.writeFieldBegin('media_name', TType.STRING, 18)
      oprot.writeString(self.media_name)
      oprot.writeFieldEnd()
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.I32, 19)
      oprot.writeI32(self.version)
      oprot.writeFieldEnd()
    if self.verified_or_not is not None:
      oprot.writeFieldBegin('verified_or_not', TType.I32, 20)
      oprot.writeI32(self.verified_or_not)
      oprot.writeFieldEnd()
    if self.group_id is not None:
      oprot.writeFieldBegin('group_id', TType.I32, 21)
      oprot.writeI32(self.group_id)
      oprot.writeFieldEnd()
    if self.plan_id is not None:
      oprot.writeFieldBegin('plan_id', TType.I32, 22)
      oprot.writeI32(self.plan_id)
      oprot.writeFieldEnd()
    if self.group_name is not None:
      oprot.writeFieldBegin('group_name', TType.STRING, 23)
      oprot.writeString(self.group_name)
      oprot.writeFieldEnd()
    if self.plan_name is not None:
      oprot.writeFieldBegin('plan_name', TType.STRING, 24)
      oprot.writeString(self.plan_name)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class StuffResponse:
  """
  Attributes:
   - totalSize
   - currentSize
   - pageSize
   - pageNumber
   - data
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'totalSize', None, None, ), # 1
    (2, TType.I32, 'currentSize', None, None, ), # 2
    (3, TType.I32, 'pageSize', None, None, ), # 3
    (4, TType.I32, 'pageNumber', None, None, ), # 4
    (5, TType.LIST, 'data', (TType.STRUCT,(StuffInfo, StuffInfo.thrift_spec)), None, ), # 5
  )

  def __init__(self, totalSize=None, currentSize=None, pageSize=None, pageNumber=None, data=None,):
    self.totalSize = totalSize
    self.currentSize = currentSize
    self.pageSize = pageSize
    self.pageNumber = pageNumber
    self.data = data

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.totalSize = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.currentSize = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.pageSize = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.pageNumber = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.data = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = StuffInfo()
            _elem5.read(iprot)
            self.data.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('StuffResponse')
    if self.totalSize is not None:
      oprot.writeFieldBegin('totalSize', TType.I32, 1)
      oprot.writeI32(self.totalSize)
      oprot.writeFieldEnd()
    if self.currentSize is not None:
      oprot.writeFieldBegin('currentSize', TType.I32, 2)
      oprot.writeI32(self.currentSize)
      oprot.writeFieldEnd()
    if self.pageSize is not None:
      oprot.writeFieldBegin('pageSize', TType.I32, 3)
      oprot.writeI32(self.pageSize)
      oprot.writeFieldEnd()
    if self.pageNumber is not None:
      oprot.writeFieldBegin('pageNumber', TType.I32, 4)
      oprot.writeI32(self.pageNumber)
      oprot.writeFieldEnd()
    if self.data is not None:
      oprot.writeFieldBegin('data', TType.LIST, 5)
      oprot.writeListBegin(TType.STRUCT, len(self.data))
      for iter6 in self.data:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
