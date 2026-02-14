#Todo 1 : Add Necessary Libaries

# Load .env if it exists (local development)
if os.path.exists(".env"):
    load_dotenv()

#Todo 2 : add avariable name PROMPT_TEMPLATE 

def get_client():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not found. Please set it as an environment variable in Cloud Run.")
    return genai.Client(api_key=api_key)

def run_agent(topic, word_limit):
    try:
        client = get_client()
        prompt = PROMPT_TEMPLATE.format(
            topic=topic,
            word_limit=word_limit
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text
    except Exception as e:
        print(f"Error in run_agent: {e}")
        raise e
