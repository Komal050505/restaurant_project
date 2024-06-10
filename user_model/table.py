from sqlalchemy import Column, String, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Restaurant_table(Base):
    __tablename__ = "restaurant"

    name = Column("name", String(50), primary_key=True)
    type = Column("type", String(100))
    items = Column("items", String(100))
    price = Column("price", Integer)
    location = Column("location", VARCHAR)

