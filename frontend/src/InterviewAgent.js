import React, { useState, useRef, useEffect } from "react";
import axios from "axios";

function InterviewAgent() {
  const [authenticated, setAuthenticated] = useState(false);
  const [userId, setUserId] = useState("");
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const chatContainerRef = useRef(null);
  const [error, setError] = useState("");

  const authenticateUser = async () => {
    try {
      const res = await axios.post("http://localhost:8000/authenticate", {
        user_id: userId,
      });
      if (res.data.authenticated) {
        setAuthenticated(true);
        setError("");
      } else {
        setError("Invalid ID. Please try again.");
      }
    } catch (err) {
      setError("Server error. Please try again.");
    }
  };

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages(prev => [...prev, userMessage]);
    setInput("");

    try {
      const res = await axios.post("http://localhost:8000/chat", { message: input });
      const botMessage = { sender: "bot", text: res.data.response };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = { sender: "bot", text: "Error getting response from the agent." };
      setMessages(prev => [...prev, errorMessage]);
    }
  };

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }
  }, [messages]);

  // Authentication form (shown if not yet authenticated)
  if (!authenticated) {
    return (
      <div style={{ padding: "2rem", maxWidth: 500, margin: "auto" }}>
        <h2>Enter your ID to start the interview</h2>
        <input
          type="text"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          placeholder="Enter your ID"
          style={{ width: "80%", padding: "0.5rem", marginRight: "0.5rem" }}
        />
        <button onClick={authenticateUser} style={{ padding: "0.5rem 1rem" }}>Submit</button>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </div>
    );
  }

  // Chat UI after successful authentication
  return (
    <div style={{ padding: "2rem", maxWidth: 600, margin: "auto" }}>
      <h2>Interview Chat</h2>
      <div
        ref={chatContainerRef}
        style={{
          maxHeight: 400,
          overflowY: "auto",
          border: "1px solid #ccc",
          padding: "1rem",
          borderRadius: "8px",
          marginBottom: "1rem"
        }}
      >
        {messages.map((msg, i) => (
          <div key={i} style={{ textAlign: msg.sender === "user" ? "right" : "left", margin: "0.5rem 0" }}>
            <strong>{msg.sender === "user" ? "You" : "Agent"}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === 'Enter' && sendMessage()}
        style={{ width: "80%", padding: "0.5rem", marginRight: "0.5rem" }}
        placeholder="Type your answer..."
      />
      <button onClick={sendMessage} style={{ padding: "0.5rem 1rem" }}>Send</button>
    </div>
  );
}

export default InterviewAgent;
