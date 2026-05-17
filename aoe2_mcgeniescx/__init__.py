"""
Pure-Python port of the Rust crate `genie-scx`.

Maintained as the standalone package **AOE2-McGenieSCX**
(https://github.com/UnluckyForSome/AOE2-McGenieSCX). Use from AoE2ScenarioParser legacy bridge,
McMinimap, or any tool that needs legacy `.scn` / `.scx` parsing in-process.
"""

from __future__ import annotations

from .scenario import Scenario
from .types import (
    DEFINITIVE_EDITION_MIN_DATA_VERSION,
    CannotDisableBuildingsError,
    CannotDisableTechsError,
    CannotDisableUnitsError,
    DefinitiveEditionScenarioError,
    LEGACY_MAX_CONTAINER_FORMAT_TOKEN,
    SCXVersion,
    TooManyDisabledBuildingsError,
    TooManyDisabledTechsError,
    UnsupportedFormatVersionError,
    VersionBundle,
    is_ascii_scx_version_prefix,
    is_definitive_edition_container_format,
    is_definitive_edition_scenario_data_version,
    normalize_scenario_data_version,
    legacy_format_version_from_prefix,
    legacy_format_version_peek_path,
)
from ._support.strings import DecodeStringError, EncodeStringError

__all__ = [
    "Scenario",
    "SCXVersion",
    "VersionBundle",
    "DEFINITIVE_EDITION_MIN_DATA_VERSION",
    "DefinitiveEditionScenarioError",
    "TooManyDisabledTechsError",
    "CannotDisableTechsError",
    "CannotDisableUnitsError",
    "TooManyDisabledBuildingsError",
    "CannotDisableBuildingsError",
    "UnsupportedFormatVersionError",
    "LEGACY_MAX_CONTAINER_FORMAT_TOKEN",
    "is_ascii_scx_version_prefix",
    "is_definitive_edition_container_format",
    "is_definitive_edition_scenario_data_version",
    "normalize_scenario_data_version",
    "legacy_format_version_from_prefix",
    "legacy_format_version_peek_path",
    "DecodeStringError",
    "EncodeStringError",
]

