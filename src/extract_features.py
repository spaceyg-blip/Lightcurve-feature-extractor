import numpy as np

def extract_features(
    flux
):

    features = {

        "mean_flux":
        np.mean(flux),

        "std_flux":
        np.std(flux),

        "median_flux":
        np.median(flux),

        "min_flux":
        np.min(flux),

        "max_flux":
        np.max(flux),

        "amplitude":
        np.max(flux)
        -
        np.min(flux),

        "n_points":
        len(flux)

    }

    return features
