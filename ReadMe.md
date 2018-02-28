# Generic Local Lottery Game

## Aim:
A CLI program that was casually developed to implement all three types of program control i.e sequential, selection and repetition. Along with that, this was also to understand initialization and performing operations on data structures (lists).

**Requrements: Supports Python 3**

## Working:
Program opens with a menu holding 4 options:

1. **Instructions**: This command displays how a game is to be played. The instruction statements is followed by menu.

![Instructions](https://github.com/asukhey/Generic-Lottery-Game/blob/master/OP/0.Instructions.PNG)

2. **Pick 3 without fireball**: This option lets a user pick 3 numbers from 0 - 9, if the numbers match the ones randomly drawn, that user wins $100. User is then asked if interested to play again and returns to menu if typed 'y'. The following images displays instances of the prior and otherwise.

![Win](https://github.com/asukhey/Generic-Lottery-Game/blob/master/OP/6.Victory_No_FB.PNG)

![Win](https://github.com/asukhey/Generic-Lottery-Game/blob/master/OP/7.Loss_No_FB.PNG)

3. **Pick 3 with fireball**: This is similar to option 2. An additional Fireball number is drawn that increases the probability of winning. Below are a few instances.

i. If a user has 2 numbers matching the numbers drawn, and one number that matches with the fireball- The fireball number replaces the unmatched number, leading to victory.
![Fireball Win](https://github.com/asukhey/Generic-Lottery-Game/blob/master/OP/1.Fireball_Victory.PNG)

ii. If user's number matches all the numbers in the pool as well as the fireball number, apart from $100, additional $50 are won for every number matching the fireball. For example, if User picked 4,8,7 and the lottery picks were also 4,8,7. User wins $100, apart from that, if the fireball pick is 4. An additional $50 is added too the prize for one of the numbers match the fireball.

![Bonus 1](https://github.com/asukhey/Generic-Lottery-Game/blob/master/OP/2.Bonus_FB_Win.PNG)

![Bonus 2](https://github.com/asukhey/Generic-Lottery-Game/blob/master/OP/3.Bonus_FB_Win2.PNG)

![Bonus 3](https://github.com/asukhey/Generic-Lottery-Game/blob/master/OP/4.Bonus_FB_Win3.PNG)
