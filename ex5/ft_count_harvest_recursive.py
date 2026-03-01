def ft_count_harvest(count, days):
    c = days - count
    if count == 0:
        print("Harvest time!")
        return
    else:
        print(f"Day {c + 1}")
    ft_count_harvest(count - 1, days)


def ft_count_harvest_recursive():
    count = int(input("Days until harvest: "))
    ft_count_harvest(count, days=count)
