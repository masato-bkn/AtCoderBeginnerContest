# B - Echo
# https://atcoder.jp/contests/abc145/submissions/15219198

n = gets.delete("\n").to_i
s = gets.delete("\n")

if n.even? 
    p "No" 
    exit
end

p if s[0..(n/2)-1] == s[(n/2)..-1] ? "Yes" : "No"
