import { Button } from "../ui/button";
import { Card } from "../ui/card";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";

function ChatBox({ from, msg, context }: { from: string; msg: string; context: string }) {
  return (
    <Card className="p-4 my-3 rounded-2xl shadow-md">
      {/* Sender */}
      <div className="w-full flex gap-2 justify-between align-middle">
        <p
          className={`text-sm mb-2 ${
            from === "LLM"
              ? "text-accent-foreground"
              : "text-secondary-foreground"
          }`}
        >
          {from}
        </p>
        {from === "LLM" ? (
          <Dialog>
            <DialogTrigger asChild>
              <Button variant="outline">Context</Button>
            </DialogTrigger>
            <DialogContent>
              <DialogHeader>
                <DialogTitle>Context</DialogTitle>
                <DialogDescription>{context}</DialogDescription>
              </DialogHeader>
            </DialogContent>
          </Dialog>
        ) : (
          <></>
        )}
      </div>

      <div
        className="prose prose-sm max-w-none
                   prose-h2:text-2xl prose-h2:font-semibold prose-h2:text-gray-800
                   prose-p:my-2 prose-p:text-gray-700
                   prose-ul:list-disc prose-ul:ml-6 prose-li:my-1
                   [&_table]:border [&_table]:border-gray-400 [&_table]:border-collapse
                   [&_th]:border [&_th]:border-gray-400 [&_th]:px-3 [&_th]:py-2
                   [&_td]:border [&_td]:border-gray-300 [&_td]:px-3 [&_td]:py-2"
        dangerouslySetInnerHTML={{ __html: msg }}
      />
    </Card>
  );
}

export default ChatBox;
