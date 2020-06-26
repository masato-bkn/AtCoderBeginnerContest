# B - Coins
# https://atcoder.jp/contests/abc087/tasks/abc087_b

x = gets.strip.to_i
y = gets.strip.to_i
z = gets.strip.to_i
t = gets.strip.to_i

# a, b, c, x = 4.times.map { gets.to_i } <= スマートなやり方

cnt = 0

(0..x).each do |i|
    (0..y).each do |j|
        (0..z).each do |k|
            if (i*500 + j*100 + k*50) == t
                cnt = cnt +1
            end
        end
    end
end

p cnt