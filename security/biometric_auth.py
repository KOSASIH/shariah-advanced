import fingerprint

class BiometricAuth:
    def __init__(self):
        self.fp = fingerprint.Fingerprint()

    def enroll_fingerprint(self, finger_id):
        self.fp.enroll_finger(finger_id)

    def verify_fingerprint(self, finger_id):
        return self.fp.verify_finger(finger_id)

    def identify_fingerprint(self, finger_id):
        return self.fp.identify_finger(finger_id)
