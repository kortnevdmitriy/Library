from boto.dynamodb2.table import Table

books = Table('books')


def createNewItem():
    books.put_item(data={
        'isbn': '978-1-60309-050-6',
        'author_name': 'Simon Gardenfors',
        'price': '$14.95',
        'book_type': 'Mature (18+)'
    })
