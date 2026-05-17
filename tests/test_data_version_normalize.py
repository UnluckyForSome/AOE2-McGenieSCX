from __future__ import annotations

import struct
from unittest import TestCase

from aoe2_mcgeniescx.types import (
    is_definitive_edition_scenario_data_version,
    normalize_scenario_data_version,
)


class TestDataVersionNormalize(TestCase):
    def test_f32_one_point_two_two_normalizes_to_exact(self):
        raw = struct.unpack("<f", struct.pack("<f", 1.22))[0]
        self.assertNotEqual(raw, 1.22)
        self.assertEqual(1.22, normalize_scenario_data_version(raw))

    def test_is_definitive_false_for_aoc_data_version(self):
        raw = struct.unpack("<f", struct.pack("<f", 1.22))[0]
        self.assertFalse(is_definitive_edition_scenario_data_version(raw))

    def test_is_definitive_true_for_de_threshold(self):
        raw = struct.unpack("<f", struct.pack("<f", 1.28))[0]
        self.assertTrue(is_definitive_edition_scenario_data_version(raw))
