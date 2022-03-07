from fastapi import APIRouter, Body, HTTPException
from sqlalchemy import select, update, delete
from pydantic import BaseModel
from database import SessionLocal
import models

class Student(BaseModel):
    id: int
    f_name: str
    l_name: str
    gpa: float
    
    class Config:
        orm_mode=True

db = SessionLocal()

router = APIRouter(
    prefix="/student",
    tags=["students"]
)

@router.post("")
async def add_student(student: Student):
    student = models.Student(
        id = student.id,
        f_name = student.f_name,
        l_name = student.l_name,
        gpa = student.gpa
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return f"Student {student.id} is successfully added"


@router.get("")
async def get_student(id):
    student = db.execute(select(models.Student).where(models.Student.id == id)).fetchone()
    if student:
        return student
    else:
        return f"Provided student ({id}) is not exist"


@router.put("")
async def update_student(student: Student):
    id = db.execute(select(models.Student).where(models.Student.id == student.id)).fetchone()
    if id:
        db.execute(update(models.Student).where(models.Student.id == student.id).\
        values(F_Name = student.f_name, L_Name = student.l_name, GPA = student.gpa))
        db.commit()

        return f"Student {student.id} is successfully updated"
    else:
        raise HTTPException(status_code = 404, detail = f"Provided student ({student.id}) is not exist")


@router.delete("")
async def delete_student(id: int = Body(...)):
    student = db.execute(select(models.Student.ID).where(models.Student.id == id)).fetchone()
    if student:
        db.execute(delete(models.Student).where(models.Student.id == id))
        db.commit()
        return f"Student {id} is successfully deleted"
    else:
        return f"Provided student ({id}) is not exist"