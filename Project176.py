import speedtest as spdt
import matplotlib.pyplot as plt
import time

downSpds = []
upSpds = []
x = list(range(1, 6))

downSpd = 0
upSpd = 0

for i in range(2):
    st = spdt.Speedtest()
    
    downSpd = round(st.download() / 10 ** 6, 2)
    upSpd = round(st.upload() / 10 ** 6, 2)
    downSpds.append(downSpd)
    upSpds.append(upSpd)

    print(f'Tick { i }:')
    print(f'* Download Speeds: { downSpds }')
    print(f'* Upload Speeds: { upSpds }')

plt.plot(x, downSpds, label = 'Download Speeds')
plt.plot(x, downSpds, label = 'Upload Speeds')
plt.title('Internet Speed')
plt.legend()
plt.show()