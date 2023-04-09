import asyncio
import importlib

from pytgcalls import idle
from rich.table import Table
from rich.console import Console
from callmusic import BOT_USERNAME, bot, call_py
from callmusic.plugins import ALL_PLUGINS

console = Console()
loop = asyncio.get_event_loop()


async def eSport_boot():
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(
        "Arnav MusicX : Best Ever Music Bot"
    )
    console.print(header)
    for all_module in ALL_PLUGINS:
        importlib.import_module("callmusic.plugins." + all_module)
    console.print("┌ [red]Starting Your Music Bot Client ...\n")
    await bot.start()
    console.print("└ [green]Started Music Bot Client")
    console.print("\n┌ [red]Booting Up The User Client...")
    await call_py.start()
    console.print("├ [yellow]Booted User Client")
    console.print("└ [green]Successfully Started Music Bot ...")
    await idle()
    print(f"ɢᴏᴏᴅʙʏᴇ!\nStopping @{BOT_USERNAME}")
    await bot.stop()


if __name__ == "__main__":
    loop.run_until_complete(eSport_boot())
