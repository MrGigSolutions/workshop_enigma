from typing import Union

from fastapi import FastAPI

from revolutionaries import rotor
from wire_warriors import machine

app = FastAPI()

app.include_router(rotor.router)
app.include_router(machine.router)