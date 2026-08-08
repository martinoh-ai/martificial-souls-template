import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class SecurityTemplateTests(unittest.TestCase):
    def test_bus_requires_authenticated_broker_and_replay_protection(self):
        text = (ROOT / "_AGENT-CORE.md").read_text(encoding="utf-8")
        for control in ("busctl", "ACL", "signature", "anti-rejeu", "usage unique"):
            self.assertIn(control, text)

    def test_retrieval_profile_has_no_sensitive_tools(self):
        text = (ROOT / "scout.md").read_text(encoding="utf-8")
        self.assertIn("profil de récupération isolé", text)
        self.assertIn("sans shell", text)
        self.assertIn("schéma JSON borné", text)

    def test_builder_cannot_deploy(self):
        text = (ROOT / "builder.md").read_text(encoding="utf-8")
        self.assertIn("aucune clé", text)
        self.assertIn("ne copie jamais", text)
        self.assertIn("revue humaine du diff exact", text)


if __name__ == "__main__":
    unittest.main()
