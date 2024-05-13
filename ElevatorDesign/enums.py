from enum import Enum


class Direction(Enum):
    UP = "upside"
    DOWN = 'downside'


class Status(Enum):
    RUNNING = 'running'
    IDLE = "idle"
