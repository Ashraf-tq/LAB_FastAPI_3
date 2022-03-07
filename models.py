from contextlib import nullcontext
from operator import index
from re import T
from database import Base
from sqlalchemy import String, Integer, Float, Column, ForeignKey

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    f_name = Column(String(30), nullable=False)
    l_name = Column(String(30), nullable=False)
    gpa = Column(Float, nullable=False)

    def __repr__(self):
        return f"Student info\nID: {self.id}\nName: {self.f_name} {self.l_name}\GPA: {self.gpa}"

class Course(Base):
    __tablename__ = "courses"
    id = Column(String, primary_key=True)
    name = Column(String, nullable = False,)

    def __repr__(self):
        return f"Course info\nID: {self.id}\nName: {self.name}"

class StudentCourses(Base):
    __tablename__ = "students_courses"
    student = Column(ForeignKey("students.id"), primary_key=True)
    course  = Column(ForeignKey("courses.id"), primary_key=True)
