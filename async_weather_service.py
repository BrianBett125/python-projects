# async_weather_service.py

import asyncio
import random
from typing import List, Protocol
from dataclasses import dataclass
import logging

# --- Setup Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# --- Domain Model ---
@dataclass
class WeatherData:
    provider: str
    temperature: float  # Celsius
    condition: str


# --- Interface for Weather Provider ---
class WeatherProvider(Protocol):
    async def fetch_weather(self, city: str) -> WeatherData:
        ...


# --- Simulated Providers ---
class ProviderA:
    async def fetch_weather(self, city: str) -> WeatherData:
        await asyncio.sleep(random.uniform(0.5, 1.5))
        return WeatherData(provider="ProviderA", temperature=24.5, condition="Sunny")


class ProviderB:
    async def fetch_weather(self, city: str) -> WeatherData:
        await asyncio.sleep(random.uniform(0.5, 1.0))
        return WeatherData(provider="ProviderB", temperature=23.0, condition="Partly Cloudy")


class FaultyProvider:
    async def fetch_weather(self, city: str) -> WeatherData:
        await asyncio.sleep(0.2)
        raise Exception("API Failure from FaultyProvider")


# --- Service Layer ---
class WeatherService:
    def __init__(self, providers: List[WeatherProvider]):
        self.providers = providers

    async def get_weather_from_all(self, city: str) -> List[WeatherData]:
        tasks = [self._safe_fetch(p, city) for p in self.providers]
        results = await asyncio.gather(*tasks)
        return [r for r in results if r]

    async def _safe_fetch(self, provider: WeatherProvider, city: str) -> WeatherData | None:
        try:
            return await asyncio.wait_for(provider.fetch_weather(city), timeout=2.0)
        except Exception as e:
            logger.warning(f"Provider failed: {e}")
            return None


# --- Entry Point ---
async def main():
    providers = [ProviderA(), ProviderB(), FaultyProvider()]
    service = WeatherService(providers)

    logger.info("Fetching weather data...")
    results = await service.get_weather_from_all("Nairobi")

    for result in results:
        logger.info(f"{result.provider}: {result.temperature}°C, {result.condition}")


if __name__ == "__main__":
    asyncio.run(main())

