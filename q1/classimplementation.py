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


  # Create two independent game objects
game1 = GameDirectoryEntry("Cyberpunk 2077", "CD Projekt Red", "RPG", True)
game2 = GameDirectoryEntry("Elden Ring", "FromSoftware", "Action RPG", True)

# Display initial states
print("BEFORE")
print(f"Object 1: {game1.displayState()}")
print(f"Object 2: {game2.displayState()}\n")

# Perform actions on Object 1
print("Performing method on Object 1...")
game1.incrementFavoriteCount()
game1.updateStatus(False)
print("Executed: game1.incremenFavoriteCount()")
print("Executed: game1.updateStatus(False)\n")

# Display updated status
print("AFTER")
print(f"Object 1: {game1.displayState()}")
print(f"Object 2: {game2.displayState()}")
