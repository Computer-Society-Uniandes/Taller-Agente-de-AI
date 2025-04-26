"""
Implementación del agente para la simulación de construcción de casas
"""

import random

class HouseBuilderAgent:
    """Un agente simple que construye casas en un entorno"""
    
    def __init__(self, environment):
        """Inicializa el agente con una referencia a su entorno"""
        self.environment = environment
        self.position = (0, 0)  # El agente comienza en la esquina superior izquierda
        self.resources = 0  # Cuántos recursos ha recolectado el agente
        self.houses_built = 0  # Contador de casas construidas
        self.perception = None
    
    def perceive(self):
        """Observa el estado actual del entorno"""
        self.perception = {
            'position': self.position,
            'resources_available': self.environment.get_resources_at(self.position),
            'suitable_for_house': self.environment.can_build_house_at(self.position),
            'resources_held': self.resources
        }
        return self.perception
    
    def decide(self):
        """Decide qué acción tomar basándose en la percepción"""
        if self.perception['resources_available'] > 0:
            return 'collect'  # Recolectar recursos
        elif self.perception['suitable_for_house'] and self.resources >= 3:
            return 'build'  # Construir casa
        else:
            return 'move'  # Moverse a otra celda
    
    def act(self, action):
        """Ejecuta la acción elegida"""
        if action == 'collect':
            collected = self.environment.collect_resources_at(self.position)
            self.resources += collected
            print(f"El agente recolectó {collected} recursos. Total: {self.resources}")
        
        elif action == 'build':
            if self.resources >= 3:
                self.environment.build_house_at(self.position)
                self.resources -= 3
                self.houses_built += 1
                print(f"¡El agente construyó una casa! Recursos restantes: {self.resources}")
            else:
                print("No hay suficientes recursos para construir una casa.")
        
        elif action == 'move':
            # Estrategia de movimiento simple: moverse aleatoriamente a una celda adyacente
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha, abajo, izquierda, arriba
            dx, dy = random.choice(moves)
            new_x = max(0, min(self.environment.grid_size-1, self.position[0] + dx))
            new_y = max(0, min(self.environment.grid_size-1, self.position[1] + dy))
            self.position = (new_x, new_y)
            print(f"El agente se movió a la posición {self.position}")