const Header = () => {
  return (
    <header className="border-b border-slate-800 bg-slate-900 px-6 py-4">
      <div className="mx-auto flex max-w-5xl items-center justify-between">
        <div>
          <h1 className="text-xl font-bold">
            AI Chatbot
          </h1>

          <p className="text-sm text-slate-400">
            Ask anything
          </p>
        </div>

        <div className="flex items-center gap-2">
          <span className="h-3 w-3 rounded-full bg-green-500"></span>

          <span className="text-sm text-slate-300">
            Online
          </span>
        </div>
      </div>
    </header>
  );
};

export default Header;