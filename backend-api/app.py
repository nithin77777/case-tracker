import fastapi
import uvicorn
import os
import dotenv


dotenv.load_dotenv()

port = int(os.getenv("PORT"))
host = os.getenv("ALLOWED_HOSTS")
app = fastapi.FastAPI()

@app.get("/", status_code=200)
def index():
    return {
        "status":"Success"
    }

if __name__=="__main__":
    uvicorn.run("app:app", port=port, host=host)