# Measurement Discipline

Content frameworks fail quietly when the measuring instrument is wrong. This file records the
specific traps found while auditing a real library and a real draft, plus the method that avoided
them.

---

## 1. Measure the target library before setting a target

An assumed length target is a liability. Measure the corpus first: word count, H2/H3 counts,
paragraph count and average, link counts (product vs blog vs collection), FAQ presence, table
presence, meta length.

Illustrative measurement of one live library (21 most recent posts):

| Dimension | Observed range | Mean |
|---|---|---|
| Words | 2,578 – 4,762 | **3,576** |
| H2 sections | 13 – 26 | 18.5 |
| Paragraphs | 39 – 89 | 64.7 |
| Avg paragraph | 35 – 72 words | 45.8 |
| FAQ present | 20 of 21 | mandatory in practice |
| Bulleted lists | 21 of 21 | mandatory in practice |
| Links to product pages | 0 – 16 | 6.5 |

A framework default of 1,800–2,200 words against a library whose mean is 3,576 produces a draft
that is structurally **nothing like** the house output, no matter how good the prose is. The
number must come from the corpus.

## 2. The audit is only as good as its parser

Three bugs found in a purpose-built auditor, each of which produced a **confident, plausible,
wrong** number:

| Bug | Symptom | Root cause |
|---|---|---|
| Headings counted as paragraphs | paragraph count inflated ~65% | the markdown→HTML step erased the `#` markers, so headings were indistinguishable from prose by the time counting happened |
| A wrapped bullet split into a fragment | avg paragraph reported far too low | blank-line block splitting: a continuation line of a bullet became its own "paragraph" |
| Auxiliary records counted as data points | a term appeared as both "has data" and "zero data" | records of a different `kind` were branched on by position, not by type |

**Method that avoids all three:** parse the raw markdown with a small state machine rather than
converting to HTML first.

- a list item **swallows its continuation lines** until a blank line
- headings, table rows, block quotes and code fences are **excluded** from paragraph stats
- when a script emits records of mixed types, **tag them** and branch on the tag

## 3. Readability must be computed on paragraph text only

Same draft, measured two ways:

| Basis | Flesch-Kincaid | Words per sentence |
|---|---|---|
| whole document (tables, lists, headings included) | 8.6 | 19.7 |
| **paragraph text only** | **7.8** | **16.9** |

The first reading says "fails"; the second is the truth. Tables, checklist items and headings are
not sentences. A rendered-HTML grader is reading `<p>` elements — so a markdown-based approximation
must exclude everything a browser would not render as a paragraph.

## 4. Count character limits in code, never by eye

Title and meta limits are exact. Build a small candidate set and search it for the exact length:

```python
for c in candidates:
    print(len(c), c)
```

Do not trim by eye and do not accept "about 65". The measured run hit 65 and 155 exactly by
searching candidates for the length, then editing the winning candidate by a word at a time and
re-counting.

## 5. The general rule

When a measurement about your own output is surprising — too good, too bad, or inconsistent with
what you can see in the text — **check the instrument before you act on the number.** In one
session three separate "failures" of the content were failures of the counter, and one of them had
already caused a near-miss where a wrong readability figure was about to be reported as fact.
