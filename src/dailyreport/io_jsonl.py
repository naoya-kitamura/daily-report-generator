from __future__ import annotations
import json
from datetime import datetime
from pathlib import Path
from .model import Event

def load_events_jsonl(path: Path) -> list[Event]:
    events: list[Event] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        obj = json.loads(line)
        try:
            ts = datetime.fromisoformat(obj["ts"])
            title = str(obj["title"]).strip()
            detail = str(obj.get("detail", "")).strip()
        except Exception as e:
            raise ValueError(f"Invalid JSONL at line {line_no}: {e}") from e
        events.append(Event(ts=ts, title=title, detail=detail))
    events.sort(key=lambda e: e.ts)
    return events
