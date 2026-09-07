# SG4 - Understanding Classes and Objects

## GameDirectory

## GameDirectory represents a video game listed in a discovery library that tracks community interest and helps users find titles matching their preferences.

## Properties
| Property | Data Type | Description |
|---|---|---|
| Title | String | Title of the game |
| Developer | String | Name of the developer |
| Genre | String | The genre of the game |
| Status | Boolean | If the game is currently active or not |
| IsFavoritedByTheUser | Boolean | Indicates whether the user has favorited the game |
| FavoriteCount | Integer | Total number of users that have favorited the game | 

## Methods
| Method | Description |
|---|---|
| updateStatus() | Updates the game's current status, if it's active or not|
| getGameDescription() | Displays a formatted string containing the title, developer, and genre |
| incrementFavoriteCount() | Increases the total favorite count by one when a user favorites the game. |

## Class Diagram
![Class Diagram](<CLASS NAME.png>)

## Design Explanation

### Why did you choose this class?

I chose the `GameDirectoryEntry` class because it models a recommendation library where users discover games matching their interests while seeing community popularity through favorite counts.

### Which property is the most important? Why?

The title is the most important property as it serves as the primary identifier for each game instance. Without a title, it would be difficult to distinguish one game object from another in a systen or database.

### Which method is the most useful? Why?

The incrementFavoriteCount() method is the most useful because it dynamically updates the game's community rating whenever a user adds it to their favorites, helping rank popular games in the directory.