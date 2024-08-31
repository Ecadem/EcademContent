from fastapi import FastAPI

from src.routers.routers import router as index
from src.routers.content import router as content

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(
    title="Ecadem Content",
    description="This API allows you to access all the content of the Ecadem.co website, including posts, images, projects, etc.",
    version="1.0",
    openapi_url="/openapi.json", 
    docs_url="/docs",
    middleware=middleware
)

routers = [
    index,
    content
]

for rout in routers:
    app.include_router(rout)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=80, host='0.0.0.0')
