from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import os
import smtplib
from email.message import EmailMessage

URL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
FILE = "BooksWebScrapper.csv"
THRESHOLD = 60  # email me if the price drops below this (current price is £51.77)


def create_csv_if_missing():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="UTF8") as f:
            csv.writer(f).writerow(["Title", "Price", "Date"])


def check_price():
    page = requests.get(URL, timeout=10)
    page.raise_for_status()
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find("h1").get_text().strip()
    price = float(soup.find("p", class_="price_color").get_text().strip()[1:])
    today = datetime.date.today()

    with open(FILE, "a+", newline="", encoding="UTF8") as f:
        csv.writer(f).writerow([title, price, today])

    return title, price


def send_mail(title, price):
    sender = os.environ["EMAIL_ADDRESS"]

    msg = EmailMessage()
    msg["Subject"] = f"{title} is now £{price}! Now is your chance to buy!"
    msg["From"] = sender
    msg["To"] = sender
    msg.set_content(f"Your book '{title}' dropped to £{price}.\n{URL}")

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, os.environ["GMAIL_APP_PASSWORD"])
    server.send_message(msg)
    server.quit()


def main():
    create_csv_if_missing()
    while True:
        title, price = check_price()
        print(f"{datetime.date.today()}: {title} is £{price}")
        if price < THRESHOLD:
            send_mail(title, price)
        time.sleep(86400)  # check once every 24 hours


if __name__ == "__main__":
    main()
