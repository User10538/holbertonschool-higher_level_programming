import logging
def generate_invitations (template, attendees):

    index = 0
    
    if not isinstance(template, str):
        logging.error("Temple must be a string")
        return

    if not isinstance(attendees, list):
        logging.error("Attendees must be a list of dictionaries.")
        return 
    
    # Check for empty template
    if not template.strip():  # Strip removes whitespace
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return
    
    try:     
        for attendee in attendees:
            
            personalized_invitation = template.format(
                name=attendee.get("name", "N/A"),
                event_title=attendee.get("event_title", "N/A"),
                event_date=attendee.get("event_date", "N/A"),
                event_location=attendee.get("event_location", "N/A")
            )
            index = index + 1
        filename = f"output_{index}.txt" 
        with open(filename, "w", encoding="utf-8") as f:
                    f.write(personalized_invitation) 

        logging.info(f"Invitation saved: {filename}")

    except Exception as e:
            logging.error(f"Error processing attendee #{index}: {e}")
