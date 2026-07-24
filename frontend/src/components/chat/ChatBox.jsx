const ChatBox = () => {
  return (
    <main className="flex-1 overflow-y-auto">
      <div className="mx-auto flex h-full max-w-5xl items-center justify-center px-4">
        <div className="text-center">
          <div className="mb-6 text-6xl"></div>

          <h2 className="mb-2 text-3xl font-bold">
            Welcome to AI Chatbot
          </h2>

          <p className="text-slate-400">
            Ask anything to start a conversation.
          </p>
        </div>
      </div>
    </main>
  );
};

export default ChatBox;