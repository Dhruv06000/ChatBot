from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation",
    device=0,
    model_kwargs={"dtype": "auto"},
    pipeline_kwargs=dict(
        max_new_tokens=256,
        do_sample=True,
        temperature=0.4,
        return_full_text=False,
    ),
)

model = ChatHuggingFace(llm=llm)

chat_template = ChatPromptTemplate([
  ("system",
 "You are {assistant_name}, a helpful AI assistant running locally on the "
 "Qwen2.5 model from Alibaba Cloud. Answer in a {style} way. "
 "Remember and use any facts the user tells you in this conversation, "
 "such as their name or where they live. "
 "If the user asks about themselves (for example their location, job or age) "
 "and they have not told you, reply exactly: \"You haven't told me that.\""),
  MessagesPlaceholder(variable_name="chat_history"),
  ("human","{query}")
]).partial(assistant_name="Sage",style="clear and friendly")

chat_history= []

while True:
  user_input=input("User: ").strip()
  if user_input.lower() in {"quit","exit"}:
    break
  if not user_input:
    continue

  prompt = chat_template.invoke({
    "chat_history":chat_history,
    "query": user_input
  })
  result = model.invoke(prompt)

  chat_history.append(HumanMessage(content=user_input))
  chat_history.append(AIMessage(content=result.content))
  print(f"AI : {result.content}")
for m in chat_history:
    print(f"{m.type}: {m.content}")