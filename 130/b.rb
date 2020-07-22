# B - Bounding
# https://atcoder.jp/contests/abc130/tasks/abc130_b

N,X = gets.chomp.split().map(&:to_i)
L = gets.chomp.split().map(&:to_i)

d = 0
cnt = 1

L.each do |l|
    d = d + l
    if d <= l
        cnt + 1    
    end
end

p cnt
