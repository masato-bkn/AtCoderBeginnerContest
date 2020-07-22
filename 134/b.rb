# B - Golden Apple
# https://atcoder.jp/contests/abc134/tasks/abc134_b

def calculate_number_of_worker(tree, range)   
    tmp = tree % ((range * 2) + 1)

    if tmp == 0
        tree / ((range * 2) + 1)
    else
        tree / ((range * 2) + 1) + 1
    end
end

n,d= gets.chomp.split(" ").map(&:to_i)

p calculate_number_of_worker(n,d)