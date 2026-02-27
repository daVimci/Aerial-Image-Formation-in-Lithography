import numpy as np
import setup as su
import copy
from scipy.fftpack import fft2, ifft2
from scipy.fftpack import fftshift


def fft_diff_pattern(
    mask_on_sheet: np.ndarray,
    wavevector: float,
    Distance: float,
    sheet_x: np.ndarray,
    sheet_y: np.ndarray,
) -> np.ndarray:
    fourier_transform_on_mask = fft2(
        mask_on_sheet
        * np.exp(1j * wavevector / (2 * Distance) * (sheet_x**2 + sheet_y**2))
    )
    pattern_to_center = fftshift(fourier_transform_on_mask)
    return pattern_to_center


def norm_diff_pattern(fft_diff: np.ndarray) -> np.ndarray:
    abs_on_diff_pattern = np.absolute(fft_diff)
    Int = abs_on_diff_pattern**2
    Int = Int / Int.sum()
    return Int


def norm_aerial_pattern(
    diff_pattern: np.ndarray,
    pupil_on_screen: np.ndarray,
    wavevector: float,
    Distance: float,
    screen_x: np.ndarray,
    screen_y: np.ndarray,
) -> np.ndarray:
    inver_ff_on_diff_pattern = ifft2(
        diff_pattern
        * pupil_on_screen
        * np.exp(1j * wavevector / (2 * Distance) * (screen_x**2 + screen_y**2))
    )
    abs_c1 = np.absolute(inver_ff_on_diff_pattern)
    Intensity = abs_c1**2
    Intensity = Intensity / Intensity.sum()
    return Intensity


def update_num_neighbors(matrix, i, j, num):
    n = len(matrix)
    m = len(matrix[0])

    for x in range(max(0, i - num), min(n, i + num)):
        for y in range(max(0, j - num), min(m, j + num)):
            if (x - i) ** 2 + (y - j) ** 2 < num**2:
                matrix[x][y] = 1


def opc(
    sheet_mask: np.ndarray,
    pupil_on_screen: np.ndarray,
    aerial_image: np.ndarray,
    wavevector: float,
    Distance: float,
    sheet_x: np.ndarray,
    sheet_y: np.ndarray,
    screen_x: np.ndarray,
    screen_y: np.ndarray,
    iter_number: int,
) -> np.ndarray:
    lengthx = len(sheet_mask[0])
    lengthy = len(sheet_mask)
    change_sheet_mask = copy.deepcopy(sheet_mask)
    variance_imag = np.multiply(aerial_image, sheet_mask)
    iter = 0
    while iter < iter_number:
        for i in range(lengthy - 1):
            for j in range(lengthx - 1):
                if sheet_mask[i][j] == 1 and variance_imag[i][j] <= 1e-5:
                    update_num_neighbors(change_sheet_mask, i, j, 10)
        new_diff_pattern = fft_diff_pattern(
            change_sheet_mask, wavevector, Distance, sheet_x, sheet_y
        )
        new_aerial_img = norm_aerial_pattern(
            new_diff_pattern, pupil_on_screen, wavevector, Distance, screen_x, screen_y
        )
        variance_imag = np.multiply(new_aerial_img, sheet_mask)
        iter = iter + 1

    # return change_sheet_mask
    # return sheet_mask
    return variance_imag
