distance = float(input("Сколько километров хотите проехать на автомобиле? "))
fuel_consumption = float(input("Сколько литров топлива расходует автомобиль на 100 километров? "))
fuel_in_tank = float(input("Сколько литров топлива в вашем баке? "))

required_fuel = fuel_consumption * (distance / 100)

if fuel_in_tank >= required_fuel:
    print("Вы сможете проехать запланированное расстояние.")
else:
    print("Вы не сможете проехать запланированное расстояние.")
