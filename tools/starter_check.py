#!/usr/bin/env python3
"""Verificador sem ROM do kit inicial do Pokemon UltraRed."""
from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "src/config.h", "scripts/make.py", "scripts/build.py",
    "scripts/insert.py", "BPRE.ld", "linker.ld",
]

def main() -> int:
    parser = argparse.ArgumentParser(description="Verificar estrutura e opcoes do CFRU")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    ok, errors, information = [], [], []

    for name in REQUIRED:
        (ok if (ROOT / name).is_file() else errors).append(
            ("Presente: " if (ROOT / name).is_file() else "Ausente: ") + name
        )

    config_file = ROOT / "src/config.h"
    if config_file.is_file():
        content = config_file.read_text(encoding="utf-8")
        defines = {
            m.group(1): m.group(2)
            for m in re.finditer(
                r"^\s*#\s*define\s+([A-Z][A-Z0-9_]*)\b(?:\s+([^\s/]+))?",
                content, re.MULTILINE,
            )
        }
        raw = defines.get("STANDARD_IV")
        try:
            iv = int(raw, 0)
            if not 0 <= iv <= 31:
                raise ValueError("Valor fora do intervalo 0-31")
            ok.append(f"STANDARD_IV = {iv} (valido)")
        except (ValueError, TypeError):
            errors.append(f"STANDARD_IV invalido: {raw!r}")
        for feature in ("MEGA_EVOLUTION_FEATURE", "TIME_ENABLED", "DISPLAY_EFFECTIVENESS_ON_MENU"):
            information.append(f"{feature}: {'habilitado' if feature in defines else 'desabilitado'}")
        for debug in ("DEBUG_MEGA", "DEBUG_QUICK_BATTLES"):
            if debug in defines:
                information.append(f"ATENCAO: modo debug {debug} ativo!")

    for name in ("scripts/make.py", "scripts/build.py", "scripts/insert.py", "tools/starter_check.py"):
        path = ROOT / name
        if path.is_file():
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=name)
                ok.append(f"Sintaxe Python: {name}")
            except SyntaxError as e:
                errors.append(f"Erro Python: {name}, linha {e.lineno}: {e.msg}")

    result = [
        "# Primeiro teste - Pokemon UltraRed", "",
        "**Este teste NAO compila nem gera uma ROM .gba.**", "",
        "## Status: " + ("APROVADO" if not errors else "FALHOU"), "",
        "## Verificacoes", "",
    ]
    result += [f"- OK: {item}" for item in ok]
    result += [f"- ERRO: {item}" for item in errors]
    result += ["", "## Configuracoes", ""]
    result += [f"- {item}" for item in information]
    result += ["", "Proximo passo: validar uma compilacao real do motor CFRU, sem distribuir ROMs comerciais.", ""]
    report = "\n".join(result)
    print(report)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding="utf-8")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
