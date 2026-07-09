from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from ..database import Base

class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, unique=True, nullable=False, index=True)
    category_slug = Column(String, unique=True, nullable=False, index=True)


    product = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id = {self.category_id}, name ='{self.category_name}')>"
    
