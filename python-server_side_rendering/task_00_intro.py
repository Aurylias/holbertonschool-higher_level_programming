"""Templating program to create invitation files."""
import logging
import os

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def generate_invitations(template: str, attendees: list[dict]) -> None:
    """Generate one invitaion file per delegate from a template.

    Placeholders like {name} are replaced by the delegate's value;
    missing or None values become 'N/A'. Files are named output_X.txt,
    X starting at 1. Existing files are not overwritten.
    """
    if not isinstance(template, str):
        log.error('Template must be a string, got %s.',
                  {type(template).__name__})
        return
    if not isinstance(attendees, list) or not all(
           isinstance(delegate, dict) for delegate in attendees):
        log.error('Attendees must be a list of dictionaries, got %s.',
                  {type(attendees).__name__})
        return
    if not template:
        log.error('Template is empty, no output files generated.')
        return
    if not attendees:
        log.error('No data provided, no output files generated.')
        return

    placeholder = ['name', 'event_title', 'event_date', 'event_location']

    for i, delegate in enumerate(attendees, start=1):
        newTemplate = template
        for key in placeholder:
            value = delegate.get(key)
            newTemplate = newTemplate.replace(
                f'{{{key}}}', "N/A" if value is None else str(value))

        filename = f'output_{i}.txt'
        if not (os.path.exists(filename)):
            with open(filename, 'w') as outputFile:
                outputFile.write(newTemplate)
        else:
            log.error(f'{filename} already exists.')


if __name__ == '__main__':
    try:
        with open('template.txt') as file:
            template_content = file.read()
    except FileNotFoundError:
        log.error('template.txt does not exists.')
    else:
        attendees = [
            {"name": "Alice", "event_title": "Python Conference",
             "event_date": "2023-07-15", "event_location": "New York"},
            {"name": "Bob", "event_title": "Data Science Workshop",
             "event_date": "2023-08-20", "event_location": "San Francisco"},
            {"name": "Charlie", "event_title": "AI Summit",
             "event_date": None, "event_location": "Boston"}
        ]

        generate_invitations(template_content, attendees)
