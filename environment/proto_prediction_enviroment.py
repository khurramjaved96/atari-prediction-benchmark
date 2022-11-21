from environment import experience_pb2
import numpy  as np

class ProtoPredictionEnvironment:
    def __init__(self, env_path, gamma):
        self.gamma = gamma
        self.x = []
        self.r = []
        self.done = []
        self.action = []

        f = open(env_path, "rb")
        add_data = f.read()
        self.buffer = experience_pb2.ExperienceBuffer()
        self.buffer.ParseFromString(add_data)
        self.real_target = np.zeros(len(self.buffer.experiences))
        self.total = len(self.buffer.experiences)
        self.time = 0
        real_target_cur = 0

        for i in range(len(self.buffer.experiences)-1, 0, -1):
            if(self.buffer.experiences[i].done == True):
                real_target_cur = 0
            self.real_target[i] = real_target_cur
            reward = self.__get_reward(i)
            real_target_cur =  real_target_cur*self.__get_gamma(i) + reward

        print(self.real_target[0:500])

    def __get_gamma(self, i):
        if(self.buffer.experiences[i].done == True):
            return 0
        return self.gamma

    def __get_reward(self, i):
        if (self.buffer.experiences[i].reward > 1):
            return 1
        elif (self.buffer.experiences[i].reward < -1):
            return -1
        else:
            return self.buffer.experiences[i].reward

    def get_reward(self):
        return self.__get_reward(self.time)

    def get_target(self):
        return self.real_target[self.time]

    def get_done(self):
        return self.buffer.experiences[self.time].done

    def step(self):
        self.time+=1
        self.time = self.time%self.total
        return self.get_state()

    def get_state(self):
        return np.array(self.buffer.experiences[self.time].sensor_reading).squeeze()

