from django import dispatch

deactivate_event = dispatch.Signal(providing_args=['event_id'])
