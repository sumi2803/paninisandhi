from .data import VOWELS, YAN, MATRA, VRIDDHI


def yan_sandhi(word1: str, word2: str) -> str:
    """इको यणचि — apply यण् sandhi if word1 ends in इक् and word2 starts with a vowel."""
    last, first = word1[-1], word2[0]
    if last in YAN and first in VOWELS:
        return word1[:-1] + "्" + YAN[last] + MATRA.get(first, "") + word2[1:]
    return word1 + word2


def is_vriddhi(sound: str) -> bool:
    """1.1.1 वृद्धिरादैच् — is this sound आ, ऐ, or औ?"""
    return sound in VRIDDHI
