from pyscript import document

CLUBS = {
    "dance": {
        "name": "Chess Club",
        "description": "dancing, choreography, and performances.",
        "meeting_time": "Wednesdays 3:30–5:00 PM",
        "location": "Room 405",
        "advisor": "Mr. Marutani",
        'category': 'Dancing, freestyle, hip-hop'
        
    },
    
    "glee": {
        "name": "glee Club",
        "description": "Singing, and performing for fun and competitions.",
        "meeting_time": "Mondays 4:00–5:00 PM",
        "location": "Room 210",
        "advisor": "Ms. David",
        'category': 'Singing'
        
    },
    
    "science": {
        "name": "Science Club",
        "description": "Hands-on experiments and science fairs.",
        "meeting_time": "Fridays 2:30–4:00 PM",
        "location": "Lab 2",
        "advisor": "Sr. Castanio/Calpo",
        'category': 'Academics'
       
    },
    
    "art": {
        'name': 'Art Club',
        'description': 'Drawing, painting and portfolio development.',
        'meeting_time': 'Thursdays 3:00–4:30 PM',
        'location': 'Art Room',
        'advisor': 'Mr. Visaya/Deguzman',
        "category": 'Creativity, expression'
    },
    
    "Math": {
        'name': "Math Club",
        'description': 'Exploring advanced math topics and competitions.',
        'meeting_time': 'Tuesdays 3:30–6:00 PM',
        'location': 'Room 308',
        'advisor': 'Mr. Ferma',
        'category': 'Academics'
    }
}

def show_club(e=None):
    sel = document.getElementById("club_select")
    if not sel:
        return
    key = sel.value
    club = CLUBS.get(key)
    out = document.getElementById("club_info")
    if not club:
        out.innerText = "No information available."
        return

    # added a format to make it look neet if thats ok (learned it from freecodecamp)
    html = f"""
    <h5>{club['name']}</h5>
    <p class="mb-1"><strong>Description:</strong> {club['description']}</p>
    <p class="mb-1"><strong>Meeting Time:</strong> {club['meeting_time']}</p>
    <p class="mb-1"><strong>Location:</strong> {club['location']}</p>
    <p class="mb-1"><strong>Advisor:</strong> {club['advisor']}</p>
    <p class="mb-0"><strong>Category:</strong> {club['category']}</p>
    """
    out.innerHTML = html
