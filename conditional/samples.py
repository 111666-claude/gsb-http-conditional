"""固定场景，用来复现题面里的锚点。"""

import json

from . import core


def _line(obj):
    print(json.dumps(obj, ensure_ascii=False))


def run(name):
    if name == "weak":
        status = core.evaluate({"if_none_match": '"x"'}, 'W/"x"', 0, core.Counter())
        _line({"status": status})
        return 0
    if name == "star":
        status = core.evaluate({"if_none_match": "*"}, '"x"', 0, core.Counter())
        _line({"status": status})
        return 0
    if name == "precedence":
        request = {"if_none_match": '"a"', "if_modified_since": 100}
        status = core.evaluate(request, '"x"', 50, core.Counter())
        _line({"status": status})
        return 0
    if name == "starmatch":
        status = core.evaluate({"if_match": "*"}, '"x"', 0, core.Counter())
        _line({"status": status})
        return 0
    if name == "work":
        tags = ['"t%04d"' % i for i in range(800)]
        counter = core.Counter()
        core.evaluate({"if_none_match": ", ".join(tags)}, '"t0799"', 0, counter)
        _line({"tags": 800, "scanned": counter.scanned})
        return 0
    raise SystemExit("未知场景：" + name)
