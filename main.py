from fastapi import FastAPI
import routes.students

app = FastAPI()

app.include_router(routes.students.router)
