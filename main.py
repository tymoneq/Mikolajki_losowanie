from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # For development, allow all. For production, specify your dashboard URL.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserInput(BaseModel):
    name: str


listOfGifts = {
    "alicja": "Tymon",
    "gaweł": "Filip",
    "agnieszka": "Gaweł",
    "filip": "Zuzia",
    "tymon": "Agnieszka",
    "zuzia": "Alicja",
}
@app.get("/")
async def read_root():
    # This tells FastAPI: "When someone visits '/', send them this file"
    return FileResponse('static/index.html')

@app.post("/getNames")
def fname(name: UserInput):
    print(name.name)
    name.name = name.name.lower()
    name_in_list = listOfGifts.get(name.name)
    error_message = "Wrong name\n"

    message = name_in_list

    if not name_in_list:
        message = error_message

    return {"message": message}
