import React, { useState, useEffect } from "react";
import axios from "axios";
import "./index.css"; // Make sure index.css is updated as well

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [darkMode, setDarkMode] = useState(false);

  const handlePredict = async (inputText) => {
    try {
      const res = await axios.post("http://localhost:8000/predict", { text: inputText });
      setResult(res.data);
    } catch (err) {
      alert("Error: " + err.message);
    }
  };

  const toggleTheme = () => setDarkMode(!darkMode);

  useEffect(() => {
    const delay = setTimeout(() => {
      if (text.trim().length > 3) {
        handlePredict(text);
      } else {
        setResult(null);
      }
    }, 500);

    return () => clearTimeout(delay);
  }, [text]);

  const getEmoji = (label) => {
    switch (label.toLowerCase()) {
      case "positive":
        return "😊";
      case "neutral":
        return "😐";
      case "negative":
        return "😠";
      default:
        return "";
    }
  };

  return (
    <div className={`container ${darkMode ? "dark-mode" : ""}`}>
      <div className="header">
        <h2>Sentiment Analyzer</h2>
        <button onClick={toggleTheme}>
          {darkMode ? "☀️ Light Mode" : "🌙 Dark Mode"}
        </button>
      </div>

      <textarea
        rows="5"
        placeholder="Type your sentence here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        style={{
          backgroundColor: darkMode ? "#1e1e1e" : "#fff",
          color: darkMode ? "#fff" : "#000",
        }}
      />

      <div className="result">
        {result ? (
          <>
            <strong>Label:</strong> {result.label} {getEmoji(result.label)} <br />
            <strong>Score:</strong> {result.score}
          </>
        ) : (
          text.trim().length <= 3 && (
            <em>Start typing to analyze sentiment...</em>
          )
        )}
      </div>
    </div>
  );
}

export default App;
