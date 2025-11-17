import os

from dotenv import load_dotenv
from datetime import datetime
from openai import OpenAI
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[0]
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_KEY")
TARGET_FILE = ROOT_DIR / "transcript" / "IELTS LISTENING PRACTICE TEST 2025 WITH ANSWERS | 16.11.2025 2025-11-17.txt"
MARKDOWN_PATH = ROOT_DIR / "markdown"
MARKDOWN_PATH.mkdir(parents=True, exist_ok=True)

MODEL = "gpt-5"
INSTRUCTIONS = """
        You are my English teacher.I'll give you a transcript and you should analyze the content and pick up all 
        collocations and explain the collocations and make example sentences relating to the collocations. 
        The definition of collocations can refer to Dictionary, OZDIC (https://ozdic.com/).
        The format of result should be suitable for Notion.
        """

def open_transcript(transcript):
    with open(file=TARGET_FILE, mode="r", encoding="utf-8") as f:
        transcript = f.read()
    return transcript

def create_collocations(ai, transcript):
    response = ai.responses.create(
        model=MODEL,
        instructions=INSTRUCTIONS,
        input=f"{transcript}",
    )
    result = response.output_text
    return result

def save_md(result, md_file):
    with open(file=md_file, mode="w", encoding="utf-8") as f:
        f.write(result)

def main():
    # get transcript
    transcript = open_transcript(TARGET_FILE)
    print(f"\nSuccessfully read file: {TARGET_FILE}")

    # connect to API
    client = OpenAI(api_key=OPENAI_API_KEY)

    print(f"\nStart analyze: {TARGET_FILE} to get collocations ...")
    print(f"\nChatGPT\nModel: {MODEL}\nInstructions: {INSTRUCTIONS}")

    # create collocations
    result = create_collocations(client, transcript)

    print("\nHas generated collocations!")
    print("Save to markdown ...")

    # save as MD file that can be uploaded to Notion
    markdown_file = MARKDOWN_PATH / f"IELTS_{datetime.today().date()}.md"
    save_md(result, markdown_file)

    print("All procedure has completed!")


if __name__ == "__main__":
    main()
