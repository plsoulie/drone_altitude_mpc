# Update positions and velocities based on applied thrusts
    x += velocity_x * dt
    y += velocity_y * dt
    altitude += velocity_z * dt
    velocity_x += (thrust_x_val / m - c * velocity_x) * dt
    velocity_y += (thrust_y_val / m - c * velocity_y) * dt
    velocity_z += (thrust_z_val / m - g - c * velocity_z) * dt

    # Store data for plotting
    x_history.append(x)
    y_history.append(y)
    altitude_history.append(altitude)
    velocity_x_history.append(velocity_x)
    velocity_y_history.append(velocity_y)
    velocity_z_history.append(velocity_z)

# Plot results
fig, axs = plt.subplots(3, 1, figsize=(12, 12))
plt.subplots_adjust(bottom=0.25)

# Initial plots
line1, = axs[0].plot(x_history, label="x Position")
line2, = axs[0].plot(y_history, label="y Position")
line3, = axs[0].plot(altitude_history, label="Altitude (z)")
axs[0].set_title("Position vs. Time")
axs[0].legend()

line4, = axs[1].plot(thrust_x_history, label="Thrust x")
line5, = axs[1].plot(thrust_y_history, label="Thrust y")
line6, = axs[1].plot(thrust_z_history, label="Thrust z")
axs[1].set_title("Thrust vs. Time")
axs[1].legend()

line7, = axs[2].plot(velocity_x_history, label="Velocity x")
line8, = axs[2].plot(velocity_y_history, label="Velocity y")
line9, = axs[2].plot(velocity_z_history, label="Velocity z")
axs[2].set_title("Velocity vs. Time")
axs[2].legend()

# Slider for scrolling through time steps
ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03])  # Position of the slider
slider = Slider(ax_slider, 'Time Step', 0, num_steps - 1, valinit=0, valstep=1)

def update(val):
    step = int(slider.val)
    # Update the plots based on the current step
    line1.set_ydata(x_history[step])
    line2.set_ydata(y_history[step])
    line3.set_ydata(altitude_history[step])
    line4.set_ydata(thrust_x_history[step])
    line5.set_ydata(thrust_y_history[step])
    line6.set_ydata(thrust_z_history[step])
    line7.set_ydata(velocity_x_history[step])
    line8.set_ydata(velocity_y_history[step])
    line9.set_ydata(velocity_z_history[step])
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.tight_layout()
plt.show()
