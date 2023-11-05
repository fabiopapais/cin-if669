a_diamonds, l_diamonds, p_diamonds = int(input()), int(input()), int(input())
hours = int(input())

def max(a, b):
    return (a + b + abs(a - b)) / 2

a_diamonds *= hours
l_diamonds *= hours
p_diamonds *= hours

print(int(max(max(a_diamonds, l_diamonds), max(a_diamonds, p_diamonds))))