# Plot-Armor
  In many movies, like the Star Wars franchise, we see the bad guys shooting at our heroes many times but failing to land any hits. Often when this happens we suspend our disbelief or chalk it off to the plot armor of the hero. But some cases get so bad that we can't even tell for sure if the bad guys have blindfold on or not. In this project I made a small game where the bad guys fire entirely randomly and the player has perfect aim, to see even in that case who would win in a fight? 
# What did I use?
  In order to simulate the fights I made a game using Pygame library in Python. This game takes multiple parameters and simulates a fight where the player character (more like a green circle at this stage) runs around trying to dogde enemy lasers while simultaneously shooting back. The enemies are stationary and they just shoot randomly in the general direction of the player. Game ends when either side loses.
 
 Then I got to simulating a bunch of results for this game, using random variables each time. When I got a sizeable data set, I wrote a predictor for the result of this game. 
 ![Figure_1](https://user-images.githubusercontent.com/55945878/166947076-0720da52-6a93-4bd5-895d-7f0e04592271.png)

 The precitor uses Torch library and employs linear neural networks to solve logistic regression problem. The collected data trains the model until we get an acceptable loss value. Then we can use this model to make predictions about future games with different parameters and see how well the prediction will work.
