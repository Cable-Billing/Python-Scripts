from random import choice

attempts = 1000
money_choices = [50, 100, 150, 200, 500, 1000]
swap_total = 0
no_swap_total = 0

for i in range(attempts):
    multipliers = [2, 0.5]
    envelop_one = choice(money_choices)
    envelop_two = int(envelop_one * choice(multipliers))

    envelop_selected = choice([1, 2])
    if envelop_selected == 1:
        swap_total += envelop_two
        no_swap_total += envelop_one
    else:
        swap_total += envelop_one
        no_swap_total += envelop_two

print()
print("Swap total after", attempts, "attempts:", swap_total)
print("No swap total after", attempts, "attempts:", no_swap_total)

increase = ((swap_total - no_swap_total) / no_swap_total) * 100
print("Swap increase:", "%.2f" % round(increase, 2))
