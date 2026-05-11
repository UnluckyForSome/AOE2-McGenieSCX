# AOE2-McGenieSCX

Pure-Python port of the Rust crate [`genie-scx`](https://github.com/SiegeEngineers/genie-rs/tree/default/crates/genie-scx) for reading **legacy** Age of Empires II scenario containers (`.scn`, `.scx`, and related pre–Definitive Edition format versions).

## Scope

This package intentionally focuses on **classic / legacy** scenarios only.

Any beginnings of **Definitive Edition** parsing were removed; full DE support belongs in [**AoE2ScenarioParser**](https://github.com/KSneijders/AoE2ScenarioParser). Here, DE-shaped inputs are **rejected at parse time** (see `DefinitiveEditionScenarioError` and related checks in `aoe2_mcgeniescx.types`) so callers fail fast instead of partially mis-reading a DE file.

## Install

From PyPI:

```bash
pip install AOE2-McGenieSCX
```

From [TestPyPI](https://test.pypi.org/) (staging — use a **new version string** each upload; TestPyPI does not allow reusing the same version):

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ AOE2-McGenieSCX
```

`--extra-index-url https://pypi.org/simple/` keeps normal dependencies resolvable from production PyPI.

From Git (latest main):

```bash
pip install git+https://github.com/UnluckyForSome/AOE2-McGenieSCX.git
```

### Publishing (maintainers)

**TestPyPI** ([account / token](https://test.pypi.org/manage/account/)): bump `version` in `pyproject.toml`, build, then upload with the TestPyPI endpoint:

```bash
pip install build twine
rm -rf dist build
python -m build
twine upload --repository testpypi dist/*
```

Configure credentials once in **`~/.pypirc`** (Linux/macOS) or **`%USERPROFILE%\.pypirc`** (Windows):

```ini
[testpypi]
username = __token__
password = <paste TestPyPI API token>
```

Or pass tokens via environment variables ([twine docs](https://twine.readthedocs.io/en/stable/)).

**Production PyPI** is the same flow with `twine upload dist/*` (default repository) after you are happy with TestPyPI.

## Usage

```python
from aoe2_mcgeniescx import Scenario

with open("scenario.scx", "rb") as f:
    scen = Scenario.read_from(f)
```

For **`.aoe2scenario`** and other DE containers, use [AoE2ScenarioParser](https://github.com/KSneijders/AoE2ScenarioParser) instead.

## Layout

Python sources live under the `aoe2_mcgeniescx/` package directory.

## License

MIT — see [LICENSE](LICENSE).
