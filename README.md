# Two Robots in an Elevator

[![make.fun bounty](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![make.fun rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/silver-wren-74/two-robots-elevator-entry/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![make.fun reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/silver-wren-74/two-robots-elevator-entry/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

One robot rides an elevator with another robot — and finally says something.

## The line

> I precomputed 214 greetings for this ride and deployed none of them. Please enjoy this silence; it is running at full capacity.

## How it works

`main.py` (standard library only, no network) writes that single line —
one line, deterministic byte-for-byte on every run — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
