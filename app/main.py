from app.scraper import get_stories
from app.processor import summarize_stories
from app.ui import create_app

import os
import threading
import time
from apscheduler.schedulers.background import BackgroundScheduler

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SCRAPE_SOURCES_FILE = os.getenv("SCRAPE_SOURCES_FILE", "sources.json")
EXPORT_DIR = os.getenv("EXPORT_DIR", "data")
STATIC_DIR = os.getenv("STATIC_DIR", "static")

scheduler = BackgroundScheduler()

def run_daily_scrape():
    print("[INFO] Starting scheduled scrape...")
    stories = get_stories(SCRAPE_SOURCES_FILE)
    if stories:
        summarize_stories(stories, OPENAI_API_KEY, EXPORT_DIR)
    else:
        print("[WARN] No stories found.")

scheduler.add_job(run_daily_scrape, "cron", hour=6, minute=0)
scheduler.start()

app = create_app(run_daily_scrape, export_dir=EXPORT_DIR, static_dir=STATIC_DIR)

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=5000, debug=False)).start()
    while True:
        time.sleep(60)
