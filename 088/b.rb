# B - Card Game for Two
# https://abc088.contest.atcoder.jp/tasks/abc088_b

n = gets.strip.to_i
nums = gets.strip.split.map(&:to_i).sort.reverse

a = 0
b = 0

until nums.empty? do
    a += nums.shift
    break if nums.empty?
    b += nums.shift
end

p a - b