import fastapi
import uvicorn
import os
import dotenv
import csv


from . import models
from . import db_connection

dotenv.load_dotenv()

port = int(os.getenv("PORT"))
host = os.getenv("ALLOWED_HOSTS")
app = fastapi.FastAPI()

# Create the database tables
# models.Base.metadata.create_all(bind=db_connection.engine )

@app.get("/", status_code=200)
def index():
    return {"message": "Hello, World!", "status": "success"}


@app.get("/index", status_code=200)
def create_obj():
    return {"message": "Hello, You are at Index!", "status": "success"}


@app.post("/create_case", status_code=201)
def create_case(data:models.CaseData):
    db = db_connection.SessionLocal()
    db.add(data)
    db.commit()
    db.refresh(data)
    return {"message": "Case created successfully!", "status": "success", "data": data}
                
        
if __name__=="__main__":
    uvicorn.run("backend_api.app:app", reload=True, port=port, host=host)
 