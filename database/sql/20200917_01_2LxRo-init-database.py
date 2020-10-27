"""
Init test table for first run
"""
from yoyo import step

__depends__ = {}


steps = [
    step("""
        create type event_type AS enum('address', 'person');
    """),
    step(
        """
        create table event (
            event_id serial primary key,
            created_at timestamp with time zone not null default now(),
            language varchar(255) not null,
            event_type event_type not null
        );
        """,
        """
            drop table event;
            drop type event_type;
        """
    )
]
