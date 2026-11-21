"""Regenerate assets/languages.svg from the language data of my public repos.

Run locally:  python scripts/gen_languages.py
Runs daily in GitHub Actions (.github/workflows/languages.yml).
"""
import collections, datetime, json, math, os, pathlib, urllib.request

USER = os.environ.get("GITHUB_REPOSITORY_OWNER", "Anurag012345")
EXCLUDE = {USER}  # repo names to leave out of the chart, e.g. {USER, "old-project"}
SHOWN = 4         # languages drawn individually; the rest are grouped as "Other"
COLORS = {"JavaScript": "#f1e05a", "Python": "#4b8bbe", "TypeScript": "#3178c6",
          "CSS": "#a371f7", "HTML": "#e34c26", "Java": "#b07219", "C++": "#f34b7d",
          "Go": "#00add8", "Rust": "#dea584", "Other": "#8b949e"}
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "languages.svg"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "profile-stats"})
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    return json.load(urllib.request.urlopen(req))


repos = [r for r in get(f"https://api.github.com/users/{USER}/repos?per_page=100")
         if not r["fork"] and r["name"] not in EXCLUDE]
total, used, per_repo = collections.Counter(), collections.defaultdict(set), {}
for r in repos:
    langs = get(f"https://api.github.com/repos/{USER}/{r['name']}/languages")
    per_repo[r["name"]] = langs
    for lang, n in langs.items():
        total[lang] += n
        used[lang].add(r["name"])
S = sum(total.values())

top = [k for k, _ in total.most_common(SHOWN)]
rest = [k for k in total if k not in top]
rows = [(k, total[k], len(used[k])) for k in top]
if rest:
    rows.append(("Other", sum(total[k] for k in rest), len(set().union(*(used[k] for k in rest)))))

big = max(per_repo, key=lambda n: sum(per_repo[n].values()))
big_lang = max(per_repo[big], key=per_repo[big].get)
color = lambda k: COLORS.get(k, "#8b949e")

C = 2 * math.pi * 72
arcs, bars, off, mx = "", "", 0.0, max(b for _, b, _ in rows)
for i, (k, b, n) in enumerate(rows):
    seg = max(C * b / S - 2, 0.5)
    arcs += (f'<circle cx="150" cy="190" r="72" fill="none" stroke="{color(k)}" stroke-width="28" '
             f'stroke-dasharray="{seg:.2f} {C - seg:.2f}" stroke-dashoffset="{-off:.2f}" '
             f'transform="rotate(-90 150 190)"/>\n')
    off += C * b / S
    y = 120 + i * 38
    bars += (f'<circle cx="308" cy="{y-5}" r="6" fill="{color(k)}"/>\n'
             f'<text x="322" y="{y}" class="lbl">{k}</text>\n'
             f'<rect x="420" y="{y-14}" width="220" height="12" rx="6" fill="#21262d"/>\n'
             f'<rect x="420" y="{y-14}" width="{220*b/mx:.1f}" height="12" rx="6" fill="{color(k)}" '
             f'class="bar" style="animation-delay:{i*0.12:.2f}s"/>\n'
             f'<text x="652" y="{y-3}" class="pct">{100*b/S:.1f}%</text>\n'
             f'<text x="704" y="{y-3}" class="sub">{n} repo{"s" if n != 1 else ""}</text>\n')

alt = ", ".join(f"{k} {100*b/S:.0f}%" for k, b, _ in rows)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{110 + 38*len(rows) + 50}" viewBox="0 0 760 {110 + 38*len(rows) + 50}" role="img" aria-label="Language share across public repositories: {alt}">
<style>
text{{font-family:'Segoe UI',Ubuntu,Helvetica,Arial,sans-serif}}
.t{{font-size:21px;font-weight:700;fill:#e6edf3}}
.s{{font-size:13px;fill:#8b949e}}
.lbl{{font-size:15px;fill:#e6edf3}}
.pct{{font-size:14px;font-weight:600;fill:#e6edf3}}
.sub{{font-size:12px;fill:#8b949e}}
.big{{font-size:24px;font-weight:700;fill:#e6edf3;text-anchor:middle}}
.small{{font-size:12px;fill:#8b949e;text-anchor:middle}}
.bar{{transform-box:fill-box;transform-origin:left center;animation:grow .9s ease-out both}}
@keyframes grow{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
</style>
<rect x=".5" y=".5" width="759" height="{110 + 38*len(rows) + 49}" rx="16" fill="#0d1117" stroke="#30363d"/>
<text x="32" y="46" class="t">Languages across my public repos</text>
<text x="32" y="68" class="s">Share of code in {len(repos)} public repos, counted {datetime.date.today():%b %Y}</text>
{arcs}<text x="150" y="190" class="big">{S/1000:.0f} KB</text>
<text x="150" y="210" class="small">of code</text>
{bars}<text x="32" y="{110 + 38*len(rows) + 28}" class="s">{big}, my largest project, is {big_lang} first.</text>
</svg>
'''
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(svg, encoding="utf-8")
print(OUT, [(k, round(100 * b / S, 1), n) for k, b, n in rows])
