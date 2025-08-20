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

## 📁 Project Structure
```text
nasa_scraper/
├── src/
│ └── scraper/
│ └── scraper.py
├── data/
│ ├── nasa_news.csv # Created automatically on script execution
│ └── urls_news.csv # Used internally for automation
└── requirements.txt
```

---

## Output Data(CSV):
```bash
publication_date,author,title,content,link_news                                                                                                                                                                                       
"Aug 07, 2025",Allison Tankersley,NASA’s Artemis II Crew Trains in Orion,"The Artemis II crew (from left to right) CSA (Canadian Space Agency) astronaut Jeremy Hansen, and NASA astronauts Christina Koch, Victor Glover, and Reid Wise       man don their Orion Crew Survival System Suits for a multi-day crew module training beginning July 31, 2025, at the agency’s Kennedy Space Center in Florida. Behind the crew, wearing clean room apparel, are members of the Artemis II        closeout crew. Testing included a suited crew test and crew equipment interface test, performing launch day and simulated orbital activities inside the Orion spacecraft. This series of tests marks the first time the crew entered th       eir spacecraft that will take them around the Moon and back to Earth while wearing their spacesuits. Image credit: NASA/Rad Sinyak",https://www.nasa.gov/image-article/nasas-artemis-ii-crew-trains-in-orion/
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
```bash
python3.11 src/scraper/scraper.py
```
