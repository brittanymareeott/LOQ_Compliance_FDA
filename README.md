# LOQ_Compliance_FDA

In the FDA, a number of studies result in file upon file of datasheets, and many times, these sheets are hard to process in programs such as Microsoft's excel. As a result, small scripts such as these can really speed up analysis. Also, when reporting or studying a certain analyte, such as Arsenic, Cesium-137, or various pesticides, you don't want to wade through line upon line of data that is unnecessary.

Additionally, detection of these analytes usually has a limit depending on what you are looking at, and in what kind of food you are looking at it in. Therefore, Total Diet Studies contain what is call the LOQ, or limit of quantitation. If the concentration of the analyte is below the LOQ, the results are not necessarily reliable, so that anything that registers as "detected", the concentration must be above the LOQ to be considered a valid reading. Therefore, this script will output a file where the LOQ has been considered. As an added parameter, the user has the option of introducing another cutoff score beyond the LOQ (_note: this script will soon backcheck the new cutoff score with the LOQ to ensure that any new cutoff requested is above the LOQ as well and warns the user if their new cutoff is above or below the designated LOQ).

Finally, an additional file is output where all samples that meet the analyte criteria where there was no detection of the analyte (concentration = 0), as this information is just as important.

This script will hopefully speed up data analysis in regards to Total Diet Studies.
