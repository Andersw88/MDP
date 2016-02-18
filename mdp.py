#!/usr/bin/env python
from pprint import pprint 

def finiteHorizon():
    timeEpochs = 10
    transition = [[[0.5,0.5], [0,1.0]], [[0.0,1.0]]]

    actions = [len(x) for x in transition]
    states = len(transition)

    rewards = [[5,10], [-1]]

    values = [[0 for x in range(states)] for y in range(timeEpochs)]

    values[-1] = [0,0] #endRewards

    chosenActions = [[0 for x in range(states)] for y in range(timeEpochs)]

    for time in range(timeEpochs):
        for state in range(states):
            maxValue = float("-inf")
            chosenAction = -1
            for action in range(actions[state]):
                reward = rewards[state][action] +  sum([transition[state][action][x]*values[time-1][x] for x in range(states)])
                if maxValue < reward:
                    chosenAction = action
                    maxValue = reward
            chosenActions[time][state] = chosenAction
            values[time][state] = maxValue

    print "Finite horizon with epochs:", timeEpochs
    print "ExpextedReward : Action"
    for state in range(states):
        print "          State",state,"",
    print ""

    for time in range(timeEpochs):
        for value,action in zip(values[time],chosenActions[time]):
            print "       ","{:6.2f}".format(value) ,":",action,
        print ""



def infiniteHorizon(gamma = 0.95):
    
    transition = [[[0.5,0.5], [0,1.0]], [[0.0,1.0]]]

    actions = [len(x) for x in transition]
    states = len(transition)

    rewards = [[5,10], [-1]]

    values = [0 for x in range(states)]
    chosenActions = [0 for x in range(states)]

    while(True):
        maxDiff = float("-inf")
        for state in range(states):
            maxValue = float("-inf")
            chosenAction = -1
            for action in range(actions[state]):
                reward = rewards[state][action] +  gamma * sum([transition[state][action][x]*values[x] for x in range(states)])
                if maxValue < reward:
                    chosenAction = action
                    maxValue = reward
            chosenActions[state] = chosenAction
            maxDiff = max(maxDiff,values[state] - maxValue)
            values[state] = maxValue
        if abs(maxDiff) < 0.0001:
            break

    print "Infinite horizon with gamma:", gamma
    print "ExpextedReward : Action"
    for state in range(states):
        print "          State",state,"",
    print ""

    for value,action in zip(values,chosenActions):
        print "       ","{:6.2f}".format(value) ,":",action,
    print ""

if __name__ == "__main__":
    infiniteHorizon(gamma = 0.90)
    infiniteHorizon(gamma = 0.91)

    finiteHorizon()


