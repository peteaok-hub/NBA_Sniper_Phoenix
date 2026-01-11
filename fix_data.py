import pandas as pd
import numpy as np
import random
import os

# --- PATH SETUP ---
current_dir = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(current_dir, 'processed_nfl_data.csv')

def format_institutional_spread(raw_spread):
    """Ensures Spread follows (-) for Favorites and (+) for Underdogs."""
    try:
        val = float(raw_spread)
        if val < 0: return f"{val}" # Favorite (-)
        elif val > 0: return f"+{val}" # Underdog (+)
        return "PK"
    except (ValueError, TypeError): return raw_spread

def calculate_market_bias(ticket_pct, money_pct):
    gap = money_pct - ticket_pct
    if gap >= 15: return "🔥 SHARP WHALE ACTION"
    if gap <= -15: return "🤡 PUBLIC TRAP"
    return "⚖️ MARKET NEUTRAL"

def calculate_market_bias_enc(bias_str):
    """Encodes Market Bias into a numerical value."""
    if "SHARP" in bias_str: return 1
    if "TRAP" in bias_str: return -1
    return 0

def generate_factor_logic(win_prob, bias):
    if "SHARP" in bias: return "Significant Sharp discrepancy detected."
    if win_prob > 0.65: return "Monte Carlo sims identify high-value edge."
    return "Neutral market sentiment."

def process_data():
    """Generates and cleans simulation data."""
    teams = ['Steelers', 'Ravens', 'Saints', 'Bills', 'Chiefs', 'Eagles', 'Lions', 'Heat', 'Pistons']
    data = []
    for _ in range(50):
        home = random.choice(teams)
        away = random.choice([t for t in teams if t != home])
        spread = random.choice([-7.5, -3.5, 3.5, 7.5])
        ticket_pct = random.randint(30, 70)
        money_pct = ticket_pct + random.randint(-20, 20)

        bias = calculate_market_bias(ticket_pct, money_pct)

        data.append({
            'Team': home, 'Away_Team': away, 'Spread': spread,
            'Market_Bias': bias,
            'Market_Bias_Enc': calculate_market_bias_enc(bias),
            'Home_Score': random.randint(10, 40), 'Home_Turnovers': random.randint(0, 3),
            'Home_Yards': random.randint(250, 450)
        })

    df = pd.DataFrame(data)
    # Applying institutional symbol logic
    df['Spread'] = df['Spread'].apply(format_institutional_spread)

    df.to_csv(OUTPUT_FILE, index=False)
    print("✅ PHOENIX SUCCESS: Symbols fixed and AI synced.")

if __name__ == "__main__":
    process_data()