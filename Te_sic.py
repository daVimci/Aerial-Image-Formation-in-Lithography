import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# from scipy.integrate import quad


k = 2 * np.pi / (520 * 1e-9)
a = 1e-6
d = 10


# Define the step function
def step_func(x):
    return np.where(np.abs(x) < 0.5, 1.0, 0.0)


# Define the range of x values
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 2000)

# Compute the step function and its Fourier transform
step_values = step_func(x_values)
fourier_transform = fft(step_values)

# Compute the frequencies corresponding to the Fourier transform
frequencies = fftfreq(len(x_values), d=(x_values[1] - x_values[0]))
rivise_freq = frequencies * d / k

# plt.plot(x_values, step_values)
plt.plot(rivise_freq, np.abs(fourier_transform) / d)
plt.show()

# def get_f_FT(f):
#     x_integrand_real = lambda x: np.real(f(x) * np.exp(-2 * np.pi * 1j * x / k))
#     x_integrand_imag = lambda x: np.imag(f(x) * np.exp(-2 * np.pi * 1j * x / k))
#     real = quad(x_integrand_real, -np.inf, np.inf)[0]
#     imag = quad(x_integrand_imag, -np.inf, np.inf)[0]
#     return real + 1j * imag
#
#
# y = np.linspace(-10, 10, 200)
# z = get_f_FT(step(y, -1, 1))
# x = np.linspace(-10, 10, 200)
#
# plt.plot(x, np.abs(z))
# plt.show()

# X, Y = np.meshgrid(x, y)
# Z = intensity(X, Y)
# plt.imshow(Z, cmap="gray")
# plt.colorbar()


# def plot_intensity():
#     x = np.linspace(-10, 10, 200)
#     y = np.linspace(-10, 10, 200)
#     X, Y = np.meshgrid(x, y)
#     Z = intensity(X, Y)
#     plt.imshow(Z, cmap="gray")
#     plt.xticks(np.arange(0, 200, 50), [str(i) for i in np.arange(-10, 10, 5)])
#     plt.yticks(np.arange(0, 200, 50), [str(i) for i in np.arange(-10, 10, 5)])
#     plt.colorbar()
#     plt.show()
#
#
# if __name__ == "__main__":
#     plot_intensity()
