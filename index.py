from datasette.app import Datasette
import json
import pathlib
static_mounts = [
    (static, str((pathlib.Path(".") / static).resolve()))
    for static in []
]
metadata = dict()
try:
    metadata = json.load(open("metadata.json"))
except Exception:
    pass
app = Datasette(
    [],
    ["mydatabase.db"],
    static_mounts=static_mounts,
    metadata=metadata,
    cors=True,
    config={}
).app()