#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
score_brier.py —— ST21-Door 公开预测栏的打分脚本（口径见 predictions/README.md 第 5 节）

规则（R-c）：
  * 只纳入已结算的 TRUE / FALSE；
  * VOID 不计分，但单独列出数量与原因（原因取自正文的 `VOID原因：...` 行）；
  * 按预测者逐项计算 Brier 分，并披露有效样本数 n；
  * 同一事件多预测者可分别计分，但会标注为同事件。

单条得分 = (probability - outcome)^2 ，其中 TRUE = 1，FALSE = 0。
个人 Brier = 该预测者所有已结算条目的平均。

用法：
  python3 predictions/score_brier.py                 # 默认扫描脚本所在目录
  python3 predictions/score_brier.py --dir <目录>
  python3 predictions/score_brier.py --json
"""

import argparse
import json
import os
import re
import sys

FIELDS = ["id", "author", "content_sha256", "claim", "probability",
          "deadline_utc", "criterion", "criterion_source", "resolver", "status"]
SKIP_FILES = {"readme.md", "index.md", "_template.md", "score_brier.py"}


def read_front_matter(path):
    """读取 md 顶部的 `--- ... ---` 块；字段值取 `: ` 之后到行尾的全部内容（原样，不折行）。"""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    lines = text.replace("\r\n", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    data = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s?(.*)$", line)
        if m:
            data[m.group(1)] = m.group(2)
    return data, text


def void_reason(text):
    for line in text.replace("\r\n", "\n").split("\n"):
        m = re.match(r"^\s*VOID原因[:：]\s*(.+)$", line)
        if m:
            return m.group(1).strip()
    return "(未写明原因)"


def collect(root):
    rows = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in sorted(filenames):
            if not fn.lower().endswith(".md") or fn.lower() in SKIP_FILES:
                continue
            path = os.path.join(dirpath, fn)
            fm, text = read_front_matter(path)
            if not fm or "id" not in fm:
                continue
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            rows.append({
                "file": rel,
                "id": fm.get("id", ""),
                "author": fm.get("author", ""),
                "probability": fm.get("probability", ""),
                "deadline_utc": fm.get("deadline_utc", ""),
                "criterion_source": fm.get("criterion_source", ""),
                "status": (fm.get("status", "") or "").strip(),
                "void_reason": void_reason(text) if (fm.get("status", "") or "").startswith("VOID") else "",
                "is_agi": rel.startswith("agi/"),
            })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=os.path.dirname(os.path.abspath(__file__)),
                    help="predictions 目录（默认：脚本所在目录）")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()

    rows = collect(args.dir)
    if not rows:
        print("没有找到任何预测文件。")
        return 0

    # 同一事件标注：criterion_source + deadline_utc 相同者视为同事件可比较组
    groups = {}
    for r in rows:
        key = (r["criterion_source"].strip(), r["deadline_utc"].strip())
        groups.setdefault(key, []).append(r["id"])
    same_event = {k: v for k, v in groups.items() if len(v) > 1}

    scored, voids, open_items, other = [], [], [], []
    for r in rows:
        s = r["status"].split("（")[0].strip().upper()
        if s in ("TRUE", "FALSE"):
            try:
                p = float(r["probability"])
            except ValueError:
                other.append((r["id"], "probability 无法解析：%r" % r["probability"]))
                continue
            outcome = 1.0 if s == "TRUE" else 0.0
            rec = dict(r)
            rec["score"] = (p - outcome) ** 2
            scored.append(rec)
        elif s.startswith("VOID"):
            voids.append(r)
        elif s == "OPEN":
            open_items.append(r)
        else:
            other.append((r["id"], "status 未识别：%r" % r["status"]))

    short_scored = [r for r in scored if not r["is_agi"]]
    agi_scored = [r for r in scored if r["is_agi"]]
    by_author = {}
    for r in short_scored:
        by_author.setdefault(r["author"], []).append(r)

    if args.json:
        print(json.dumps({
            "scored": [{"id": r["id"], "author": r["author"], "probability": r["probability"],
                        "status": r["status"], "score": r["score"]} for r in scored],
            "voids": [{"id": r["id"], "author": r["author"], "reason": r["void_reason"]} for r in voids],
            "open": [{"id": r["id"], "author": r["author"], "deadline_utc": r["deadline_utc"]} for r in open_items],
            "same_event_groups": {("%s | %s" % k): v for k, v in same_event.items()},
        }, ensure_ascii=False, indent=2))
        return 0

    print("预测总数：%d  ｜ 已结算(TRUE/FALSE)：%d  ｜ VOID：%d  ｜ 待结算(OPEN)：%d  ｜ 异常：%d"
          % (len(rows), len(scored), len(voids), len(open_items), len(other)))
    print()

    print("== 个人 Brier 分（短期，不含 AGI 条）==")
    if not by_author:
        print("  （暂无已结算条目）")
    for author in sorted(by_author):
        rs = by_author[author]
        mean = sum(x["score"] for x in rs) / len(rs)
        ids = ", ".join(x["id"] for x in rs)
        print("  %-6s Brier = %.4f   n = %d   （%s）" % (author, mean, len(rs), ids))
    print()

    if agi_scored:
        print("== AGI 条（单独判定）==")
        for r in agi_scored:
            print("  %s  Brier = %.4f   status = %s" % (r["id"], r["score"], r["status"]))
        print()

    if voids:
        print("== VOID（不计分，附原因）==")
        for r in voids:
            print("  %s（%s）原因：%s" % (r["id"], r["author"], r["void_reason"]))
        print()

    if open_items:
        print("== 尚未结算（OPEN）==")
        for r in open_items:
            print("  %-11s %-4s deadline=%s" % (r["id"], r["author"], r["deadline_utc"]))
        print()

    if same_event:
        print("== 同一事件（可分别计分，但非同一样本）==")
        for (src, dl), ids in same_event.items():
            print("  %s  <- source=%s deadline=%s" % (", ".join(ids), src, dl))
        print()

    if other:
        print("== 异常 ==")
        for i, msg in other:
            print("  %s：%s" % (i, msg))

    return 0


if __name__ == "__main__":
    sys.exit(main())

