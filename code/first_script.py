# ==========================================================================
# FIRST SCRIPT
# ------------------------------
# This is a basic script which gets a url and parses a news source from it.
# I created this so I can see how feedparser works in a fundamental way. 
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
url = "https://feeds.bbci.co.uk/news/rss.xml?edition=uk"



# ------------------------------
# PARSING THE RSS FEED
# ------------------------------

# Fetches and parses the RSS feed into a FeedParserDict object
newsfeed = feedparser.parse(url)

# Extracts the most recent article (first item in the feed)
entry = newsfeed.entries[0]



# ------------------------------
# GETTING THE KEYS
# ------------------------------
# This code gives me the keys that exist:
print(entry.keys())

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
# GETTING STUFF
# ------------------------------
# prints the title
print(f"Post Title: {entry.title}")
# prints the summary
print(f"Post Summary: {entry.summary}")