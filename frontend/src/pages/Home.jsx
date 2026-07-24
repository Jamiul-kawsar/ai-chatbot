import { useState } from "react";
import Header from "../components/chat/Header";
import ChatBox from "../components/chat/ChatBox";
import ChatInput from "../components/chat/ChatInput";

const Home = () => {
  const [messages, setMessages] = useState([]);

  const handleSendMessage = (text) => {
    const newMessage = {
      id: Date.now(),
      role: "user",
      content: text,
    };

    setMessages((prev) => [...prev, newMessage]);
  };

  return (
    <div className="flex min-h-screen flex-col bg-slate-950 text-white">
      <Header />

      <ChatBox messages={messages} />

      <ChatInput onSend={handleSendMessage} />
    </div>
  );
};

export default Home;