"""
Implementación del entorno para la simulación de construcción de casas
"""

import random

class BuildingEnvironment:
    """Entorno donde el agente puede recolectar recursos y construir casas"""
    
    def __init__(self, grid_size=10):
        """Inicializa el entorno con una cuadrícula del tamaño especificado"""
        self.grid_size = grid_size
        # Las celdas de la cuadrícula contienen: (recursos, tiene_casa)
        self.grid = [[(random.randint(0, 2), False) for _ in range(grid_size)] 
                     for _ in range(grid_size)]
    
    def get_resources_at(self, position):
        """Devuelve la cantidad de recursos en la posición dada"""
        x, y = position
        return self.grid[y][x][0]
    
    def collect_resources_at(self, position):
        """Recolecta recursos en la posición dada y devuelve la cantidad recolectada"""
        x, y = position
        resources = self.grid[y][x][0]
        # Establece los recursos a 0 después de la recolección
        self.grid[y][x] = (0, self.grid[y][x][1])
        return resources
    
    def can_build_house_at(self, position):
        """Verifica si se puede construir una casa en la posición dada"""
        x, y = position
        # Se puede construir si no hay recursos y no hay una casa ya
        return self.grid[y][x][0] == 0 and not self.grid[y][x][1]
    
    def build_house_at(self, position):
        """Construye una casa en la posición dada"""
        x, y = position
        self.grid[y][x] = (0, True)  # Sin recursos, tiene casa
    
    def update(self):
        """Actualiza el entorno (por ejemplo, los recursos pueden volver a crecer)"""
        # Regeneración simple: pequeña probabilidad de que las celdas vacías ganen recursos
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.grid[y][x][0] == 0 and not self.grid[y][x][1]:  # Sin recursos, sin casa
                    if random.random() < 0.1:  # 10% de probabilidad
                        self.grid[y][x] = (1, False)  # Añade 1 recurso
    
    def display(self):
        """Muestra el estado actual del entorno"""
        for y in range(self.grid_size):
            row = ""
            for x in range(self.grid_size):
                resources, has_house = self.grid[y][x]
                if has_house:
                    cell = "H"  # Casa
                elif resources > 0:
                    cell = str(resources)  # Cantidad de recursos
                else:
                    cell = "."  # Vacío
                row += cell + " "
            print(row)