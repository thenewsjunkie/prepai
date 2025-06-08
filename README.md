# Prep AI

**Prep AI** is a self-hosted Docker web application that scrapes trending news stories daily, uses OpenAI to generate broadcast-ready summaries, and serves them via a printable web interface.

## 🔧 Features
- 📰 Automatically scrapes RSS news feeds and parses full article content
- 🤖 Uses OpenAI GPT-4 to create show-prep formatted summaries
- 📅 Runs every day at 6AM and also supports on-demand scraping
- 🌐 Web-based UI for browsing and printing stories
- 🖼 Custom Unraid Docker icon and full container support

## 📦 Setup
### 1. Clone the repository
```bash
git clone https://github.com/your-username/prep-ai.git
cd prep-ai
```

### 2. Add your OpenAI API key
Create a `.env` file or pass it as an environment variable:
```
OPENAI_API_KEY=sk-xxxxx
```

### 3. Build and run with Docker
```bash
docker build -t prep-ai .
docker run -d -p 5000:5000 \
  -e OPENAI_API_KEY=sk-xxxxx \
  -v $(pwd)/data:/app/data \
  prep-ai
```

### 4. Access the app
Visit: [http://localhost:5000](http://localhost:5000)

## 📁 Output
Summaries are stored in `data/prep_YYYY-MM-DD.json`. Each entry includes:
- Title
- Link
- Summary
- Talking Points
- Why Should You Care?
- Dispatch Question

## 🎯 Ideal For
- Radio show hosts
- Podcasters
- Content curators
- Media producers

---
Made with ❤️ by [Your Name or Org]
