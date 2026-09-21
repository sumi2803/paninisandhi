# paninisandhi

A small Python toolkit that represents Paninian sutras as code — starting with
sandhi rules and सञ्ज्ञा (naming) checks, built for a PG Diploma in
Computational Linguistics project on Sanskrit and Prakrit.

## What's included

- **`yan_sandhi(word1, word2)`** — implements **इको यणचि** (Aṣṭādhyāyī 6.1.77):
  replaces a final इक् vowel (इ/ई, उ/ऊ, ऋ/ॠ, ऌ) with its यण् semivowel
  (य्/व्/र्/ल्) when the next word starts with a dissimilar vowel.
- **`is_vriddhi(sound)`** — implements **वृद्धिरादैच्** (Aṣṭādhyāyī 1.1.1):
  checks whether a given sound is आ, ऐ, or औ.
- Shared Devanagari data (vowels, matras, यण् mapping) in `data.py`, reused
  across rules so each new sutra doesn't need its own copy.

More sutras will be added here as the project grows (e.g. तिङन्त generation).

## Installation

Clone or download this repository, then from inside the folder:

```bash
pip install -e .
```

The `-e` (editable) flag means you can keep editing the source files and the
installed package stays up to date — no reinstalling needed.

## Usage

```python
from paninisandhi import yan_sandhi, is_vriddhi

print(yan_sandhi("मातृ", "आज्ञा"))   # मात्राज्ञा
print(yan_sandhi("दधि", "अत्र"))     # दध्यत्र
print(is_vriddhi("ऐ"))               # True
print(is_vriddhi("इ"))               # False
```

## Project structure

```
paninisandhi/
├── pyproject.toml
└── paninisandhi/
    ├── __init__.py   # exposes yan_sandhi(), is_vriddhi()
    ├── data.py        # VOWELS, YAN, MATRA, VRIDDHI lookup tables
    └── rules.py        # the actual sutra logic
```

## Background

This project treats Paninian grammar rules as literal algorithms — each
sutra reduces to input → sequence of checks → output, in the same way any
step-by-step procedure does. Built as part of ongoing coursework; contributions
and corrections welcome.

## License

MIT
