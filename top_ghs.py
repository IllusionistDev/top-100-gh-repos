import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://github.com/trending"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

repos = []
for repo in soup.find_all("article", class_="Box-row"):
    name = repo.h1.a.text.strip()
    stars = repo.find("a", class_="social-count").text.strip()
    link = "https://github.com" + repo.h1.a["href"]
    repos.append({"repo_name": name, "stars": stars, "link": link})

df = pd.DataFrame(repos)
df.to_csv("github_trending_repos.csv", index=False)
print("Scraping complete. Saved to github_trending_repos.csv")
