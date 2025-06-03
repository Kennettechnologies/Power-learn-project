import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class CryptoAdvisor:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
        self.supported_coins = self._get_supported_coins()

    def _get_supported_coins(self):
        """Get list of supported cryptocurrencies."""
        try:
            response = requests.get(f"{self.base_url}/coins/list")
            return response.json()
        except Exception as e:
            print(f"Error fetching supported coins: {e}")
            return []

    def get_coin_price(self, coin_id):
        """Get current price for a specific cryptocurrency."""
        try:
            response = requests.get(f"{self.base_url}/simple/price", 
                                  params={"ids": coin_id, "vs_currencies": "usd"})
            return response.json().get(coin_id, {}).get("usd")
        except Exception as e:
            print(f"Error fetching price for {coin_id}: {e}")
            return None

    def get_market_data(self, coin_id, days=30):
        """Get historical market data for analysis."""
        try:
            response = requests.get(
                f"{self.base_url}/coins/{coin_id}/market_chart",
                params={"vs_currency": "usd", "days": days}
            )
            data = response.json()
            return pd.DataFrame(data["prices"], columns=["timestamp", "price"])
        except Exception as e:
            print(f"Error fetching market data for {coin_id}: {e}")
            return None

    def analyze_trend(self, market_data):
        """Analyze price trend and provide basic insights."""
        if market_data is None or len(market_data) < 2:
            return "Insufficient data for analysis"

        # Calculate basic statistics
        current_price = market_data["price"].iloc[-1]
        avg_price = market_data["price"].mean()
        price_change = ((current_price - market_data["price"].iloc[0]) / 
                       market_data["price"].iloc[0] * 100)

        # Generate trend analysis
        if price_change > 5:
            trend = "Strong upward trend"
        elif price_change > 0:
            trend = "Slight upward trend"
        elif price_change > -5:
            trend = "Slight downward trend"
        else:
            trend = "Strong downward trend"

        return {
            "current_price": current_price,
            "average_price": avg_price,
            "price_change_percent": price_change,
            "trend": trend
        }

    def plot_price_history(self, market_data, coin_id):
        """Plot historical price data."""
        if market_data is None:
            return

        plt.figure(figsize=(12, 6))
        plt.plot(market_data["timestamp"], market_data["price"])
        plt.title(f"{coin_id.upper()} Price History")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.grid(True)
        plt.show()

def main():
    advisor = CryptoAdvisor()
    
    # Example usage
    coin_id = "bitcoin"
    print(f"\nAnalyzing {coin_id.upper()}...")
    
    # Get current price
    current_price = advisor.get_coin_price(coin_id)
    print(f"Current price: ${current_price:,.2f}")
    
    # Get and analyze market data
    market_data = advisor.get_market_data(coin_id)
    analysis = advisor.analyze_trend(market_data)
    
    print("\nMarket Analysis:")
    for key, value in analysis.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Plot price history
    advisor.plot_price_history(market_data, coin_id)

if __name__ == "__main__":
    main() 