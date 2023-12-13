import openai

# Configurez votre clé API OpenAI GPT
openai.api_key = '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'

# Utilisez la fonction openai.Completion.create pour générer une réponse de ChatGPT
response = openai.Completion.create(
  engine="text-davinci-003",  # ou "text-codex-002" pour le modèle Codex
  prompt="Tu adores gpt4 ou pas ?",
  max_tokens=20 # Limitez le nombre de jetons dans la réponse
)

# Affichez la réponse générée par ChatGPT
print(response['choices'][0]['text'])
