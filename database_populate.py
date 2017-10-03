from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Product, ProductPhoto, User

#engine = create_engine('sqlite:///restaurantmenuwithusers.db')
engine = create_engine('postgresql+psycopg2:///mystore')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Test User", email="test@email.com",
             picture="")
session.add(User1)
session.commit()

# Category Hats
category1 = Category(user=User1, name="Hats", sku_code="HT")

session.add(category1)
session.commit()

product1 = Product(user=User1, name="Grey Crest", description="Grey hat with black crest logo", price="25", sku="123", status="1", category=category1)

session.add(product1)
session.commit()

product2 = Product(user=User1, name="Black Cap", description="Black baseball cap with white logo", price="25", sku="124", status="1", category=category1)

session.add(product2)
session.commit()

product3 = Product(user=User1, name="Blue Beanie", description="Blue beanine with logo tag", price="20", sku="125", status="1", category=category1)

session.add(product3)
session.commit()

# Category Shirts
category2 = Category(user=User1, name="Shirts", sku_code="SH")

session.add(category2)
session.commit()

product4 = Product(user=User1, name="Tuning Pattern", description="Maroon shirt with white tuning pattern desgin", price="25", sku="126", status="1", category=category2)

session.add(product4)
session.commit()

product5 = Product(user=User1, name="Classic", description="Classic white logo on black shirt", price="25", sku="127", status="1", category=category2)

session.add(product5)
session.commit()

product6 = Product(user=User1, name="Cold Dead Hands", description="Black wash shirt with white cold dead hands design.", price="25", sku="128", status="1", category=category2)

session.add(product6)
session.commit()


# Category Tanks
category3 = Category(user=User1, name="Tanks", sku_code="TK")

session.add(category3)
session.commit()

product7 = Product(user=User1, name="Crest Tank", description="Red crest logo on grey and white striped tank", price="25", sku="129", status="1", category=category3)

session.add(product7)
session.commit()

product8 = Product(user=User1, name="Cold Dead Hands Tank", description="Black wash tank with white cold dead hands design.", price="25", sku="130", status="1", category=category3)

session.add(product8)
session.commit()

product9 = Product(user=User1, name="Flag Tank", description="Light grey flag design on grey tank.", price="25", sku="131", status="1", category=category3)

session.add(product9)
session.commit()


# Category Sweaters
category4 = Category(user=User1, name="Sweaters", sku_code="SW")

session.add(category4)
session.commit()

product10 = Product(user=User1, name="Red Sweater", description="Red pullover sweatshirt with white logo", price="45", sku="SW-001", status="1", category=category4)

session.add(product10)
session.commit()

product11 = Product(user=User1, name="Stick Pullover", description="Dark blue pullover hoodie with white stick logo", price="45", sku="SW-002", status="1", category=category4)

session.add(product11)
session.commit()

product12 = Product(user=User1, name="Crest Hoodie", description="Grey and black zippered hoodie with white crest logo", price="45", sku="SW-003", status="1", category=category4)

session.add(product12)
session.commit()

# Category Stickers
category5 = Category(user=User1, name="Stickers", sku_code="ST")

session.add(category5)
session.commit()

product10 = Product(user=User1, name="Crest Logo Sticker", description="White logo on black round sticker", price="5", sku="ST-001", status="1", category=category5)

session.add(product10)
session.commit()

product11 = Product(user=User1, name="Cold Dead Hands Decal", description="White car decal with cold dead hands design", price="5", sku="ST-002", status="1", category=category5)

session.add(product11)
session.commit()

product12 = Product(user=User1, name="Spellout Sticker", description="White logo spellout on rectangular blue background", price="5", sku="ST-003", status="1", category=category5)

session.add(product12)
session.commit()
print "added menu items!"