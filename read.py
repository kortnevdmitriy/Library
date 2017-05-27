from  boto.dynamodb2.table import Table

books = Table('books')


def findRecord():
    records = books.get_item(isbn='978-1-60309-050-6', author_name="Simon Gardenfors")
    print(records['isbn'])
    print(records['author_name'])
