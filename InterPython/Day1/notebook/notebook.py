import datetime

# Store the next available id for all new notes
last_id = 0


class Note:
    """
    Represent a note in the notebook. Match against a
    string in searches and store tags for each note.
    """
    def __init__(self, memo, tags=''):
        """
        Initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.
        """
        self._memo = memo
        self._tags = tags
        self._creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self._id = last_id

    def match(self, filter):
        """
        Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.
        """
        return filter in self._memo or filter in self._tags


class Notebook:
    """
    Represent a collection of notes that can be tagged,
    modified, and searched.
    """
    def __init__(self):
        """
        Initialize a notebook with an empty list.
        """
        self._notes = []

    def new_note(self, memo, tags=''):
        """
        Create a new note and add it to the list.
        :param memo: Note memo
        :param tags: Tags for memo.
        :return: Nothing
        """
        self._notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """
        Locate the note with a given id
        :param note_id: Note id
        :return: Note object if found
                None if not found
        """
        for note in self._notes:
            if note._id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        """
        Find the note with the given id and change its
        memo to the given value.
        :param note_id: Note_id number
        :param memo: Memo for note
        :return: Nothing
        """
        note = self._find_note(note_id)
        if note:
            note._memo = memo
            return note
        return None

    def modify_tags(self, note_id, tags):
        """
        Find the note with the given id and change its
        tags to the given value.
        :param note_id:  Note_id number
        :param tags: Tags to search
        :return: Nothing
        """
        note = self._find_note(note_id)
        if note:
            note._tags = tags
            return note
        return None

    def search(self, filter):
        """
        Find all notes that match the given filter
        string
        :param filter:
        :return: Nothing
        """
        return [note for note in self._notes
                if note.match(filter)]
