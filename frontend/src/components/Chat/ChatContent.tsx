import type { LLM_Response, UserQuerey } from "@/utils/ai-response";
import ChatBox from "./ChatBox";

function ChatContent({
  messages,
}: {
  messages: (LLM_Response | UserQuerey)[];
}) {
  return (
    <div className="h-full w-full overflow-scroll">
      {messages.map((msg, i) => (
        <ChatBox
          key={i}
          from={msg.sender}
          msg={
            msg.sender === "User"
              ? (msg as UserQuerey).question
              : (msg as LLM_Response).answer
          }
        />
      ))}
    </div>
  );
}

export default ChatContent;
