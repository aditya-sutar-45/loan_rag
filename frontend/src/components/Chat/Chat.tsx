import { useState } from "react";
import ChatContent from "./ChatContent";
import ChatInput from "./ChatInput";
import { type LLM_Response, type UserQuerey } from "@/utils/ai-response";

function Chat() {
  const [messages, setMessages] = useState<(LLM_Response | UserQuerey)[]>([]);

  const addMessage = (message: (LLM_Response | UserQuerey)) => {
    setMessages((prev) => [...prev, message]);
  }

  return (
    <>
      <div className="w-full h-[85%] bg-background rounded-md m-2 p-2">
        <ChatContent messages={messages} />
      </div>
      <div className="w-full h-[10%] my-2">
        <ChatInput addMessage={addMessage} />
      </div>
    </>
  );
}

export default Chat;
