from django.db import connection


class SportsRepository:

    @staticmethod
    def create_sport(payload):
        query = 'INSERT INTO sports (name, slug, active) VALUES (%s, %s, %s)'
        values = [payload['name'], payload['slug'], (1 if payload['active'] else 0)]

        with connection.cursor() as cursor:
            cursor.execute(query, values)
            cursor.execute('SELECT id, name, slug, active FROM sports WHERE id = %s', [cursor.lastrowid])
            row = cursor.fetchone()

        return row

    @staticmethod
    def update_sport(payload):
        query = []
        values = []

        for field, value in payload.items():
            if field != 'id' and value:
                query.append(f'{field} = %s')
                values.append(value)

        with connection.cursor() as cursor:
            if query:
                query = 'UPDATE sports SET ' + ', '.join(query)
                cursor.execute(query, values)

            cursor.execute("SELECT id, name, slug, active FROM sports WHERE id = %s", [payload['id']])

            row = cursor.fetchone()

        return row

    @staticmethod
    def list_sports(filters):
        supported_filters = {
            'name_regex': {'expression': 'name REGEXP %s', 'value': filters.get('name_regex')},
            'is_active': {'expression': 'active = %s', 'value': 1 if filters.get('is_active') else 0}
        }

        query_filters = []
        filter_values = []
        query = 'SELECT * FROM sports '

        for _filter, value in filters.items():
            if _filter in supported_filters.keys() and value:

                if len(query_filters) < 1:
                    query_filters.append(f'WHERE {supported_filters[_filter]["expression"]}')
                else:
                    query_filters.append(f'AND {supported_filters[_filter]["expression"]}')

                filter_values.append(supported_filters[_filter]['value'])

        with connection.cursor() as cursor:
            if query_filters:
                query = query + ' '.join(query_filters)

            cursor.execute(
                query,
                filter_values
            )

            sports = cursor.fetchall()

        return sports

    @staticmethod
    def check_sport(pk):
        query = 'SELECT id FROM sports WHERE id = %s'

        with connection.cursor() as cursor:
            cursor.execute(
                query,
                [pk]
            )

            sport = cursor.fetchone()

        return sport
