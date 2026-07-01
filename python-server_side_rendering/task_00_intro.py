#!/usr/bin/env python3
"""
Module creating a templating program
"""

import os
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def generate_invitations(template, attendees):

    """generate invitation from template an attendees"""

    placeholders = ["name", "event_title", "event_date", "event_location"]

    if not isinstance(template, str):
        logging.error("error, template must be a string")
        return

    if not isinstance(attendees, list):
        logging.error("error attendees must be a list")
        return

    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for i in placeholders:
            value = attendee.get(i)
            if value is None:
                value = "N/A"

            invitation = invitation.replace(f"{{{i}}}", str(value))

        output = f"output_{index}.txt"

        try:
            if os.path.exists(output):
                logging.warning(f"File {output} already exists. Overwriting")

            with open(output, 'w', encoding='utf-8') as file:
                file.write(invitation)
            logging.info(f"Successfully generated {output}")

        except IOError as error:
            logging.error(f"Failed to write file {output}. Error: {error}")
