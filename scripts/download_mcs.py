"""Download the USGS Mineral Commodity Summaries chapters for 2023, 2024 and 2025 into ../p2-raw.

It reads each year's directory listing (https://pubs.usgs.gov/periodicals/mcsYYYY/), keeps the files named
mcsYYYY-<commodity>.pdf (the individual chapters), and skips the complete volume (mcsYYYY.pdf), the appendixes,
the superseded copies (silver_old, ver.1.0 and the like) and the cover images. File names are kept as they are,
so every one still has its year and commodity in it.

It can be run again at any time: a file that is already a complete PDF is skipped, a download goes to a .part file
that is renamed only when the PDF is complete, and a failure on one file never touches the others.
It stops before downloading anything if the listings say more than 500 MB would come down.

Run it from work/p2-rag:    python3 scripts/download_mcs.py
"""

import http.client
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

YEARS = (2023, 2024, 2025)
LISTING = "https://pubs.usgs.gov/periodicals/mcs{year}/"
DEST = Path(__file__).resolve().parents[2] / "p2-raw"  # work/p2-raw, which is ../p2-raw from work/p2-rag
NOT_COMMODITIES = {"appendixes", "appendix", "intro", "introduction"}
MAX_BYTES = 500 * 1024 * 1024
TIMEOUT_S = 60
ATTEMPTS = 3
PAUSE_S = 0.3  # between files, to be polite to the server
HEADERS = {"User-Agent": "p2-rag-course-project (student downloader)"}
LINK = re.compile(r'<a href="mcs(\d{4})-([a-z0-9]+(?:-[a-z0-9]+)*)\.pdf">')  # a dot, underscore or "ver" in the name: not a chapter
SIZE = re.compile(r'align="right">\s*([\d.]+)([KMG]?)\s*</td>')
UNITS = {"": 1, "K": 1024, "M": 1024**2, "G": 1024**3}
ERRORS = (OSError, http.client.HTTPException, ValueError)  # URLError, HTTPError and timeouts are OSErrors


def parse_listing(html, year):
    """[(file name, size in bytes from the listing)] for the commodity chapters of one year's directory listing."""
    found = []
    for row in html.split("<tr>"):
        link = LINK.search(row)
        if not link or link.group(1) != str(year) or link.group(2) in NOT_COMMODITIES:
            continue
        size = SIZE.search(row.split("</a>", 1)[1])
        found.append((f"mcs{year}-{link.group(2)}.pdf", int(float(size.group(1)) * UNITS[size.group(2)]) if size else 0))
    return found


def is_valid_pdf(path):
    """True for a file that starts like a PDF and ends with its %%EOF marker (a cut-off download does not)."""
    try:
        if path.stat().st_size < 1024:
            return False
        with open(path, "rb") as f:
            head = f.read(5)
            f.seek(-1024, os.SEEK_END)
            return head == b"%PDF-" and b"%%EOF" in f.read()
    except OSError:
        return False


def fetch(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=TIMEOUT_S)


def download(url, dest):
    """Fetch url into dest by way of dest.part; raises on any problem and leaves no partial file behind."""
    part = dest.with_name(dest.name + ".part")
    try:
        with fetch(url) as response, open(part, "wb") as out:
            expected = response.headers.get("Content-Length")
            shutil.copyfileobj(response, out)
        if expected and part.stat().st_size != int(expected):
            raise ValueError(f"got {part.stat().st_size} bytes of {expected}")
        if not is_valid_pdf(part):
            raise ValueError("the file is not a complete PDF")
        os.replace(part, dest)
    finally:
        part.unlink(missing_ok=True)


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    failures = []  # (what, why)
    wanted = []  # (url, file name, size from the listing)
    for year in YEARS:
        url = LISTING.format(year=year)
        try:
            with fetch(url) as response:
                html = response.read().decode("utf-8", errors="replace")
        except ERRORS as err:
            failures.append((f"the {year} listing", str(err)))
            continue
        chapters = parse_listing(html, year)
        print(f"{year}: {len(chapters)} commodity chapters listed")
        wanted += [(url + name, name, size) for name, size in chapters]

    todo = [w for w in wanted if not is_valid_pdf(DEST / w[1])]
    expected = sum(size for _, _, size in todo)
    print(f"{len(wanted)} chapters listed, {len(wanted) - len(todo)} already downloaded, {len(todo)} to download (about {expected / 1024**2:.0f} MB)")
    if expected > MAX_BYTES:
        sys.exit(f"Stopping: that is more than {MAX_BYTES // 1024**2} MB. Nothing was downloaded.")

    new = 0
    for n, (url, name, size) in enumerate(todo, 1):
        print(f"[{n}/{len(todo)}] {name} ({size / 1024:.0f} KB)", flush=True)
        for attempt in range(1, ATTEMPTS + 1):
            try:
                download(url, DEST / name)
                new += 1
                break
            except ERRORS as err:
                gone_for_good = isinstance(err, urllib.error.HTTPError) and err.code < 500 and err.code != 429
                if attempt == ATTEMPTS or gone_for_good:
                    failures.append((name, str(err)))
                    print(f"  failed: {err}")
                    break
                time.sleep(2 * attempt)
        time.sleep(PAUSE_S)

    have = [DEST / name for _, name, _ in wanted if is_valid_pdf(DEST / name)]
    print(f"\nDownloaded now: {new}. Already there: {len(wanted) - len(todo)}. Failed: {len(failures)}.")
    for what, why in failures:
        print(f"  FAILED {what}: {why}")
    print(f"PDFs in {DEST}: {len(have)} of {len(wanted)} listed, {sum(p.stat().st_size for p in have) / 1024**2:.1f} MB")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
