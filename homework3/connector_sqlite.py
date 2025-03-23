from sqlalchemy import create_engine, Integer, String, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from decimal import Decimal

URL = "sqlite:///:memory:"

engine = create_engine(URL, echo=True, echo_pool=True)

Base = declarative_base()


class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))

    products: Mapped[list["Product"]] = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id"))
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[Decimal] = mapped_column(Numeric(5, 2))
    in_stock: Mapped[bool] = mapped_column(Boolean, default=True, server_default="1")

    category: Mapped["Category"] = relationship("Category", back_populates="products")


Base.metadata.create_all(engine)














