#Authon Ivor
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:mysql123@127.0.0.1:3306/test")

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    #创建一个关联关系，通过外键，与对应的表进行关联，获取到Address的一个类对象。
    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])



class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(16))
    city = Column(String(16))
    state = Column(String(16))

# Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
s = session()

# addr1 = Address(street='wudaokou',city='beijing',state='bj')
# addr2 = Address(street='tongzhou',city='beijing',state='bj')
# addr3 = Address(street='yanjiao',city='beijing',state='bj')
# # s.add_all([addr1,addr2,addr3])
# c1 = Customer(name='jack',billing_address=addr1,shipping_address=addr2)
# c2 = Customer(name='jack',billing_address=addr3,shipping_address=addr3)
# s.add(c1)
# s.commit()
obj = s.query(Customer).all()
for i in obj:
    print(i.billing_address_id)
    print(i.billing_address.street)