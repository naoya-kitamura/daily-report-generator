from __future__ import annotations
from .model import Event, TaskBlock

def group_into_blocks(events: list[Event]) -> list[TaskBlock]:
    if not events:
        return []

    blocks: list[TaskBlock] = []
    cur_title = events[0].title
    cur_events: list[Event] = [events[0]]

    for e in events[1:]:
        if e.title == cur_title:
            cur_events.append(e)
        else:
            blocks.append(
                TaskBlock(
                    title=cur_title,
                    start=cur_events[0].ts,
                    end=cur_events[-1].ts,
                    events=cur_events,
                )
            )
            cur_title = e.title
            cur_events = [e]

    blocks.append(
        TaskBlock(
            title=cur_title,
            start=cur_events[0].ts,
            end=cur_events[-1].ts,
            events=cur_events,
        )
    )
    return blocks

def block_bullets(block: TaskBlock) -> list[str]:
    bullets = []
    for e in block.events:
        if e.detail:
            bullets.append(e.detail)

    seen = set()
    uniq = []
    for b in bullets:
        if b not in seen:
            seen.add(b)
            uniq.append(b)
    return uniq[:10]
