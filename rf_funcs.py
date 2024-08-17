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