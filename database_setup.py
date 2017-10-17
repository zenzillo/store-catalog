from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, UniqueConstraint

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    sku_code = Column(String(10), unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    products = relationship("Product", primaryjoin="and_(Category.id==Product.category_id )")

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'name'       : self.name,
           'sku_code'   : self.sku_code
       }

    @property
    def serializeWithProducts(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'name'       : self.name,
           'sku_code'   : self.sku_code,
           'products'   : [{'id': product.id,
                            'name': product.name,
                            'price':product.price,
                            'sku':product.sku,
                            'status':product.status,
                            'description':product.description}
                            for product in self.products]
       }

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    description = Column(String(250))
    price = Column(String(8))
    sku = Column(String(50), unique=True)
    status = Column(Integer)
    category_id = Column(Integer,ForeignKey('categories.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    photos = relationship("ProductPhoto", primaryjoin="and_(Product.id==ProductPhoto.product_id )")

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'           : self.id,
           'name'         : self.name,
           'sku'          : self.sku,
           'price'        : self.price,
           'status'       : self.status,
           'description'  : self.description,
       }

class ProductPhoto(Base):
    __tablename__ = 'product_photos'

    id = Column(Integer, primary_key = True)
    filename = Column(String(80), nullable = False)
    order_placement = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship(Product)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'filename'         : self.filename,
           'order_placement'         : self.order_placement,
           'id'         : self.id,
       }

#engine = create_engine('sqlite:///restaurantmenuwithusers.db')
engine = create_engine('postgresql+psycopg2:///mystore')


Base.metadata.create_all(engine)
