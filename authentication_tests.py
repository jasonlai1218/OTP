import unittest
from unittest.mock import patch

from authentication_service import is_valid


class AuthenticationServiceTests(unittest.TestCase):
    def test_is_valid(self):
        self.given_password("91")
        self.given_otp("000000")
        self.should_be_valid("Jason", "91000000")

    def test_is_invalid(self):
        self.given_password("91")
        self.given_otp("000000")
        self.should_be_invalid("Jason", "wrong password")

    def should_be_invalid(self, account, password):
        self.assertEqual(False, is_valid(account, password))

    def test_should_log_account_when_invalid(self):
        self.when_invalid("jason")
        self.should_log("jason", "login failed")

    def should_log(self, account, status):
        self.fake_info.assert_called_once()
        message = self.fake_info.call_args[0][0]
        self.assertIn(account, message)
        self.assertIn(status, message)

    def when_invalid(self, account):
        self.given_password("91")
        self.given_otp("000000")
        is_valid(account, "wrong password")

    def should_be_valid(self, account, password):
        self.assertEqual(True, is_valid(account, password))

    def given_otp(self, otp):
        self.fake_get_otp.return_value = otp

    def given_password(self, password):
        self.fake_get_password.return_value = password

    def setUp(self) -> None:
        get_password_patch = patch('authentication_service.get_password_from_db')
        self.fake_get_password = get_password_patch.start()
        get_otp_patch = patch('authentication_service.get_otp')
        self.fake_get_otp = get_otp_patch.start()
        info_patch = patch('authentication_service.MyLogger.info')
        self.fake_info = info_patch.start()

    def tearDown(self) -> None:
        patch.stopall()


if __name__ == '__main__':
    unittest.main()
