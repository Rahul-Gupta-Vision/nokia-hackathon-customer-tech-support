import React, { useState, useEffect, useRef } from "react";
import { Bot, Send } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { data } from "./customer-tech-team-login";

const ChatPage = () => {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "👋 Hello! How can I assist you today?" },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
  if (!input.trim()) return;

  const userMessage = input;
  setMessages((prev) => [...prev, { sender: "user", text: userMessage }]);
  setInput("");
  setLoading(true);

  try {
    const response = await fetch("http://localhost:8000/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: userMessage }), // ✅ backend expects 'question'
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();

    // ✅ Display model answer
    const botMessage = data.answer
      ? data.answer
      : "⚠️ No answer received from backend.";

    // ✅ Optionally include sources below the answer
    const sourcesText = data.sources?.length
      ? "\n\n📚 **Sources:**\n" +
        data.sources
          .map((src, i) => `(${i + 1}) ${src.source}: ${src.snippet.slice(0, 120)}...`)
          .join("\n")
      : "";

    setMessages((prev) => [
      ...prev,
      { sender: "bot", text: botMessage + sourcesText },
    ]);
  } catch (error) {
    console.error("Fetch error:", error);
    setMessages((prev) => [
      ...prev,
      { sender: "bot", text: "⚠️ Backend not reachable or invalid response." },
    ]);
  } finally {
    setLoading(false);
  }
};


  const isCodeLike = (text) => {
    const patterns = [
      "```",
      "<",
      ">",
      "{",
      "}",
      "int ",
      "void ",
      "def ",
      "class ",
    ];
    return patterns.some((p) => text.includes(p)) && text.includes("\n");
  };

  return (
    <div className="min-h-screen w-full flex flex-col items-center justify-center bg-gradient-to-br from-blue-900 via-blue-700 to-blue-500 p-0">
      <div className="h-[90vh] w-[90vw] bg-white/10 backdrop-blur-md rounded-2xl shadow-2xl flex flex-col overflow-hidden border border-white/20">
        {/* Header */}
        <header className="flex items-center gap-3 bg-white/10 px-6 py-4 border-b border-white/20 text-white">
          <Bot className="h-6 w-6 text-blue-200" />
          <h1 className="text-xl font-semibold tracking-wide">
            {data() == "LoginPageCustomerTech"
              ? "Customer Tech Support Assistant"
              : "Customer Support Assistant"}
          </h1>
        </header>

        {/* Chat Area */}
        <main className="flex-1 overflow-y-auto px-6 py-4 space-y-4 text-white">
          {messages.map((msg, i) => {
            const showAsCode = msg.sender === "bot" && isCodeLike(msg.text);
            const isUser = msg.sender === "user";

            return (
              <div
                key={i}
                className={`flex ${isUser ? "justify-end" : "justify-start"}`}
              >
                <div
                  className={`max-w-[75%] rounded-2xl px-4 py-3 ${
                    isUser
                      ? "bg-blue-500 text-white"
                      : "bg-white/20 text-blue-50 border border-white/10"
                  }`}
                >
                  {showAsCode ? (
                    <pre className="bg-black/30 p-3 rounded-md text-xs text-green-300 overflow-x-auto">
                      <code>{msg.text.replace(/```/g, "").trim()}</code>
                    </pre>
                  ) : (
                    msg.text
                  )}
                </div>
              </div>
            );
          })}
          {loading && (
            <div className="flex justify-start">
              <div className="bg-white/20 text-blue-50 border border-white/10 rounded-2xl px-4 py-3 flex items-center space-x-2">
                <div className="flex gap-1">
                  <span className="h-2 w-2 bg-blue-300 rounded-full animate-bounce [animation-delay:-0.3s]"></span>
                  <span className="h-2 w-2 bg-blue-300 rounded-full animate-bounce [animation-delay:-0.15s]"></span>
                  <span className="h-2 w-2 bg-blue-300 rounded-full animate-bounce"></span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </main>

        {/* Input Area */}
        <footer className="flex items-center gap-3 px-6 py-4 bg-white/10 border-t border-white/20">
          <Textarea
            id="message"
            placeholder=" Please enter your message ...."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            className="flex-1 bg-white/20 text-white placeholder:text-gray-300 border-none focus-visible:ring-blue-300"
            rows={2}
          />
          <Button
            onClick={handleSend}
            className="bg-blue-500 hover:bg-blue-600 text-white p-3 rounded-xl"
          >
            <Send className="h-5 w-5" />
          </Button>
        </footer>
      </div>
    </div>
  );
};

export default ChatPage;
