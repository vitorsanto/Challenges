from django.db import connection


class EventsRepository:

    @staticmethod
    def create_event(payload):
        query = """
            INSERT INTO events (name, slug, active, type, sport_id, status, scheduled_start) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = [
            payload['name'], payload['slug'],
            (1 if payload['active'] else 0),
            payload['type'], payload['sport_id'],
            payload['status'], payload['scheduled_start']
        ]

        with connection.cursor() as cursor:
            cursor.execute(query, values)
            cursor.execute('SELECT * FROM events WHERE id = %s', [cursor.lastrowid])

            row = cursor.fetchone()

        return row

    @staticmethod
    def update_event(payload):
        query = []
        values = []

        for field, value in payload.items():
            if field != 'id':
                query.append(f'{field} = %s')
                values.append(value)

        with connection.cursor() as cursor:
            if query:
                query = 'UPDATE events SET ' + ', '.join(query) + 'WHERE id = %s'
                values.append(payload['id'])
                cursor.execute(query, values)

            cursor.execute("SELECT * FROM events WHERE id = %s", [payload['id']])

            row = cursor.fetchone()

        return row

    @staticmethod
    def list_events(filters):
        query_filters = []
        filter_values = []
        supported_filters = {
            'name_regex': {'expression': 'name REGEXP %s', 'value': filters.get('name_regex')},
            'is_active': {'expression': 'active = %s', 'value': 1 if filters.get('is_active') else 0}
        }

        for _filter, value in filters.items():
            if _filter in supported_filters.keys() and len(str(value)):
                if len(query_filters) < 1:
                    query_filters.append(f'WHERE {supported_filters[_filter]["expression"]}')
                else:
                    query_filters.append(f'AND {supported_filters[_filter]["expression"]}')

                filter_values.append(supported_filters[_filter]['value'])

        with connection.cursor() as cursor:
            query = 'SELECT * FROM events '

            if query_filters:
                query += ' '.join(query_filters)

            cursor.execute(query, filter_values)
            events = cursor.fetchall()

        return events

    @staticmethod
    def check_event(pk):
        query = 'SELECT count(id) FROM events WHERE id = %s'

        with connection.cursor() as cursor:
            cursor.execute(query, [pk])
            event = cursor.fetchone()

        return event

    @staticmethod
    def events_active_from_sport(sport_id):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT count(id) FROM events WHERE sport_id = %s AND active = 1",
                [sport_id]
            )

            events_active = cursor.fetchone()

        return events_active[0]
