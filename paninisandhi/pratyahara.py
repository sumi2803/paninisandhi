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


def _print_table(headers, rows, col_widths):
    def fmt_row(cells):
        return " | ".join(str(c).ljust(w) for c, w in zip(cells, col_widths))
    print(fmt_row(headers))
    print("-+-".join("-" * w for w in col_widths))
    for row in rows:
        print(fmt_row(row))


def print_sutras():
    """Prints all 14 sutras with their इत् letter clearly shown."""
    print("14 माहेश्वरसूत्राणि (अक्षर-सूची सहित इत्संज्ञकवर्ण)")
    rows = []
    for i, sutra in enumerate(SUTRAS, start=1):
        letters = " ".join(ak for ak, _ in sutra)
        it_letter = [ak for ak, is_it in sutra if is_it][0]
        rows.append([i, letters, it_letter])
    _print_table(["सूत्र", "अक्षर-सूची", "इत्"], rows, [6, 40, 6])


def print_method1():
    """Method 1: per अक्षर, how many इत् letters occur after it."""
    flat = _flatten()
    it_positions = [i for i, item in enumerate(flat) if item['is_it']]
    print("\nMETHOD 1 : प्रत्येक अक्षरात् -> तत्पश्चात् आगच्छन्तः इत्-वर्णाः")
    rows = []
    for idx, item in enumerate(flat):
        if not item['is_it']:
            count_after = sum(1 for p in it_positions if p > idx)
            if count_after > 0:
                rows.append([item['letter'], item['sutra'], count_after])
    _print_table(["अक्षर", "सूत्र", "प्रत्याहार-संख्या"], rows, [8, 8, 18])


def print_method2():
    """Method 2: per इत् letter, how many अक्षर occur before it."""
    flat = _flatten()
    it_positions = [i for i, item in enumerate(flat) if item['is_it']]
    non_it_positions = [i for i, item in enumerate(flat) if not item['is_it']]
    print("\nMETHOD 2 : प्रत्येक इत्संज्ञकवर्णात् -> पूर्ववर्ती अक्षर-संख्या")
    rows = []
    for p in it_positions:
        count_before = sum(1 for np in non_it_positions if np < p)
        rows.append([flat[p]['letter'], flat[p]['sutra'], count_before])
    _print_table(["इत् वर्ण", "सूत्र", "प्रत्याहार-संख्या"], rows, [10, 8, 18])


def print_report():
    """Prints everything: sutras, both methods, totals, and the full generated list."""
    print_sutras()
    print_method1()
    print_method2()
    m1, m2 = count_pratyaharas()
    print(f"\nMETHOD 1 TOTAL = {m1}")
    print(f"METHOD 2 TOTAL = {m2}")
    plist = generate_pratyaharas()
    print(f"\nकुल जनितप्रत्याहाराः = {len(plist)}")
    for i in range(0, len(plist), 10):
        print(plist[i:i + 10])
