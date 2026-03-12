import fastapi
import uvicorn
import os
import dotenv
import csv

dotenv.load_dotenv()

port = int(os.getenv("PORT"))
host = os.getenv("ALLOWED_HOSTS")
app = fastapi.FastAPI()

@app.get("/", status_code=200)
def index():
    return {
        "status":"Success"
    }

def create_file():
    i=1
    with open("../data.csv", mode='w',newline='\n') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow(["hello","world"])
        # f.write("hello,world\n")
        f.close()

        
    

        
if __name__=="__main__":
    uvicorn.run("app:app", port=port, host=host)
    create_file()