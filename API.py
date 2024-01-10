#name = Clo_1
#key = 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

from openai import OpenAI

client = OpenAI(api_key='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')

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Comment fonctionne un laser ?"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")