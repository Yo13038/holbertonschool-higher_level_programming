#!/usr/bin/python3
"""
Lists all cities of a specific state provided as an argument,
from the database hbtn_0e_4_usa. Safe from SQL injection.
"""
import sys
import MySQLdb

if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    data_base = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=data_base
    )

    cursor = db.cursor()

    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;"
    )

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    
    cities = [row[1] for row in rows]

    print(", ".join(cities))

    cursor.close()
    db.close()