from __future__ import annotations
from datetime import date
from .model import TaskBlock
from .summarize import block_bullets

def render_daily_markdown(day: date, blocks: list[TaskBlock]) -> str:
    lines: list[str] = []
    lines.append(f"# 日報 {day.isoformat()}")
    lines.append("")
    lines.append("## 今日の作業")
    lines.append("")

    for b in blocks:
        lines.append(f"### {b.title}（{b.start.strftime('%H:%M')}–{b.end.strftime('%H:%M')}）")
        bullets = block_bullets(b)
        if bullets:
            for x in bullets:
                lines.append(f"- {x}")
        else:
            lines.append("- （詳細未記入）")
        lines.append("")

    lines.append("## まとめ")
    lines.append(f"- 作業ブロック数: {len(blocks)}")
    return "\n".join(lines)
