---
description: "Selected geospatial and data science projects: urban heat and green space change in Pekanbaru, oil palm tree counting from UAV imagery, biodiversity data quality tooling for GBIF, and satellite observation coverage for flood monitoring."
keywords:
  - geospatial projects
  - oil palm detection
  - YOLOv8
  - GBIF
  - biodiversity data
  - flood monitoring
  - Sentinel-1
  - Python GIS projects
hide:
  - toc
  - navigation
---

# Projects

Five projects in forestry, remote sensing, and environmental data.

<div class="index-list" markdown>

<div class="index-row" markdown>

<div class="index-num">01</div>

<div class="index-body" markdown>

## [Palm Tree Counting](palm-tree-counting.md)

Oil palm counting from UAV orthophotos with a YOLOv8 detector. The detections are
georeferenced points with crown sizes; 24,966 trees over 310.8 hectares were checked
against a 500 m river setback.

`Python` `YOLOv8` `GDAL` `Colab` `QGIS`

</div>

<div class="index-plate" markdown>

<a href="palm-tree-counting/"><img class="dither-img" src="../assets/images/1bit/palm-1.png" alt="Oil palm crowns detected across a merged orthomosaic" width="280" height="280" loading="lazy"></a>

</div>

</div>

<div class="index-row" markdown>

<div class="index-num">02</div>

<div class="index-body" markdown>

## [BioSift](biosift.md)

A web app for checking GBIF species occurrence records before analysis. It runs ten quality
checks, flags spatial outliers, and exports a Darwin Core Archive. Submitted to the 2026
GBIF Ebbe Nielsen Challenge.

`Python` `Streamlit` `GBIF` `scikit-learn` `folium`

</div>

<div class="index-plate" markdown>

<a href="biosift/"><img class="dither-img" src="../assets/images/1bit/biosift-1.png" alt="The BioSift quality report and map view" width="280" height="157" loading="lazy"></a>

</div>

</div>

<div class="index-row" markdown>

<div class="index-num">03</div>

<div class="index-body" markdown>

## [Flood Coverage](flood-coverage.md)

A measurement of how often Sentinel-1 sees a flood while it is rising, across four river
basins in Europe and Indonesia. It uses one year of acquisition metadata and asks whether a
GloFAS forecast peak can be checked with a satellite pass.

`Python` `STAC` `Sentinel-1` `GloFAS` `JavaScript`

</div>

<div class="index-plate" markdown>

<a href="flood-coverage/"><img class="dither-img" src="../assets/images/1bit/flood-1.png" alt="Coverage figures for the four basins" width="280" height="190" loading="lazy"></a>

</div>

</div>

<div class="index-row" markdown>

<div class="index-num">04</div>

<div class="index-body" markdown>

## [Urban Heat Island](urban-heat-island.md)

Surface temperature across Pekanbaru from Landsat thermal data. A medoid composite and a
regression fill bring clear coverage to 79.9%, with an uncertainty layer. Three intervention
zones are ranked by heat and vegetation loss.

`Python` `Landsat` `Google Earth Engine` `rasterio` `NumPy`

</div>

<div class="index-plate" markdown>

<a href="urban-heat-island/"><img class="dither-img" src="../assets/images/1bit/uhi-1.png" alt="Land surface temperature across Pekanbaru" width="280" height="211" loading="lazy"></a>

</div>

</div>

<div class="index-row" markdown>

<div class="index-num">05</div>

<div class="index-body" markdown>

## [Urban Green Space Change](urban-green-space.md)

Vegetation loss and gain in Kota Pekanbaru between 2019 and 2025, from Sentinel-2 at 20 m.
The analysis covers 62,110 ha, attributes every pixel to a land-cover class, and checks the
result against Landsat.

`Python` `Sentinel-2` `Google Earth Engine` `WorldCover` `Matplotlib`

</div>

<div class="index-plate" markdown>

<a href="urban-green-space/"><img class="dither-img" src="../assets/images/1bit/green-1.png" alt="NDVI change across Kota Pekanbaru" width="280" height="261" loading="lazy"></a>

</div>

</div>

</div>
