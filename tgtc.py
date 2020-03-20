from pyrogram.api.core import TLObject
from pyrogram.session import Auth, Session
from pyrogram.client.ext import BaseClient
from pyrogram.client.storage import MemoryStorage

class TelegramThinClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.api_id = 1
        self.app_version = '1'
        self.device_model = '1'
        self.system_version = '1'
        self.lang_code = 'en'
        self.ipv6 = False
        self.proxy = {}
        self.storage = MemoryStorage(':memory:')

    def __enter__(self):
        try:
            self.storage.open()
            self.storage.auth_key(Auth(self, self.storage.dc_id()).create())
            Session.notice_displayed = True
            self.session = Session(self, self.storage.dc_id(), self.storage.auth_key())
            self.session.start()
        except (Exception, KeyboardInterrupt):
            self.disconnect()
            raise
        else:
            return self

    def __exit__(self, *args):
        self.session.stop()
        self.storage.close()

    def send(self, data: TLObject, retries: int = Session.MAX_RETRIES, timeout: float = Session.WAIT_TIMEOUT):
        return self.session.send(data, retries, timeout)

