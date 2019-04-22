# Test datasets

Please upload tables of **observed** stellar data for test datasets here.
These tables will be fit with various isochrone-fitting methods to compare.


Each dataset should be a whitespace- or comma-separated table, with the following format/content requirements:

* First row is a header row with column names.
* First column is a useful identifier of some sort (no spaces, please; e.g., KIC12345678).
* `ra` and `dec` should be columns.
* Subsequent columns should be observed properties of the star, and associated uncertainty.
* Broadband magnitudes should have a `_mag` tag; e.g., `J_mag`, `G_mag`, etc.
* Other allowed properties are `Teff`, `logg`, `feh`, `parallax`, `density`,
    `nu_max`, `delta_nu`, `<other?>`
* Uncertainties should be labeled `<property>_unc`; e.g., `J_mag_unc`, `parallax_unc`.
* Any other useful information about the star that is not to be treated as an observed property
  (e.g. "single" or "binary") can be called whatever, but should be without an accompanying `_unc`
  column.

Each contributed dataset should be accompanied with a description below explaining what it is, and
where it comes from.

