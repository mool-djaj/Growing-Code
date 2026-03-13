def ft_count_harvest_recursive():
    count = int(input("Days until harvest: "))

    def helper(day, total_days):
        if day > total_days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        helper(day + 1, total_days)
    helper(1, count)
