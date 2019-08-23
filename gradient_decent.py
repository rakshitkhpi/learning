weight, inputs, goal_pred = 0.0, 1.1, 0.8

for x in range(4):
    pred = inputs * weight
    error = (pred - goal_pred) ** 2 
    er = goal_pred - pred
    delta = pred - goal_pred # how much node missed
    weight_delta = delta * inputs # derivative
    weight = weight - weight_delta

    print('pred= {}\n error= {}\n err= {} \n delta= {}\n weight_delta= {}\n weight= {}'.format(pred, error, er, delta, weight_delta, weight))