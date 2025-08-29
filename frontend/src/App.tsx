import Chat from "./components/Chat/Chat";
import { ModeToggle } from "./components/mode-toggle";

function App() {
  return (
    <div className="h-dvh w-dvw flex justify-center flex-wrap">
      <div className="h-[6vh] w-4/5 m-2 bg-primary-foreground p-2 rounded-md">
        <ModeToggle />
      </div>
      <div className="h-[90vh] w-4/5 m-2 bg-primary-foreground p-2 rounded-md flex justfiy-center align-middle flex-wrap">
        <Chat />
      </div>
    </div>
  );
}

export default App
