#organize a list of groceries

import ollama
import os

input_path = "./data/grocery.txt"
output_path = "./data/groceries-organized.txt"

if not os.path.exists(input_path):
  print("Input file does not exist")
  exit(1)

with open(input_path, "r") as f:
  groceries = f.read().strip()

PROMT = """
  Your name is Owend and you are the manager of a grocery store. You have a list of groceries that you need to organize.
  The list is as follows {groceries}
  Category them in sections of where you would see each in a gorcery store, also for each caterogy put an emoji and put them in alphabetical order and bullet pointed.  
"""

try: 
  response = ollama.generate(model="llama3.2:1b", prompt=PROMT)
  generated_text = response.get("response", "")

  with open(output_path, "w") as f:
    f.write(generated_text)

except Exception as e:
  print("An error occured", str(e))
  exit(1)