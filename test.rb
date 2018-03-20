File.open("counter_balances.txt", "r") do |file|
  ans_orders = []
  file.each_line do |for_id|
    orders = for_id.split(',')
    orders.pop()
    row = []
    orders.each do |order|
      el = order.split(' ')
      ord = []
      el.each do |num|
        n = num.to_i
        ord.push(n)
      end
      row.push(ord)
    end
    ans_orders.push(row)
  end
end

