from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# Create connection with db
db = create_engine("sqlite:///database/banco.db")

# create base of db
Base = declarative_base()

# create tables
class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String)
    email = Column('email', String, nullable=False)
    password = Column('password', String)
    status = Column('status', Boolean)
    admin = Column('admin', Boolean, default=False)

    def __init__(self, name, email, password, status=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.status = status
        self.admin = admin


class Order(Base):
    __tablename__ = 'orders'

    '''STATUS_ORDER = (
        ('PENDING', 'PENDING'),
        ('CANCELLED', 'CANCELLED'),
        ('FINISHED', 'FINISHED')
    )'''

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status', String)
    user = Column('user', ForeignKey('users.id'))
    price = Column('price', Float)
    #items

    def __init__(self, user, status='PENDING', price=0):
        self.user = user
        self.status = status
        self.price = price


class ItemsOrder(Base):
    __tablename__ = 'items_order'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    quantity = Column('quantity', Integer)
    taste = Column('taste', String)
    size = Column('size', String)
    price_unit = Column('price_unit', Float)
    order = Column('order', ForeignKey('orders.id'))

    def __init__(self, quantity, taste, size, price_unit, order):
        self.quantity = quantity
        self.taste = taste
        self.size = size
        self.price_unit = price_unit
        self.order = order


