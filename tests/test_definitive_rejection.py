from __future__ import annotations

import io
import struct
from unittest import TestCase

from aoe2_mcgeniescx import Scenario
from aoe2_mcgeniescx._io import deflate_raw
from aoe2_mcgeniescx.header import SCXHeader
from aoe2_mcgeniescx.types import DefinitiveEditionScenarioError, SCXVersion


def _build_detection_fixture(format_token: bytes, data_version: float) -> bytes:
    out = io.BytesIO()
    out.write(format_token)
    header = SCXHeader(
        version=2,
        timestamp=0,
        description=None,
        author_name=None,
        any_sp_victory=True,
        active_player_count=8,
        dlc_options=None,
    )
    header.write_to(out, SCXVersion(format_token), 2)
    payload = struct.pack("<if", 0, float(data_version))
    out.write(deflate_raw(payload))
    return out.getvalue()


class TestDefinitiveRejection(TestCase):
    def test_rejects_de_container_format(self):
        with self.assertRaises(DefinitiveEditionScenarioError) as ctx:
            Scenario.read_from_bytes(b"1.36")

        self.assertEqual("1.36", ctx.exception.container_format)
        self.assertIsNone(ctx.exception.data_version)

    def test_rejects_de_payload_data_version(self):
        data = _build_detection_fixture(b"1.21", 1.30)

        with self.assertRaises(DefinitiveEditionScenarioError) as ctx:
            Scenario.read_from_bytes(data)

        self.assertIsNone(ctx.exception.container_format)
        self.assertAlmostEqual(1.30, ctx.exception.data_version)
