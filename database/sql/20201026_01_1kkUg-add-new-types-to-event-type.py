"""
Add new types to event_type
"""
from yoyo import step

__depends__ = {'20200917_01_2LxRo-init-database'}

steps = [
    step("""
        ALTER TYPE "event_type" ADD VALUE IF NOT EXISTS 'random_sentence';
        ALTER TYPE "event_type" ADD VALUE IF NOT EXISTS 'random_sentences';
        ALTER TYPE "event_type" ADD VALUE IF NOT EXISTS 'sentence_limits';
        ALTER TYPE "event_type" ADD VALUE IF NOT EXISTS 'lorem_limits';
        ALTER TYPE "event_type" ADD VALUE IF NOT EXISTS 'lorem_bytes';
        ALTER TYPE "event_type" ADD VALUE IF NOT EXISTS 'lorem_words';
        ALTER TYPE "event_type" ADD VALUE IF NOT EXISTS 'lorem_paragraphs';
        ALTER TYPE "event_type" ADD VALUE IF NOT EXISTS 'lorem_paragraphs_break';
        ALTER TYPE "event_type" ADD VALUE IF NOT EXISTS 'lorem_lists';
        """)
]
