# AGN Host Galaxy - SMBH Scaling Relations

This project investigates how supermassive black hole(SMBH) growth relates to host galaxy properties in the local universe, using data from the NASA-Sloan Atlas(NSA).

Rather than assuming a universal SMBH-host scaling relation, the analysis demonstrates that galaxy structure and morphology are the primary drivers of the observed trends. By combining a Sérsic-index based SMBH scaling relations emerge mainly in bulge-dominated galaxies, while disk-dominated systems follow a distinct evolutionary path.

The analysis is fully reproducible and is intended as a research-grade, portfolio-ready study suitable for PhD preparation and galaxy evolution work.

## agn-host-galaxy-scaling
Observational analysis of AGN host galaxy scaling relations using SDSS and NASA-Sloan Atlas data.

## Goal:
Investigate how AGN host galaxies differ from inactive galaxies in their stellar mass-size relation.

## Status:
Data ingestion and sample definition.

## Project structure

- `data/` -  raw and processed data (not tracked in Git)
- `scripts/` - analysis scripts
- `figures/` - generated plots and figures

## SMBH Proxy Analysis: Sérsic Index vs Stellar Mass

Because direct supermassive black hole masses are not available for most galaxies in the NSA, we use the Sérsic index ($n$) as a structural proxy for bulge dominance, which is empirically linked to SMBH growth.

### Global behaviour

When all galaxies are considered together, the Sérsic index shows a broad, scattered increase with stellar mass. However, this apparent trend is not fundamental and is driven by the mixing of structurally distinct galaxy populations.

### Morphology-dependent behaviour

Separating galaxies by Sérsic index reveals two clearly different regimes:

- **Disk-like galaxies ($n < 2.5$)**  
  These systems occupy a nearly horizontal band in Sérsic index across a wide stellar mass range. Even massive disk galaxies retain low $n$ values, indicating weak bulge growth and, by implication, inefficient SMBH growth.

- **Spheroid-like galaxies ($n \ge 2.5$)**  
  These systems show a clear increase in Sérsic index with stellar mass and significantly reduced scatter. This population defines the classical SMBH–host scaling relations seen in the literature.

### Physical interpretation

The results demonstrate that SMBH–host galaxy scaling relations are not universal. Instead, they primarily arise in bulge-dominated galaxies, while disk-dominated systems follow a different evolutionary path. The large scatter seen in global relations is largely a consequence of combining these two populations.

## Unified Interpretation: Galaxy Structure as the Primary Driver

Across both projects, galaxy structure emerges as the primary organizing parameter of the observed scaling relations. In the mass-size analysis, the large scatter in the global relation is largely resolved by separating disk and bulge dominated systems using the Sérsic index, revealing two distinct and internally tight relations.

In the SMBH proxy analysis, the same structural division explains the residual scatter at fixed stellar mass: disk-dominated galaxies maintain low central concentrations over a wide mass range, while bulge-dominated system show systematically increasing concentration and tighter SMBH proxy correlations. 

Taken together, these results indicate that stellar mass alone is insufficient to describe galaxy or black hole growth. Instead, bulge formation marks a key evolutionary bifurcation, with the commonly reported global scaling relations arising primarily from the superposition of structurally distinct galaxy populations.

## Redshift sanity check

The redshift distribution of the cleaned sample spans $-0.004 \lesssim z \lesssim 0.15$, with a median redshift of $z \approx 0.085$. The small number of negative redshifts is expected for very nearby galaxies due to peculiar velocities.

This confirms that the observed morphology-dependent SMBH proxy trends are not driven by distance-related systematics or resolution effects, but reflect intrinsic differences in galaxy structure.