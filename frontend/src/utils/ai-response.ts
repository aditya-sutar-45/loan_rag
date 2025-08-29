export interface UserQuerey {
  sender: "User";
  question: string;
}

export interface LLM_Response {
  sender: string;
  question: string;
  answer: string;
  context: string;
}
