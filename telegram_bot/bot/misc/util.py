import sys
from subprocess import Popen
from misc.path import PathManager


def start_user_bot(string_session: str, telegram_id: int, vip_status: int = 0):
    Popen([sys.executable, PathManager.get("user_bot/main.py"), string_session, f'{telegram_id}', f'{vip_status}'])
