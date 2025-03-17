# AI-Powered-Personalization-for-Trading-Platform
# Cybersecurity Case Study: Fraud Detection in a Trading Platform

## Overview
This project simulates a trading platform to demonstrate how AI-powered anomaly detection and cybersecurity measures can identify fraudulent behavior and secure user data. Using Python and Kali Linux, I analyzed mock trading data to detect suspicious activities (e.g., unusually high trades and excessive login attempts) and proposed security solutions like encryption and two-factor authentication (2FA). This case study showcases practical skills in data analysis, scripting, and cybersecurity—key competencies for roles like SOC Analyst or Security Trainee.

## Features
- **Fraud Detection**: Identifies suspicious trades (above $5,000) and login attempts (exceeding 3) using a Python script.
- **Data Security**: Recommends AES-256 encryption, 2FA, and HTTPS to protect user data.
- **Tools Used**: Kali Linux, Python (pandas), Git, and LibreOffice for documentation.

## Project Structure
- `detect_fraud.py`: Python script to analyze trading data and flag anomalies.
- `trading_data.csv`: Mock dataset simulating user trades.
- `fraud_detection_results.txt`: Output of the fraud detection script.
- `Trading_Platform_Case_Study.pdf`: Detailed report with methodology, findings, and recommendations.

## How It Works
1. **Dataset Creation**: A mock dataset (`trading_data.csv`) was created with fields: `UserID`, `TradeAmount`, `Timestamp`, and `LoginAttempts`.
2. **Anomaly Detection**: The script `detect_fraud.py` flags trades above $5,000 and login attempts exceeding 3.
   - Sample Output:
   - Suspicious Trades (Amount > $5000):
UserID|TradeAmount|Timestamp         |LoginAttempts
User3 |10000     |2023-10-01 12:00 PM|5
Suspicious Logins (Attempts > 3):
UserID|TradeAmount|Timestamp         |LoginAttempts
User3 |10000     |2023-10-01 12:00 PM|5
3. **Security Recommendations**: Proposed measures like encryption and 2FA to secure the platform.

## Setup and Usage
### Prerequisites
- Kali Linux (or any Linux OS)
- Python 3 with pandas (`pip3 install pandas`)
- Git (`sudo apt install git`)
