from __future__ import annotations
import argparse
from datetime import date
from pathlib import Path

from .io_jsonl import load_events_jsonl
from .summarize import group_into_blocks
from .render_md import render_daily_markdown

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="in_path", required=True, help="input jsonl path")
    p.add_argument("--out", dest="out_path", required=True, help="output md path")
    p.add_argument("--day", dest="day", required=True, help="YYYY-MM-DD")
    args = p.parse_args()

    in_path = Path(args.in_path)
    out_path = Path(args.out_path)
    day = date.fromisoformat(args.day)

    events = load_events_jsonl(in_path)
    blocks = group_into_blocks(events)
    md = render_daily_markdown(day, blocks)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")
    print(f"✅ wrote: {out_path}")

if __name__ == "__main__":
    main()
