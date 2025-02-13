import { useState } from "react";
import { TextField, Button, Box, Typography, CircularProgress } from "@mui/material";
import axios from "axios";

const Chatbox = () => {
    const [input, setInput] = useState("");
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const sendMessage = async () => {
        if (!input.trim()) return;

        const userMessage = { sender: "You", text: input };
        setMessages([...messages, userMessage]);
        setLoading(true);

        try {
            const response = await axios.post("http://127.0.0.1:8000/api/ask", { question: input }, {
                headers: { "Content-Type": "application/json" }
            });

            const aiMessage = { sender: "AI", text: response.data.response };
            setMessages([...messages, userMessage, aiMessage]);
        } catch (error) {
            setMessages([...messages, userMessage, { sender: "AI", text: "❌ Error fetching response" }]);
            console.error("Error fetching AI response:", error);
        } finally {
            setLoading(false);
        }

        setInput("");
    };

    return (
        <Box sx={{ maxWidth: 600, margin: "auto", textAlign: "center", padding: 3 }}>
            <Typography variant="h5">Chat with AI 🐶🐱</Typography>
            <Box sx={{ border: "1px solid #ccc", borderRadius: 2, padding: 2, minHeight: 300, overflowY: "auto" }}>
                {messages.map((msg, index) => (
                    <Typography key={index} sx={{ textAlign: msg.sender === "You" ? "right" : "left", margin: 1 }}>
                        <strong>{msg.sender}:</strong> {msg.text}
                    </Typography>
                ))}
                {loading && <CircularProgress size={20} />}
            </Box>
            <TextField
                fullWidth
                label="Ask something..."
                variant="outlined"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={(e) => e.key === "Enter" ? sendMessage() : null}
                sx={{ marginTop: 2 }}
            />
            <Button variant="contained" onClick={sendMessage} sx={{ marginTop: 2 }}>
                Send
            </Button>
        </Box>
    );
};

export default Chatbox;
