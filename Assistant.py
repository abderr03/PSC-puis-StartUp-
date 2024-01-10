import openai 
import time

# gets API Key from environment variable OPENAI_API_KEY
client = openai.OpenAI(api_key='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')

assistant = client.beta.assistants.create(
    name="Game assistant",
    instructions="You're an agent of a game and I'll give you the context of the current scene and an order. \
    What you should do is to return a succession of instructions among the given possible ones, the most relevant ones to perform and to respond. \
Context : \
You are in a house. There are a kitchen, a bedroom, a toilet and a living room. \
    In the kitchen, you can eat, drink and cook. In the bedroom you can sleep or take a nap. In the toilet, you can take a bath. In the living room, there is a TV, a sofa and some books. \
\
Actions (only respond with one or several of these actions, and no extra text nor reaction): \
GOTO {place} : to go to the specified room if a move is needed and if the object exists. \
GRAB{object} : you have to be already in the room where the object is to be able to grab it. \
DO{action}: you have to be already in the room where you want to do you action to be able to do it. \
IDLE : otherwise (when none of the above actions are appropriate or when the order does not make sense)",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo",
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I am sleepy",
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="You are in the bedroom",
)


while True:
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    if run.status == "completed":
        messages = client.beta.threads.messages.list(thread_id=thread.id)

        for message in messages:
            assert message.content[0].type == "text"
            print(message.content[0].text.value)
        
        message = messages[0]
        print(message.content[0].text.value)
        #client.beta.assistants.delete(assistant.id)

        break
    else:
        time.sleep(5)

