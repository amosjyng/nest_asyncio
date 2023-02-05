import nest_asyncio
import asyncio

nest_asyncio.apply()

async def hello():
    return "world"

result = asyncio.get_event_loop().run_until_complete(hello())

def test_warning():
    assert result == "world"
