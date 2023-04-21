class Datamining:
    """
    Class that represent linear model which can predict y-coordinate.
    Constructor input should contain training dataset.
    def predict(self, x): return predicted y-coordinate for given x-coordinate.
    """
    # learnable parameters
    b0 = 0
    b1 = 0
    
    def __init__(self, train_set):
        self.b0, self.b1 = self.coefficients(train_set)

    def mean(self, values):
        return sum(values) / float(len(values))
    
    def variance(self, values, mean):
        return sum([(x-mean)**2 for x in values])
    
    # Calculate covariance between x and y
    def covariance(self, x, mean_x, y, mean_y):
        covar = 0.0
        for i in range(len(x)):
            covar += (x[i] - mean_x) * (y[i] - mean_y)
        return covar
    
    # Calculate coefficients
    def coefficients(self, dataset):
        x = [col[0] for col in dataset]
        y = [col[1] for col in dataset]
        x_mean, y_mean = self.mean(x), self.mean(y)
        b1 = self.covariance(x, x_mean, y, y_mean) / self.variance(x, x_mean)
        b0 = y_mean - b1 * x_mean
        return [b0, b1]

    def predict(self, x):
        return self.b1 * x + self.b0

# Test
t_set = [(0, 1),
    (2, 2),
    (4, 3),
    (9, 8),
    (3, 5)]  
dm = Datamining(t_set)
print(dm.predict(32))
print(dm.b1, dm.b0)
