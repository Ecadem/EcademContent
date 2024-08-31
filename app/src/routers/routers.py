# -*- coding: utf-8 -*-
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def root():
   with open("/workspaces/EcademContent/app/src/templates/index.html", "r") as file:
       return file.read()

        