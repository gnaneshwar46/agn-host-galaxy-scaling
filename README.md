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
