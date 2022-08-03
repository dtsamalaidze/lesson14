import sqlite3


class DB:
    def connect_db(self, query):
        with sqlite3.connect('db/netflix.db') as connection:
            result = []
            connection.row_factory = sqlite3.Row
            my_dict = connection.execute(query).fetchall()
            for item in my_dict:
                result.append(dict(item))
            return result



    def get_by_title(self, title, order='DESC'):
        query = f"""
            SELECT title, country, release_year, listed_in, description 
            FROM netflix 
            WHERE title 
            LIKE '%{title}%'
            ORDER BY release_year {order}
            LIMIT 1
            """
        return self.connect_db(query)

    def get_between_dates(self, start=0, end=9999, limit=100, offset=0):
        query = f"""
            SELECT title, release_year 
            FROM netflix 
            WHERE release_year 
            BETWEEN {start} and {end}
            LIMIT {limit} 
            OFFSET {offset}
            """
        return self.connect_db(query)

    def get_by_rating(self, rating):
        query = f"""
            SELECT title, rating, description 
            FROM netflix 
            WHERE rating IN {rating}
            """
        return self.connect_db(query)

    def get_by_genre(self, genre, order='DESC', limit=10, offset=0):
        query = f"""
            SELECT title, description 
            FROM netflix 
            WHERE listed_in
            LIKE '%{genre}%'
            ORDER BY release_year {order}
            LIMIT {limit} 
            OFFSET {offset}
            """
        return self.connect_db(query)

    def get_description(self, _type, release_year, ganre):
        query = f"""
            SELECT title, description, listed_in
            FROM netflix
            WHERE type
            LIKE '%{_type}%'
            AND release_year
            LIKE {release_year}
            AND listed_in
            LIKE '%{ganre}%'
            """
        return self.connect_db(query)

    def get_cast(self, actor_first, actor_second):
        query = f"""
            SELECT netflix.cast
            FROM netflix
            WHERE netflix.cast
            LIKE '%{actor_first}%'
            AND netflix.cast 
            LIKE '%{actor_second}%'
            """
        return self.connect_db(query)
