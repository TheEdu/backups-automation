import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import sys
sys.path.append('../')
from config import DATABASE_CONFIG

_con_url = ('{dialect}://{user}:{password}@{host}:{port}/{database}'
            .format(**DATABASE_CONFIG))

engine = create_engine(_con_url)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def _test(query_string):
    conn = engine.connect()
    query = conn.execute(query_string)
    print(_con_url)
    print(query.keys())
    for result in query.fetchall():
        print(result)
    conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--query',
                        help='query to execute and print the result',
                        type=str,
                        default="SELECT * FROM backups.hosts")
    args = parser.parse_args()
    _test(args.query)
