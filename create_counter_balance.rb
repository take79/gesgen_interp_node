orders = [0, 1, 2].permutation().to_a
ans_orders = []
for num in 0..9 do
  ans_orders.push(orders.shuffle)
end

out = File.open("counter_balances.txt", "w")

ans_orders.each do |for_id|
  for_id.each do |order|
    out.print(order[0].to_s + " " + order[1].to_s + " " + order[2].to_s + ",")
  end
  out.print("\n")
end
