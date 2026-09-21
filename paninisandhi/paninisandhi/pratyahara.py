# 14 माहेश्वरसूत्राणि — each sutra stored as a list of (akshara, is_it) pairs.

SUTRAS = [
    [('अ', False), ('इ', False), ('उ', False), ('ण्', True)],
    [('ऋ', False), ('ऌ', False), ('क्', True)],
    [('ए', False), ('ओ', False), ('ङ्', True)],
    [('ऐ', False), ('औ', False), ('च्', True)],
    [('ह', False), ('य', False), ('व', False), ('र', False), ('ट्', True)],
    [('ल', False), ('ण्', True)],
    [('ञ', False), ('म', False), ('ङ', False), ('ण', False), ('न', False), ('म्', True)],
    [('झ', False), ('भ', False), ('ञ्', True)],
    [('घ', False), ('ढ', False), ('ध', False), ('ष्', True)],
    [('ज', False), ('ब', False), ('ग', False), ('ड', False), ('द', False), ('श्', True)],
    [('ख', False), ('फ', False), ('छ', False), ('ठ', False), ('थ', False),
     ('च', False), ('ट', False), ('त', False), ('व्', True)],
    [('क', False), ('प', False), ('य्', True)],
    [('श', False), ('ष', False), ('स', False), ('र्', True)],
    [('ह', False), ('ल्', True)],
]


def _flatten():
    flat = []
    for si, sutra in enumerate(SUTRAS, start=1):
        for letter, is_it in sutra:
            flat.append({'letter': letter, 'is_it': is_it, 'sutra': si})
    return flat


def count_pratyaharas():
    """Returns (method1_total, method2_total) — both should equal 305."""
    flat = _flatten()
    it_positions = [i for i, item in enumerate(flat) if item['is_it']]
    non_it_positions = [i for i, item in enumerate(flat) if not item['is_it']]

    method1 = sum(
        sum(1 for p in it_positions if p > i)
        for i, item in enumerate(flat) if not item['is_it']
    )
    method2 = sum(
        sum(1 for np in non_it_positions if np < p)
        for p in it_positions
    )
    return method1, method2


def generate_pratyaharas():
    """Returns the list of all valid forward-propagating प्रत्याहार names."""
    flat = _flatten()
    it_positions = [i for i, item in enumerate(flat) if item['is_it']]

    pratyaharas = []
    for idx, item in enumerate(flat):
        if not item['is_it']:
            for p in it_positions:
                if p > idx:
                    pratyaharas.append(item['letter'] + flat[p]['letter'])
    return pratyaharas
