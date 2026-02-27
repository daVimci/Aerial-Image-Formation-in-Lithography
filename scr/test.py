# import numpy as np
#
#
# A = [[1, 2], [2, 3]]
# B = [[1, 2], [2, 3]]
#
# H = np.multiply(A, B)
# print(H)


# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def apply_opc(original_layout):
#     # Simulated OPC: In a real OPC tool, this would involve complex algorithms
#     # Here, let's just add a small random offset to each feature for demonstration purposes
#     opc_layout = original_layout + np.random.normal(0, 0.01, original_layout.shape)
#
#     return opc_layout
#
#
# # Example: Creating a simple layout with features
# original_layout = np.zeros((100, 100))
# original_layout[40:60, 30:70] = 1  # Example feature
#
# # Applying OPC
# opc_result = apply_opc(original_layout)
#
# # Plotting the results
# plt.figure(figsize=(8, 4))
#
# plt.subplot(1, 2, 1)
# plt.imshow(original_layout, cmap="gray", origin="upper", interpolation="nearest")
# plt.title("Original Layout")
# plt.colorbar()
#
# plt.subplot(1, 2, 2)
# plt.imshow(opc_result, cmap="gray", origin="upper", interpolation="nearest")
# plt.title("OPC Applied")
# plt.colorbar()
#
# plt.tight_layout()
# plt.show()

# Lx = 1 * 1e-6  # 140 um
# Ly = 1 * 1e-6  # 40 um
# Nx = 2500
# Ny = 1500
#
# # The distance from the slit to the screen
# z = 2 * 1e-8  # 0.2 um
#
# # The wavelength of the light
# wavelength = 300 * 1e-9  # 300 nm
# wavevector = 2 * np.pi / wavelength
#
# print(Lx * Ly / (z * wavelength))

# import numpy as np
# import copy
#
# H = [[1, 2], [3, 4]]
# cop_H = copy.deepcopy(H)
#
# while cop_H[0][1] < 5:
#     cop_H[0][1] = cop_H[0][1] + 1
#     print(H[0][1])
#     print(cop_H[0][1])
