# Arcade prediction environment 

A small test policy for Pong is included in the repo. The full policies for all environments can be downloaded from [Google drive link](https://drive.google.com/file/d/1zOWay0-9rGrmJMa9vP4qEwTjd-kziDTu/view?usp=sharing). Each environment contains over 100 million steps of interactions of a pre-trained rainbow DQN agent from the Chiner RL model zoo [1]. 

![Visualization of the experience](images/envs.png)
Environments down-scaled to 16 x 16. Looking at a single frame, it's hard to figure out information information about the environment. For instance in Pong, the ball is often not visible in a single frame. However, looking at the sequence of frames, we can tell the position and the direction of the ball. This partial observability due to down-scaling makes 16 x 16 Atari an interesting benchmark for studying state construction.

[1] Fujita, Yasuhiro, et al. "Chainerrl: A deep reinforcement learning library." The Journal of Machine Learning Research 22.1 (2021): 3557-3570.
