import sys

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

def main():
    portfolio = StockPortfolio()
    
    while True:
        print("\nStock Portfolio Management")
        print("1. Add stock")
        print("2. Update stock price")
        print("3. Remove stock")
        print("4. View portfolio")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            price = float(input("Enter price per share: "))
            portfolio.add_stock(symbol, shares, price)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            new_price = float(input("Enter new price: "))
            portfolio.update_price(symbol, new_price)
        elif choice == '3':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == '4':
            portfolio.view_portfolio()
        elif choice == '5':
            print("Thank you for using the Stock Portfolio Management system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()