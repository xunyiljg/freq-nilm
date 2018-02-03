import numpy as np
import random
from sklearn.metrics.pairwise import cosine_similarity

def aug_random(train,num_aug):
    print ("random")
    new = []
    for i in range(num_aug):
        index = random.sample(list(np.arange(len(train))), 2)
    #     print index
        new_sample = 0.5*train[index[0], :, :, :] + 0.5*train[index[1], :, :, :]
        new.append(new_sample)
    new = np.array(new)
    return new


def aug_appliance(train, num_aug):
    print ("appliance")
    new = np.zeros((num_aug, 6, 112, 24))
    for i in range(num_aug):
        home_agg = np.zeros((112,24))
        for appliance in range(1,6):
            index = np.random.choice(list(range(len(train))))
            new[i, appliance, :, :] = train.copy()[index, appliance, : :]
            home_agg += train.copy()[index, appliance, :, :]
        new[i, 0, :, :] = home_agg
    return new


def aug_noise(train, num_aug):
    print ("noise")
    new = []
    for i in range(num_aug):
        index = np.random.choice(list(range(len(train))))
        noise = np.random.normal(0,1,112*24*5).reshape(5, 112, 24)
        new_sample = train.copy()[index]
        new_sample[1:] = new_sample[1:] + noise
        new_sample[0] = 0 
        for j in range(1, 6):
            new_sample[0] += new_sample[j]
        new.append(new_sample)
    new = np.array(new)
    return new


def selective(train, test):
    test_aggregate = test[:, 0, :, :]
    train_aggregate = train[:, 0, :, :]
    
    test_aggregate = test_aggregate.reshape(test_aggregate.shape[0], -1)
    train_aggregate = train_aggregate.reshape(train_aggregate.shape[0], -1)
    
    concated = np.vstack([train_aggregate, test_aggregate])
    
    cosine_similarity = cosine_similarity(concated)
    cosine_similarity = cosine_similarity[:len(train_aggregate), len(train_aggregate):]
    
    train_max = cosine_similarity.max(axis=1)
    
    k = int(0.5*len(train_aggregate))
    index = np.argpartition(train_max, -k)[-k:]
    
    return train[index]


def augmented_data(train, test=None, num_aug, case, select=False):
    
    if num_aug == 0:
        return train
    else:
        continue
    
    if select:
        train = selective(train, test)
    else:
        continue
        
    if case == 1:
        new = aug_random(train, num_aug)
    if case == 2:
        new = aug_appliance(train, num_aug)
    if case == 3:
        new = aug_noise(train, num_aug)
    return np.vstack([train, new])