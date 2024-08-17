class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares, price):
        if symbol in self.portfolio:
            print(f"Updating {symbol} in the portfolio.")
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'price': price}
        print(f"Added {shares} shares of {symbol} at ${price:.2f} per share.")

    def update_price(self, symbol, new_price):
        if symbol in self.portfolio:
            self.portfolio[symbol]['price'] = new_price
            print(f"Updated price of {symbol} to ${new_price:.2f}")
        else:
            print(f"{symbol} not found in the portfolio.")

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]['shares']:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol} from the portfolio.")
            else:
                self.portfolio[symbol]['shares'] -= shares
                print(f"Removed {shares} shares of {symbol} from the portfolio.")
        else:
            print(f"{symbol} not found in the portfolio.")

    def view_portfolio(self):
        print("\nCurrent Portfolio:")
        print("------------------")
        total_value = 0
        for symbol, data in self.portfolio.items():
            shares = data['shares']
            price = data['price']
            value = shares * price
            total_value += value
            print(f"{symbol}: {shares} shares at ${price:.2f} - Total Value: ${value:.2f}")
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

# Example usage
portfolio = StockPortfolio()

# Add some stocks
portfolio.add_stock("AAPL", 10, 150.50)
portfolio.add_stock("GOOGL", 5, 2700.75)
portfolio.add_stock("MSFT", 15, 300.25)

# View the portfolio
portfolio.view_portfolio()

# Update a stock price
portfolio.update_price("AAPL", 155.75)

# Remove some shares
portfolio.remove_stock("GOOGL", 2)

# View the updated portfolio
portfolio.view_portfolio()