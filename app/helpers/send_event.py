from app.db import database
from app.models.db.event import events


async def send_event(event_type, language):
    query = events.insert().values(
        event_type=event_type,
        language=language
    )
    return await database.execute(query=query)
