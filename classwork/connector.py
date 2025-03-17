# Возможные варианты подключения к базам данных

# URI -> "<DBMS>+<library_name>://<user>:<password>@<host>:<port>/<database_name>"
    #    "mysql+pymysql://root:rootpassword123@localhost:3306/my_database"
    #    "sqlite:///<db_name>"

from sqlalchemy import (
    create_engine,
    BigInteger,
    String,
    Integer
)
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base,
    mapped_column,
    Mapped
)

Base = declarative_base()


sqla_engine = create_engine(
    url="sqlite:///../example.db",
    echo=True,
    echo_pool=True,
)


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )  # id INTEGER PRIMARY KEY AUTOINCREMENT
    name: Mapped[str] = mapped_column(
        String(25)
    )
    age: Mapped[int] = mapped_column(
        Integer,
    )

# Classic mapping style
from sqlalchemy import Table, Column, String, Text, Numeric
from sqlalchemy.orm import registry

Register = registry()

metadata = Register.metadata

news_table = Table(
    'news',
    metadata,
    Column('title', String(50), unique=True),
    Column('description', Text, nullable=True),
    Column('rating', Numeric(3, 2)),
)


class News:
    def __init__(self, title: str, description: str, rating: float) -> None:
        self.title = title
        self.description = description
        self.rating = rating


Register.map_imperatively(News, news_table)

Register.metadata.create_all(bind=sqla_engine)

Base.metadata.create_all(bind=sqla_engine)

user = User(
    id=1,
    name="Alex Black",
    age=28
)


