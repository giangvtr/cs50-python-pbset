import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s): #s is a HTML
    matches = re.search(r'^.+src=\"https?://(?:www\.)?youtube\.com/embed/(.+)\".+$', s, re.IGNORECASE)
    if matches:
        short_url = f"https://youtu.be/{matches.group(1)}"
        return short_url
    else:
        return None

if __name__ == "__main__":
    main()
