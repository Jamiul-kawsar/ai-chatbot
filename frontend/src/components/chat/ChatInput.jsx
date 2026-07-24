import { useState } from "react";

const ChatInput = ({ onSend }) => {
  const [input, setInput] = useState("");

  const handleSend = () => {
    const message = input.trim();

    if (!message) return;

    onSend(message);

    setInput("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="border-t border-slate-800 bg-slate-900 p-4">
      <div className="mx-auto flex max-w-5xl gap-3">
        <input
          type="text"
          placeholder="Type your message..."
          className="flex-1 rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none focus:border-blue-500"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
        />

        <button
          onClick={handleSend}
          disabled={!input.trim()}
          className="rounded-lg bg-blue-600 px-6 py-3 font-medium transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatInput;