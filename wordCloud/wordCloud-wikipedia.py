import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


# Function to fetch text content from a Wikipedia page
def fetch_wikipedia_content(page_title):
  try:
    page = wikipedia.page(page_title)
    return page.content
  except wikipedia.exceptions.PageError:
    print("Page does not exist.")
    return None
  except wikipedia.exceptions.DisambiguationError:
    print("Page title is ambiguous.")
    return None


# Sample Wikipedia page title
page_title = "Cristiano Ronaldo"

# Fetch text content from the Wikipedia page
text = fetch_wikipedia_content(page_title)

if text:
  # Load the image mask
  mask = np.array(Image.open("sui.jpg"))

  # Generate word cloud
  wordcloud = WordCloud(mask=mask, background_color="white").generate(text)

  # Display the generated word cloud
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.show()
