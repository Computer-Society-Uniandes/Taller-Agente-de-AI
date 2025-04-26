# Agente de IA Simple: Constructor de Casas en AI Group - Computer Society Uniandes

Este proyecto demuestra un agente de IA simple que construye casas en un entorno simulado. Fue creado para un taller de AI Group sobre agentes de IA.

## Descripción del Proyecto

El agente opera en un entorno basado en cuadrícula donde puede:
- Moverse por la cuadrícula
- Recolectar recursos
- Construir casas cuando tiene suficientes recursos

El agente sigue un ciclo simple de percepción-decisión-acción, que es la base de muchas arquitecturas de agentes de IA.

## Cómo Ejecutar

1. Asegúrate de tener Python 3.6+ instalado
2. Navega al directorio del proyecto
3. Ejecuta la simulación:

```
python src/main.py
```

## Entendiendo el Código

- `main.py`: Configura y ejecuta la simulación
- `agent.py`: Implementa la clase HouseBuilderAgent con el ciclo percibir-decidir-actuar
- `environment.py`: Implementa el entorno donde opera el agente

## Ejercicios del Taller

1. Modificar la toma de decisiones del agente para que sea más inteligente (por ejemplo, priorizar celdas con más recursos)
2. Añadir más tipos de acciones que el agente pueda realizar
3. Implementar una visualización utilizando una biblioteca como Pygame
4. Crear múltiples agentes que puedan cooperar o competir