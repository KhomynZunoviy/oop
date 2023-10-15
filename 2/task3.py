x = object()
y = object()

x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print("x_list складається з %d обє'ктів" % len(x_list))
print("y_list складається з %d обє'ктів" % len(y_list))
print("big_list складається з %d обє'ктів" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Майже там...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Чудово!")