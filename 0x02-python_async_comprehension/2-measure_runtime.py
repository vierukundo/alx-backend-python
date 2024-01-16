#!/usr/bin/env python3
"""Required modules"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures runtime for async_comprehension"""
    start = time.perf_counter()
    result = await asyncio.gather(
            async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())

    end = time.perf_counter()

    return end - start
