import React, { useState } from "react";
import { View, TextInput, Button, StyleSheet, Alert } from "react-native";

const InputPage = ({ navigation }) => {
  const [ipAddress, setIpAddress] = useState("");
  const [port, setPort] = useState("");

  const handleSubmit = () => {
    if (!ipAddress || !port) {
      Alert.alert("Error", "Please enter both IP address and port.");
      return;
    }
    const webSocketUrl = `ws://${ipAddress}:${port}`;
    navigation.navigate("WebSocketPage", { webSocketUrl });
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Enter IP Address (e.g., 10.195.38.128)"
        value={ipAddress}
        onChangeText={setIpAddress}
        keyboardType="numeric"
      />
      <TextInput
        style={styles.input}
        placeholder="Enter Port (e.g., 12345)"
        value={port}
        onChangeText={setPort}
        keyboardType="numeric"
      />
      <Button title="Connect" onPress={handleSubmit} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 20,
    backgroundColor: "#f5f5f5",
  },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 10,
    marginBottom: 20,
    fontSize: 16,
    backgroundColor: "#fff",
  },
});

export default InputPage;
