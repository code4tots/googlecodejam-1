h = {}
ch = 'a'
(2..6).each do |number|
  (1..3).each do |repeat|
    h[ch] = [number.to_s,repeat]
    ch.next!
  end
end

(1..4).each do |repeat|
  h[ch] = ['7',repeat]
  ch.next!
end

(1..3).each do |repeat|
  h[ch] = ['8',repeat]
  ch.next!
end

(1..4).each do |repeat|
  h[ch] = ['9',repeat]
  ch.next!
end

a = 'a'.ord
(1..gets.to_i).each do |i|
  ans = ''
  gets.chomp.each_char do |c|
    if c == ' '
      if ans.end_with? '0'
        # not sure if space is needed here...
        # But code jam's test case only passes with this here.
        # So I guess it is needed.
        # Though I felt problem could have been clearer about this.
        ans << ' '
      end
      ans << '0'
    else
      number, repeat = h[c]
      if ans.end_with? number
        ans << ' '
      end
      ans << (number * repeat)
    end
  end
  puts %Q{Case ##{i}: #{ans}}
end