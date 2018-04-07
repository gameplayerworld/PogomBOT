from geopy.distance import vincenty


class DSPokemon:
    def __init__(self, encounter_id, spawnpoint_id, pokemon_id, latitude,
                 longitude, disappear_time, ivs, move1, move2, weight, height,
                 gender, form, cp, cp_multiplier):
        self.encounter_id = encounter_id
        self.spawnpoint_id = spawnpoint_id
        self.pokemon_id = pokemon_id
        self.latitude = latitude
        self.longitude = longitude
        self.disappear_time = disappear_time  # Should be datetime
        self.ivs = ivs
        self.move1 = move1
        self.move2 = move2
        self.weight = weight
        self.height = height
        self.gender = gender
        self.form = form
        self.cp = cp
        self.cp_multiplier = cp_multiplier
        self.level = self.calcPokemonLevel(
            cp_multiplier) if cp_multiplier is not None else None

    def getEncounterID(self):
        return self.encounter_id

    def getSpawnpointID(self):
        return self.spawnpoint_id

    def getPokemonID(self):
        return self.pokemon_id

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def getDisappearTime(self):
        return self.disappear_time

    def getIVs(self):
        return self.ivs

    def getMove1(self):
        return self.move1

    def getMove2(self):
        return self.move2

    def getWeight(self):
        return self.weight

    def getHeight(self):
        return self.height

    def getGender(self):
        return self.gender

    def getForm(self):
        return self.form

    def getCP(self):
        return self.cp

    def getCPMultiplier(self):
        return self.cp_multiplier

    def getLevel(self):
        return self.level

    def getDistance(self, user_location):
        user_lat_lon = (user_location[0], user_location[1])
        pok_loc = (self.latitude, self.longitude)
        return vincenty(user_lat_lon, pok_loc).km

    def filterbylocation(self, user_location):
        return self.getDistance(user_location) <= user_location[2]

    def calcPokemonLevel(self, cp_multiplier):
        if cp_multiplier < 0.734:
            pokemon_level = (58.35178527 * cp_multiplier * cp_multiplier -
                             2.838007664 * cp_multiplier + 0.8539209906)
        else:
            pokemon_level = 171.0112688 * cp_multiplier - 95.20425243
        pokemon_level = int((round(pokemon_level) * 2) / 2)
        return pokemon_level
