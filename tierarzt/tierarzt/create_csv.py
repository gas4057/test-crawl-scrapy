import csv
import os
from datetime import datetime


def makeCsv(items):
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
        writer.writerow(row)
