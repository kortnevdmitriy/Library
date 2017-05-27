from boto.dynamodb2.fields import HashKey, RangeKey, GlobalAllIndex
from boto.dynamodb2.table import Table


# Creating a Table
def createTable():
    books = Table.create('books', schema=[HashKey('isbn'), RangeKey('author_name'), ],
                         throughput={'read': 5, 'write': 15}, global_indexes=[
            GlobalAllIndex('EverythingIndex', parts=[HashKey('book_type'), ], throughput={'read': 1, 'write': 1})])
    print("Table created successfully")
