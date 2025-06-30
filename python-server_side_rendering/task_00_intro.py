def generate_invitations(template, attendees):
    # Tip yoxlaması
    if not isinstance(template, str):
        print(f"Error: Template should be a string but got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Boş template yoxlaması
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Boş iştirakçı siyahısı yoxlaması
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Hər iştirakçı üçün fayl yaratmaq
    for i, attendee in enumerate(attendees, start=1):
        # Məlumatları "N/A" ilə tamamla, əgər məlumat yoxdursa və ya None-dursa
        name = attendee.get('name') or "N/A"
        event_title = attendee.get('event_title') or "N/A"
        event_date = attendee.get('event_date') or "N/A"
        event_location = attendee.get('event_location') or "N/A"

        # Şablonu doldur
        invitation_text = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        # Faylı yaz
        filename = f"output_{i}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(invitation_text)
        except Exception as e:
            print(f"Failed to write {filename}: {e}")
