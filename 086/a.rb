# A - Product
# https://atcoder.jp/contests/abc086/tasks/abc086_a

a, b = gets.strip.split.map(&:to_i) # <- おまじない?
puts (a*b).odd? ? 'Odd':'Even'