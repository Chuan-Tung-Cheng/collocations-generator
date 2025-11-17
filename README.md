# YouTube Transcript & Collocation Generator

This project contains two Python scripts:

1. **Transcript Fetcher** – Downloads YouTube video transcripts and saves them as `.txt` files.
2. **Collocation Generator** – Sends the transcript to OpenAI's API and generates a list of collocations formatted for Notion.

---

## Features

### 1. Transcript Fetcher

* Fetches YouTube transcripts using `youtube_transcript_api`.
* Retrieves the YouTube video title automatically.
* Saves the transcript in a local folder with a timestamp.
* Output format is plain text.

**Note:** `youtube_transcript_api` is a third-party Python library, not an official YouTube API. It only retrieves publicly available subtitles (CC) and does not require an API key. It cannot access videos without subtitles, and its functionality may be affected by changes in YouTube's site structure.

### 2. Collocation Generator

* Reads a transcript file.
* Sends the content to OpenAI (GPT-5) with predefined instructions.
* Extracts and explains collocations.
* Saves the result as a Markdown file that can be uploaded directly to Notion.

---

## Folder Structure

```
your_project/
├── transcript/         # All transcript .txt files
├── Markdown/           # AI-generated collocation .md output
├── main_transcript.py  # Script for downloading transcripts
├── collocation_ai.py   # Script for generating collocations
└── README.md
```

---

## How to Use

### 0. Clone the Repository

```
git clone <repository_url>
cd <repository_folder>
```

### 1. Install Dependencies

Using Poetry, install all dependencies listed in `pyproject.toml`:

```
poetry install
```

To add a new package manually:

```
poetry add youtube-transcript-api requests beautifulsoup4 lxml python-dotenv openai
```

### 2. Prepare Environment Variables

Create a `.env` file:

```
OPENAI_KEY=your_api_key_here
```

### 3. Run Transcript Fetcher

```
python main_transcript.py <YOUTUBE_VIDEO_ID>
```

Example:

```
python main_transcript.py RwIspUe78Bg
```

### 4. Run Collocation Generator

```
python collocation_ai.py
```

The script will:

* Read the newest transcript.
* Generate collocations.
* Save the Markdown output in `/Markdown`.

---

## Notes

* You must have access to GPT-5 API (or adjust the model name).
* Make sure transcript file names do not contain characters illegal in file systems.

---

## License

MIT
