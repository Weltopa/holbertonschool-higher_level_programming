#!/usr/bin/python3
"""List all states from database"""

if __name__ == "__main__":

    import MySQLdb
    import sys
    con = MySQLdb.connect(host="localhost", port=3306,
                          user=sys.argv[1], passwd=sys.argv[2],
                          db=sys.argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    con.close()
