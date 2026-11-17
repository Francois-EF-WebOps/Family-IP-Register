import json
import tempfile
import unittest
from pathlib import Path
from scripts.generate import GenerationError, generate, load_identity_context, render, safe_output


class GeneratorTests(unittest.TestCase):
    def test_render_nested_values(self):
        self.assertEqual(render("Hello {{person.name}}", {"person": {"name": "Ada"}}), "Hello Ada")

    def test_missing_value_fails(self):
        with self.assertRaises(GenerationError):
            render("{{missing}}", {})

    def test_path_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(GenerationError):
                safe_output(Path(tmp), "../escape.txt")

    def test_identity_reference_is_available_to_templates(self):
        identity, receipt = load_identity_context(["persona.captain-narrator"])
        rendered = render("{{identity.entities.persona_captain_narrator.display_name}}", {"identity": identity})
        self.assertEqual(rendered, "Captain Narrator — Digital Voyager")
        self.assertEqual(receipt["refs"], ["persona.captain-narrator"])
        self.assertEqual(len(receipt["registry_sha256"]), 64)

    def test_unknown_identity_reference_fails_closed(self):
        with self.assertRaises(GenerationError):
            load_identity_context(["persona.not-defined"])

    def test_content_generation_and_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            job = root / "job.json"
            job.write_text(json.dumps({
                "kind": "content",
                "identity_refs": ["persona.captain-narrator"],
                "source_refs": ["https://example.invalid/source"],
                "data": {"title": "Test", "audience": "Readers", "purpose": "Explain",
                         "body": "Draft body", "source_notes": "Source pending verification"}
            }), encoding="utf-8")
            paths = generate(job, root / "out")
            self.assertEqual(len(paths), 2)
            self.assertTrue((root / "out" / "content.md").is_file())
            receipt = json.loads((root / "out" / "generation-receipt.json").read_text())
            self.assertEqual(receipt["review_status"], "DRAFT_REQUIRES_HUMAN_REVIEW")
            self.assertEqual(receipt["identity"]["refs"], ["persona.captain-narrator"])


if __name__ == "__main__":
    unittest.main()
