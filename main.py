import numpy as np
import setup as su
import operate as op
import figure as fg

# ====================================================================
#                    Parametr for the setup
# ====================================================================
# The dimensions of the mask
Lx = 1 * 1e-6  # 140 um
Ly = 1 * 1e-6  # 40 um
Nx = 2500
Ny = 2500

# The distance from the slit to the screen
Distance = 2 * 1e-8  # 10 nm

# The wavelength of the light
wavelength = 300 * 1e-9  # 300 nm
wavevector = 2 * np.pi / wavelength

# slit seperation
nm = 1e-9  # 1e-9 m = 1nm
D = 128 * nm  # 128 nm
# ====================================================================

chsh = su.Sheet(extentX=2 * Lx, extentY=2 * Ly, Nx=Nx, Ny=Ny)
# ===== Construct the mask =====
sheet = su.Sheet(extentX=2 * Lx, extentY=2 * Ly, Nx=Nx, Ny=Ny)
sheet.rectangular_slit(x0=0, y0=-250 * nm, lx=500 * nm, ly=200 * nm)
sheet.rectangular_slit(x0=0, y0=0, lx=200 * nm, ly=300 * nm)
# ===== Construct the mask =====

# ===== The Corresponding mask on screen =====
screen = su.Screen(
    extentX=2 * Lx,
    extentY=2 * Ly,
    Nx=Nx,
    Ny=Ny,
    Distance=1 * 1e-8,
    wavelength=wavelength,
)
screen.construct_pupil(x0=0, y0=0, lx=400 * nm, ly=400 * nm)
# ===== The corresponding mask on screen =====


# =============================================================================
#                      calculate the diffraction pattern
# =============================================================================
diffraction_pattern = op.fft_diff_pattern(
    sheet.mask, wavevector, Distance, sheet.xx, sheet.yy
)
norm_diffraction_pattern = op.norm_diff_pattern(diffraction_pattern)
norm_inv_diff_pattern = op.norm_aerial_pattern(
    diffraction_pattern, screen.pupil, wavevector, Distance, screen.xx, screen.yy
)
# variance = op.opc(
#     sheet.mask,
#     screen.pupil,
#     norm_inv_diff_pattern,
#     wavevector,
#     Distance,
#     sheet.xx,
#     sheet.yy,
#     screen.xx,
#     screen.yy,
#     iter_number=10,
# )
# =============================================================================


if __name__ == "__main__":
    # fg.draw_mask(sheet.mask, Lx, Ly, 1, 1)

    fg.draw_diffraction_pattern(
        norm_diffraction_pattern,
        wavelength,
        Distance,
        Lx,
        Ly,
        Nx,
        Ny,
        scale_x=1e-1,
        scale_y=1e-1,
    )

    # fg.draw_diffraction_pattern(
    #     screen.pupil,
    #     wavelength,
    #     Distance,
    #     Lx,
    #     Ly,
    #     Nx,
    #     Ny,
    #     scale_x=1e-1,
    #     scale_y=1e-1,
    # )

    fg.draw_aerial_image(norm_inv_diff_pattern, Lx, Ly, scale_x=0.5, scale_y=0.5)
    # fg.draw_aerial_image(variance, Lx, Ly, scale_x=0.5, scale_y=0.5)
    # fg.draw_mask(variance, Lx, Ly, 0.5, 0.5)
