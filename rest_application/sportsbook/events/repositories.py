from django.db import connection


class EventsRepository:

    @staticmethod
    def create_event(payload):
        query = """
            INSERT INTO events (name, slug, active, type, sport_id, status, scheduled_start) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = [
            payload['name'], payload['slug'], (1 if payload['active'] else 0), payload['type'], payload['sport'],
            payload['status'], payload['scheduled_start']
        ]

        with connection.cursor() as cursor:
            cursor.execute(query, values)
            cursor.execute(
                'SELECT * FROM events WHERE id = %s',
                [cursor.lastrowid]
            )

            row = cursor.fetchone()

        return row

    @staticmethod
    def update_event(payload):
        query = []
        values = []

        for field, value in payload.items():
            if field != 'id' and value:
                query.append(f'{field} = %s')
                values.append(value)

        with connection.cursor() as cursor:
            if query:
                query = 'UPDATE events SET ' + ', '.join(query)
                cursor.execute(query, values)

            cursor.execute(
                "SELECT * FROM events WHERE id = %s",
                [payload['id']]
            )

            row = cursor.fetchone()

        return row

    @staticmethod
    def list_events(filters):
        supported_filters = {
            'name_regex': {'expression': 'name REGEXP %s', 'value': filters.get('name_regex')},
            'is_active': {'expression': 'active = %s', 'value': 1 if filters.get('is_active') else 0}
        }

        query_filters = []
        filter_values = []
        query = 'SELECT * FROM events '

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

            events = cursor.fetchall()

        return events

    @staticmethod
    def fetch_event(pk):
        query = 'SELECT id FROM events WHERE id = %s'

        with connection.cursor() as cursor:
            cursor.execute(
                query,
                [pk]
            )

            event = cursor.fetchone()

        return event
