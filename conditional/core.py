"""判定条件请求。"""


class Counter:
    """记录比较次数。"""

    def __init__(self):
        self.scanned = 0


def _strong_equal(a, b):
    return a.replace("W/", "") == b.replace("W/", "")


def evaluate(request, etag, last_modified, counter):
    if "if_none_match" in request:
        header = request["if_none_match"]
        tags = header.split(",")
        for i in range(len(tags)):
            counter.scanned += len(tags)
            tag = header.split(",")[i].strip()
            if _strong_equal(tag, etag):
                return 304
    if "if_match" in request:
        counter.scanned += 1
        if not _strong_equal(request["if_match"], etag):
            return 412
    if "if_modified_since" in request and last_modified <= request["if_modified_since"]:
        counter.scanned += 1
        return 304
    return 200
