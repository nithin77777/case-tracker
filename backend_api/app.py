import fastapi
import uvicorn
import os
from dotenv import load_dotenv

from . import models
from . import schema
from . import db_connection

load_dotenv()

port = int(os.getenv("PORT"))
host = os.getenv("ALLOWED_HOSTS")
app = fastapi.FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=db_connection.engine)


@app.get("/", status_code=200)
def index():
    return {"message": "Hello, World!", "status": "success"}


@app.get("/index", status_code=200)
def create_obj():
    return {"message": "Hello, You are at Index!", "status": "success"}


@app.post("/create_case", status_code=201)
def create_case(data: schema.CaseSchema):
    db = db_connection.SessionLocal()
    try:
        db_case = models.CaseData(**data.dict(exclude={'id'}))
        db.add(db_case)
        db.commit()
        db.refresh(db_case)
        return {"message": "Case created successfully!", "status": "success", "data": schema.CaseSchema.from_orm(db_case)}
    except Exception as e:
        db.rollback()
        return {"message": f"Error creating case: {str(e)}", "status": "error"}
    finally:
        db.close()


@app.get("/cases", status_code=200)
def get_all_cases():
    db = db_connection.SessionLocal()
    try:
        cases = db.query(models.CaseData).all()
        return {"message": "Cases retrieved successfully!", "status": "success", "data": [schema.CaseSchema.from_orm(case) for case in cases]}
    except Exception as e:
        return {"message": f"Error retrieving cases: {str(e)}", "status": "error"}
    finally:
        db.close()


@app.get("/cases/{case_id}", status_code=200)
def get_case(case_id: int):
    db = db_connection.SessionLocal()
    try:
        case = db.query(models.CaseData).filter(
            models.CaseData.id == case_id).first()
        if case:
            return {"message": "Case retrieved successfully!", "status": "success", "data": schema.CaseSchema.from_orm(case)}
        else:
            return {"message": "Case not found", "status": "error"}
    except Exception as e:
        return {"message": f"Error retrieving case: {str(e)}", "status": "error"}
    finally:
        db.close()


if __name__ == "__main__":
    uvicorn.run("backend_api.app:app", reload=True, port=port, host=host)
