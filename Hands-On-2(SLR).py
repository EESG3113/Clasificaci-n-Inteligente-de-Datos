import sys

class SimpleLinearRegression:
    def __init__(self):
        # Dataset hardcoded
        self.data = [
            {"Year": 1, "Sales": 651, "Advertising": 23},
            {"Year": 2, "Sales": 762, "Advertising": 26},
            {"Year": 3, "Sales": 856, "Advertising": 30},
            {"Year": 4, "Sales": 1063, "Advertising": 34},
            {"Year": 5, "Sales": 1190, "Advertising": 43},
            {"Year": 6, "Sales": 1298, "Advertising": 48},
            {"Year": 7, "Sales": 1421, "Advertising": 52},
            {"Year": 8, "Sales": 1440, "Advertising": 57},
            {"Year": 9, "Sales": 1518, "Advertising": 58}
        ]
        
        # Inicializar los coeficientes de la regresión
        self.beta_0 = 0
        self.beta_1 = 0

    def fit(self):
        # Calcular los valores de beta_0 y beta_1 usando el dataset
        n = len(self.data)
        sum_x = sum(d["Advertising"] for d in self.data)
        sum_y = sum(d["Sales"] for d in self.data)
        sum_xy = sum(d["Advertising"] * d["Sales"] for d in self.data)
        sum_x_squared = sum(d["Advertising"] ** 2 for d in self.data)
        
        # Fórmulas para beta_1 y beta_0
        self.beta_1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
        self.beta_0 = (sum_y - self.beta_1 * sum_x) / n

    def predict(self, x):
        # Predecir el valor de Y (Sales) dado un valor de X (Advertising)
        return self.beta_0 + self.beta_1 * x

    def print_regression_equation(self, advertising):
        # Imprimir la ecuación de regresión
        print(f"[+] Ecuación de Regresión: Sales = {self.beta_0:.2f} + {self.beta_1:.2f} * {advertising}\n")

    def run(self):
        # Ajustar el modelo y mostrar la ecuación de regresión
        self.fit()
        
        # Tomar valores de "Advertising" desde la terminal e imprimir predicciones
        try:
            advertising_value = float(input("[*] Ingrese el valor de Advertising para predecir Sales: "))
            prediction = self.predict(advertising_value)
            self.print_regression_equation(advertising_value)
            print(f"[+] Predicción de Sales para Advertising ({advertising_value}): {prediction:.2f}\n")
        except ValueError:
            print("[-] Por favor, ingrese un valor numérico válido para Advertising.\n")


# Clase Main para ejecutar la aplicación
if __name__ == "__main__":
    regression_model = SimpleLinearRegression()
    regression_model.run()
