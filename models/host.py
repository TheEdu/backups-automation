
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Host(Base):
    __tablename__ = 'hosts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(String)
    ip = Column(String)
    user = Column(String)
    password = Column(String)

    tipo = Column(Integer, ForeignKey("host_types.id"))
    host_type_id = relationship("HostType")

    def __init__(self,
                 nombre,
                 ip,
                 descripcion,
                 user,
                 password,
                 tipo):
        self.nombre = nombre
        self.ip = ip
        self.descripcion = descripcion
        self.user = user
        self.password = password
        self.tipo = tipo


class HostType(Base):
    __tablename__ = 'host_types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String)
    descripcion = Column(String)
