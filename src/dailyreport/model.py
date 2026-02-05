from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Event:
    ts: datetime
    title: str
    detail: str

@dataclass(frozen=True)
class TaskBlock:
    title: str
    start: datetime
    end: datetime
    events: list[Event]
