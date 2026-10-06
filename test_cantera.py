import cantera as ct


def run_smoke_test():
    gas = ct.Solution("gri30.yaml")

    fuel = "CH4"
    pressure_bar = 10.0
    phi = 1.0
    temperature_start = 600.0
    temperature_end = 1800.0
    step = 100.0

    pressure_pa = pressure_bar * 1e5
    temperatures = []
    current = temperature_start
    while current <= temperature_end + 1e-9:
        temperatures.append(current)
        current += step

    print(f"Running Cantera smoke test for {fuel} at {pressure_bar} bar, phi={phi}")
    print("Temp[K]   H2O       CO2       CO        H2        O2")

    for temp in temperatures:
        gas.TP = (temp, pressure_pa)
        gas.set_equivalence_ratio(phi, fuel, "O2:1.0, N2:3.76")
        gas.equilibrate("HP")

        h2o = gas.mole_fraction_dict()["H2O"]
        co2 = gas.mole_fraction_dict()["CO2"]
        co = gas.mole_fraction_dict()["CO"]
        h2 = gas.mole_fraction_dict()["H2"]
        o2 = gas.mole_fraction_dict()["O2"]

        print(f"{temp:7.1f}   {h2o:7.4f}   {co2:7.4f}   {co:7.4f}   {h2:7.4f}   {o2:7.4f}")

    print("\nSmoke test completed successfully.")


if __name__ == "__main__":
    run_smoke_test()
