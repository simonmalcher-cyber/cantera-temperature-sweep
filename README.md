# cantera-temperature-sweep

A small web dashboard for running a temperature sweep with Cantera. The form lets the user select a fuel, pressure, equivalence ratio, and temperature range. The backend runs the calculations in Cantera and displays the equilibrium results in a table.

## Features
- Fuel selection (CH4, H2, C2H6, C3H8, C8H18, CO, NH3)
- Pressure input in bar
- Equivalence ratio input
- Temperature sweep from min to max in configurable steps
- Cantera equilibrium calculations using GRI-Mech 3.0
- Result table with selected major species

## Local setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the app:
   ```bash
   python app.py
   ```

4. Open the app in your browser:
   ```text
   http://127.0.0.1:5000
   ```

## Notes
- The app uses the Cantera `gri30.yaml` mechanism by default.
- Pressure is entered in bar and converted internally to Pa.
- The experiments are equilibrium calculations at each temperature in the requested sweep.

## Example use case
- Fuel: CH4
- Pressure: 10 bar
- Equivalence ratio: 1.0
- Temperature range: 500 K to 2000 K
- Step: 50 K

This produces a temperature sweep for the selected reacting mixture.
