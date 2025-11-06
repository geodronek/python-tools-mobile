def basic_calc():
    car_name = input("Wpisz markę samochodu: ")
    car_fuel_consumption = float(input('Wpisz średnie spalanie (l/100km): '))
    car_fuel_price = float(input("Wpisz cene paliwa (pln/l): "))
    trail_km = float(input("Wpisz ile trasa ma kilometrów: "))

#outputs:
    final_fuel_consumption = (car_fuel_consumption * trail_km) / 100 
    final_fuel_price = final_fuel_consumption * car_fuel_price

    print(f'\n{car_name.title()} podczas {trail_km} km trasy,\nspali {final_fuel_consumption:.2f} litrów paliwa,\nza {final_fuel_price:.2f} pln')

basic_calc() # 06//11/2025
