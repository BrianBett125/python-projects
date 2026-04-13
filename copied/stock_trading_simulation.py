import threading
import time
import random
import logging
from queue import Queue

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Simulated stock data
SIMULATED_STOCKS = {
    'AAPL': 150.00,
    'GOOG': 2800.00,
    'AMZN': 3400.00,
    'TSLA': 720.00,
    'MSFT': 299.00
}


class StockMarket:
    """Simulates a real-time stock market with price updates."""
    def __init__(self):
        self.prices = SIMULATED_STOCKS.copy()
        self.lock = threading.Lock()

    def update_prices(self):
        """Randomly update stock prices in a thread-safe way."""
        with self.lock:
            for symbol in self.prices:
                change = random.uniform(-2, 2)
                self.prices[symbol] = round(self.prices[symbol] + change, 2)
                logging.info(f"[Market] {symbol} updated to ${self.prices[symbol]}")

    def get_price(self, symbol):
        """Get current stock price."""
        with self.lock:
            return self.prices.get(symbol, None)


class Trader(threading.Thread):
    """Trader class representing an individual who buys and sells stocks."""
    def __init__(self, trader_id, market: StockMarket, order_queue: Queue):
        super().__init__(daemon=True)
        self.trader_id = trader_id
        self.market = market
        self.order_queue = order_queue
        self.portfolio = {}

    def run(self):
        while True:
            try:
                symbol = random.choice(list(SIMULATED_STOCKS.keys()))
                price = self.market.get_price(symbol)
                action = random.choice(['buy', 'sell'])
                quantity = random.randint(1, 10)

                if action == 'buy':
                    self.portfolio[symbol] = self.portfolio.get(symbol, 0) + quantity
                    logging.info(f"[Trader {self.trader_id}] Bought {quantity} shares of {symbol} at ${price}")
                elif action == 'sell' and self.portfolio.get(symbol, 0) >= quantity:
                    self.portfolio[symbol] -= quantity
                    logging.info(f"[Trader {self.trader_id}] Sold {quantity} shares of {symbol} at ${price}")

                self.order_queue.put((self.trader_id, action, symbol, quantity, price))
                time.sleep(random.uniform(1, 3))

            except Exception as e:
                logging.error(f"[Trader {self.trader_id}] Error: {e}")


class MarketSupervisor(threading.Thread):
    """Monitors all trades and logs summaries."""
    def __init__(self, order_queue: Queue):
        super().__init__(daemon=True)
        self.order_queue = order_queue

    def run(self):
        while True:
            try:
                trader_id, action, symbol, quantity, price = self.order_queue.get(timeout=5)
                logging.info(f"[Supervisor] Trader {trader_id} executed {action.upper()} {quantity} of {symbol} at ${price}")
            except Exception:
                continue


def start_simulation():
    market = StockMarket()
    order_queue = Queue()

    # Create and start supervisor
    supervisor = MarketSupervisor(order_queue)
    supervisor.start()

    # Create and start traders
    traders = [Trader(i, market, order_queue) for i in range(5)]
    for trader in traders:
        trader.start()

    # Simulate market price updates
    while True:
        market.update_prices()
        time.sleep(5)


if __name__ == "__main__":
    try:
        start_simulation()
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

