from fastapi import FastAPI, Request
from app.models import models 
from app.controller.database import engine
from app.models.failure import Failure
from app.router.urls import router
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
models.base.metadata.create_all(bind=engine)

app = FastAPI()

@app.exception_handler(Failure)
async def name_exception_handler(request: Request, exc: Failure):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": str(exc.detail)},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)},
    )

app.include_router(router=router)