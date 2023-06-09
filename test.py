import gym
game = "Pong" +"NoFrameskip-v4"
env = gym.make(game)
# This seed is fixed and was used
# by the pre-trained agents to record actions.
# Changing it will break the benchmark
env.seed(1)


with open("policies/"+ game +".txt", "rb") as f:
    byte = f.read(1)
    ep_reward = 0
    while byte != b"":
        val = int.from_bytes(byte, 'big')
        if(val==82):
            print("Resetting; prev epiode return ", ep_reward)
            env.reset()
            ep_reward = 0
        else:
            obs, r, _, _ = env.step(val - 97)
            ep_reward += r
        byte = f.read(1)
