from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="Trabajo 5 MLoops API",
    version="0.0.1"
)

users = {}
tasks = {}

@app.post("/api/v1/users")
async def create_user(username: str, name: str):
    user_id = str(uuid.uuid4())
    users[user_id] = {"username": username, "name": name}
    return JSONResponse(
        content={
            "username": username,
            "name": name,
            "ID": user_id,
            "message": "The user was created successfully",
        },
        status_code=status.HTTP_201_CREATED
    )

@app.get("/api/v1/users/{user_id}")
async def get_user(user_id: str):
    if user_id in users:
        return JSONResponse(
            content=users[user_id],
            status_code=status.HTTP_200_OK
        )
    else:
        return JSONResponse(
            content="User not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

