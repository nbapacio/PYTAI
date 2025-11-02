import os
from openai import OpenAI

# Initialize the client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if not client.api_key:
    print("Please set the OPENAI_API_KEY environment variable.")
    exit(1)

def main():
    print("OpenAI Assistant")
    print("How can I help you today?\n")
    while True:
        user_input = input("Your question (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            break

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if you have access
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,
                temperature=0.7,
            )

            answer = response.choices[0].message.content.strip()
            print("\nAssistant: " + answer + "\n")
        except Exception as e:
            print(f"An error occurred: {e}")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

### How to use this script:
# 1. Save it as, for example, `openai_chatbot.py`.
# 2. Set your OpenAI API key as an environment variable:
#   - On Linux or macOS:
#     ```bash
#     export OPENAI_API_KEY='your-api-key-here'
#     ```
#   - On Windows Command Prompt:
#     ```cmd
#     set OPENAI_API_KEY=your-api-key-here
#     ```
# 3. Install the OpenAI library if you haven not already:
#   ```bash
#   pip install openai
#   ```
# 4. Run the script:
#   ```bash
#   python openai_chatbot.py
#   ```
#END  
