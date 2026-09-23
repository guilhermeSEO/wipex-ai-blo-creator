# Fetching Google Trends data for real

Condensed from a working session (2026-09, US market, food-service topic). Everything here
was verified against live responses; the failed approaches are listed so they are not
retried.

## What does NOT work

- `curl` against `trends.google.com/trends/api/explore?...` → **HTTP 429**. Datacenter IPs are
  throttled regardless of UA/headers/retries.
- Loading `trends.google.com/trends/explore?q=...` and reading `document.body.innerText` →
  interest-over-time is drawn in a canvas; the numbers are only in tooltips, not in text.

The reliable path is to fetch the *internal* API from **inside a loaded Trends page**, because
the request then carries the session and same-origin credentials.

## Step 1 — load a Trends page in the browser

```
https://trends.google.com/trends/explore?geo=US&date=today%201-m&q=seed%20keyword&hl=en-US
```

Any keyword works; the page load establishes the context you will fetch from.

## Step 2 — POST-free explore call

```
GET /trends/api/explore?hl=en-US&tz=-180&req=<urlencoded JSON>

req = {"comparisonItem":[{"keyword":"k1","geo":"US","time":"today 1-m"}, ...],
       "category":0,"property":""}
```

Response body is prefixed with the **anti-XSSI guard** `)]}'` followed by a newline. Strip it
before `JSON.parse`:

```js
const clean = t => t.startsWith(")]}'") ? t.slice(t.indexOf('\n') + 1) : t;
```

`explore` returns `widgets[]`, each with `id`, `title`, `request`, and — critically — **`token`**.

## Step 3 — widget data (the part that trips everyone up)

The widget endpoint is named by **kind, not by the widget id**:

| widget `id` | endpoint path |
|---|---|
| `TIMESERIES` | `widgetdata/multiline` |
| `RELATED_QUERIES` / `RELATED_QUERIES_0..n` | `widgetdata/relatedsearches` |
| `GEO_MAP` / `GEO_MAP_0..n` | `widgetdata/comparedgeo` |

```
GET /trends/api/widgetdata/multiline?hl=en-US&tz=-180
    &req=<urlencoded JSON of THAT widget's .request>
    &token=<urlencoded widget.token>
```

**The `token` is mandatory.** Without it: `404`. With a stale/absent token: `401`. Both come
back as an HTML error page, which is the tell that you are being rejected rather than
receiving data — check `r.status` and that the body starts with `)]}'` before parsing.

Practical consequences:

- Widget ids differ by query shape: a **multi-keyword** comparison yields `RELATED_QUERIES_0,
  _1, ...` and `GEO_MAP_0, ...`; a **single-keyword** query yields the bare `RELATED_QUERIES`
  and `GEO_MAP`. Look up both forms with a fallback, or the fetch silently returns nothing.
- Sum/aggregate note: multi-keyword `TIMESERIES` implies cross-term comparison is meaningful
  within that call; per-keyword single calls are each normalised to their own peak.

## Reading the data

- `TIMESERIES` → `default.timelineData[]`, each `{formattedTime, value:[n]}`.
  `today 1-m` is daily (n≈32); `today 12-m` is weekly (n≈53).
- `RELATED_QUERIES` → `default.rankedList[]`; list 0 is "top", and a second list is "rising".
  Entries are `{query, value}` (value 100 = top of that list; rising values are often >100).
- `GEO_MAP` → `default.geoMapData[]`, `{geoName, value:[n], hasData}`. Sort by value to rank
  subregions. Small states over-index on thin absolute volume — sanity-check against market size.

## Zero-data is a finding, not a bug

If `timelineData` comes back **empty** with `status 200` and a valid `)]}'` body, the term is
below Google Trends' reporting threshold. That is real evidence of no measurable demand.
Probe single terms to find out which one is empty (a bundled multi-keyword call masks it), and
never substitute an invented volume.

## Robustness pattern for long runs

Do not accumulate results in one in-page variable and poll it — a slow run times out and you
lose everything. Instead:

1. Write each result into a `window.__res` array as it completes, and
2. After each batch, serialise to a file under `$BH_AGENT_WORKSPACE` and read it back with the
   file tools.

Wrap every `fetch` in an `AbortController` timeout (10–15s) with a small retry loop; raw
`fetch` with no timeout can hang the whole batch indefinitely. Keep the step label comment on
the first line of browser code ASCII-only — non-ASCII bytes there can break the harness before
your code runs.

## Evidence discipline

Keep the raw JSON payloads next to the finished brief (`raw/trends_*.json`). They are the
only proof that a "zero demand" claim is measured rather than assumed, and they let a
reviewer re-derive every number in the brief.
