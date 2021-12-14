from django.db import connection


class SelectionsRepository:

    @staticmethod
    def create_selection(payload):
        query = """
            INSERT INTO selections (name, active, price, outcome, event_id) 
            VALUES (%s, %s, %s, %s, %s)
        """
        values = [
            payload['name'],
            (1 if payload['active'] else 0),
            payload['price'],
            payload['outcome'],
            payload['event_id']
        ]

        with connection.cursor() as cursor:
            cursor.execute(query, values)
            cursor.execute(
                'SELECT * FROM selections WHERE id = %s',
                [cursor.lastrowid]
            )

            row = cursor.fetchone()

        return row

    @staticmethod
    def update_selection(payload):
        query = []
        values = []

        for field, value in payload.items():
            if field != 'id' and value:
                query.append(f'{field} = %s')
                values.append(value)

        with connection.cursor() as cursor:
            if query:
                query = 'UPDATE selections SET ' + ', '.join(query)
                cursor.execute(query, values)

            cursor.execute(
                "SELECT * FROM selections WHERE id = %s",
                [payload['id']]
            )

            row = cursor.fetchone()

        return row

    @staticmethod
    def list_selections(filters):
        supported_filters = {
            'name_regex': {'expression': 'name REGEXP %s', 'value': filters.get('name_regex')},
            'is_active': {'expression': 'active = %s', 'value': 1 if filters.get('is_active') else 0}
        }

        query_filters = []
        filter_values = []
        query = 'SELECT * FROM selections '

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

            selections = cursor.fetchall()

        return selections

    @staticmethod
    def fetch_selection(pk):
        query = 'SELECT id FROM selections WHERE id = %s'

        with connection.cursor() as cursor:
            cursor.execute(
                query,
                [pk]
            )

            selection = cursor.fetchone()

        return selection
