from fileinput import filename


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: Template should be a string but got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list ")
        return
    
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provide, no outpud files generated.")
        return
    
    for i, attendee in enumerate(attendees, star=1):
        name = attendee.get('name') or "N/A"
        event_title = attendee.get('event_title') or "N/A"
        event_data = attendee.get('event_data') or "N/A"
        event_location = attendee.get('event_location') or "N/A"

        invitation_text = template.format(
            name=name
            event_title=event_title,
            event_data=event_data,
            event_location=event_location
        )

        filename = f"output_{1}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(invitation_text)
        except Exception as e:
            print(f"Failed to write {filename}: {e}")
            

