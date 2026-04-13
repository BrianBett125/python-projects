"""
Filename: complex_pipeline.py
Author: Brian Bett
Description:
    A complex Python script demonstrating nested dictionaries, decorators,
    loops, concurrency, and CLI arguments for pipeline control.
"""

import json
import threading
import random
import time
import argparse
from functools import wraps, lru_cache
from contextlib import contextmanager
from concurrent.futures import ThreadPoolExecutor, as_completed


# ====================== Custom Exceptions ======================

class DataValidationError(Exception):
    pass


class ExternalAPILookupError(Exception):
    pass


# ====================== Decorators ======================

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[TIMER] {func.__name__} executed in {(end - start):.4f}s")
        return result
    return wrapper


def retry(times=3, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"[RETRY] Attempt {attempt + 1} failed for {func.__name__}: {e}")
                    last_exc = e
                    time.sleep(0.2)
            raise last_exc
        return wrapper
    return decorator


# ====================== Context Manager ======================

@contextmanager
def file_writer(filename):
    try:
        f = open(filename, "w", encoding="utf-8")
        yield f
    finally:
        f.close()


# ====================== Thread-safe Logger ======================

class ThreadSafeLogger:
    _lock = threading.Lock()

    @classmethod
    def log(cls, message):
        with cls._lock:
            print(f"[LOG] {message}")


# ====================== Utility Functions ======================

def generate_fake_data(num_records=10):
    for i in range(num_records):
        yield {
            "id": i + 1,
            "user": {
                "name": f"User_{i+1}",
                "email": f"user{i+1}@example.com"
            },
            "metrics": {
                "score": random.randint(1, 100),
                "active": random.choice([True, False])
            }
        }


@retry(times=2, exceptions=(DataValidationError,))
def validate_data(record):
    if not record.get("user") or "email" not in record["user"]:
        raise DataValidationError("Missing user email")
    return record


@lru_cache(maxsize=50)
def enrich_data(record_id):
    if random.random() < 0.1:
        raise ExternalAPILookupError("Simulated API failure")
    return {"external_info": f"Data_for_{record_id}"}


def categorize_score(score):
    if score >= 80:
        return "Excellent"
    elif score >= 50:
        return "Average"
    else:
        return "Poor"


# ====================== Main Pipeline ======================

class DataPipeline:

    def __init__(self, data_source):
        self.data_source = data_source
        self.processed = []

    @time_it
    def run(self):
        ThreadSafeLogger.log("Pipeline started.")
        validated = []
        for record in self.data_source:
            try:
                validated.append(validate_data(record))
            except DataValidationError as e:
                ThreadSafeLogger.log(f"Validation failed: {e}")

        enriched = self._enrich_in_parallel(validated)
        for rec in enriched:
            rec["category"] = categorize_score(rec["metrics"]["score"])
            self.processed.append(rec)

        ThreadSafeLogger.log("Pipeline completed.")
        return self.processed

    def _enrich_in_parallel(self, records):
        results = []
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(self._enrich_record, r): r for r in records}
            for future in as_completed(futures):
                try:
                    results.append(future.result())
                except ExternalAPILookupError as e:
                    ThreadSafeLogger.log(f"Enrichment failed: {e}")
        return results

    def _enrich_record(self, record):
        record.update(enrich_data(record["id"]))
        return record


# ====================== CLI Entry Point ======================

def main():
    parser = argparse.ArgumentParser(description="Run the data pipeline.")
    parser.add_argument("--records", type=int, default=10, help="Number of fake records to generate.")
    parser.add_argument("--output", type=str, default="output_results.json", help="Output file name.")
    args = parser.parse_args()

    data = list(generate_fake_data(args.records))
    pipeline = DataPipeline(data)
    processed = pipeline.run()

    with file_writer(args.output) as f:
        json.dump(processed, f, indent=4)

    print("\n=== PIPELINE SUMMARY ===")
    print(f"Processed Records: {len(processed)}")
    print(f"Sample Output:\n{json.dumps(processed[:3], indent=4)}")


if __name__ == "__main__":
    main()

