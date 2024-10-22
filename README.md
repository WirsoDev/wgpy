
# WordGen Project - README

## Overview

**WordGen** is a Python program that scrapes the text from a given website and counts word frequencies, ignoring common words like "the" or "and." It processes links within the same domain, following up to a specified number of URLs (default: 20). The most frequent words (default: 1000) are saved to a `.txt` file named after the domain of the website.

## Features

- Scrapes and counts word frequencies from the content of a website.
- Follows links to pages within the same domain (up to a specified limit).
- Ignores common English words based on a customizable list.
- Saves the most frequent words to a `.txt` file.
- Uses an iterative approach with a queue to manage links and prevent revisiting the same page.

## Requirements

The following libraries are required:

- `requests`
- `bs4` (BeautifulSoup)
- `art`

Install the required packages by running:

```bash
pip install -r requirements.txt
```

## How to Use

1. **Run the program:**

   Use the command below to start the program:

   ```bash
   python main.py
   ```

2. **Input:**

   You will be prompted to enter the URL of the website to scrape and optionally specify:
   
   - The **maximum number of words** to save (default: 1000).
   - The **maximum number of URLs** to visit (default: 20).

3. **Example interaction:**

   ```plaintext
   WGPY (ASCII art)
   
   Enter the URL of the website: https://example.com
   Enter the word limit (default 1000): 500
   Enter the url limit (default 20): 10
   ```

4. **Output:**

   The program will display the progress of the scraping and save the word counts in a `.txt` file. For example, scraping `https://example.com` will generate a file `example.com.txt` with the most common words and their frequencies.

## Files

- **`word_gen.py`**: Contains the `WordGen` class that handles the scraping and word counting logic.
- **`main.py`**: The main entry point of the program that interacts with the user.
- **`comon_words.py`**: A module that includes a list of common words to ignore during word counting.

## Configuration

- **Word limits**: You can adjust the maximum number of words saved by passing a different value for `max_words` in the `WordGen` class.
- **URL limits**: Modify the maximum number of URLs to visit by passing a different value for `max_urls` in the `WordGen` class.
- **Common words**: The list of ignored common words is defined in the `comon_words.py` module and can be customized.

## Example Output

For a website like `https://example.com`, the output in `example.com.txt` will look like:

```plaintext
example: 50
website: 40
page: 35
...
```

## License

This project is licensed under the MIT License.

---

Enjoy using WordGen!
