from homework4.models import User, Order, Category, Product
from homework4.db_connector import engine, Base, session
from datetime import datetime, timedelta
from sqlalchemy import func

Base.metadata.create_all(engine)


user1 = User(name="Alice", age=30)
user2 = User(name="Bob", age=22)

session.add_all([user1, user2])
session.commit()



order1 = Order(user_id=user1.id, amount=100.50, created_at=datetime.now() - timedelta(days=1))
order2 = Order(user_id=user1.id, amount=200.75, created_at=datetime.now())
order3 = Order(user_id=user2.id, amount=80.99, created_at=datetime.now() - timedelta(days=2))

session.add_all([order1, order2, order3])
session.commit()



category_electronics = Category(name="Электроника", description="Гаджеты и устройства.")
category_books = Category(name="Книги", description="Печатные книги и электронные книги.")
category_clothing = Category(name="Одежда", description="Одежда для мужчин и женщин.")

session.add_all([category_electronics, category_books, category_clothing])
session.commit()



product_smartphone = Product(name="Смартфон", price=299.99, in_stock=True, category_id=category_electronics.id)
product_laptop = Product(name="Ноутбук", price=499.99, in_stock=True, category_id=category_electronics.id)
product_book = Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category_id=category_books.id)
product_jeans = Product(name="Джинсы", price=40.50, in_stock=True, category_id=category_clothing.id)
product_tshirt = Product(name="Футболка", price=20.00, in_stock=True, category_id=category_clothing.id)

session.add_all([product_smartphone, product_laptop, product_book, product_jeans, product_tshirt])
session.commit()


categories = (session.query(
    Category.name,
    Product.name.label('product_name'),
    Product.price.label('product_price')
).join(Product, Product.category_id == Category.id).all())

for elem in categories:
    print(f"Category: {elem.name}, Product_name: {elem.product_name}, Price: {elem.product_price}")



product = session.query(Product).filter(Product.name == "Смартфон").first()

if product:
    product.price = 349.99
    session.commit()
    print("Цена обновлена.")
else:
    print("Продукт 'Смартфон' не найден.")