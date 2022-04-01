#  Copyright (C) 2020  sandeep.n(π.$)
# credits to (@hitokizzy)
import asyncio
import os
import re

from tod import tod

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)

plugin_category = "fun"


@tod.tod_cmd(
    pattern="fakegs(?:\s|$)([\s\S]*)",
    command=("fakegs", plugin_category),
    info={
        "header": "Fake google search meme",
        "usage": "{tr}fakegs search query ; what you mean text",
        "examples": "{tr}fakegs TODUBOT ; One of the Popular userbot",
    },
)
async def nekobot(tod):
    "Fake google search meme"
    text = tod.pattern_match.group(1)
    reply_to_id = await reply_id(tod)
    if not text:
        if tod.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            return await edit_delete(tod, "`What should i search in google.`", 5)
    sade = await edit_or_reply(tod, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            tod,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    sadfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await tod.client.send_file(tod.chat_id, sadfile, reply_to=reply_to_id)
    await sade.delete()
    if os.path.exists(sadfile):
        os.remove(sadfile)


@tod.tod_cmd(
    pattern="trump(?:\s|$)([\s\S]*)",
    command=("trump", plugin_category),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}trump <text>",
        "examples": "{tr}trump TODUBOT is One of the Popular userbot",
    },
)
async def nekobot(tod):
    "trump tweet sticker with given custom text_"
    text = tod.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(tod)

    reply = await tod.get_reply_message()
    if not text:
        if tod.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(tod, "**Trump : **`What should I tweet`", 5)
    sade = await edit_or_reply(tod, "`Requesting trump to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    sadfile = await trumptweet(text)
    await tod.client.send_file(tod.chat_id, sadfile, reply_to=reply_to_id)
    await sade.delete()
    if os.path.exists(sadfile):
        os.remove(sadfile)


@tod.tod_cmd(
    pattern="modi(?:\s|$)([\s\S]*)",
    command=("modi", plugin_category),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}modi <text>",
        "examples": "{tr}modi TODUBOT is One of the Popular userbot",
    },
)
async def nekobot(tod):
    "modi tweet sticker with given custom text"
    text = tod.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(tod)

    reply = await tod.get_reply_message()
    if not text:
        if tod.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(tod, "**Modi : **`What should I tweet`", 5)
    sade = await edit_or_reply(tod, "Requesting modi to tweet...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    sadfile = await moditweet(text)
    await tod.client.send_file(tod.chat_id, sadfile, reply_to=reply_to_id)
    await sade.delete()
    if os.path.exists(sadfile):
        os.remove(sadfile)


@tod.tod_cmd(
    pattern="cmm(?:\s|$)([\s\S]*)",
    command=("cmm", plugin_category),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}cmm <text>",
        "examples": "{tr}cmm TODUBOT is One of the Popular userbot",
    },
)
async def nekobot(tod):
    text = tod.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(tod)

    reply = await tod.get_reply_message()
    if not text:
        if tod.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(tod, "`Give text to write on banner, man`", 5)
    sade = await edit_or_reply(tod, "`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    sadfile = await changemymind(text)
    await tod.client.send_file(tod.chat_id, sadfile, reply_to=reply_to_id)
    await sade.delete()
    if os.path.exists(sadfile):
        os.remove(sadfile)


@tod.tod_cmd(
    pattern="kanna(?:\s|$)([\s\S]*)",
    command=("kanna", plugin_category),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}kanna text",
        "examples": "{tr}kanna TODUBOT is One of the Popular userbot",
    },
)
async def nekobot(tod):
    "kanna chan sticker with given custom text"
    text = tod.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(tod)

    reply = await tod.get_reply_message()
    if not text:
        if tod.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(tod, "**Kanna : **`What should i show you`", 5)
    sade = await edit_or_reply(tod, "`Kanna is writing your text...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    sadfile = await kannagen(text)
    await tod.client.send_file(tod.chat_id, sadfile, reply_to=reply_to_id)
    await sade.delete()
    if os.path.exists(sadfile):
        os.remove(sadfile)


@tod.tod_cmd(
    pattern="tweet(?:\s|$)([\s\S]*)",
    command=("tweet", plugin_category),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}tweet <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; TODUBOT is One of the Popular userbot",
    },
)
async def nekobot(tod):
    "The desired person tweet sticker with given custom text"
    text = tod.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(tod)

    reply = await tod.get_reply_message()
    if not text:
        if tod.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(
                tod,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            tod,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    sade = await edit_or_reply(tod, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    sadfile = await tweets(text, username)
    await tod.client.send_file(tod.chat_id, sadfile, reply_to=reply_to_id)
    await sade.delete()
    if os.path.exists(sadfile):
        os.remove(sadfile)
