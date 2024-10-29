# Archaeology Segmentation and Volume Creation Tool (ArchSandV)
---
## Description:
This tool is designed to simplify the creation of volumes for discrete archaeological features. Can be integrated with the Blender GIS addon to allow for reimporting into a GIS, maintaining georeferencing for meshes. Can be used in conjunction with 3D print addon to allow volume calculation.

## Instructions:
* Add a Bezier Curve to the scene
* Enter edit mode and delete all control points
* Switch to draw mode and surface projection
* Draw a circle in a central location of the context
* Exit edit mode
* Go to Geometry Nodes tab and Add>ArchSandV
* Add the base mesh (guide mesh optional) and fine tune filtering to make proper selection
* Choose output type
* Choose resolution and simplification
* Convert curve to mesh

## Use-cases:
* Semi-automated polyline/polygon creation
* Semi-automated volumetric mesh creation
**Future directions:**
* Distance-based context segmentation
* Automated hachure drawings
* Colour assisted filtering
* Texture manipulation

## Requirements
* Blender 4.2+
* Mesh of archaeological context (ideally whole area)
* Additional functionality with multiple properly aligned meshes
