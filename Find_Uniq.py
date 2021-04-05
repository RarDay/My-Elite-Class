from fuzzywuzzy import fuzz
import Levenshtein
import statistics as st

s1 = "ABCD ABCD"
s2 = "DCBA ABCD"


def search_partial_text(src, dst):
    dst_buf = dst
    result = 0
    for char in src:
        if char in dst_buf:
            dst_buf = dst_buf.replace(char, '', 1)
            result += 1
    r1 = int(result / len(src) * 100)
    r2 = int(result / len(dst) * 100)
    return '{}%'.format(r1 if r1 < r2 else r2)


print(search_partial_text(s1, s2))
print(fuzz.ratio(s1, s2))
print(Levenshtein.jaro_winkler(s1, s2))
