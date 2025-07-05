# event_bus.py

from typing import Callable, Dict, List, Type, Any
import logging
from dataclasses import dataclass

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# --- Event Base ---
@dataclass
class Event:
    """Base class for all events."""
    pass


# --- Concrete Events ---
@dataclass
class UserRegisteredEvent(Event):
    username: str
    email: str


@dataclass
class OrderPlacedEvent(Event):
    order_id: str
    user_id: str
    amount: float


# --- Event Bus Implementation ---
class EventBus:
    def __init__(self):
        self._subscribers: Dict[Type[Event], List[Callable[[Event], None]]] = {}

    def subscribe(self, event_type: Type[Event], handler: Callable[[Event], None]) -> None:
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)
        logger.debug(f"Subscribed to {event_type.__name__}")

    def publish(self, event: Event) -> None:
        handlers = self._subscribers.get(type(event), [])
        logger.info(f"Publishing event: {event}")
        for handler in handlers:
            try:
                handler(event)
            except Exception as e:
                logger.exception(f"Error handling event {event}: {e}")


# --- Handlers ---
def send_welcome_email(event: UserRegisteredEvent) -> None:
    logger.info(f"Sending welcome email to {event.username} at {event.email}")


def log_order(event: OrderPlacedEvent) -> None:
    logger.info(f"Order {event.order_id} for user {event.user_id} of amount ${event.amount:.2f} received.")


# --- Example Usage ---
def main():
    bus = EventBus()

    # Register handlers
    bus.subscribe(UserRegisteredEvent, send_welcome_email)
    bus.subscribe(OrderPlacedEvent, log_order)

    # Trigger events
    bus.publish(UserRegisteredEvent(username="brianbett", email="brian@example.com"))
    bus.publish(OrderPlacedEvent(order_id="ORD123", user_id="brianbett", amount=199.99))


if __name__ == "__main__":
    main()

