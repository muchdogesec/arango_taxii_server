import glob
import json
import os
from pathlib import Path
import time
from types import SimpleNamespace
from urllib.parse import urljoin



def read_all_objects():
    v = {}
    for bundle in glob.glob('tests/bundles/*.json'):
        dct = json.loads(Path(bundle).read_text())
        for obj in dct['objects']:
            obj_s = v.setdefault(obj['id'], [])
            obj_s.append(obj)
    for vv in v.values():
        vv.sort(key=lambda x: (x['modified'], x['created']), reverse=True)
    return v

objects = [(k, [y['modified'] for y in v]) for k, v in read_all_objects().items()]

last_objects = [(k, v[-1]) for k, v in objects]
first_objects = [(k, v[0]) for k, v in objects]
all_versions = list(set([(k, vv) for k, v in objects for vv in v]))
print(f"{last_objects=}")
print(f"{first_objects=}")
print(f"{all_versions=}")