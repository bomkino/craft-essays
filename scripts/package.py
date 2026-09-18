#!/usr/bin/env python3
"""Build the portable skill ZIP with a reproducible member order and timestamp."""
from hashlib import sha256
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "craft-essays"
FILES = [
    "LICENSE",
    "SKILL.md",
    "agents/openai.yaml",
    "references/expression.md",
    "references/origins.md",
    "references/structure.md",
    "references/substance.md",
]

def main():
    contents = {}
    for name in FILES:
        path = SOURCE / name
        if path.is_symlink() or not path.is_file():
            raise SystemExit(f"Missing or unsupported package member: {name}")
        contents[name] = path.read_bytes()
    destination = ROOT / "dist"
    destination.mkdir(exist_ok=True)
    archive = destination / "craft-essays.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
        for name, data in contents.items():
            member = ZipInfo(f"craft-essays/{name}", date_time=(2026, 1, 1, 0, 0, 0))
            member.compress_type = ZIP_DEFLATED
            member.create_system = 3
            member.external_attr = 0o100644 << 16
            bundle.writestr(member, data)
    digest = sha256(archive.read_bytes()).hexdigest()
    (destination / "SHA256SUMS").write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(f"{archive.name}: {archive.stat().st_size} bytes, SHA-256 {digest}")

if __name__ == "__main__":
    main()
