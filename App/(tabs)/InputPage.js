import React, { useState } from "react";
import { View, TextInput, Button, StyleSheet, Alert } from "react-native";

const InputPage = ({ navigation }) => {
  const [ipAddress, setIpAddress] = useState("");
  const [port, setPort] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false); // 增加状态以控制提交流程

  const handleSubmit = async () => {
    if (!ipAddress || !port) {
      Alert.alert("Error", "Please enter both IP address and port.");
      return;
    }

    setIsSubmitting(true); // 开始提交
    try {
      const webSocketUrl = `ws://${ipAddress}:${port}`;
      // 可以在这里执行其他必要逻辑（如验证 WebSocket URL 是否可用等）
      await new Promise((resolve) => setTimeout(resolve, 1000)); // 模拟异步操作
      navigation.navigate("WebSocketPage", { webSocketUrl });
    } catch (error) {
      Alert.alert("Error", "Failed to prepare WebSocket connection.");
    } finally {
      setIsSubmitting(false); // 恢复提交状态
    }
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
      <Button title="Connect" onPress={handleSubmit} disabled={isSubmitting} />
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
