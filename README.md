# Book Price Tracker

A Python script that scrapes the price of a book from
[Books to Scrape](https://books.toscrape.com), saves it to a CSV file once a day,
and sends an email alert when the price drops below a threshold.

## What it does

1. Fetches the product page with `requests`
2. Parses the title and price with `BeautifulSoup`
3. Appends `Title, Price, Date` to `BooksWebScrapper.csv`
4. Emails me if the price is below `THRESHOLD`
5. Waits 24 hours and repeats

## Setup

```bash
pip install -r requirements.txt
```

Set your Gmail address and a Gmail **App Password** as environment variables
(never write them in the code):

```bash
export EMAIL_ADDRESS="you@gmail.com"
export GMAIL_APP_PASSWORD="your16characterpassword"
```

To create an App Password, turn on 2-Step Verification in your Google account,
then generate one under Security > App passwords.

## Notes

- The https://books.toscrape.com is a practice site built for scraping.
- Change `URL` and `THRESHOLD` at the top of the script to track another book.

## Skills 

`requests`, `BeautifulSoup`, CSV handling, `smtplib`, environment variables,

