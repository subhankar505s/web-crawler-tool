import requests
from bs4 import BeautifulSoup

try:
    url = "https://www.tryhackme.com"  # Any url You want to Craw
    r = requests.get(url)
    r.raise_for_status()  # Throw an Error message incase of invalid url
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("🆃🅸🆃🅻🅴 🅾🅵 🆃🅷🅴 🅿🅰🅶🅴​\n")
        f.write("\t\n")
        f.write(str(soup.title) + "\n")  # Get the title of HTML page
        f.write("\t\n")
        f.write("🅰🅻🅻 🆃🅷🅴 🅿🅰🆁🅰🅶🆁🅰🅿🅷🆂\n")
        f.write("\t\n")
        paras = soup.find_all('p')  # Get all the Paragraphs
        for para in paras:
            f.write(str(para) + "\n")
        f.write("\t\n")
        f.write("🅵🅸🆁🆂🆃 🅴🅻🅔🅼🅴🅽🆃 🅸🅽 🆃🅷🅴 🅷🆃🅼🅻 🅿🅰🅶🅴\n")
        f.write("\t\n")
        f.write(str(soup.find('p')) + "\n")  # Get the first Element in the html page
        f.write("\t\n")
        f.write("🅰🅻🅻 🆃🅷🅴 🆃🅴🆇🆃🆂 🅵🆁🅾🅼 🆃🅷🅴 🅿🅰🆁🅰🅶🆁🅰🅿🅷 🆃🅰🅶🆂 🅸🅽 🆃🅷🅴 🅷🆃🅼🅻 🆄🆁🅻\n")
        f.write("\t\n")
        f.write(soup.get_text() + "\n")  # Get All the Texts from The paragraph tags
        f.write("\t\n")
        f.write("🅰🅻🅻 🆃🅷🅴 🅰🅽🅻🅾🆁🆂 🆃🅰🅶🆂\n")
        f.write("\t\n")
        anchors = soup.find_all('a')  # Get all the Anchor tags
        for anchor in anchors:
            f.write(str(anchor) + "\n")
        f.write("\t\n")
        f.write("🅰🅻🅻 🆃🅷🅴 🅻🅸🅽🅺🆂 🅾🅵 🅰🅽🅻🅾🆁 🆃🅰🅶🆂\n")
        f.write("\t\n")
        all_links = set()
        for link in anchors:  # Get all the links from Anchor tags
            if (link.get('href') != '#'):  # Print only the clean links
                linkText = url + link.get('href')
                all_links.add(link)
                print(linkText)
                f.write(linkText+ '\n')
        f.write("\t\n")
        f.write("🅲🅾🅼🅿🅻🅴🆃🅴 🅷🆃🅼🅻 🅲🅾🅽🆃🅴🅽🆃 🅵🆁🅾🅼 🆃🅷🅴 🆄🆁🅻 🅴🅽🆃🅴🆁🅴🅳\n")
        f.write("\t\n")
        f.write("🅿🆁🅴🆃🆃🅸🅵🆈 🅵🅾🆁🅼 🅾🅵 🆃🅷🅴 🅷🆃🅼🅻 🅲🅾🅽🆃🅴🅽🆃\n")

except Exception as e:
    print(e)