#!/usr/bin/python3
"""
Module to list state from a database
"""

import sys
import MySQLdb

if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    data_base = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=data_base
    )

    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states
                   WHERE name LIKE BINARY 'N%'
                   ORDER BY id ASC;""")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # 6. Fermeture propre des ressources
    cursor.close()
    db.close()
