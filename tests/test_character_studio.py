import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = json.loads((ROOT / "character-studio" / "characters.json").read_text(encoding="utf-8"))
SCHEMA = json.loads((ROOT / "character-studio" / "schema.json").read_text(encoding="utf-8"))
SCRIPT = (ROOT / "character-studio" / "studio.js").read_text(encoding="utf-8")


class CharacterStudioFixtureTests(unittest.TestCase):
    def test_schema_is_versioned_and_closes_unknown_top_level_fields(self):
        self.assertEqual(SCHEMA["properties"]["schema_version"]["const"], 1)
        self.assertFalse(SCHEMA["additionalProperties"])

    def test_fin_and_nik_have_stable_unique_ids_and_provenance(self):
        chars = FIXTURES["characters"]
        self.assertEqual(set(chars), {"fin", "nik"})
        ids = [item["character_id"] for item in chars.values()]
        self.assertEqual(len(ids), len(set(ids)))
        for item in chars.values():
            self.assertTrue(item["provenance"]["source_refs"])
            self.assertEqual(item["provenance"]["review_status"], "DRAFT_REQUIRES_HUMAN_REVIEW")
            self.assertIsNone(item["identity"]["body_proportions"])

    def test_fixtures_preserve_documented_canon_without_inventing_body_proportions(self):
        fin = FIXTURES["characters"]["fin"]
        nik = FIXTURES["characters"]["nik"]
        self.assertEqual(fin["identity"]["age_years"], 4)
        self.assertEqual(nik["identity"]["age_years"], 8)
        self.assertIn("short dark coily hair", fin["identity"]["hair_description"])
        self.assertIn("long dark-brown hair", nik["identity"]["hair_description"])
        self.assertIsNone(nik["appearance"]["lower_garment"])

    def test_appearance_controls_do_not_write_to_identity(self):
        self.assertIn('current.appearance.garment_colour = $("garment-colour").value', SCRIPT)
        self.assertIn('current.appearance.garment_style = $("garment-style").value', SCRIPT)
        self.assertIn('current.appearance.show_accessory = $("show-accessory").checked', SCRIPT)
        self.assertNotRegex(SCRIPT, r'current\.identity\.[A-Za-z_]+\s*=')
        self.assertIn('current.identity = JSON.parse(originalIdentity)', SCRIPT)

    def test_svg_renderer_is_deterministic_function_of_character_data(self):
        self.assertIn("function renderSvg(character)", SCRIPT)
        self.assertIn("return '<svg", SCRIPT)
        self.assertNotIn("Math.random", SCRIPT)
        self.assertNotIn("Date.now", SCRIPT)

    def test_exports_include_provenance_and_review_state(self):
        self.assertIn('exported.provenance.exported_at', SCRIPT)
        self.assertIn('exported.provenance.review_status = "DRAFT_REQUIRES_HUMAN_REVIEW"', SCRIPT)
        self.assertIn('download(current.character_id.replaceAll(".","-")+".svg"', SCRIPT)

    def test_html_has_accessible_mobile_editor_controls(self):
        html = (ROOT / "character-studio" / "index.html").read_text(encoding="utf-8")
        self.assertIn('name="viewport"', html)
        self.assertIn('aria-live="polite"', html)
        self.assertIn('id="identity-summary"', html)


if __name__ == "__main__":
    unittest.main()
