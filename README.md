# http-conditional

判定条件请求：ETag 强弱比较、`If-None-Match` 列表与 `*`、`If-Modified-Since`、以及两者的优先级。只用 Python 标准库。

```
python3 -m unittest discover -s tests
python3 -m conditional --sample=weak
python3 -m conditional --sample=star
python3 -m conditional --sample=precedence
python3 -m conditional --sample=starmatch
python3 -m conditional --sample=work
```

## 口径

- **强弱**：`W/"x"` 与 `"x"` 不相等；只有两边的标签都不带 `W/` 且内容相同才算强匹配。
- **列表**：`If-None-Match` 用逗号分隔，逐个比较，任意一个匹配即可。
- **星号**：`*` 匹配任何已存在的资源。
- **优先级**：同时有 `If-None-Match` 和 `If-Modified-Since` 时，只看前者。
- **判定**：`If-None-Match` 命中返回 304，`If-Match` 未命中返回 412，其余返回 200。
- **查找**：比较只跟请求里给出的标签个数成正比。

## 不变量

- 带 `W/` 的标签永远不参与强匹配。
- `If-None-Match` 存在时 `If-Modified-Since` 不参与判定。
- `scanned` 不随标签数乘查询次数放大：八百个标签的 `scanned` 不超过 6000。

## 输出契约

`evaluate(request, etag, last_modified)` 返回状态码。场景打印一行 JSON。
`--sample=work` 打印 `{"tags": N, "scanned": N}`。
