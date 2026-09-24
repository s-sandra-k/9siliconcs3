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
    print("BEFORE RELATIONSHIP")
    user_lib = UserLibrary("Shun")

    game1 = GameDirectoryEntry("Mobile Legends Bang Bang", "Moonton", "MOBA", True)
    game2 = GameDirectoryEntry("Call of Duty Mobile", "TiMi Studio Group", "Action FPS, Battle Royale", True)
    game3 = GameDirectoryEntry("PUBG Mobile", "Tencent Games", "Action FPS, Battle Royale", True)
    game1.incrementFavoriteCount()
    game2.incrementFavoriteCount()
    game3.incrementFavoriteCount()

    print(f"Created user library for {user_lib.owner_name}.")
    print(f"Created game entry: '{game1.title}', '{game2.title}', '{game3.title}'.")

    print("\nBUILDIING RELATIONSHIP")
    user_lib.addGame(game1)
    user_lib.addGame(game2)
    user_lib.addGame(game3)

    print("\nAFTER RELATIONSHIP")
    user_lib.displayLibrary()
