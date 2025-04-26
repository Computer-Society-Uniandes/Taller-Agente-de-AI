"""
Agente de IA Simple para Construir Casas
Un proyecto de demostración para un taller universitario
"""

import random
import time
from agent import HouseBuilderAgent
from environment import BuildingEnvironment

def main():
    """Ejecuta la simulación de construcción de casas"""
    print("Iniciando Simulación del Agente Constructor de Casas")
    
    # Crear el entorno
    environment = BuildingEnvironment(grid_size=10)
    
    # Crear el agente
    agent = HouseBuilderAgent(environment)
    
    # Ejecutar la simulación durante 20 pasos
    for step in range(20):
        print(f"\nPaso {step+1}:")
        agent.perceive()
        action = agent.decide()
        agent.act(action)
        environment.update()
        environment.display()
        time.sleep(0.5)  # Ralentizar la simulación para mejor visibilidad
    
    print("\n¡Simulación completada!")
    print(f"Casas construidas: {agent.houses_built}")

if __name__ == "__main__":
    main()