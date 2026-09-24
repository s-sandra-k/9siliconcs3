class GameDirectoryEntry:
    def __init__(self, title: str, developer: str, genre: str, status: bool = True):
        self.title = title
        self.developer = developer
        self.genre = genre
        self.status = status
        self.favorite_count = 0
        self.__is_favorited_by_user = False

    def updateStatus(self, new_status: bool):
        self.status = new_status

    def getGameDetails(self) -> str:
        return f"{self.title} by {self.developer} [{self.genre}]"

    def incrementFavoriteCount(self):
        if self.__is_favorited_by_user:
            self.__is_favorited_by_user = False
            self.favorite_count -= 1
        else:
            self.__is_favorited_by_user = True
            self.favorite_count += 1

    def displayState(self):
        return f"Title: {self.title} | Active: {self.status} | Favorites: {self.favorite_count} | Favorited: {self.__is_favorited_by_user}"

class SteamGame(GameDirectoryEntry):
    def __init__(self, title: str, developer: str, genre: str, app_id: str, status: bool = True):
        super().__init__(title, developer, genre, status)
        self.app_id = app_id
        self.achievements_unlocked = 0

    def unlockAchievement(self):
        self.achievements_unlocked += 1
        print(f"Achievement unlocked! Total achievements: {self.achievements_unlocked}")

    def getGameDetails(self) -> str:
        base_details = super().getGameDetails()
        return f"[Steam AppID: {self.app_id}] {base_details} | Achievements Unlocked: {self.achievements_unlocked}"


class UserLibrary:
    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.__games = []

    def addGame(self, game_entry):
        self.__games.append(game_entry)
        print(f"Added '{game_entry.title}' to {self.owner_name}'s library.")

    def removeGame(self, game_entry):
        if game in self.__games:
            self.__games.remove(game_entry)
            print(f"Removed '{game_entry.title}' from {self.owner_name}'s library.")

    def displayLibrary(self):
        print(f"\n--- {self.owner_name}'s Game Library ---")
        if not self.__games:
            print("Library is currently empty.") 
        else:
            for game in self.__games:
                print(f"- {game.getGameDetails()} | Active: {game.status} | Favorites: {game.favorite_count} | Favorited: {game._GameDirectoryEntry__is_favorited_by_user}")  


if __name__ == "__main__":
    print("TEST 1: Inheritance and Super()")
    steam_game  = SteamGame("Counter Strike 2", "Valve", "FPS", "730")
    print(f"Parent attribute inherited: Title = {steam_game.title}")
    print(f"Child attribute added: AppID = {steam_game.app_id}")
    steam_game.unlockAchievement()

    print("\nTEST 2: Aggregation")
    user_lib = UserLibrary("Shun")

    generic_game = GameDirectoryEntry("Brawl Stars", "Supercell", "MOBA")\
    
    generic_game.incrementFavoriteCount()
    steam_game.incrementFavoriteCount()
    
    user_lib.addGame(generic_game)
    user_lib.addGame(steam_game)

    print("\nTEST 3: Displaying Library")
    user_lib.displayLibrary()