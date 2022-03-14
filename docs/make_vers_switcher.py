import json
from pathlib import Path

docs_dir = Path(__file__).parent.resolve()
all_vers = sorted(
    (i.name for i in docs_dir.glob('*') if i.is_dir()),
    key=lambda i: i if not i[-1].isdigit() else i + 'z'
)
vers_switcher = [
    {
        "name": "dev" if idx == 0 else ("stable" if idx == 1 else vers),
        "version": vers,
    } for idx, vers in enumerate(all_vers)
]
with docs_dir.joinpath('switcher.json').open('w') as fh:
    json.dump(vers_switcher, fh)
