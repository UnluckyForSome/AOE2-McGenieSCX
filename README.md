# genie-scx-py

Pure-Python port of the Rust crate [`genie-scx`](https://github.com/SiegeEngineers/genie-rs/tree/default/crates/genie-scx) for reading **legacy** Age of Empires II scenario containers (`.scn`, `.scx`, and related pre–Definitive Edition format versions).

## Scope

This package intentionally focuses on **classic / legacy** scenarios only.

Any beginnings of **Definitive Edition** parsing were removed; full DE support belongs in [**AoE2ScenarioParser**](https://github.com/KSneijders/AoE2ScenarioParser). Here, DE-shaped inputs are **rejected at parse time** (see `DefinitiveEditionScenarioError` and related checks in `genie_scx_py.types`) so callers fail fast instead of partially mis-reading a DE file.

## Install

```bash
pip install git+https://github.com/UnluckyForSome/genie-scx-py.git
```

## Usage

```python
from genie_scx_py import Scenario

with open("scenario.scx", "rb") as f:
    scen = Scenario.read_from(f)
```

For **`.aoe2scenario`** and other DE containers, use [AoE2ScenarioParser](https://github.com/KSneijders/AoE2ScenarioParser) instead.

## Layout

Python sources live under the `genie_scx_py/` package directory.

## License

MIT — see [LICENSE](LICENSE).
