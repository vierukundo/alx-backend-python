#!/usr/bin/env python3
"""Required modules"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Iterate over async_generator,
    then return the 10 random numbers."""
    numbers = [num async for num in async_generator()]
    return numbers
