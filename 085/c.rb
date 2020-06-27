# C - Otoshidama
# https://atcoder.jp/contests/abc085/tasks/abc085_c

n,m = gets.strip.split.map(&:to_i)

(0..n).each do |i|
    (0..n-i).each do |j|
        k = n - (i + j)
        if i*10000 + j*5000 + k*1000 == m
            p "#{i} #{j} #{k}"
            exit
        end
    end
end

p "-1 -1 -1"


