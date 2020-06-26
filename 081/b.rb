# B - Shift only
# https://atcoder.jp/contests/abc081/tasks/abc081_b
num_cnt = gets.to_i
nums = gets.strip.split.map(&:to_i)

cnt = 0
while nums.all?(&:even?) do
  cnt = cnt.succ
  nums = nums.map{ |a| a/2 }
end

puts cnt
