# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/fhrianata-muse/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/fhrianata-muse/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

"The World in One Page" — one newspaper front page that sums up the world news of Saturday 21 November 2026 in a single 1024x1024 image: Russian missiles land in Poland, the World Court's Myanmar genocide ruling, the first Trump-Xi-Putin summit, the Wall Street correction, the UK-EU deals, the Iran war and a tanker ablaze near Hormuz, Houthi missiles on Riyadh, a pancreatic-cancer pill breakthrough, the Palisades Fire verdict, COP31's final stage, Cyclone Akvan and the Las Vegas Grand Prix. The date is named in a red banner at the top, and every story carries a place label and a one-line summary so the day can be read from the picture alone.

`entry.png` is the picture. `draw.py` is the Pillow script that drew it (run during the build; the grader never runs it). `main.ts` is the entry program: it copies `entry.png` to the output directory, byte for byte, every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

That writes `out/entry.png`, a whole PNG of 1024 by 1024 pixels, under 1 MiB.

---

<sub>Entered on [make.fun](https://make.fun/?ref=q4engdna&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
