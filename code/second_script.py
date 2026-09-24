# ==========================================================================
# SECOND SCRIPT
# ------------------------------
# This script is a progression from my first script. 
# It gets a url and parses 5 news sources from it.
# I like the format in which it gets printed in my terminal. 
# ==========================================================================




# ------------------------------
# MODULES
# ------------------------------
# Imports the feedparser module (which the script needs to work)
import feedparser


# ------------------------------
# URL
# ------------------------------
# BBC News Front Page
feed_url = "https://feeds.bbci.co.uk/news/rss.xml?edition=uk"



# ------------------------------
# PARSING THE RSS FEED
# ------------------------------
# Fetches and parses the RSS feed into a FeedParserDict object
newsfeed = feedparser.parse(feed_url)



# ------------------------------
# GETTING THE TITLE
# ------------------------------
# Extracts the channel/feed title
feed_title = newsfeed.feed.title
print(feed_title) # BBC News



# ------------------------------
# GETTING THE CONTENT KEYS
# ------------------------------
# Extracts the keys used for the content
content_keys = newsfeed.entries[0].keys()
print(content_keys)

# Output:
# -------
# 'title'
# 'title_detail'
# 'summary'
# 'summary_detail'
# 'links'
# 'link'
# 'id'
# 'guidislink'
# 'published'
# 'published_parsed'
# 'media_thumbnail'
# 'href'

# I can now use these keys to get the information that I want.



# ------------------------------
# GETS THE CONTENT
# ------------------------------
# Extracts the content
content = newsfeed.entries



# ------------------------------
# GETS THE FIRST ARTICLE
# ------------------------------
# Extracts the first article
first_article = content[0]

# Prints the first articles title
print(f"Title: {first_article.title}")
# Prints the first articles link
print(f"Link: {first_article.link}")
# Prints the first articles date
print(f"Date: {first_article.published}")

# OUTPUT
# ------
# Title: NHS trust to review 4,500 breast cancer cases after unnecessary surgeries found
# Link: https://www.bbc.co.uk/news/articles/ckddvje77m2zo?at_medium=RSS&at_campaign=rss
# Date: Thu, 24 Sep 2026 11:12:59 GMT



# ------------------------------
# GETS THE FIRST 5 ARTICLES
# ------------------------------
# Extracts the first 5 articles
for i, article in enumerate(content[:5], start=1):
    print(f"ARTICLE {i}")
    print("-" * 30)
    print(f"Title:\t{article.title}")
    print(f"Link:\t{article.link}")
    print(f"Date:\t{article.published}")
    print("\n\n")