import random
import time

events_text = (
        {"event": 1, "text": "You stumble across an old statute to the gods. You kneel respectully. The gods reward "
            "you with a free card upgrade", "options": ("accept", "decline")},

    )


def decide_event(player, deck):
    event = random.choice(events_text)
    print(event)
    print(event["text"])
    time.sleep(0.5)
    for counter in range(len(event["options"])):
        print(f"{counter}) {event['options'][counter]}")





