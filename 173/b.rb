n = gets.to_i

results = {}

n.times {
    jedge = gets.delete("\n")

    if !results[jedge]
        results[jedge] = 1
    else
        results[jedge] += 1
    end
}

p "AC x " + (results["AC"].nil? ? "0" : results["AC"]).to_s
p "WA x " + (results["WA"].nil? ? "0" : results["WA"]).to_s
p "TLE x " + (results["TLE"].nil? ? "0" : results["TLE"]).to_s
p "RE x " + (results["RE"].nil? ? "0" : results["RE"]).to_s