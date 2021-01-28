# MultiplayerSnek
My Snek game except it cam be played on multiple computers over the same internet.

There are a lot of files so let me explain. On the internet there needs to be 3 things, 2 clients and 1 host. These can be the same device or the host and 1 client on 1 computer or all on separate machines.
When setting these "apps" up theres a couple things to do:
  ServerSide.py needs access to: 
    Game.py
    Snek.py
  ClientSide.py needs access to:
    network.py
    Drawing.py
    Snek.py
    Game.py
    
Saying "needs access to" meaning in the same folder as each other
    
Drawing.py - Functions on drawing the game
Game.py - Class with a few functions on the game system
Snek.py - Class with a few functions on the snakes 
network.py - What ClientSide.py uses to connect to ServerSide.py
ServerSide.py - Host program
ClientSide.py - Client program

This needs a few libraries, socket and pickle which are system libraries, and pygame which you will need to install. Here are instructions on installing it: http://automatetheboringstuff.com/2e/appendixa/

Current bug/issue:
  `Exception has occurred: UnpicklingError`
  `invalid load key, '\x04'.`
  Which is thrown on line 12 of network.py
  
This game is currently not playable. The ETA on it being playable is about Feb. 12th
