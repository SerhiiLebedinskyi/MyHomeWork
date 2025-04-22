user_numeric = int(input("Введіть 5-ти значне число:"))
div, mod = user_numeric // 10, user_numeric % 10
div1, mod1 = div // 10, div % 10
div2, mod2 = div1 // 10, div1 % 10
div3, mod3 = div2 // 10, div2 % 10
mod4 = div3 % 10
turn_numeric = mod * 10000 + mod1 * 1000 + mod2 * 100 + mod3 * 10 + mod4
print(turn_numeric)
