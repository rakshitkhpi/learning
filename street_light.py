import numpy as np 

street_light = np.array([[ 1, 0, 1 ],
                          [ 0, 1, 1 ],
                          [ 0, 0, 1 ],
                          [ 1, 1, 1 ],
                          [ 0, 1, 1 ],
                          [ 1, 0, 1 ] ])


walk_stop = np.array([0, 1, 0, 1, 1, 0])

weights = np.array([0.5, 0.48, -0.7])

for i in range(40):

    for x in range(len(walk_stop)):
        total_error = 0
        inputs = street_light[x]
        goal = walk_stop[x]

        pred = inputs.dot(weights)
        error = (goal - pred) ** 2
        total_error += error

        delta =  pred - goal
        weights = weights - (0.1 * (inputs * delta))

    print('pred:{}\nerror:{}\ntotal_error:{}\n'.format( pred, error, total_error))

