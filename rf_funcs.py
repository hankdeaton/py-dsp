import numpy as np

def shannon_hartley_theorem_dbm(B, S, N=None, psumm = False):
    # Shannon-Hartley Theorem for Channel Capacity

    B = float(B)
    S = float(S)

    if N is None:
        N = thermal_noise_dbm(B, 293) + 5
    else:
        N = float(N)

    C = B*np.log2(1 + dbm2w(S)/dbm2w(N))

    if psumm:
        print(f'Given\n\tB: {B:.0f} Hz,\n\tS: {S:.2f} dBm\n\tN: {N:.2f} dBm\nThen\n\tC: {C/1e6:.3f} Mbps\n')

    return C


def thermal_noise_dbm(B, T):
    # Thermal Noise power in dBm

    k = 1.380649E-23    # Boltzmann's constant

    return 10*np.log10(k*T*B/.001)


def dbm2w(dbm):
    # dBm to Watts

    return 10 ** ((dbm - 30) / 10)


def w2dbm(w):
    # Watts to dBm

    return 10*np.log10(w/.001)


def db2lin(db):
    # dB to linear

    return 10 ** (db / 10)


def pathloss_friis(d, h_t, h_r, g_t_db, g_r_db, f_c, r=0):
    # Function that computes Friis Equation Free Space Path Loss

    # Calculate distance of Line of Sight and Reflection paths
    d_los = np.sqrt(d ** 2 + (h_t - h_r) ** 2)

    # calculate wavelength
    wl = 3e8 / f_c

    return 20 * np.log10(wl / (4 * np.pi * d_los)) + g_t_db + g_r_db


def pathloss_tworay(d, h_t, h_r, g_t, g_r, f_c, r):
    # Function that calcualtes path loss via the Two-Ray Model

    g_total = 10 ** ((g_t+g_r)/10)

    # Calculate wavelength
    wl = 3e8 / f_c

    # Calculate distance of Line of Sight and Reflection paths
    d_los = np.sqrt(d ** 2 + (h_t - h_r) ** 2)
    d_ref = np.sqrt(d ** 2 + (h_t + h_r) ** 2)

    # Calculate phase offset between paths
    phi = 2 * np.pi * (d_ref - d_los) / wl

    # Calculate Line of Sight and Reflection coefficients
    los = np.sqrt(g_total) / d_los
    ref = r * (np.sqrt(g_total) * np.exp(-1j*phi)) / d_ref

    # compute path loss
    pl = ((wl / (4*np.pi)) * abs(los+ref)) ** 2
    pl_db = 10*np.log10(pl)

    return pl_db


