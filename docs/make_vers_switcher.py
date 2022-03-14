import json
from pathlib import Path

all_vers = sorted(
    (i.name for i in Path('.').glob('*') if i.is_dir()),
    key=lambda i: i if not i[-1].isdigit() else i + 'z'
)
vers_switcher = [
    {
        "name": "dev" if idx == 0 else ("stable" if idx == 1 else vers),
        "version": vers,
    } for idx, vers in enumerate(all_vers)
]
docs_dir = Path(__file__).parent.resolve()
with Path('switcher.json').open('w') as fh:
    json.dump(str(docs_dir.join(vers_switcher)), fh)
