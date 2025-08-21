# Archaeology Segmentation and Volume Creation Tool (ArchSV)
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
* Blender 4.5+
* Mesh of archaeological context (ideally whole area)
* Additional functionality with multiple properly aligned meshes

# Documentation
---
## Base Mesh
Object type. Input the mesh that makes up the "cut" of a context. For positive features, this would be the primary mesh.

## Guide Mesh
Object type. Optional input. For negative features, input enclosing mesh, for positive, the mesh of the context underneath.

## Decimation Ratio
Float type. Default value 0.9. Ratio of points remaining in mesh. Smaller, the ration, smaller the no of points. This will speed up calculations but will decrease accuracy.

## XY/Z Variance
Float type. Default value 5.0. Increases selection of points based on the variation of points within the Bezier Curve.

## Normal Segmentation
Boolean type. Groups normals into slope and flat surfaces. Automatically selects slopes.
### Base
Boolean type. Selects flat surfaces in 'Slope Segmentation'.
### Slope Fac
Integer type. The factor with which to separate the slopes from bases.

## Max/Min Z
Float type. 'Z' coordinate input for additional filtering.

## Poly Res
Integer type. Select the number of vertices in the polyline/polygon. This polygon is used as an additional level of filtering for meshes, as well as the capping layer of meshes without 'Guide Mesh' input.
### Translation XYZ
Vector type. Translate polyline/polygon. Useful if missing geometry in 'Base Mesh'

## Output
Menu type. Select between 'Mesh', 'Polyline', 'Polygon', 'SphereVolume', 'VoxelVolume'.
Mesh: Raw mesh
Polyline : polyline mesh.
Polygon: polygonal mesh.
SphereVolume: Iteratively fits a sphere to the raw mesh with the    addition of the 'Guide Mesh' or 'Polygon'.
  
### Volume Resolution
Float type. 

For SphereVolume selects the number of iterations.
For VoxelVolume selects the voxel size.

### Volume Sub Level
Integer type. 

For SphereVolume selects the subdivision level of the sphere.
For VoxelVolume subdivides resulting voxel mesh and fits to raw mesh coordinates.

## Simplify
Boolean type. Selects if distance simplification is required.

### End Resolution
Float type. The max distance between vertices.
