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

Five projects, each built to answer a question that existing maps or dashboards did not.
The numbers on their pages come from the projects themselves.

<div class="index-list" markdown>

<div class="index-row" markdown>

<div class="index-num">01</div>

<div class="index-body" markdown>

## [Palm Tree Counting](palm-tree-counting.md)

Oil palm tree counting from UAV orthophotos. A YOLOv8 detector runs on a free Colab GPU,
detections return as georeferenced points with crown sizes, and 24,966 trees over 310
hectares are counted against a 500 m river setback.

`Python` `YOLOv8` `GDAL` `Colab` `QGIS`

</div>

<div class="index-plate" markdown>

[![Oil palm crowns detected across a merged orthomosaic](../assets/images/palm-1.jpg)](palm-tree-counting.md)

</div>

</div>

<div class="index-row" markdown>

<div class="index-num">02</div>

<div class="index-body" markdown>

## [BioSift](biosift.md)

Web app that checks the quality of GBIF species occurrence records. Ten automated quality
checks, spatial outlier detection, and Darwin Core Archive export. Built for the 2026 GBIF
Ebbe Nielsen Challenge.

`Python` `Streamlit` `GBIF` `scikit-learn` `folium`

</div>

<div class="index-plate" markdown>

[![The BioSift quality report and map view](../assets/images/biosift-1.png)](biosift.md)

</div>

</div>

<div class="index-row" markdown>

<div class="index-num">03</div>

<div class="index-body" markdown>

## [Flood Coverage](flood-coverage.md)

Measures how often a Sentinel-1 pass lands inside a flood's rise, across four river basins
in Europe and Indonesia, and whether a GloFAS forecast peak can actually be checked. One
year of real acquisition metadata, computed locally.

`Python` `STAC` `Sentinel-1` `GloFAS` `JavaScript`

</div>

<div class="index-plate" markdown>

[![Coverage figures for the four basins](../assets/images/flood-1.png)](flood-coverage.md)

</div>

</div>

<div class="index-row" markdown>

<div class="index-num">04</div>

<div class="index-body" markdown>

## [Urban Heat Island](urban-heat-island.md)

Surface heat across Pekanbaru from Landsat thermal data. A medoid composite closed with
per-pixel regression raises clear coverage to 79.9%, ships its own uncertainty layer, and
ranks three intervention zones on heat and vegetation loss.

`Python` `Landsat` `Google Earth Engine` `rasterio` `NumPy`

</div>

<div class="index-plate" markdown>

[![Land surface temperature across Pekanbaru](../assets/images/uhi-1.jpg)](urban-heat-island.md)

</div>

</div>

<div class="index-row" markdown>

<div class="index-num">05</div>

<div class="index-body" markdown>

## [Urban Green Space Change](urban-green-space.md)

Where Kota Pekanbaru lost and gained vegetation between 2019 and 2025, from Sentinel-2 at
20 m. 62,110 ha analysed, every pixel attributed to a land-cover class, and the result
tested against a second sensor.

`Python` `Sentinel-2` `Google Earth Engine` `WorldCover` `Matplotlib`

</div>

<div class="index-plate" markdown>

[![NDVI change across Kota Pekanbaru](../assets/images/green-1.jpg)](urban-green-space.md)

</div>

</div>

</div>
