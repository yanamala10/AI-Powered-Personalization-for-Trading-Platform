import pandas as pd

# Read the CSV file
data = pd.read_csv('trading_data.csv')

# Define thresholds for suspicious behavior
trade_threshold = 5000  # Trades above $5000 are suspicious
login_threshold = 3     # More than 3 login attempts are suspicious

# Flag suspicious trades and logins
suspicious_trades = data[data['TradeAmount'] > trade_threshold]
suspicious_logins = data[data['LoginAttempts'] > login_threshold]

# Print results
print("Suspicious Trades (Amount > $5000):")
print(suspicious_trades)
print("\nSuspicious Logins (Attempts > 3):")
print(suspicious_logins)
