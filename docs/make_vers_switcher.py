import json
from pathlib import Path

docs_dir = Path(__file__).parent.resolve()
all_vers = sorted(
    (i.name for i in docs_dir.glob('*') if i.is_dir() and not i.is_symlink()),
    key=lambda i: i if not i[-1].isdigit() else i + 'z'
)
vers_switcher = [
    {
        "name": f"dev ({vers})" if idx == 0 else (f"stable ({vers})" if idx == 1 else vers),
        "version": vers.lstrip('v'),
    } for idx, vers in enumerate(all_vers)
]
with docs_dir.joinpath('switcher.json').open('w') as fh:
    json.dump(vers_switcher, fh, indent=4)
