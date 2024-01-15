#!/usr/bin/env python3
"""Required modules"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Counts times it takes for wait_n to return"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    runtime = end - start

    return runtime/n
