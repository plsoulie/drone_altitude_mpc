# Thrust-Based Motion Simulation with Interactive Visualization

This Python script simulates the motion of an object in 3D space under the influence of thrust forces, accounting for drag and gravity. It features an interactive visualization where users can analyze the object's position, velocity, and applied thrusts over time.

## Features

- **Simulation Dynamics**: 
  - Updates position and velocity using applied thrust values.
  - Considers drag (`c`), gravity (`g`), and mass (`m`) in the equations of motion.
- **Interactive Visualization**: 
  - Plots positions, thrusts, and velocities in separate subplots.
  - Includes a slider to scroll through simulation time steps dynamically.

## Requirements

- Python 3.x
- Libraries:
  - `matplotlib`: For plotting results and interactive slider.
  - `numpy`: For numerical computations.

Install required libraries using:
```bash
pip install matplotlib numpy
```

## Code Overview

### Dynamics
The object's motion is calculated using:
- Position updates: 
  \[
  x, y, z += \text{velocity} \cdot \text{time\_step}
  \]
- Velocity updates:
  \[
  v_x, v_y, v_z += \left(\frac{\text{thrust}}{\text{mass}} - \text{drag\_force} - \text{gravity\_force}\right) \cdot \text{time\_step}
  \]

### Data Visualization
- **Position Plot**: Tracks `x`, `y`, and altitude (`z`) over time.
- **Thrust Plot**: Shows thrust values applied in `x`, `y`, and `z` directions.
- **Velocity Plot**: Displays velocities in `x`, `y`, and `z` directions.
- **Interactive Slider**: Adjusts the time step dynamically, updating the plots.

### How to Run
1. Run the script in a Python environment.
2. The plots and slider will appear:
   - Use the slider to explore different time steps.
3. Analyze the trajectory, applied forces, and resulting velocities.

## Customization
- Adjust parameters such as:
  - `m`: Mass of the object.
  - `c`: Drag coefficient.
  - `g`: Gravitational acceleration.
  - `dt`: Time step size.
  - `num_steps`: Number of simulation steps.
- Modify thrust values (`thrust_x_val`, `thrust_y_val`, `thrust_z_val`) for different motion scenarios.

## Example Use Cases
- Analyze motion under specific force conditions.
- Explore the effects of drag and gravity on object dynamics.
- Use as a foundation for more complex motion simulations (e.g., drone flight, spacecraft dynamics).
