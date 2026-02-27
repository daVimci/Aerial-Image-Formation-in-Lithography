import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
#                            plot using matplotlib
# =============================================================================
def draw_mask(
    sheet_mask: np.ndarray,
    Lx: float,
    Ly: float,
    scale_x: float,
    scale_y: float,
):
    # ===== Plot the mask =====
    plt.imshow(
        sheet_mask,
        extent=[-Lx, Lx, Ly, -Ly],
        cmap="gray",
    )
    plt.xlim([-Lx * scale_x, Lx * scale_x])
    plt.ylim([-Ly * scale_y, Ly * scale_y])
    # plt.colorbar()
    # ===== Plot the mask =====

    plt.show()


def draw_diffraction_pattern(
    Intensity: np.ndarray,
    wavelength: float,
    Distance: float,
    Lx: float,
    Ly: float,
    Nx: int,
    Ny: int,
    scale_x: float,
    scale_y: float,
):
    # ===== Plot the diffraction pattern =====
    # screen size mm
    dx_screen = Distance * wavelength / (2 * Lx)
    dy_screen = Distance * wavelength / (2 * Ly)
    x_screen = dx_screen * (np.arange(Nx) - Nx // 2)  # 1e3 converts milis to microns
    y_screen = dy_screen * (np.arange(Ny) - Ny // 2)  # 1e3 converts milis to microns

    plt.imshow(
        Intensity,
        # screen.pupil,
        extent=[
            x_screen[0],
            x_screen[-1] + dx_screen,
            y_screen[-1] + dy_screen,
            y_screen[0],
        ],
        cmap="inferno",
        interpolation="bilinear",
        aspect="auto",
    )
    plt.colorbar(label="Intensity", format="%.1e")

    plt.ylabel("y (m)")
    plt.xlabel("x (m)")
    plt.xlim([x_screen[0] * scale_x, x_screen[-1] * scale_x])
    plt.ylim([y_screen[0] * scale_y, y_screen[-1] * scale_y])
    plt.title("Diffraction Pattern")
    # ===== Plot the diffraction pattern =====

    plt.show()


def draw_aerial_image(
    Intensity: np.ndarray, Lx: float, Ly: float, scale_x: float, scale_y: float
):
    # ===== Plot the aerial image =====
    plt.imshow(
        Intensity,
        extent=[-Lx, Lx, Ly, -Ly],
        cmap="gray",
    )
    plt.colorbar(label="Intensity", format="%.1e")
    #
    plt.ylabel("y (m)")
    plt.xlabel("x (m)")
    plt.xlim([-Lx * scale_x, Lx * scale_x])
    plt.ylim([-Ly * scale_y, Ly * scale_y])
    plt.title("Aerial Pattern")
    # ===== Plot the aerial image =====

    # fig = plt.figure(figsize=(6, 6))
    # ax1 = fig.add_subplot(2, 1, 1)
    # ax2 = fig.add_subplot(2, 1, 2, sharex=ax1, yticklabels=[])
    # ax2.plot(x_screen, abs_c[Ny // 2] ** 2, linewidth=1)
    # ax2.set_ylabel("Probability Density $|\psi|^{2}$")
    # ax1.set_xlim([-2, 2])
    # plt.setp(ax1.get_xticklabels(), visible=False)

    plt.show()
