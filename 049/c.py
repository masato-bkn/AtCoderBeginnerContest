# C - 白昼夢 / Daydream
# https://atcoder.jp/contests/abc049/tasks/arc065_a

import re

print("YES" if re.match("^(dream|dreamer|erase|eraser)+$",input()) else "NO")

# ^  行の先頭にあるもの文字のみ検索
# () グループ検索
# +  直前の文字の繰り返し
# $  最後にある文字のみ検索