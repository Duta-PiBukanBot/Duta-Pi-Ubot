import asyncio

from . import edit_or_reply, tod

plugin_category = "fun"


@tod.tod_cmd(
    pattern="pamulang$",
    command=("pamulang", plugin_category),
    info={
        "header": "Fun animation try yourself to see.",
        "usage": "{tr}pamulang",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "pamulang")
    await event.edit("KE PAMULANG NAIK GOJEK")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("JANGAN MAMPIR KE RUMAH DUTA")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("PULANG LU ANAK BELEK")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("MAO DISUAPIN MAKAN SAMA MAMA")
    await asyncio.sleep(3)
    await event.edit("CAKEP...😎😎😎")


@tod.tod_cmd(
    pattern="krukut$",
    command=("krukut", plugin_category),
    info={
        "header": "Fun animation try yourself to see.",
        "usage": "{tr}krukut",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "krukut")
    await event.edit("KRUKUT KUBURAN CINA")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("KUBURAN ISLAM BIAR GUA YANG NGAJIIN")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("KALO EMANG ITU MAONYA")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("SAMPE DIMANA BAKAL GUA LADENIN")
    await asyncio.sleep(3)
    await event.edit("CAKEP...😎😎😎")


@tod.tod_cmd(
    pattern="saka$",
    command=("saka", plugin_category),
    info={
        "header": "Fun animation try yourself to see.",
        "usage": "{tr}saka",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "saka")
    await event.edit("DUA TIGA ADUDU MAKAN TERI")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("MAKANNYA SAMBIL LIAT PETA")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("KALO LU EMANG JAGOAN DIMARI")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("NIH KENALIN NIH JAGONYA SAMBUNG KATA")
    await asyncio.sleep(3)
    await event.edit("CHUAKSS...😎😎😎")


@tod.tod_cmd(
    pattern="masakaer$",
    command=("masakaer", plugin_category),
    info={
        "header": "Fun animation try yourself to see.",
        "usage": "{tr}masaker",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "masakaer")
    await event.edit("MASAK AER BIAR MATENG")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("ADA KUDA MAKAN JERAMI")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("LU JANGAN SOK GANTENG")
    await asyncio.sleep(3)
    await event.edit("CAKEP...")
    await asyncio.sleep(0.5)
    await event.edit("MUKA LU KAYA GARPU POPMIE")
    await asyncio.sleep(3)
    await event.edit("CAKEP...😎😎😎")


@tod.tod_cmd(
    pattern="botol$",
    command=("botol", plugin_category),
    info={
        "header": "Fun animation try yourself to see.",
        "usage": "{tr}botol",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "botol")
    await event.edit("DUA TIGA TUTUP BOTOL")
    await asyncio.sleep(3)
    await event.edit("MUKA LU KAYA KONT*L")
    await asyncio.sleep(3)
    await event.edit("CAKEP...😎😎😎")


@tod.tod_cmd(
    pattern="joinvcg$",
    command=("joinvcg", plugin_category),
    info={
        "header": "Fun animation try yourself to see.",
        "usage": "{tr}botol",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "joining")
    await event.edit("joining vcg")
    await asyncio.sleep(3)
    await event.edit("joined succesed")
