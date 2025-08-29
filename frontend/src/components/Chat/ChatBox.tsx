import { Card } from "../ui/card";

function ChatBox({ from, msg }: { from: string; msg: string }) {
    return (
  <Card className="p-2 my-2 rounded-md">
    <p className={`text-xl ${from === "LLM" ? "text-blue-500" : "text-green-500"}`}>
      {from}
    </p>
    <p>{msg}</p>
  </Card>
);

}

export default ChatBox;
