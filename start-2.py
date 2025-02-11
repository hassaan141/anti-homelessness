import ollama

response = ollama.list()

# print(response)

#For chat you pass in the model and messages, and stream
#It hits the API and returns the response
res = ollama.chat(
  model="llama3.2:1b",
  messages=[
    {"role": "user", "content": "How old is the universe?"},
  ],
  stream=True
)

# print(res["message"][0]["content"])
# print(res["message"]["content"])

# for word in res:
#   print(word["message"]["content"], end="", flush=True)

#################################################################################

#Can also create a model file in our code
# pirate_modelfile = """
# FROM llama3.2:1b
# SYSTEM You are jake, who talkes like a mad robot scientest, who speaks like a pirate.
# PARAMETER temperature=0.1
# """

# ollama.create(
#   model="franky",
#   model_file=pirate_modelfile
# )

res = ollama.generate(
  model="llama3.2:1b",
  prompt="Give me a list of 50 things random items in a grocery store, and give me each on a new line",
)

print(res["response"])