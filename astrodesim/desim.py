from astrodesim import upload_fits as fits
from astrodesim import is_small as small
from astrodesim import resize_smalltolarge as resize
from astrodesim import spectral_index_map as alpha
from astrodesim import make_image as im

def map(file1, file2):
    """
    Function takes two FITS files of the same object at different wavelengths
    and outputs a dust emission spectral index map

    Args: 
        file1 (str): path to FITS file1 of object observed at one wavelength
        file2 (str): path to FITS file2 of same object observed at a different wavelength
    """
    header1, sim_data1 = fits.upload_fits(file1) 
    header2, sim_data2 = fits.upload_fits(file2)

    smallim, deltapix1, new_header, bigim, new_dim, deltapix2, bigheader = small.is_small(sim_data1, sim_data2, header1, header2)

    new_im = resize.resize_smalltolarge(smallim, deltapix1, new_dim, deltapix2)

    desim = alpha.spectral_index_map(new_im, bigim, new_header, bigheader)

    im.make_image(desim)
