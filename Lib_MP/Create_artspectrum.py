import sys
sys.path.append('/home/mathias/sfit-processing-environment/Lib_MP/')
from sfit4_setup import sfit4_ctl
from datetime import datetime as dt

class spectrum():
    def __init__(self,ctl_file='sfit4.ctl'):
        self.ctl = sfit4_ctl()
        self.ctl.read_ctl_file(ctl_file)
        
        
    def art_spectrum(self, sza=0, date = '20000101010101', noise=1000, latitude=0, longitude=0, earth_radius=6357.5476):
        # Creates a spectrum for the microwindows given in sfit.ctl
        # input parameters:
        # the sza
        # date = <YYYYMMDDHHMMSS>
        # noise or SNR (depends if the spectrum is emission or transmission, respectively)
        # latitude
        # longitude
        # earth_radius (in km)

        self.sza = sza
        self.earth_rad = earth_radius
        self.latitude = longitude
        self.longitude = latitude
        self.snr = noise
        self.meas_date = dt.strptime ( date,'%Y%m%d%H%M%S')
        self.comment = 'created by Create_artspectrum'

        max_opd = 0
        spec_name = self.ctl.get_value('file.in.spectrum')
        if spec_name == -1:
            spec_name = 'art_spectrum'
        fid = open(spec_name, 'w')
        
        nr_mw = map(lambda x: int(x), self.ctl.get_value('band').split())
        for nr in nr_mw:
            tmp = '%.2f %.2f %.2f %.2f %.2f' % (self.sza, self.earth_rad, self.latitude, self.longitude, self.snr)
            fid.write(tmp+'\n')
            fid.write(self.meas_date.strftime('%Y %m %d %H %M %S\n'))
            fid.write(self.comment+'\n')
            vstart= self.ctl.get_value('band.{}.nu_start'.format(nr))
            vstop = self.ctl.get_value('band.{}.nu_stop'.format(nr))
            opd = self.ctl.get_value('band.{}.max_opd'.format(nr))
            if vstart == -1 or vstop == -1:
                break
            max_opd = max(float(opd),max_opd)
            self.nu_start = float(vstart)
            self.nu_stop = float(vstop)

            self.nu_res = 0.9/max_opd/10.0
            self.nr_nu = int((self.nu_stop - self.nu_start) / self.nu_res)
            fid.write('%.10f %.10f %.20f %d \n'% 
                      (self.nu_start, self.nu_stop, self.nu_res, self.nr_nu))
        
            for n in range(0,self.nr_nu):
                fid.write('1.0\n')

        fid.close()


        

if __name__ == '__main__':

    import os, sys
    sys.path.append(os.path.dirname(sys.argv[0]))

    sp = spectrum()
    sp.art_spectrum()
    