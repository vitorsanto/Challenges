from django import dispatch

deactivate_sport = dispatch.Signal(providing_args=['sport_id'])
