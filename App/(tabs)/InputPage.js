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

export default InputPage;import React, { useState } from "react";
import { View, TextInput, TouchableOpacity, Text, StyleSheet, Alert, ActivityIndicator } from "react-native";



const InputPage = ({ navigation }) => {
  const [ipAddress, setIpAddress] = useState("");
  const [port, setPort] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false); // 控制提交流程
  const [theme, setTheme] = useState("light"); // 控制当前主题，默认为浅色模式

  const handleSubmit = async () => {
    if (!ipAddress || !port) {
      Alert.alert("Error", "Please enter both IP address and port.");
      return;
    }

    setIsSubmitting(true); // 开始提交
    try {
      const webSocketUrl = `ws://${ipAddress}:${port}`;
      // 模拟异步操作，如连接 WebSocket
      await new Promise((resolve) => setTimeout(resolve, 1000)); // 模拟延时
      navigation.navigate("WebSocketPage", { webSocketUrl });
    } catch (error) {
      Alert.alert("Error", "Failed to prepare WebSocket connection.");
    } finally {
      setIsSubmitting(false); // 恢复提交状态
    }
  };

  // 切换主题的函数
  const toggleTheme = () => {
    setTheme(theme === "light" ? "dark" : "light");
  };

  return (
    <View style={[styles.container, theme === "light" ? styles.lightBackground : styles.darkBackground]}>
      {/* 标题和主题切换按钮放置在同一行 */}
      <View style={[styles.header, theme === "light" ? styles.lightHeader : styles.darkHeader]}>
        <Text style={[styles.headerTitle, theme === "light" ? styles.lightHeaderText : styles.darkHeaderText]}>
          Enter WebSocket Info
        </Text>
        <TouchableOpacity style={styles.toggleButton} onPress={toggleTheme}>
          <Text style={styles.toggleButtonText}>
            {theme === "light" ? "Dark" : "Light"} Mode
          </Text>
        </TouchableOpacity>
      </View>

       {/* Logo: 圆形图标
      <View style={styles.logoContainer}>
        <Icon name="" size={60} color={theme === "light" ? "#000" : "#fff"} />
      </View> */}

      <View style={[styles.inputContainer, theme === "light" ? styles.lightInputContainer : styles.darkInputContainer]}>
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

      <TouchableOpacity 
        style={[styles.button, isSubmitting && styles.buttonDisabled]} 
        onPress={handleSubmit} 
        disabled={isSubmitting}
      >
        {isSubmitting ? (
          <ActivityIndicator size="small" color="#fff" />
        ) : (
          <Text style={styles.buttonText}>Connect</Text>
        )}
      </TouchableOpacity>
    </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 30,
  },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 10,
    marginBottom: 40, // 增加输入框之间的距离
    fontSize: 16,
    backgroundColor: "#fff",
  },
  button: {
    backgroundColor: "#007bff",  // 按钮背景色
    padding: 12,
    borderRadius: 8,
    alignItems: "center",
    justifyContent: "center",
  },
  buttonDisabled: {
    backgroundColor: "#cccccc",  // 禁用状态下的按钮背景色
  },
  buttonText: {
    color: "#fff",
    fontSize: 18,
  },
  lightBackground: {
    backgroundColor: "#f5f5f5",  // 浅色背景
  },
  darkBackground: {
    backgroundColor: "#333",  // 深色背景
  },
  lightHeader: {
    backgroundColor: "#fff",  // 浅色模式下的标题背景
  },
  darkHeader: {
    backgroundColor: "#444",  // 深色模式下的标题背景
  },
  header: {
    flexDirection: "row",  // 水平排列标题和按钮
    justifyContent: "space-between",  // 使标题和按钮分开
    alignItems: "center",  // 垂直居中
    marginBottom: 20,  // 给标题区域底部添加间距
    paddingHorizontal: 10,  // 给标题区域添加左右内边距
    paddingVertical: 10,  // 给标题区域添加上下内边距
    borderRadius: 8,  // 圆角效果
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#000",
  },
  lightHeaderText: {
    color: "#000",  // 浅色模式下的文字颜色
  },
  darkHeaderText: {
    color: "#fff",  // 深色模式下的文字颜色
  },
  toggleButton: {
    padding: 10,
    backgroundColor: "#444",
    borderRadius: 5,
    alignItems: "center",
  },
  toggleButtonText: {
    color: "#fff",
    fontSize: 14,
  },
  inputContainer: {
    backgroundColor: "#fff",  // 输入区域背景色
    padding: 30,  // 内边距
    borderRadius: 20,  // 圆角效果
    shadowColor: "#000",  // 阴影
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.5,  // 阴影透明度
    shadowRadius: 20,  // 阴影模糊度
    elevation: 10,  // Android 阴影效果
  },
  lightInputContainer: {
    backgroundColor: "#fff",  // 浅色背景
  },
  darkInputContainer: {
    backgroundColor: "#111",  // 深色背景
  },
  // logoContainer: {
  //   justifyContent: 'center',
  //   alignItems: 'center',
  //   marginBottom: 20, // 控制logo和其他元素之间的间距
  // },
  // logo: {
  //   width: 100,  // logo宽度
  //   height: 100, // logo高度
  //   borderRadius: 50, // 使 logo 成为圆形
  //   resizeMode: "cover", // 保持比例缩放，并填充整个区域
  // },
});

export default InputPage;
