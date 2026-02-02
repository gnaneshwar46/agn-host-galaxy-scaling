print("SCRIPT FILE LOADED")


"""
AGN Host Galaxy - SMBH Scaling Relations
Exploratory analysis using the NASA-Sloan Atlas (NSA)
"""

from astropy.io import fits
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = "data/nsa_v1_0_1.fits"

def main():
    print("Opening NSA FITS file...")

    hdul = fits.open(DATA_PATH)
    data = Table(hdul[1].data)

    print("Number of galaxies:", len(data))
    print("Total number of columns:", len(data.colnames))

    # --------------------------------------------------
    # SMBH PROXY: Sérsic index (SERSIC_N)
    # Purpose: sanity check before using it scientifically
    # --------------------------------------------------

    n = data["SERSIC_N"]

    print("\nSERSIC_N sanity check:")
    print("Min:", np.nanmin(n))
    print("Max:", np.nanmax(n))
    print("Mean:", float(np.nanmean(n)))

    # ----------------------------------------------------
    # Quality cut on SMBH proxy (Sérsic index)
    # ----------------------------------------------------

    good_n = np.isfinite(n) & (n > 0)

    n_clean = n[good_n]

    print("\nAfter SERSIC_N quality cut:")
    print("Number of galaxies:", len(n_clean))

    # -----------------------------------------------------
    # Host galaxy property: stellar mass
    # -----------------------------------------------------

    mstar = data["SERSIC_MASS"]

    good_mass = np.isfinite(mstar) & (mstar > 0)

    # Combined clean sample
    good = good_n & good_mass

    n_clean = n[good]
    mstar_clean = mstar[good]

    logM = np.log10(mstar_clean)

    print("\nStellar mass sanity check:")
    print("Min logM:", logM.min())
    print("Max logM:", logM.max())
    print("Median logM:", float(np.median(logM)))

    # -----------------------------------------------
    # Redshift sanity check
    # -----------------------------------------------

    z = data["Z"][good]

    print("\nRedshift sanity check:")
    print("Min z:", z.min())
    print("Max z:", z.max())
    print("Median z:", float(np.median(z)))

    # -----------------------------------------------
    # SMBH proxy vs host stellar mass (exploratory plot)
    # -----------------------------------------------
    
    plt.figure(figsize=(6,5))
    plt.scatter(logM, n_clean, s = 1, alpha = 0.1)
    plt.xlabel(r"$\log_{10}(M_\star/M_\odot)$")
    plt.ylabel(r"Sérsic index $n$")
    plt.title("SMBH Proxy (Sérsic n) vs Stellar mass")
    plt.tight_layout()
    plt.savefig("figures/sersic_n_vs_mass.png", dpi = 300)
    plt.close()

    print("\nSaved figure: figures/sersic_n_vs_mass.png")

    # --------------------------------------------------
    # Morphology split using Sérsic index
    # --------------------------------------------------

    disk = n_clean < 2.5
    spheroid = n_clean >= 2.5

    print("\nMorphology split:")
    print("Disk-like galaxies (n < 2.5):", disk.sum())
    print("spheroid-like galaxies (n >= 2.5):", spheroid.sum())

    # ------------------------------------------------------
    # SMBH proxy vs stellar mass by morphology (plot)
    # ------------------------------------------------------

    plt.figure(figsize=(6,5))

    plt.scatter(
        logM[disk],
        n_clean[disk],
        s=1,
        alpha=0.1,
        label="Disk-like (n < 2.5)"
    )

    plt.scatter(
        logM[spheroid],
        n_clean[spheroid],
        s=1,
        alpha=0.1,
        label= "Spheroid-like (n ≥ 2.5)"
    )

    plt.xlabel(r"$\log_{10}(M_\star/M_\odot)$")
    plt.ylabel(r"Sérsic index $n$")
    plt.title("SMBH Proxy vs Stellar Mass by Morphology")
    plt.legend(markerscale = 5)
    plt.tight_layout()
    plt.savefig("figures/sersic_n_vs_mass_morphology.png", dpi = 300)
    plt.close()

    print("\nSaved figure: figures/sersic_n_vs_mass_morphology.png")

    # --------------------------------------------------------
    # Median Sérsic index vs stellar mass (quantification)
    # --------------------------------------------------------

    # Define mass bins
    bins = np.arange(8.0, 12.5, 0.25)
    bin_centers = 0.5 * (bins[1:] + bins[:-1])

    def binned_median(x,y, bins):
        med = []
        for i in range(len(bins) - 1):
            mask = (x >= bins[i]) & (x < bins[i + 1])
            if mask.sum() > 10:
                med.append(np.median(y[mask]))
            else:
                med.append(np.nan)
        return np.array(med)
    n_med_disk = binned_median(logM[disk], n_clean[disk], bins)
    n_med_sph = binned_median(logM[spheroid], n_clean[spheroid], bins)

    print("\nComputed binned medians for disk and spheroid populations.")

    # ---------------------------------------------------
    # Plot scatter + median trends
    # ---------------------------------------------------

    plt.figure(figsize=(6,5))

    # Scatter (faint, for context)
    plt.scatter(logM[disk], n_clean[disk], s = 1, alpha = 0.03, color = "tab:blue")
    plt.scatter(logM[spheroid], n_clean[spheroid], s = 1, alpha = 0.03, color = "tab:orange")

    plt.xlabel(r"$\log_{10}(M_\star/M_\odot)$")
    plt.ylabel(r"Sérsic index $n$")
    plt.title("MedianSMBH Proxy vs Stellar Mass by Morphology")
    plt.legend()
    plt.tight_layout()
    plt.savefig("figures/sersic_n_vs_mass_medians.png", dpi = 300)
    plt.close()

    print("\nSaved figure: figures/sersic_n_vs_mass_medians.png")

    hdul.close()

if __name__ == "__main__":
    main()
