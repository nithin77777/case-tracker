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
models.Base.metadata.create_all(bind=db_connection.engine )

        
if __name__=="__main__":
    uvicorn.run("backend_api.app:app", port=port, host=host)
 