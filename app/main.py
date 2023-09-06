from fastapi import FastAPI
from app.models import Course, session

app = FastAPI()


@app.post("/create")
async def create_course(title: str, price:int):
    course = Course(title=title, price=price)
    session.add(course)
    session.commit()
    return {"Course added": course.title}

@app.get("/")
async def get_all_courses():
    courses_query = session.query(Course)
    return courses_query.all()

@app.put("/update/{id}")
async def update_course(
    id: int,
    title: str = "",
    price: int = 0 
):
    course_query = session.query(Course).filter(Course.id==id)
    course = course_query.first()
    if title:
        course.title = title
    course.price = price
    session.add(course)
    session.commit()

@app.delete("/delete/{id}")
async def delete_course(id: int):
    course = session.query(Course).filter(Course.id==id).first()
    session.delete(course)
    session.commit()
    return {"course deleted": course.title}
