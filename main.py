from rf_funcs import *

print(f'33dBm is equal to {dbm2w(33):.3f}W')
print(f'30dBm is equal to {dbm2w(30):.3f}W')
print(f'20dBm is equal to {dbm2w(20):.3f}W')
print(f'')

print(f'2W is equal to {w2dbm(2):.0f}dBm')
print(f'1W is equal to {w2dbm(1):.0f}dBm')
print(f'500mW is equal to {w2dbm(.5):.0f}dBm')
print(f'100mW is equal to {w2dbm(.1):.0f}dBm')
print(f'')

print(f'An S/N of 20 dB is equal to {db2lin(20)}')
print(f'An S/N of 10 dB is equal to {db2lin(10)}')
print(f'An S/N of 0 dB is equal to {db2lin(0)}')
print(f'')

B = 20e6    # 20 MHz bandwidth
T = 293     # Kelvin

# f'hanning{num}.pdf'

print(f'For a {B:.0f} Hz bandwidth signal...')
print(f'\tThermal noise floor: {thermal_noise_dbm(B, T):.2f} dBm')
print(f'Assuming:\n\tNoise Figure:\t5 dB\n\tPath loss:\t\t100 dB')
shannon_hartley_theorem_dbm(B, -90, psumm=True)
shannon_hartley_theorem_dbm(B, -90, -90, psumm=True)
shannon_hartley_theorem_dbm(B, -87, -90, psumm=True)
shannon_hartley_theorem_dbm(4e3, -70, -90, psumm=True)
shannon_hartley_theorem_dbm(4e3, -67, -90, psumm=True)
shannon_hartley_theorem_dbm(5e3, -70, -90, psumm=True)

print()

print(pathloss_friis(10000, 2, 50, 1, 1, 900e6))
print(pathloss_tworay(10000, 2, 50, 1, 1, 900e6, -0.9))