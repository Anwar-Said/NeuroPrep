from nilearn.image import load_img
from NeuroPrep import utils
import numpy as np

image_path = "data/raw/1.nii.gz"
regs_path = "data/raw/1.txt"
num_rois = 100
image = load_img(image_path)
fmri = image.get_fdata()


parcels = utils.parcellation(fmri, num_rois)
Y = utils.remove_drifts(parcels)
regs = np.loadtxt(regs_path)
Y = utils.regress_head_motions(Y, regs)
corr = utils.construct_corr(Y)

print(corr.shape)
