# Billboard Songs Scraper
Background:<br>Instead of having to copy and paste the Billboard Hot 100 songs(I only cared about top 15 though) in Youtube, I thought about automating the task,which led to the creation of this project.<br>

Working:<br>This program will load Billboard Hot 100 songs in a chronological order. Once a song is finished playing, next song will be loaded in a new tab.

Installation:<br>
Install urllib3, beautifulSoup, and requests<br>

Running:<br>
python scraping.py<br>

Further development:<br>
1)Currently, when the next song is loaded in a new tab, it will not close the previous tab. My initial search says that it can be done using Selenium.<br>
2)The current code can be more efficient. For instance, the two for loops can be one.
