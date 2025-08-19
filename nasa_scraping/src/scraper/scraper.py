import csv
import sys
import json
import time
import random

import asyncio
import aiohttp
import fake_useragent
from bs4 import BeautifulSoup


async def param(link, is_json=False, session=None):
    ua = fake_useragent.UserAgent().random
    headers = {
        "user-agent": ua,
    }
    if session is None:
        async with aiohttp.ClientSession(headers=headers) as new_session:
            return await _fetch(new_session, link, is_json)
    else:
        return await _fetch(session, link, is_json)


async def _fetch(session, link, is_json):
    async with session.get(link) as response:
        r = await response.text()
        if is_json:
            html = json.loads(r)
            soup = BeautifulSoup(html["html"], "lxml")
        else:
            soup = BeautifulSoup(r, "lxml")
        return soup


async def get_page(session):
    soup = await param("https://www.nasa.gov/news/recently-published/", session=session)
    page_num = soup.find_all("a", class_="page-numbers")[-2].find("span").text.strip()
    return int(page_num)


async def get_urls():
    urls = []
    try:
        with open("../../data/urls_news.csv") as file:
            urls_csv = csv.DictReader(file)
            for url in urls_csv:
                urls.append(url["url"])
    except FileNotFoundError:
        with open("../../data/urls_news.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow((
                "page",
                "url"
            ))

    async with aiohttp.ClientSession() as session:
        page_num = await get_page(session)
        for page in range(1, page_num + 1):
            if page > 0 and page % 1000 == 0:
                print("A little pause")
                time.sleep(60)
            soup = await param(
                f"https://www.nasa.gov/wp-json/nasa-hds/v1/content-lists?postType=post%2Cnasa-blog%2Cfeature%2Cpress-release%2Cimage-article%2Cpodcast&postId=383829&maxPages={page_num}&perPage=25&categories=&newsTags=&layout=list&showThumbnails=yes&showReadTime=yes&showExcerpts=yes&showContentTypeTags=yes&pageClicked={page}",
                is_json=True,
                session=session
            )
            href = soup.find_all("div", class_="hds-content-item-inner")
            print(page, "/", page_num)
            for link in href:
                links = link.find("a", class_="hds-content-item-heading", href=True)["href"]
                if links not in urls:
                    urls.append(links)
                    with open("../../data/urls_news.csv", "a") as file:
                        writer = csv.writer(file)
                        writer.writerow((page, links))
                else:
                    return urls
    return urls


async def scraper():
    csv.field_size_limit(sys.maxsize)
    urls = await get_urls()
    url_news = []
    try:
        with open("../../data/nasa_news.csv") as file:
            urls_csv = csv.DictReader(file)
            for url in urls_csv:
                url_news.append(url["link_news"])
    except FileNotFoundError:
        with open("../../data/nasa_news.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow((
                "publication_date",
                "author",
                "title",
                "content",
                "link_news"
            ))
    urls_news = []
    for url in urls:
        if not url in url_news:
            urls_news.append(url)
    progress = 0
    async with aiohttp.ClientSession() as session:
        for news in urls_news:
            if progress > 0 and progress % 4000 == 0:
                print("A little pause")
                time.sleep(30)
            try:
                soup = await param(news, session=session)
            except aiohttp.client_exceptions.ClientConnectorCertificateError as e:
                print("Skip:", news)
                continue    
            link_news = news
            try:
                publication_date = soup.find("span", class_=["heading-12", "text-uppercase"]).text.strip()
            except:
                try:
                    publication_date = soup.find("time").text.strip()
                except:
                    try:
                        publication_date = soup.find("span", class_="hds-podcast-date").text.strip()
                    except:
                        publication_date = "None"
            try:
                author = soup.find("h3", class_=["hds-meta-heading", "heading-14"]).text.strip()
            except:
                try:
                    author = soup.find("p", class_="author-name").text.strip()
                except:
                    author = "None"

            try:
                title = soup.find("h1").text.strip()
            except:
                title = "None"

            try:
                content_list = soup.find("div", class_="entry-content").find_all("p")
            except:
                try:
                    content_list = soup.find_all("p")
                except:
                    content_list = []

            content = ""
            for cont in content_list:
                content = content + " " + cont.text.strip()

            with open("../../data/nasa_news.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow((
                    publication_date,
                    author,
                    title,
                    content[1:],
                    link_news
                ))
            progress += 1
            print(progress, "/", len(urls_news))


def main():
    asyncio.run(scraper())

if __name__ == "__main__":
    main()

