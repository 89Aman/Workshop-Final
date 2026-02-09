from dotenv import load_dotenv
#todo-1: Import necessary libraries

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

#todo-2 :  create a variable name PROMPT_TEMPLATE and add prompt style

def run_agent(topic, word_limit):
    prompt = PROMPT_TEMPLATE.format(
        topic=topic,
        word_limit=word_limit
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text
