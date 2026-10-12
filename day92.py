# embeddings

import os
from google import genai
from dotenv import load_dotenv

# loading apikey

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


sentences = ["I love learning Python programming."]


# generating embadding
response = client.models.embed_content(
    model = "gemini-embedding-2",
    contents = sentences
)


for i, embadding in enumerate (response.embeddings):
    print("text ",sentences[i])
    print("vector size:",len(embadding.values))
    print()