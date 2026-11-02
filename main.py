
import requests
from bs4 import BeautifulSoup

# Web Scraper for Headlines and Quotes

def scrape_headlines():
    print("\n--- LATEST TECH HEADLINES ---")

    url = "https://news.ycombinator.com/"

    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=15
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.select(".titleline > a")

        if not headlines:
            print("No headlines found.")
            return

        with open("headlines.txt", "w", encoding="utf-8") as file:
            for index, headline in enumerate(headlines[:20], start=1):
                title = headline.get_text(strip=True)
                link = headline.get("href", "")

                print(f"{index}. {title}")
                file.write(f"{index}. {title}\n")
                file.write(f"Link: {link}\n\n")

        print("\nHeadlines saved to headlines.txt")

    except requests.RequestException as error:
        print("Unable to fetch headlines:", error)


def scrape_quotes():
    print("\n--- FAMOUS QUOTES ---")

    url = "https://quotes.toscrape.com/"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.select(".quote")

        if not quotes:
            print("No quotes found.")
            return

        with open("quotes.txt", "w", encoding="utf-8") as file:
            for index, item in enumerate(quotes, start=1):
                quote = item.select_one(".text").get_text(strip=True)
                author = item.select_one(".author").get_text(strip=True)

                print(f"\n{index}. {quote}")
                print("Author:", author)

                file.write(f"{index}. {quote}\n")
                file.write(f"Author: {author}\n\n")

        print("\nQuotes saved to quotes.txt")

    except requests.RequestException as error:
        print("Unable to fetch quotes:", error)


def main():
    while True:
        print("\n================================")
        print(" WEB SCRAPER")
        print("================================")
        print("1. Scrape Tech Headlines")
        print("2. Scrape Famous Quotes")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            scrape_headlines()

        elif choice == "2":
            scrape_quotes()

        elif choice == "3":
            print("Thank you for using Web Scraper!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
