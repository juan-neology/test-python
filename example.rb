puts "salida"
my_variable = 5

if my_variable > 0
  puts my_variable

end
#arrays
games_played = [["uno", true], ["dos", false]]
puts games_played
puts games_played[0][0]
#hashes

cocktail = {"martini" => {
                        "vodka" => true,
                        "gin" => false,
                          }
          }

puts "------"
puts cocktail["martini"]["vodka"]

#Array sorting
my_array = [1, 2, 3]
puts my_array
puts my_array.map

odd_or_even = my_array.map do |element|
  element % 2 == 0 ? "even" : "odd"
end
puts "11111111111"
puts odd_or_even
