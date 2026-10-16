"""Flag substantive Markdown lines that carry no citation or epistemic label.

Usage: python3 -E check_citations.py file1.md [file2.md ...]
Prints file:line: text for each uncited line and a per-file count.
Exit status 1 if anything is flagged.
"""
import re, sys, pathlib

CITE = re.compile(
    r"(R[12]/|R[12]-\d|R[12] |Release [12]|Bylaws|Art\. ?[IVX]+|§|C\.F\.R|U\.S\.C|CPLR|PHL|GML|Educ\. Law|"
    r"Labor Law|Exec\. Law|Fin\. Law|Agreement p\.|Addendum|Intake|Summary|Notes p|Minutes|"
    r"VERIFIED|INFERRED|\bINF\b|OPEN|\[M\]|\bG\d+\b|\(0\d\)|\bsee 0\d|\bE\d+\b|Assignment 2 memo|"
    r"p\.\d|pp\.\d|\.pdf|\.png|\.docx?|Q\d)"
)

def exempt(s: str) -> bool:
    t = s.strip()
    if not t or t.startswith(("#", "```", "|", ">")):
        return True
    if re.fullmatch(r"\*\*[^*]+\*\*:?", t):           # bold headings (entry titles)
        return True
    if re.fullmatch(r"[-*] \*[^*]+:\*\s*(No|Yes|Unknown|DT|RA|AA|scan|text|image|partial|—)?\.?", t):
        return True
    if re.match(r"^- \*\*[A-Z]{2,4}\*\*:", t) or t.endswith("is one of the following:"):
        return True  # label definitions
    if "<!-- nocite -->" in t:
        return True  # explicit structural line
    body = re.sub(r"^[-*\d.]+\s*", "", t)
    return len(body) < 25  # short field values / labels

def main(paths):
    """Entries (a **bold** title followed by '- *Field:*' bullets) count as cited
    if any line in the entry carries a citation. Other lines are checked alone."""
    total = 0
    for p in paths:
        lines = pathlib.Path(p).read_text().split("\n")
        in_code = False; n = 0; i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith("```"):
                in_code = not in_code; i += 1; continue
            if not in_code and re.fullmatch(r"\*\*[^*]+\*\*:?", line.strip()):
                j = i + 1
                while j < len(lines) and lines[j].startswith("- *"):
                    j += 1
                block = "\n".join(lines[i:j])
                title = line.strip()
                numbered = j < len(lines) and re.match(r"^\s*$", lines[j]) and j+1 < len(lines) and re.match(r"^\d+\.", lines[j+1])
                if title.endswith(".md**") or numbered:
                    i = j; continue  # file-list entries / headings over cited numbered lists
                if not CITE.search(block):
                    n += 1; print(f"{pathlib.Path(p).name}:{i+1}: ENTRY {line.strip()[:120]}")
                i = j; continue
            if not in_code and not exempt(line) and not CITE.search(line):
                n += 1; print(f"{pathlib.Path(p).name}:{i+1}: {line.strip()[:160]}")
            i += 1
        print(f"== {pathlib.Path(p).name}: {n} uncited"); total += n
    print(f"TOTAL uncited: {total}")
    return 1 if total else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
