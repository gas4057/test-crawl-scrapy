import csv
import os
from datetime import datetime

from .items import TierarztItem


class TierarztPipeline:
    filename = 'ready.csv'
    fields = ['Name', 'Subtitle', 'Open Time',
              'Address', 'Score', 'Comments', 'Created_at']

    def open_spider(self, spider):
        self.file = open(self.filename, 'a', encoding='utf8', newline='')
        self.writer = csv.DictWriter(self.file, fieldnames=self.fields)

        if os.stat(self.filename).st_size == 0:
            self.writer.writerow({i: i for i in self.fields})
            print('File was created')

    def process_item(self, item, spider):
        if isinstance(item, TierarztItem):
            self.makeCsv(item)
        return item

    def close_spider(self, spider):
        self.file.close()

    def makeCsv(self, items):
        now = datetime.now()
        created_at = now.strftime("%Y-%m-%d %H:%M:%S")

        row = {
            'Name': items['name'],
            'Subtitle': items['subtitle'],
            'Open Time': items['open_time'],
            'Address': items['address'],
            'Score': items['score'],
            "Comments": items['comments'],
            "Created_at": created_at,
        }
        self.writer.writerow(row)
