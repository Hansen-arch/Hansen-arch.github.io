---
description: "Selected geospatial and data science projects: oil palm tree counting from UAV imagery, biodiversity data quality tooling for GBIF, satellite observation coverage for flood monitoring, and Python-based spatial workflows."
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

Selected work in geospatial analysis, forestry, and data science.

<div class="grid" markdown>

<div class="project-card" markdown>
![](../assets/images/palm-1.jpg)

**[Palm Tree Counting](palm-tree-counting.md)**

Oil palm tree counting from UAV orthophotos. A YOLOv8 detector runs on a free Colab GPU, detections return as georeferenced points with crown sizes, and 24,966 trees over 310 hectares are counted against a 500 m river setback.

`Python` `YOLOv8` `GDAL` `Colab` `QGIS`

[View Project](palm-tree-counting.md){ .md-button }
</div>

<div class="project-card" markdown>
![](../assets/images/biosift-1.png)

**[BioSift](biosift.md)**

Web app that checks the quality of GBIF species occurrence records. Ten automated quality checks, spatial outlier detection, and Darwin Core Archive export. Built for the 2026 GBIF Ebbe Nielsen Challenge.

`Python` `Streamlit` `GBIF` `scikit-learn` `folium`

[View Project](biosift.md){ .md-button }
</div>

<div class="project-card" markdown>
![](../assets/images/flood-1.png)

**[Flood Coverage](flood-coverage.md)**

Measures how often a Sentinel-1 pass lands inside a flood's rise, across four river basins in Europe and Indonesia, and whether a GloFAS forecast peak can actually be checked. One year of real acquisition metadata, computed locally.

`Python` `STAC` `Sentinel-1` `GloFAS` `JavaScript`

[View Project](flood-coverage.md){ .md-button }
</div>

</div>
