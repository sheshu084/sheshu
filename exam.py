

class LineModel:
    def __init__(self, slope=0, intercept=0):
        self.slope = slope
        self.intercept = intercept
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def get_line_params(self):
        return self.slope, self.intercept

    def set_line_params(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept

    def calculate_perpendicular_distance(self, x, y):
        # Perpendicular distance from point (x, y) to the line y = mx + c
        numerator = abs(self.slope * x - y + self.intercept)
        denominator = (self.slope**2 + 1)
        return numerator / denominator

    def total_perpendicular_distance(self):
        total_distance = 0
        for x, y in self.points:
            total_distance += self.calculate_perpendicular_distance(x, y)
        return total_distance

class OptimizeLineModel(LineModel):
    def __init__(self, slope=0, intercept=0, learning_rate=0.01, iterations=1000):
        super().__init__(slope, intercept)
        self.learning_rate = learning_rate
        self.iterations = iterations

    def optimize(self):
        for _ in range(self.iterations):
            self.gradient_descent_step()

    def gradient_descent_step(self):
        slope_gradient = 0
        intercept_gradient = 0
        n = len(self.points)

        for x, y in self.points:
            distance = self.calculate_perpendicular_distance(x, y)
            slope_gradient += -x * distance / (self.slope**2 + 1)
            intercept_gradient += -distance / (self.slope**2 + 1)

        slope_gradient *= 2 / n
        intercept_gradient *= 2 / n

        self.slope -= self.learning_rate * slope_gradient
        self.intercept -= self.learning_rate * intercept_gradient

# Example usage:
line_model = OptimizeLineModel(learning_rate=0.001, iterations=10000)
line_model.add_point(1, 2)
line_model.add_point(2, 2)
line_model.add_point(3, 4)
line_model.add_point(4, 5)
line_model.optimize()
print("Optimized line parameters:", line_model.get_line_params())

