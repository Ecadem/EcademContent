from fastapi import FastAPI

from src.routers import router

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
    description="Esta API te permite acceder a todo el contenido de la pagina Ecadem.co posts, imagenes, proyectos, etc.",
    version = "1.0",
    openapi_url="/openapi.json", 
    docs_url="/docs",
    middleware=middleware
)

app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=80, host='0.0.0.0')
