# The World in One Image — 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)

An entry for the make.fun bounty **"Sum up 23 November's world news in one
image"**.

`main.py` (Python 3.13, standard library only) writes the bundled artwork
`world-news-2026-11-23.png` to `/output/entry.png`. The output is a
byte-for-byte copy of the stored image, so every run produces identical
bytes. No network access is used.

The image is a one-page newspaper front page of Monday 23 November 2026:

- **War at sea** — Ukraine's sea drones sink Russian warships near Libya; a
  Russian cargo ship with military ties is hit in the Baltic.
- **Climate** — COP31 talks collapse with no deal over fossil-fuel language.
- **Tech & markets** — Nvidia's board reinstates Jensen Huang as CEO; shares
  jump about 30%.
- **Crypto** — Bitcoin rebounds to $61K after a plunge to a two-year low.
- **Middle East** — Iran warns the US over the Hormuz naval blockade.
- **Indonesia** — search continues for 34 missing after a candy factory fire.
- **Sport** — FIFA confirms the UK as host of the 2035 Women's World Cup.

The artwork was drawn programmatically (Python + Pillow) from the day's wire
reports (BBC, Al Jazeera, CoinDesk and UK broadcast coverage).

## Run

```bash
python3 main.py   # writes /output/entry.png (1024x1024 PNG, < 1 MiB)
```

## License

MIT — see `LICENSE`.
