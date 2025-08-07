# Juego de Policía con Pygame

Este proyecto es un ejercicio de aprendizaje para desarrollar videojuegos utilizando Python y la biblioteca Pygame.

## 🎮 Estado Actual del Proyecto

Actualmente el juego cuenta con:
- Un personaje policía controlable
- Movimiento fluido izquierda/derecha
- Animaciones básicas (cambio de sprite según dirección)
- Sistema de límites de pantalla
- Cambio de fondo con espacio

## 🛠️ Tecnologías Utilizadas

- Python
- Pygame
- Sistema de sprites personalizados

## 🎯 Controles

- `A` - Mover a la izquierda
- `D` - Mover a la derecha
- `ESPACIO` - Cambiar color de fondo
- `ESC` o `X` en la ventana - Salir del juego

## 🖼️ Assets

Los recursos gráficos se encuentran en la carpeta `recursos/`:
- `policia_frente.png` - Sprite del policía mirando al frente
- `policia_corriendo_derecha.png` - Sprite del policía corriendo hacia la derecha
- `policia_corriendo_izquierda.png` - Sprite del policía corriendo hacia la izquierda

## 🚀 Características Técnicas

- Resolución: 800x600 píxeles
- FPS: 60
- Velocidad del personaje: 5 unidades/frame
- Colisión con bordes de pantalla implementada

## 🔧 Instalación

1. Clona el repositorio
```bash
git clone https://github.com/Jesb21/Juego1.git
```

2. Crea un entorno virtual
```bash
python -m venv venv
```

3. Activa el entorno virtual
```bash
# En Windows
venv\Scripts\activate

# En Unix o MacOS
source venv/bin/activate
```

4. Instala las dependencias
```bash
pip install pygame
```

## 🎯 Objetivos Futuros

- [ ] Implementar física de salto
- [ ] Agregar obstáculos
- [ ] Implementar sistema de puntuación
- [ ] Agregar efectos de sonido
- [ ] Mejorar las animaciones del personaje

## 👨‍💻 Desarrollo

Este es un proyecto de aprendizaje para familiarizarse con:
- Desarrollo de videojuegos en Python
- Manejo de eventos y entrada de usuario
- Sistemas de animación básica
- Física básica de videojuegos
- Gestión de assets y recursos gráficos

## 📝 Licencia

Este proyecto es de código abierto y está disponible para cualquier persona que quiera aprender sobre desarrollo de juegos con Python y Pygame.
