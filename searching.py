# IMPORTS
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, KEYWORD

schema = Schema(name=TEXT(stored=True, phrase=False), content=TEXT(stored=True), keywords=KEYWORD)
idx = create_in("indexdir", schema)

writer = idx.writer()

products = [
    {
        "name": "Apple iPhone 12",
        "content": "This is a cool smartphone with 16 GB of RAM and 256 GB of internal storage.",
        "keywords": "smartphone,apple,iphone"
    },
    {
        "name": "Red T-Shirt by Roller",
        "content": "Obviously red t-shirt. Available in all sizes"
    },
    {
        "name": "Samsung Galaxy S20",
        "content": "This is one of its kind smartphone with 64 MP Camera."
    }
]

for product in products:
    writer.add_document(
        name=product["name"], 
        content=product["content"],
        keywords=product.get("keywords")
    )

writer.commit()

# Searching the index


def perform_search(query_string):
    from whoosh.qparser import QueryParser, FuzzyTermPlugin, MultifieldParser

    with idx.searcher() as searcher:
        qp = MultifieldParser(["name", "content"], idx.schema)
        qp.add_plugins([FuzzyTermPlugin()])
        if len(query_string) < 4:
            query = qp.parse(query_string)
        else:
            query = qp.parse(query_string + "~2/3")

        print(query)
        results = searcher.search(query)
        print([hit["name"] for hit in results])

        # Special treatment to keywords
        qp = QueryParser("keywords", schema)
        # qp.add_plugins([FuzzyTermPlugin()])
        query = qp.parse(query_string)
        special_results = searcher.search(query)
        print([hit for hit in special_results])

    

# perform_search("apple")
perform_search("smartphone")
