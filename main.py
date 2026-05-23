import lightkurve as lk
import pandas as pd

from src.extract_features import extract_features

target = "AB Dor"

search = lk.search_lightcurve(
    target,
    mission="TESS"
)

lc = search.download()

flux = lc.flux.value

features = extract_features(
    flux
)

table = pd.DataFrame(
    [features]
)

print(
    table
)

table.to_csv(
    "features.csv",
    index=False
)
