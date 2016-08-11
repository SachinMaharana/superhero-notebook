import datetime
last_id = 0

class Hero:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.name or filter in self.place

class Superhero:
    def __init__(self):
        self.heroes = []

    def add_hero(self, name, place):
        self.heroes.append(Hero(name, place))

    def _find_note(self, note_id):
        for hero in self.heroes:
            if str(hero.id) == str(note_id):
                return hero
        return None

    def modify_hero_name(self, note_id, name):
        note = self._find_note(note_id)
        if note:
            note.name = name
            return True
        return False

    def modify_hero_place(self, note_id, place):
        note = self._find_note(note_id)
        if note:
            note.place = place
            return True
        return False

    def search(self, filter):
        return [hero for hero in self.heroes if hero.match(filter)]
