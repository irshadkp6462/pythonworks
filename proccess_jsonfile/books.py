from json import load

f=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\books.json")

data=load(f)

#for book in data:

# print(book)

all_titles=[book.get("title") for book in data]


page_filter=[book.get("title") for book in data if book.get("pages") < 250]


all_genres=[book.get("genre") for book in data ]

#print(all_genres)

genre_count={genre:all_genres.count(genre) for genre in all_genres}

#print(genre_count)

#print(set(page_filter))

costly_book=max(data,key=lambda d:d.get("price"))

#print(costly_book)

#author with more than one book

all_author=[book.get("author") for book in data ]

#print(all_author)

count_of_author={au:all_author.count(au) for au in all_author}

#print(count_of_author)

print([k for k,v in count_of_author.item() if v > 1 ])
