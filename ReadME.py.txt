ReadME.py
A summary of the project goals:

Here are the milestones I reached-
Create knight class
Create an enemy class (hurts)
Create a wall class, and add collision between enemies and walls
Add coins
Add collision between knight with walls, coins, and enemies
Add placer to select wall position
Make wall move to player, and iterate through different walls in the list
Add lives
Add scoring and timer
Add state transition between gameplay and instructions

Overall, I wanted to make a game with interaction between different sprites and checking for collision/distance parameters. Which I certainly got. Of course, the game should also be fun. The walls being limited and not moving forces the player to take risks to evade enemies to increase the score, since the coins aren't moving. The game should encourage the player to constantly move their walls to increase their score, and work to beat their previously recorded score from the last session of the game. 


Instructions the player may need

The knight is moved using the direction arrows in their corresponsing directions. The sprite used to show where walls will be placed is moved with WASD keys in their corresponding directions. Upon pressing q, a wall moves to the spot of the placer. Upon contact with the walls, enemies you should avoid will reset to corners of the screen. You only get 4 walls, and upon placing 4, the first (or 0th) will be moved when you press q. The player knight can't move through walls. Collect coins to increase your score.

A list of technologies and techniques you used

Distance detection- checking if sprites are too close to the another sprite (using the pythagorean theorem)
Collision detection - checking if sprites collided with others
State Transition - Moved between Instructions and the Game state
List iteration - changed which wall sprite in a list was ustilized
while loops - used while loops to make certai featutures continure to occur, primarily updating x/y coordinates for movement/collision
Initialzation - had to initalize most of my classses with super itersation to make sure they could interact in a scene

Citations for any external resources you used:
https://www.pygame.org/wiki/CalculateDist
^This link was used to find out I could calculate the hypotenuse without having to layer a bunch of parentheses, by importig math and using math.hypot()
Code from Dr Andy Harris was used to assist in this project, specifically from moveOnMap.py and platformer.py to help with tracking sprite postion and movemtn ditection

A description of your process

My process was bad and unhealthy. I would write down a goal, write some psudocode, and try to achieve it, without differentiating from that goal unless I got super frustrated. I got super frustrated a few times. It was always good to have a backup goal to achieve in case I just couldn't get once done. I would try to get 2 or 3 goals doen a day, but some of them were far harder than others. This led to me feeling behind, even though just trhough messing with the code I was learning. Ultimately, this process did get me to the finish line, and I think those backup goals I could switch to helped me keep making progress.


What did you learn?

I learned to manage my expectations. I ahd a genreal idea how to do everything for my pseudocode, but ultimtately I'm not good enough to just sit down and get it the first try. By the end, I had a much better feel for how quickly I worked through code and didn't get as mad with time commitment. I also learned a lot about parameters. The majority of my code is just checking for x and y movements. I learned all the ways I could check (such as the pythagorean theorem, or simply > or < x and y), and what appropriate on screen movement looked like.

Where did you get stuck?
The main place was with checking the movement between a sprite that was moving and a sprite that wasn't. The slide and catch game had you player character collecting coins, so I thought it would be easy. It wasn't. The differece for writing code for sprites in a list or not also threw me off. Should movement be in the sprite class or the Game class? A lot of time was spent figuring out where stuff went. Of course, writing all the collision code made me have to think hard about the 2D space sprites existed in. Where is 290 degrees exactly? I had to adjust values quite a bit to make sure things moved appropriately.

What would you like to improve?

Currently, the wall can be placed upon the kngiht and basically stops movement of the kngiht. I would fix this by making the placer not be able to get too close to the player, which is realistic. Additionally, it would be cool to have sprite animations, but I didn't have time with my goals to learn it. Finally, I would have the enemies speed up as time passed. However, I was having trouble getting the timer to work and certain time to trigger things, so I gave up on this goal and focused elsewhere.

How would you do things differently next time?

I would spread it out over a few more days and plan goals further ahead. I had a list of goals, but not really an idea of when I wanted them finished by or what order. I think acutally setting out the order of my goals would help quite a bit in terms of frutstration. I also would have given myself more time, but I have been pretty busy, so I don't know if that was even realistic. 

How far did you stray from the game design document?

Not too far from the inital one. I had lives, a placer, enemies, and collision. I removed aestetic things, such as the lives appearing as hearts instead of a label. I also changed hwo some of the mechanics worked, such as the placer no longer following the mouse.

How did you stay on track?

I sat down and forced myself to work. I set 3 or so goals to get done by a certain time of day and got to work. Generally this worked, however, it was pretty frustrating to work on this project exlcuisvely and not do much else between. However, this method did work and got done most of my goals.