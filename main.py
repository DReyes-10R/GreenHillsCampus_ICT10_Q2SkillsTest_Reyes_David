from pyscript import display, document


# I might be wrong with the advisors of the clubs because im not really familiar with themm, even the rom numbers might also be incorrect and also the meeting time
dance_info = {
    'Name': 'Dance Club',
    'Description': 'Dancing, choreography, and performances.',
    'Meeting_Time': 'Wednesdays 3:30–5:00 PM',
    'Location': 'Room 405',
    'Advisor': 'Mr. Marutani',
    'Category': 'Dancing, freestyle, hip-hop'
}

glee_info = {
    'Name': 'Glee Club',
    'Description': 'Singing, and performing for fun and competitions.',
    'Meeting_Time': 'Mondays 4:00–5:00 PM',
    'Location': 'Room 210',
    'Advisor': 'Ms. David',
    'Category': 'Singing'
}

science_info = {
    'Name': 'Science Club',
    'Description': 'Hands-on experiments and science fairs.',
    'Meeting_Time': 'Fridays 2:30–4:00 PM',
    'Location': 'Lab 2',
    'Advisor': 'Sr. Castanio/Calpo',
    'Category': 'Academics'
}

art_info = {
    'Name': 'Art Club',
    'Description': 'Drawing, painting and portfolio development.',
    'Meeting_Time': 'Thursdays 3:00–4:30 PM',
    'Location': 'Art Room',
    'Advisor': 'Mr. Visaya/Deguzman',
    'Category': 'Creativity, expression'
}

math_info = {
    'Name': 'Math Club',
    'Description': 'Exploring advanced math topics and competitions.',
    'Meeting_Time': 'Tuesdays 3:30–6:00 PM',
    'Location': 'Room 308',
    'Advisor': 'Mr. Ferma',
    'Category': 'Academics'
}

CLUBS = {
    'dance': dance_info,
    'glee': glee_info,
    'science': science_info,
    'art': art_info,
    'math': math_info
}

def show_club(e):
    sel = document.getElementById('club_select')
    if not sel:
        return
    key = sel.value
    club = CLUBS.get(key)
    out = document.getElementById('club_info')

    
    # basically I just added the <strong> next to the stuff/labels to make it bold
    html = f"""
    <h5>{club['Name']}</h5>
    <p class="mb-1"><strong>Description:</strong> {club['Description']}</p>
    <p class="mb-1"><strong>Meeting Time:</strong> {club['Meeting_Time']}</p>
    <p class="mb-1"><strong>Location:</strong> {club['Location']}</p>
    <p class="mb-1"><strong>Advisor:</strong> {club['Advisor']}</p>
    <p class="mb-0"><strong>Category:</strong> {club['Category']}</p>
    """
    out.innerHTML = html
