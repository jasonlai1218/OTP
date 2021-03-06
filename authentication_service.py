from my_logger import MyLogger
from otp_service import get_otp
from profile_dao import get_password_from_db


def is_valid(account, password):
    password_from_db = get_password_from_db(account)
    otp = get_otp(account)
    valid_password = password_from_db + otp
    if valid_password == password:
        return True
    else:
        MyLogger().info("account: %s try to login failed" % account)
        return False
