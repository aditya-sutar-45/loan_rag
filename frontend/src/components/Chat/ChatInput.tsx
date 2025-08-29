import { Send } from "lucide-react";
import { Button } from "../ui/button";
import { Textarea } from "../ui/textarea";
import { useState } from "react";
import axios from "axios";
import type { LLM_Response, UserQuerey } from "@/utils/ai-response";

const api = axios.create({
  baseURL: "http://localhost:5000/",
});

interface AddMessageProp {
  addMessage: (message: LLM_Response | UserQuerey) => void;
}

function ChatInput({ addMessage }: AddMessageProp) {
  const [question, setQuestion] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = () => {
    setIsLoading(true);
    addMessage({
      sender: "User",
      question: question,
    });
    setQuestion("");
    api
      .post("/ask", {
        question: question,
      })
      .then((res) => {
        addMessage({
          sender: "LLM",
          question: res.data.question,
          answer: res.data.answer,
          context: res.data.context,
        });
        setIsLoading(false);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="w-full h-full flex justify-center align-middle">
      <Textarea
        className="mx-1 h-full"
        placeholder="Enter your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <Button
        className="h-full w-[5%] mx-1 cursor-pointer"
        onClick={handleSubmit}
        disabled={isLoading}
      >
        <Send />
      </Button>
    </div>
  );
}

export default ChatInput;
