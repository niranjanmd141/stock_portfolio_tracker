import yfinance as yf
import pandas as pd
import os
import time


def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_stock_data(ticker):
    """Fetches real-time stock data using yfinance."""
    try:
        stock = yf.Ticker(ticker)
        data = stock.info
        return data
    except Exception as e:
        print(f"❌ Error fetching data for {ticker}: {e}")
        return None


def display_portfolio(portfolio):
    """Displays the current stock portfolio."""
    clear_screen()
    print("\n📊 Your Current Portfolio")
    print("=" * 50)

    if not portfolio:
        print("🚫 Your portfolio is empty.")
        return

    df = pd.DataFrame(portfolio).T
    df['totalValue'] = df['currentPrice'] * df['quantity']
    print(df[['shortName', 'currentPrice', 'quantity', 'totalValue', 'previousClose', 'marketCap', 'sector']].to_string())
    print("=" * 50)


def show_menu():
    print("\n💼 Welcome to Stock Portfolio Tracker")
    print("1️⃣ Add Stock")
    print("2️⃣ Remove Stock")
    print("3️⃣ View Portfolio")
    print("4️⃣ Exit")


def main():
    """Main function to run the stock portfolio tracker."""
    portfolio = {}

    while True:
        clear_screen()
        show_menu()

        choice = input("\n👉 Enter your choice (1-4): ")

        if choice == '1':
            ticker = input("🔎 Enter stock ticker (e.g., AAPL): ").upper()
            try:
                quantity = int(input("📈 Enter quantity: "))
            except ValueError:
                print("⚠️ Please enter a valid number for quantity.")
                time.sleep(2)
                continue

            stock_data = get_stock_data(ticker)

            if stock_data:
                if ticker in portfolio:
                    portfolio[ticker]['quantity'] += quantity
                else:
                    portfolio[ticker] = stock_data
                    portfolio[ticker]['quantity'] = quantity
                print(f"✅ {ticker} added to portfolio with {quantity} shares.")
            input("\n🔄 Press Enter to return to menu...")

        elif choice == '2':
            ticker = input("❌ Enter stock ticker to remove: ").upper()
            if ticker in portfolio:
                del portfolio[ticker]
                print(f"🗑️ {ticker} removed from portfolio.")
            else:
                print(f"⚠️ {ticker} not found in portfolio.")
            input("\n🔄 Press Enter to return to menu...")

        elif choice == '3':
            display_portfolio(portfolio)
            input("\n🔄 Press Enter to return to menu...")

        elif choice == '4':
            print("👋 Exiting... Happy investing!")
            break

        else:
            print("⚠️ Invalid choice. Please select an option from 1 to 4.")
            time.sleep(2)


if __name__ == "__main__":
    main()
