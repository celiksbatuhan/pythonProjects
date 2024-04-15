interval_start = int(input("Introduceti startul intervalului:"))
interval_end = int(input("Introduceti sfarsitul intervalului:"))

numar = float(input("Introduceti un numar:"))

if interval_start <= numar <= interval_end:
    print(f"numarul {numar}, apartine intervalului {[interval_start,interval_end]}")
else:
    print(f"numarul {numar}, nu apartine intervalului {[interval_start,interval_end]}")