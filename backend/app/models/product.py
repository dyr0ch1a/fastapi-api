from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class Product(Base):

    __tablename__ = "products"

    products_id = Column(Integer, primary_key=True, index=True)
    products_name = Column(String, unique=True, nullable=False, index=True)
    products_description = Column(Text)
    products_price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    products_images_url = Column(String)
    create_at = Column(DateTime, default=datetime.utcnow)

    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Products(id = {self.products_id}, name = '{self.products_name}')>"
