from environment import proto_prediction_enviroment as atari_environment
import matplotlib.pyplot as plt

if __name__=="__main__":
    env_file_path = "WizardOfWorNoFrameskip-v4.proto"
    gamma = 0.98
    env = atari_environment.ProtoPredictionEnvironment(env_file_path, gamma)
    for i in range(0, 100):
       x = env.step()
       reward = env.get_reward()
       target  = env.get_target()

       # Visualize environment
       x = x.reshape((16,16))
       plt.imshow(x)
       plt.show()

