import json
from pyrogram.api import functions
from tgtc import TelegramThinClient

client = TelegramThinClient()
with client:
    tg_config = client.send(functions.help.GetConfig())

    dcs = {}
    for dc in tg_config['dc_options']:
        if not dc.ipv6:
            if dc.id not in dcs:
                dcs[dc.id] = []
            if dc.ip_address not in dcs[dc.id]:
                dcs[dc.id].append(dc.ip_address)

    print(dcs)
