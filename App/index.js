import React from "react";
import { NavigationContainer, NavigationIndependentTree } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import InputPage from "./(tabs)/InputPage"; // 页面组件
import WebSocketPage from "./(tabs)/WebSocketPage"; // 页面组件

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationIndependentTree>
      <Stack.Navigator initialRouteName="InputPage">  
        <Stack.Screen 
          name="InputPage" 
          component={InputPage} 
          options={{ title: "Enter WebSocket Info" }} 
        />
        <Stack.Screen 
          name="WebSocketPage" 
          component={WebSocketPage} 
          options={{ title: "WebSocket Viewer" }} 
        />
      </Stack.Navigator>
    </NavigationIndependentTree>
  );
}
