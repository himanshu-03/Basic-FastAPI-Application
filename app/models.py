from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from starlette.applications import Starlette
from starlette_admin.contrib.sqla import Admin, ModelView


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="himanshu",
    host="localhost",
    database="postgres",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)


Base.metadata.create_all(engine)

app = Starlette()  

admin = Admin(engine, title="Book Store")

admin.add_view(ModelView(Course, session))

admin.mount_to(app)