# 🛰️ NASA News Scraper
This Python-based web scraper collects all news articles published on [nasa.gov](https://www.nasa.gov/news/recently-published/) starting from **March 1, 1952**, up to the date of execution.

---

## 📄 Data Fields Collected (CSV)
- **publication_date** – date of publication  
- **author** – author of the article  
- **title** – article title  
- **content** – full content of the article  
- **link_news** – direct link to the article  

---

```text
## 📁 Project Structure
nasa_scraper/
├── src/
│ └── scraper/
│ └── scraper.py
├── data/
│ ├── nasa_news.csv # Created automatically on script execution
│ └── urls_news.csv # Used internally for automation
├── README.md
└── requirements.txt
```

---

## ⚙️ Requirements
- Python 3.11

### Python Libraries
Install the required dependencies using:    
```bash
pip install -r requirements.txt
```
---

## 🚀 Running the Scraper
To run the scraper:
    python3.11 src/scraper/scraper.py

