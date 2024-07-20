import React, { useState, useEffect } from "react";
import { View, Text, Button } from"react-native";

const App = () => {
  const [otp, setOtp] = useState("");
  const [verified, setVerified] = useState(false);

  useEffect(() => {
    const totp = new TwoFactorAuth();
    const otp = totp.generate_otp();
    setOtp(otp);
  }, []);

  const handleVerify = () => {
    const totp = new TwoFactorAuth();
    if (totp.verify_otp(otp)) {
      setVerified(true);
    } else {
      alert("Invalid OTP");
    }
  };

  return (
    <View>
      <Text>Enter OTP: {otp}</Text>
      <Button title="Verify" onPress={handleVerify} />
      {verified? <Text>Verified!</Text> : <Text>Not Verified</Text>}
    </View>
  );
};

export default App;
