# PHOENIX AI: Terminal Rules
Primary Goal: Maintain 10%+ ROI through institutional data integrity.

Spread Logic: Always verify that Spread in processed_nfl_data.csv uses (-) for Favorites and (+) for Underdogs.

Simulation Check: If a task fails, check if the laptop was awake and if fix_brain.py was run after the last data change.

PR Instructions: Always run py -3.11 fix_data.py before proposing a change to auto_pilot.py.