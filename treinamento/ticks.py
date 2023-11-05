# dia (minecraft) inicia 0 e termina 12000 ticks
# cada dia (com luz) (minecraft) tem 10min, resto tem 10min
# ele joga 3 horas por dia (real)

real_days, houses = int(input()), int(input())

# 1h (real) => 30min de dia (mine)
# 30min de dia (mine) = 36000 ticks
# 3h (real) = 108000 ticks
ticks_per_day = 108000

ticks_per_house = (real_days * ticks_per_day) / houses

print(int(ticks_per_house))