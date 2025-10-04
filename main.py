from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# If you want to allow *all* origins (i.e. fully global)
origins = ["*"]

# Or better: specify the allowed origins
# origins = [
#     "http://localhost:3000",
#     "https://myfrontenddomain.com",
#     # etc.
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,    # if you use cookies, or Authorization headers
    allow_methods=["*"],        # GET, POST, etc.
    allow_headers=["*"],        # which headers the client can send
    # optionally: expose_headers, allow_origin_regex, max_age, etc.
)

# Then define your endpoints
@app.get("/my-endpoint")
async def some_endpoint():
    return {"msg": "Hello from FastAPI!"}
