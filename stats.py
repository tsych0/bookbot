from collections import defaultdict
from typing import Any

def count_words(text: str) -> int:
    return len(text.split())

def frequency(text: str) -> dict[str, int]:
    res = defaultdict(lambda: 0)
    for c in text.lower():
        res[c] += 1
    return dict(res)

def get_sorted_frequency(freq: dict[str, int]) -> list[dict[str, Any]]:
    res = []
    for k, v in freq.items():
        res.append({'char': k, 'count': v})

    res.sort(key=lambda x: x['count'], reverse=True)
    return res
