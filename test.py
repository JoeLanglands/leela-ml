import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

def main():
    test_data =  np.load('Wfs_180921_1500_DUN_09000_5000_25.npy')[0]
    wvfm = test_data['wvfmdata']
    fs = 1/test_data['sampleinterval']
    print(fs)
    N_samp = wvfm.size
    
    upsamp_2 = sig.resample(wvfm, N_samp*2)
    up2_x = np.arange(0, 1024, 0.5)
    up3_x = np.arange(0, 1024, 1/3)
    up4_x = np.arange(0, 1024, 0.25)
    
    upsamp_3 = sig.resample(wvfm, N_samp*3)
    upsamp_4 = sig.resample(wvfm, N_samp*4)
    

    #plt.plot(wvfm, 'm-')
    #plt.plot(up2_x, upsamp_2, 'r.')
    #plt.plot(up3_x, upsamp_3, 'g.')
    #plt.plot(up4_x, upsamp_4, 'b.')

    #plt.show()


    fig, ax = plt.subplots(2, 2, figsize=(14,14))

    ax[0][0].plot(wvfm, 'm-')
    ax[0][0].set_title('Original Waveform')

    NPS = 32
    
    f, t, Sxx = sig.spectrogram(wvfm, fs)
    
    ax[1][0].pcolormesh(t, f, Sxx)
    ax[1][0].set_ylabel('Frequency [Hz]')
    ax[1][0].set_xlabel('Time [s]')

    ax[0][1].plot(upsamp_2)
    ax[0][1].set_title('Upsampled (x4)')
    
    f2, t2, Sxx2 = sig.spectrogram(upsamp_4, 4*fs)

    ax[1][1].pcolormesh(t2, f2, Sxx2)
    ax[1][1].set_ylabel('Frequency [Hz]')
    ax[1][1].set_xlabel('Time [s]')
    
    plt.show()

if __name__=='__main__':
    main()
