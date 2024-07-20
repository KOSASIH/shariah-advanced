import pyotp

class TwoFactorAuth:
    def __init__(self):
        self.totp = pyotp.TOTP("base32secretkey")

    def generate_otp(self):
        return self.totp.now()

    def verify_otp(self, otp):
        return self.totp.verify(otp)
