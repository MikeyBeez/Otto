import wikipedia
import os
import slugify

# Set the number of articles to download
num_articles = 10

# Get a list of random article titles
titles = []
for i in range(num_articles):
	title = wikipedia.random(pages=1)
	titles.append(title)
	print(f"Got title: {title}")

# Download and save each article as a text file
for i, title in enumerate(titles):
	try:
		page = wikipedia.page(title)
	except wikipedia.exceptions.PageError:
		print(f"Skipping non-existent title: {title}")
		continue
	filename = slugify.slugify(title) + ".txt"
	with open(filename, 'w') as f:
		f.write(page.content)
	print(f"Downloaded and saved: {title} -> {filename}")

print("Download complete!")
