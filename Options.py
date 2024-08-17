class Option:
    def __init__(self, underlying, strike, expiration, option_type, premium):
        self.underlying = underlying
        self.strike = strike
        self.expiration = expiration
        self.option_type = option_type
        self.premium = premium

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
        self.options = {}

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

    def add_option(self, underlying, strike, expiration, option_type, premium, contracts):
        option = Option(underlying, strike, expiration, option_type, premium)
        key = f"{underlying}_{strike}_{expiration}_{option_type}"
        if key in self.options:
            self.options[key]['contracts'] += contracts
        else:
            self.options[key] = {'option': option, 'contracts': contracts}
        print(f"Added {contracts} contracts of {underlying} {option_type} option with strike ${strike:.2f} expiring on {expiration}")

    def remove_option(self, underlying, strike, expiration, option_type, contracts):
        key = f"{underlying}_{strike}_{expiration}_{option_type}"
        if key in self.options:
            if contracts >= self.options[key]['contracts']:
                del self.options[key]
                print(f"Removed all contracts of {underlying} {option_type} option with strike ${strike:.2f} expiring on {expiration}")
            else:
                self.options[key]['contracts'] -= contracts
                print(f"Removed {contracts} contracts of {underlying} {option_type} option with strike ${strike:.2f} expiring on {expiration}")
        else:
            print(f"Option not found in the portfolio.")

    def view_portfolio(self):
        print("\nCurrent Portfolio:")
        print("------------------")
        total_value = 0
        
        print("Stocks:")
        for symbol, data in self.portfolio.items():
            shares = data['shares']
            price = data['price']
            value = shares * price
            total_value += value
            print(f"{symbol}: {shares} shares at ${price:.2f} - Total Value: ${value:.2f}")
        
        print("\nOptions:")
        for key, data in self.options.items():
            option = data['option']
            contracts = data['contracts']
            value = contracts * 100 * option.premium
            total_value += value
            print(f"{option.underlying} {option.option_type} {option.strike:.2f} {option.expiration}: {contracts} contracts at ${option.premium:.2f} - Total Value: ${value:.2f}")
        
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

# Example usage
portfolio = StockPortfolio()

# Add some stocks
portfolio.add_stock("AAPL", 10, 150.50)
portfolio.add_stock("GOOGL", 5, 2700.75)
portfolio.add_stock("MSFT", 15, 300.25)

# Add some options
portfolio.add_option("AAPL", 160, "2023-12-15", "CALL", 5.50, 2)
portfolio.add_option("GOOGL", 2800, "2023-12-15", "PUT", 100.25, 1)

# View the portfolio
portfolio.view_portfolio()

# Update a stock price
portfolio.update_price("AAPL", 155.75)

# Remove some shares and options
portfolio.remove_stock("GOOGL", 2)
portfolio.remove_option("AAPL", 160, "2023-12-15", "CALL", 1)

# View the updated portfolio
portfolio.view_portfolio()