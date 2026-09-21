# Shared Devanagari data used across sandhi rules.

VOWELS = "अआइईउऊऋॠऌएऐओऔ"

# इको यणचि : इक् (इ/ई, उ/ऊ, ऋ/ॠ, ऌ) -> यण् (य्/व्/र्/ल्)
# covers both the independent vowel and its matra form
YAN = {
    'इ': 'य', 'ई': 'य', 'ि': 'य', 'ी': 'य',
    'उ': 'व', 'ऊ': 'व', 'ु': 'व', 'ू': 'व',
    'ऋ': 'र', 'ॠ': 'र', 'ृ': 'र', 'ॄ': 'र',
    'ऌ': 'ल', 'ॢ': 'ल',
}

# independent vowel -> its dependent matra sign (अ has none)
MATRA = {
    'आ': 'ा', 'इ': 'ि', 'ई': 'ी', 'उ': 'ु', 'ऊ': 'ू',
    'ऋ': 'ृ', 'ॠ': 'ॄ', 'ऌ': 'ॢ', 'ए': 'े', 'ऐ': 'ै',
    'ओ': 'ो', 'औ': 'ौ',
}

# वृद्धि : आ, ऐ, औ (used by the 1.1.1 algorithm)
VRIDDHI = {'आ', 'ऐ', 'औ'}
