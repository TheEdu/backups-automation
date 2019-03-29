import sys
sys.path.append('./models')
from models.base import Session
from models.host.host import Host, HostType

session = Session()

# Test add new host
# host = Host('nombre', 'ip', 'descripcion', 'user', 'password', 1)
# session.add(host)
# session.commit()

#  Test fetch all host
hosts = session.query(Host).all()
for host in hosts:
    print(vars(host))

 # Test fetch all host types
host_types = session.query(HostType).all()
for host_type in host_types:
    print(vars(host_type))

session.close()
