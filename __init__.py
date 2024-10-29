bl_info = {
	"name" : "Arch SandV",
				"description" : "Edge and volume creation for arch features",
	"author" : "Benedict Dyson",
	"version" : (1, 0, 0),
	"blender" : (4, 2, 3),
	"location" : "Node",
	"category" : "Geometry Nodes",
}

import bpy
import mathutils
import os

class Arch_SandV(bpy.types.Operator):
	bl_idname = "node.arch_sandv"
	bl_label = "Arch SandV"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize nodegroup_001 node group
		def nodegroup_001_node_group():
			nodegroup_001 = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "NodeGroup.001")

			nodegroup_001.color_tag = 'NONE'
			nodegroup_001.description = ""

			nodegroup_001.is_modifier = True
			
			#nodegroup_001 interface
			#Socket Output
			output_socket = nodegroup_001.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			output_socket.attribute_domain = 'POINT'
			
			#Socket Target
			target_socket = nodegroup_001.interface.new_socket(name = "Target", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			target_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = nodegroup_001.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketVector')
			value_socket.default_value = (0.0, 0.0, 0.0)
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket Iterations
			iterations_socket = nodegroup_001.interface.new_socket(name = "Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			iterations_socket.default_value = 35
			iterations_socket.min_value = 0
			iterations_socket.max_value = 2147483647
			iterations_socket.subtype = 'NONE'
			iterations_socket.attribute_domain = 'POINT'
			
			#Socket Shphere resolution
			shphere_resolution_socket = nodegroup_001.interface.new_socket(name = "Shphere resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			shphere_resolution_socket.default_value = 6
			shphere_resolution_socket.min_value = 0
			shphere_resolution_socket.max_value = 6
			shphere_resolution_socket.subtype = 'NONE'
			shphere_resolution_socket.attribute_domain = 'POINT'
			
			
			#initialize nodegroup_001 nodes
			#node Cube
			cube = nodegroup_001.nodes.new("GeometryNodeMeshCube")
			cube.name = "Cube"
			#Size
			cube.inputs[0].default_value = (1.0, 1.0, 1.0)
			#Vertices X
			cube.inputs[1].default_value = 2
			#Vertices Y
			cube.inputs[2].default_value = 2
			#Vertices Z
			cube.inputs[3].default_value = 2
			
			#node Transform Geometry
			transform_geometry = nodegroup_001.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.mode = 'COMPONENTS'
			#Rotation
			transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Attribute Statistic
			attribute_statistic = nodegroup_001.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic.name = "Attribute Statistic"
			attribute_statistic.data_type = 'FLOAT_VECTOR'
			attribute_statistic.domain = 'POINT'
			#Selection
			attribute_statistic.inputs[1].default_value = True
			
			#node Position
			position = nodegroup_001.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Vector Math
			vector_math = nodegroup_001.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001 = nodegroup_001.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'LENGTH'
			
			#node Combine XYZ
			combine_xyz = nodegroup_001.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz.name = "Combine XYZ"
			
			#node Vector Math.002
			vector_math_002 = nodegroup_001.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'MULTIPLY'
			
			#node Group Output
			group_output = nodegroup_001.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Subdivision Surface
			subdivision_surface = nodegroup_001.nodes.new("GeometryNodeSubdivisionSurface")
			subdivision_surface.name = "Subdivision Surface"
			subdivision_surface.boundary_smooth = 'ALL'
			subdivision_surface.uv_smooth = 'PRESERVE_BOUNDARIES'
			#Edge Crease
			subdivision_surface.inputs[2].default_value = 0.0
			#Vertex Crease
			subdivision_surface.inputs[3].default_value = 0.0
			
			#node Group Input
			group_input = nodegroup_001.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Repeat Input
			repeat_input = nodegroup_001.nodes.new("GeometryNodeRepeatInput")
			repeat_input.name = "Repeat Input"
			#node Set Position
			set_position = nodegroup_001.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Position.001
			position_001 = nodegroup_001.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Mix
			mix = nodegroup_001.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#Factor_Float
			mix.inputs[0].default_value = 0.8999999761581421
			
			#node Geometry Proximity
			geometry_proximity = nodegroup_001.nodes.new("GeometryNodeProximity")
			geometry_proximity.name = "Geometry Proximity"
			geometry_proximity.target_element = 'FACES'
			#Group ID
			geometry_proximity.inputs[1].default_value = 0
			#Source Position
			geometry_proximity.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Sample Group ID
			geometry_proximity.inputs[3].default_value = 0
			
			#node Dual Mesh
			dual_mesh = nodegroup_001.nodes.new("GeometryNodeDualMesh")
			dual_mesh.name = "Dual Mesh"
			#Keep Boundaries
			dual_mesh.inputs[1].default_value = False
			
			#node Repeat Output
			repeat_output = nodegroup_001.nodes.new("GeometryNodeRepeatOutput")
			repeat_output.name = "Repeat Output"
			repeat_output.active_index = 0
			repeat_output.inspection_index = 0
			repeat_output.repeat_items.clear()
			# Create item "Geometry"
			repeat_output.repeat_items.new('GEOMETRY', "Geometry")
			
			#node Mesh to Volume
			mesh_to_volume = nodegroup_001.nodes.new("GeometryNodeMeshToVolume")
			mesh_to_volume.name = "Mesh to Volume"
			mesh_to_volume.resolution_mode = 'VOXEL_AMOUNT'
			#Density
			mesh_to_volume.inputs[1].default_value = 1.0
			#Voxel Amount
			mesh_to_volume.inputs[3].default_value = 128.0
			#Interior Band Width
			mesh_to_volume.inputs[4].default_value = 0.10000000149011612
			
			#node Volume to Mesh
			volume_to_mesh = nodegroup_001.nodes.new("GeometryNodeVolumeToMesh")
			volume_to_mesh.name = "Volume to Mesh"
			volume_to_mesh.resolution_mode = 'GRID'
			#Threshold
			volume_to_mesh.inputs[3].default_value = 0.10000000149011612
			#Adaptivity
			volume_to_mesh.inputs[4].default_value = 0.0
			
			#node Set Position.002
			set_position_002 = nodegroup_001.nodes.new("GeometryNodeSetPosition")
			set_position_002.name = "Set Position.002"
			#Selection
			set_position_002.inputs[1].default_value = True
			#Offset
			set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			
			#Process zone input Repeat Input
			repeat_input.pair_with_output(repeat_output)
			
			
			
			
			#Set locations
			cube.location = (-1613.4854736328125, 775.5514526367188)
			transform_geometry.location = (-794.30908203125, 539.7982788085938)
			attribute_statistic.location = (-1762.3712158203125, 503.6514587402344)
			position.location = (-1764.99072265625, 168.2726287841797)
			vector_math.location = (-1602.598876953125, 424.02044677734375)
			vector_math_001.location = (-1414.3858642578125, 394.0818176269531)
			combine_xyz.location = (-1238.4346923828125, 419.05889892578125)
			vector_math_002.location = (-1017.0291748046875, 372.63262939453125)
			group_output.location = (2596.6474609375, -27.902938842773438)
			subdivision_surface.location = (-626.1663818359375, 528.8346557617188)
			group_input.location = (-2011.2294921875, 4.220835208892822)
			repeat_input.location = (241.62359619140625, 438.03863525390625)
			set_position.location = (450.811767578125, 418.271728515625)
			position_001.location = (-81.18180847167969, 72.5733642578125)
			mix.location = (167.36700439453125, 231.65232849121094)
			geometry_proximity.location = (-79.62028503417969, 250.5527801513672)
			dual_mesh.location = (660.311767578125, 390.2865905761719)
			repeat_output.location = (844.30126953125, 458.767578125)
			mesh_to_volume.location = (1032.3992919921875, 382.8833312988281)
			volume_to_mesh.location = (1275.4102783203125, 333.3008117675781)
			set_position_002.location = (1473.3026123046875, 288.8031311035156)
			
			#Set dimensions
			cube.width, cube.height = 140.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			combine_xyz.width, combine_xyz.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			subdivision_surface.width, subdivision_surface.height = 150.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			repeat_input.width, repeat_input.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			geometry_proximity.width, geometry_proximity.height = 140.0, 100.0
			dual_mesh.width, dual_mesh.height = 140.0, 100.0
			repeat_output.width, repeat_output.height = 140.0, 100.0
			mesh_to_volume.width, mesh_to_volume.height = 200.0, 100.0
			volume_to_mesh.width, volume_to_mesh.height = 170.0, 100.0
			set_position_002.width, set_position_002.height = 140.0, 100.0
			
			#initialize nodegroup_001 links
			#cube.Mesh -> transform_geometry.Geometry
			nodegroup_001.links.new(cube.outputs[0], transform_geometry.inputs[0])
			#vector_math.Vector -> vector_math_001.Vector
			nodegroup_001.links.new(vector_math.outputs[0], vector_math_001.inputs[0])
			#position_001.Position -> mix.B
			nodegroup_001.links.new(position_001.outputs[0], mix.inputs[5])
			#position.Position -> attribute_statistic.Attribute
			nodegroup_001.links.new(position.outputs[0], attribute_statistic.inputs[2])
			#transform_geometry.Geometry -> subdivision_surface.Mesh
			nodegroup_001.links.new(transform_geometry.outputs[0], subdivision_surface.inputs[0])
			#mesh_to_volume.Volume -> volume_to_mesh.Volume
			nodegroup_001.links.new(mesh_to_volume.outputs[0], volume_to_mesh.inputs[0])
			#geometry_proximity.Position -> mix.A
			nodegroup_001.links.new(geometry_proximity.outputs[0], mix.inputs[4])
			#mix.Result -> set_position.Position
			nodegroup_001.links.new(mix.outputs[1], set_position.inputs[2])
			#attribute_statistic.Max -> vector_math.Vector
			nodegroup_001.links.new(attribute_statistic.outputs[4], vector_math.inputs[0])
			#attribute_statistic.Min -> vector_math.Vector
			nodegroup_001.links.new(attribute_statistic.outputs[3], vector_math.inputs[1])
			#group_input.Target -> attribute_statistic.Geometry
			nodegroup_001.links.new(group_input.outputs[0], attribute_statistic.inputs[0])
			#vector_math_001.Value -> combine_xyz.X
			nodegroup_001.links.new(vector_math_001.outputs[1], combine_xyz.inputs[0])
			#vector_math_001.Value -> combine_xyz.Y
			nodegroup_001.links.new(vector_math_001.outputs[1], combine_xyz.inputs[1])
			#vector_math_001.Value -> combine_xyz.Z
			nodegroup_001.links.new(vector_math_001.outputs[1], combine_xyz.inputs[2])
			#combine_xyz.Vector -> vector_math_002.Vector
			nodegroup_001.links.new(combine_xyz.outputs[0], vector_math_002.inputs[0])
			#vector_math_002.Vector -> transform_geometry.Scale
			nodegroup_001.links.new(vector_math_002.outputs[0], transform_geometry.inputs[3])
			#group_input.Value -> vector_math_002.Vector
			nodegroup_001.links.new(group_input.outputs[1], vector_math_002.inputs[1])
			#set_position.Geometry -> dual_mesh.Mesh
			nodegroup_001.links.new(set_position.outputs[0], dual_mesh.inputs[0])
			#group_input.Target -> geometry_proximity.Geometry
			nodegroup_001.links.new(group_input.outputs[0], geometry_proximity.inputs[0])
			#subdivision_surface.Mesh -> repeat_input.Geometry
			nodegroup_001.links.new(subdivision_surface.outputs[0], repeat_input.inputs[1])
			#group_input.Iterations -> repeat_input.Iterations
			nodegroup_001.links.new(group_input.outputs[2], repeat_input.inputs[0])
			#repeat_input.Geometry -> set_position.Geometry
			nodegroup_001.links.new(repeat_input.outputs[0], set_position.inputs[0])
			#dual_mesh.Dual Mesh -> repeat_output.Geometry
			nodegroup_001.links.new(dual_mesh.outputs[0], repeat_output.inputs[0])
			#attribute_statistic.Median -> transform_geometry.Translation
			nodegroup_001.links.new(attribute_statistic.outputs[1], transform_geometry.inputs[1])
			#volume_to_mesh.Mesh -> set_position_002.Geometry
			nodegroup_001.links.new(volume_to_mesh.outputs[0], set_position_002.inputs[0])
			#geometry_proximity.Position -> set_position_002.Position
			nodegroup_001.links.new(geometry_proximity.outputs[0], set_position_002.inputs[2])
			#repeat_output.Geometry -> mesh_to_volume.Mesh
			nodegroup_001.links.new(repeat_output.outputs[0], mesh_to_volume.inputs[0])
			#group_input.Shphere resolution -> subdivision_surface.Level
			nodegroup_001.links.new(group_input.outputs[3], subdivision_surface.inputs[1])
			#set_position_002.Geometry -> group_output.Output
			nodegroup_001.links.new(set_position_002.outputs[0], group_output.inputs[0])
			return nodegroup_001

		nodegroup_001 = nodegroup_001_node_group()

		#initialize nodegroup_003 node group
		def nodegroup_003_node_group():
			nodegroup_003 = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "NodeGroup.003")

			nodegroup_003.color_tag = 'NONE'
			nodegroup_003.description = ""

			nodegroup_003.is_modifier = True
			
			#nodegroup_003 interface
			#Socket Geometry
			geometry_socket = nodegroup_003.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = nodegroup_003.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Voxel Amount
			voxel_amount_socket = nodegroup_003.interface.new_socket(name = "Voxel Amount", in_out='INPUT', socket_type = 'NodeSocketFloat')
			voxel_amount_socket.default_value = 384.0
			voxel_amount_socket.min_value = 0.0
			voxel_amount_socket.max_value = 3.4028234663852886e+38
			voxel_amount_socket.subtype = 'NONE'
			voxel_amount_socket.attribute_domain = 'POINT'
			
			#Socket Level
			level_socket = nodegroup_003.interface.new_socket(name = "Level", in_out='INPUT', socket_type = 'NodeSocketInt')
			level_socket.default_value = 1
			level_socket.min_value = 0
			level_socket.max_value = 6
			level_socket.subtype = 'NONE'
			level_socket.attribute_domain = 'POINT'
			
			
			#initialize nodegroup_003 nodes
			#node Geometry Proximity
			geometry_proximity_1 = nodegroup_003.nodes.new("GeometryNodeProximity")
			geometry_proximity_1.name = "Geometry Proximity"
			geometry_proximity_1.target_element = 'FACES'
			#Group ID
			geometry_proximity_1.inputs[1].default_value = 0
			#Source Position
			geometry_proximity_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Sample Group ID
			geometry_proximity_1.inputs[3].default_value = 0
			
			#node Mesh to Volume
			mesh_to_volume_1 = nodegroup_003.nodes.new("GeometryNodeMeshToVolume")
			mesh_to_volume_1.name = "Mesh to Volume"
			mesh_to_volume_1.resolution_mode = 'VOXEL_SIZE'
			#Density
			mesh_to_volume_1.inputs[1].default_value = 1.0
			#Interior Band Width
			mesh_to_volume_1.inputs[4].default_value = 0.0
			
			#node Group Output
			group_output_1 = nodegroup_003.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Set Position
			set_position_1 = nodegroup_003.nodes.new("GeometryNodeSetPosition")
			set_position_1.name = "Set Position"
			#Selection
			set_position_1.inputs[1].default_value = True
			#Offset
			set_position_1.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Merge by Distance
			merge_by_distance = nodegroup_003.nodes.new("GeometryNodeMergeByDistance")
			merge_by_distance.name = "Merge by Distance"
			merge_by_distance.mode = 'ALL'
			#Selection
			merge_by_distance.inputs[1].default_value = True
			#Distance
			merge_by_distance.inputs[2].default_value = 0.05000000074505806
			
			#node Volume to Mesh
			volume_to_mesh_1 = nodegroup_003.nodes.new("GeometryNodeVolumeToMesh")
			volume_to_mesh_1.name = "Volume to Mesh"
			volume_to_mesh_1.resolution_mode = 'VOXEL_SIZE'
			#Threshold
			volume_to_mesh_1.inputs[3].default_value = 1.0000000116860974e-07
			#Adaptivity
			volume_to_mesh_1.inputs[4].default_value = 0.0
			
			#node Group Input
			group_input_1 = nodegroup_003.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Math
			math = nodegroup_003.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'DIVIDE'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 500.0
			
			#node Subdivide Mesh
			subdivide_mesh = nodegroup_003.nodes.new("GeometryNodeSubdivideMesh")
			subdivide_mesh.name = "Subdivide Mesh"
			
			
			
			
			#Set locations
			geometry_proximity_1.location = (21.6322021484375, 130.75357055664062)
			mesh_to_volume_1.location = (-156.89674377441406, -203.3596649169922)
			group_output_1.location = (996.32763671875, -6.402298450469971)
			set_position_1.location = (543.8839111328125, -25.98114013671875)
			merge_by_distance.location = (-289.9984436035156, 217.69677734375)
			volume_to_mesh_1.location = (64.85460662841797, -101.37010955810547)
			group_input_1.location = (-652.0271606445312, -17.44196128845215)
			math.location = (-426.9098205566406, -65.9204330444336)
			subdivide_mesh.location = (316.2466125488281, -106.52388763427734)
			
			#Set dimensions
			geometry_proximity_1.width, geometry_proximity_1.height = 140.0, 100.0
			mesh_to_volume_1.width, mesh_to_volume_1.height = 200.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			set_position_1.width, set_position_1.height = 140.0, 100.0
			merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
			volume_to_mesh_1.width, volume_to_mesh_1.height = 170.0, 100.0
			group_input_1.width, group_input_1.height = 150.770263671875, 100.0
			math.width, math.height = 140.0, 100.0
			subdivide_mesh.width, subdivide_mesh.height = 140.0, 100.0
			
			#initialize nodegroup_003 links
			#geometry_proximity_1.Position -> set_position_1.Position
			nodegroup_003.links.new(geometry_proximity_1.outputs[0], set_position_1.inputs[2])
			#group_input_1.Geometry -> merge_by_distance.Geometry
			nodegroup_003.links.new(group_input_1.outputs[0], merge_by_distance.inputs[0])
			#group_input_1.Voxel Amount -> volume_to_mesh_1.Voxel Amount
			nodegroup_003.links.new(group_input_1.outputs[1], volume_to_mesh_1.inputs[2])
			#mesh_to_volume_1.Volume -> volume_to_mesh_1.Volume
			nodegroup_003.links.new(mesh_to_volume_1.outputs[0], volume_to_mesh_1.inputs[0])
			#group_input_1.Geometry -> mesh_to_volume_1.Mesh
			nodegroup_003.links.new(group_input_1.outputs[0], mesh_to_volume_1.inputs[0])
			#group_input_1.Geometry -> geometry_proximity_1.Geometry
			nodegroup_003.links.new(group_input_1.outputs[0], geometry_proximity_1.inputs[0])
			#group_input_1.Voxel Amount -> math.Value
			nodegroup_003.links.new(group_input_1.outputs[1], math.inputs[0])
			#math.Value -> mesh_to_volume_1.Voxel Size
			nodegroup_003.links.new(math.outputs[0], mesh_to_volume_1.inputs[2])
			#math.Value -> volume_to_mesh_1.Voxel Size
			nodegroup_003.links.new(math.outputs[0], volume_to_mesh_1.inputs[1])
			#math.Value -> mesh_to_volume_1.Voxel Amount
			nodegroup_003.links.new(math.outputs[0], mesh_to_volume_1.inputs[3])
			#set_position_1.Geometry -> group_output_1.Geometry
			nodegroup_003.links.new(set_position_1.outputs[0], group_output_1.inputs[0])
			#volume_to_mesh_1.Mesh -> subdivide_mesh.Mesh
			nodegroup_003.links.new(volume_to_mesh_1.outputs[0], subdivide_mesh.inputs[0])
			#subdivide_mesh.Mesh -> set_position_1.Geometry
			nodegroup_003.links.new(subdivide_mesh.outputs[0], set_position_1.inputs[0])
			#group_input_1.Level -> subdivide_mesh.Level
			nodegroup_003.links.new(group_input_1.outputs[2], subdivide_mesh.inputs[1])
			return nodegroup_003

		nodegroup_003 = nodegroup_003_node_group()

		#initialize volumeapproximation node group
		def volumeapproximation_node_group():
			volumeapproximation = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "VolumeApproximation")

			volumeapproximation.color_tag = 'NONE'
			volumeapproximation.description = ""

			volumeapproximation.is_modifier = True
			
			#volumeapproximation interface
			#Socket SphereVolume
			spherevolume_socket = volumeapproximation.interface.new_socket(name = "SphereVolume", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			spherevolume_socket.attribute_domain = 'POINT'
			
			#Socket VoxelVolume
			voxelvolume_socket = volumeapproximation.interface.new_socket(name = "VoxelVolume", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			voxelvolume_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_2 = volumeapproximation.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_2.attribute_domain = 'POINT'
			
			#Socket View Sphere
			view_sphere_socket = volumeapproximation.interface.new_socket(name = "View Sphere", in_out='INPUT', socket_type = 'NodeSocketBool')
			view_sphere_socket.default_value = False
			view_sphere_socket.attribute_domain = 'POINT'
			
			#Socket Sphere Size
			sphere_size_socket = volumeapproximation.interface.new_socket(name = "Sphere Size", in_out='INPUT', socket_type = 'NodeSocketVector')
			sphere_size_socket.default_value = (1.2000000476837158, 1.2000000476837158, 1.2000000476837158)
			sphere_size_socket.min_value = 4.0
			sphere_size_socket.max_value = 4.0
			sphere_size_socket.subtype = 'NONE'
			sphere_size_socket.attribute_domain = 'POINT'
			
			#Socket Sphere Volume Iterations
			sphere_volume_iterations_socket = volumeapproximation.interface.new_socket(name = "Sphere Volume Iterations", in_out='INPUT', socket_type = 'NodeSocketFloat')
			sphere_volume_iterations_socket.default_value = 0.0
			sphere_volume_iterations_socket.min_value = -3.4028234663852886e+38
			sphere_volume_iterations_socket.max_value = 3.4028234663852886e+38
			sphere_volume_iterations_socket.subtype = 'NONE'
			sphere_volume_iterations_socket.attribute_domain = 'POINT'
			
			#Socket Voxel Amount
			voxel_amount_socket_1 = volumeapproximation.interface.new_socket(name = "Voxel Amount", in_out='INPUT', socket_type = 'NodeSocketInt')
			voxel_amount_socket_1.default_value = 6
			voxel_amount_socket_1.min_value = 2
			voxel_amount_socket_1.max_value = 10
			voxel_amount_socket_1.subtype = 'NONE'
			voxel_amount_socket_1.attribute_domain = 'POINT'
			
			
			#initialize volumeapproximation nodes
			#node Frame
			frame = volumeapproximation.nodes.new("NodeFrame")
			frame.label = "Switch between different volume calculations"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Group Output
			group_output_2 = volumeapproximation.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node SphereVolumeCalculation
			spherevolumecalculation = volumeapproximation.nodes.new("GeometryNodeGroup")
			spherevolumecalculation.label = "SphereVolumeCalculation"
			spherevolumecalculation.name = "SphereVolumeCalculation"
			spherevolumecalculation.node_tree = nodegroup_001
			
			#node VoxelVolumeCalculation
			voxelvolumecalculation = volumeapproximation.nodes.new("GeometryNodeGroup")
			voxelvolumecalculation.label = "VoxelVolumeCalculation"
			voxelvolumecalculation.name = "VoxelVolumeCalculation"
			voxelvolumecalculation.node_tree = nodegroup_003
			
			#node Group Input
			group_input_2 = volumeapproximation.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			
			
			#Set parents
			spherevolumecalculation.parent = frame
			voxelvolumecalculation.parent = frame
			
			#Set locations
			frame.location = (-1379.173828125, 108.0466537475586)
			group_output_2.location = (919.0576171875, -96.09332275390625)
			spherevolumecalculation.location = (1700.635498046875, -37.58912658691406)
			voxelvolumecalculation.location = (1702.9774169921875, -209.36839294433594)
			group_input_2.location = (-340.0, 0.0)
			
			#Set dimensions
			frame.width, frame.height = 200.6666259765625, 374.5
			group_output_2.width, group_output_2.height = 140.0, 100.0
			spherevolumecalculation.width, spherevolumecalculation.height = 140.0, 100.0
			voxelvolumecalculation.width, voxelvolumecalculation.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			
			#initialize volumeapproximation links
			#group_input_2.Geometry -> voxelvolumecalculation.Geometry
			volumeapproximation.links.new(group_input_2.outputs[0], voxelvolumecalculation.inputs[0])
			#group_input_2.Geometry -> spherevolumecalculation.Target
			volumeapproximation.links.new(group_input_2.outputs[0], spherevolumecalculation.inputs[0])
			#group_input_2.Sphere Size -> spherevolumecalculation.Value
			volumeapproximation.links.new(group_input_2.outputs[2], spherevolumecalculation.inputs[1])
			#group_input_2.Sphere Volume Iterations -> spherevolumecalculation.Iterations
			volumeapproximation.links.new(group_input_2.outputs[3], spherevolumecalculation.inputs[2])
			#spherevolumecalculation.Output -> group_output_2.SphereVolume
			volumeapproximation.links.new(spherevolumecalculation.outputs[0], group_output_2.inputs[0])
			#voxelvolumecalculation.Geometry -> group_output_2.VoxelVolume
			volumeapproximation.links.new(voxelvolumecalculation.outputs[0], group_output_2.inputs[1])
			#group_input_2.Sphere Volume Iterations -> voxelvolumecalculation.Voxel Amount
			volumeapproximation.links.new(group_input_2.outputs[3], voxelvolumecalculation.inputs[1])
			#group_input_2.Voxel Amount -> spherevolumecalculation.Shphere resolution
			volumeapproximation.links.new(group_input_2.outputs[4], spherevolumecalculation.inputs[3])
			#group_input_2.Voxel Amount -> voxelvolumecalculation.Level
			volumeapproximation.links.new(group_input_2.outputs[4], voxelvolumecalculation.inputs[2])
			return volumeapproximation

		volumeapproximation = volumeapproximation_node_group()

		#initialize seperate_by_xyz node group
		def seperate_by_xyz_node_group():
			seperate_by_xyz = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Seperate by XYZ")

			seperate_by_xyz.color_tag = 'NONE'
			seperate_by_xyz.description = ""

			
			#seperate_by_xyz interface
			#Socket Inverted
			inverted_socket = seperate_by_xyz.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_3 = seperate_by_xyz.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_3.attribute_domain = 'POINT'
			
			#Socket Socket
			socket_socket = seperate_by_xyz.interface.new_socket(name = "Socket", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			socket_socket.attribute_domain = 'POINT'
			
			#Socket Attribute
			attribute_socket = seperate_by_xyz.interface.new_socket(name = "Attribute", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			attribute_socket.attribute_domain = 'POINT'
			attribute_socket.hide_value = True
			
			#Socket XY
			xy_socket = seperate_by_xyz.interface.new_socket(name = "XY", in_out='INPUT', socket_type = 'NodeSocketFloat')
			xy_socket.default_value = 0.5
			xy_socket.min_value = -10000.0
			xy_socket.max_value = 10000.0
			xy_socket.subtype = 'NONE'
			xy_socket.attribute_domain = 'POINT'
			
			#Socket Z
			z_socket = seperate_by_xyz.interface.new_socket(name = "Z", in_out='INPUT', socket_type = 'NodeSocketFloat')
			z_socket.default_value = 0.5
			z_socket.min_value = -10000.0
			z_socket.max_value = 10000.0
			z_socket.subtype = 'NONE'
			z_socket.attribute_domain = 'POINT'
			
			
			#initialize seperate_by_xyz nodes
			#node Group Output
			group_output_3 = seperate_by_xyz.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = seperate_by_xyz.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Attribute Statistic
			attribute_statistic_1 = seperate_by_xyz.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic_1.name = "Attribute Statistic"
			attribute_statistic_1.data_type = 'FLOAT_VECTOR'
			attribute_statistic_1.domain = 'POINT'
			
			#node Separate XYZ
			separate_xyz = seperate_by_xyz.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz.name = "Separate XYZ"
			separate_xyz.hide = True
			
			#node Separate XYZ.001
			separate_xyz_001 = seperate_by_xyz.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz_001.name = "Separate XYZ.001"
			separate_xyz_001.hide = True
			
			#node Math
			math_1 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.hide = True
			math_1.operation = 'ADD'
			math_1.use_clamp = False
			
			#node Math.001
			math_001 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.hide = True
			math_001.operation = 'SUBTRACT'
			math_001.use_clamp = False
			
			#node Math.002
			math_002 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.hide = True
			math_002.operation = 'ADD'
			math_002.use_clamp = False
			
			#node Math.003
			math_003 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.hide = True
			math_003.operation = 'SUBTRACT'
			math_003.use_clamp = False
			
			#node Math.004
			math_004 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.hide = True
			math_004.operation = 'MULTIPLY'
			math_004.use_clamp = False
			
			#node Math.005
			math_005 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_005.name = "Math.005"
			math_005.hide = True
			math_005.operation = 'MULTIPLY'
			math_005.use_clamp = False
			
			#node Math.006
			math_006 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_006.name = "Math.006"
			math_006.hide = True
			math_006.operation = 'MULTIPLY'
			math_006.use_clamp = False
			
			#node Position
			position_1 = seperate_by_xyz.nodes.new("GeometryNodeInputPosition")
			position_1.name = "Position"
			position_1.hide = True
			
			#node Separate XYZ.002
			separate_xyz_002 = seperate_by_xyz.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz_002.name = "Separate XYZ.002"
			separate_xyz_002.hide = True
			
			#node Math.007
			math_007 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_007.name = "Math.007"
			math_007.hide = True
			math_007.operation = 'LESS_THAN'
			math_007.use_clamp = False
			
			#node Math.008
			math_008 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_008.name = "Math.008"
			math_008.hide = True
			math_008.operation = 'GREATER_THAN'
			math_008.use_clamp = False
			
			#node Boolean Math
			boolean_math = seperate_by_xyz.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.hide = True
			boolean_math.operation = 'OR'
			
			#node Math.009
			math_009 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_009.name = "Math.009"
			math_009.hide = True
			math_009.operation = 'LESS_THAN'
			math_009.use_clamp = False
			
			#node Math.010
			math_010 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_010.name = "Math.010"
			math_010.hide = True
			math_010.operation = 'GREATER_THAN'
			math_010.use_clamp = False
			
			#node Boolean Math.001
			boolean_math_001 = seperate_by_xyz.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.hide = True
			boolean_math_001.operation = 'OR'
			
			#node Boolean Math.002
			boolean_math_002 = seperate_by_xyz.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.hide = True
			boolean_math_002.operation = 'OR'
			
			#node Math.011
			math_011 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_011.name = "Math.011"
			math_011.hide = True
			math_011.operation = 'ADD'
			math_011.use_clamp = False
			
			#node Math.012
			math_012 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_012.name = "Math.012"
			math_012.hide = True
			math_012.operation = 'SUBTRACT'
			math_012.use_clamp = False
			
			#node Math.013
			math_013 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_013.name = "Math.013"
			math_013.hide = True
			math_013.operation = 'LESS_THAN'
			math_013.use_clamp = False
			
			#node Math.014
			math_014 = seperate_by_xyz.nodes.new("ShaderNodeMath")
			math_014.name = "Math.014"
			math_014.hide = True
			math_014.operation = 'GREATER_THAN'
			math_014.use_clamp = False
			
			#node Boolean Math.003
			boolean_math_003 = seperate_by_xyz.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.hide = True
			boolean_math_003.operation = 'OR'
			
			#node Boolean Math.004
			boolean_math_004 = seperate_by_xyz.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004.name = "Boolean Math.004"
			boolean_math_004.hide = True
			boolean_math_004.operation = 'OR'
			
			#node Separate Geometry
			separate_geometry = seperate_by_xyz.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'FACE'
			
			#node Group Input.001
			group_input_001 = seperate_by_xyz.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			
			#node Position.001
			position_001_1 = seperate_by_xyz.nodes.new("GeometryNodeInputPosition")
			position_001_1.name = "Position.001"
			
			#node Raycast
			raycast = seperate_by_xyz.nodes.new("GeometryNodeRaycast")
			raycast.name = "Raycast"
			raycast.data_type = 'FLOAT'
			raycast.mapping = 'INTERPOLATED'
			#Attribute
			raycast.inputs[1].default_value = 0.0
			#Source Position
			raycast.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Ray Direction
			raycast.inputs[3].default_value = (0.0, 0.0, -1.0)
			#Ray Length
			raycast.inputs[4].default_value = 0.20000000298023224
			
			
			
			
			#Set locations
			group_output_3.location = (1820.10888671875, 0.0)
			group_input_3.location = (-2435.820556640625, -48.31698226928711)
			attribute_statistic_1.location = (-1630.1090087890625, -7.1005859375)
			separate_xyz.location = (-1444.6546630859375, -30.464502334594727)
			separate_xyz_001.location = (-1447.003662109375, -155.1033935546875)
			math_1.location = (-910.458984375, 70.102294921875)
			math_001.location = (-911.6494140625, -57.723262786865234)
			math_002.location = (-914.3742065429688, 30.12378692626953)
			math_003.location = (-911.6494140625, -100.053466796875)
			math_004.location = (-1239.525390625, -106.34754943847656)
			math_005.location = (-1242.422607421875, -149.85415649414062)
			math_006.location = (-1240.9739990234375, -192.63565063476562)
			position_1.location = (-746.8046875, -244.73916625976562)
			separate_xyz_002.location = (-745.2809448242188, -211.70936584472656)
			math_007.location = (-249.4171142578125, 63.39513397216797)
			math_008.location = (-246.87744140625, 101.53231811523438)
			boolean_math.location = (29.67626953125, 97.56399536132812)
			math_009.location = (-254.4964599609375, -100.17059326171875)
			math_010.location = (-251.9566650390625, -62.03341293334961)
			boolean_math_001.location = (11.05224609375, -73.62914276123047)
			boolean_math_002.location = (302.3251953125, 71.44686889648438)
			math_011.location = (-915.2893676757812, -10.1893310546875)
			math_012.location = (-912.5646362304688, -140.3665771484375)
			math_013.location = (-256.3267822265625, -217.4451141357422)
			math_014.location = (-253.787109375, -179.3079376220703)
			boolean_math_003.location = (1.900390625, -194.56851196289062)
			boolean_math_004.location = (474.380126953125, 8.228561401367188)
			separate_geometry.location = (1273.5380859375, 164.16757202148438)
			group_input_001.location = (1030.9969482421875, 238.57826232910156)
			position_001_1.location = (-1625.1973876953125, -320.2380065917969)
			raycast.location = (-2047.8201904296875, -245.8093719482422)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			attribute_statistic_1.width, attribute_statistic_1.height = 140.0, 100.0
			separate_xyz.width, separate_xyz.height = 140.0, 100.0
			separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			position_1.width, position_1.height = 140.0, 100.0
			separate_xyz_002.width, separate_xyz_002.height = 140.0, 100.0
			math_007.width, math_007.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			math_009.width, math_009.height = 140.0, 100.0
			math_010.width, math_010.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			math_011.width, math_011.height = 140.0, 100.0
			math_012.width, math_012.height = 140.0, 100.0
			math_013.width, math_013.height = 140.0, 100.0
			math_014.width, math_014.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			boolean_math_004.width, boolean_math_004.height = 129.9329376220703, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			position_001_1.width, position_001_1.height = 140.0, 100.0
			raycast.width, raycast.height = 150.0, 100.0
			
			#initialize seperate_by_xyz links
			#math_006.Value -> math_011.Value
			seperate_by_xyz.links.new(math_006.outputs[0], math_011.inputs[1])
			#separate_xyz.X -> math_001.Value
			seperate_by_xyz.links.new(separate_xyz.outputs[0], math_001.inputs[0])
			#separate_xyz_002.Y -> math_009.Value
			seperate_by_xyz.links.new(separate_xyz_002.outputs[1], math_009.inputs[0])
			#boolean_math.Boolean -> boolean_math_002.Boolean
			seperate_by_xyz.links.new(boolean_math.outputs[0], boolean_math_002.inputs[0])
			#separate_xyz_001.Y -> math_005.Value
			seperate_by_xyz.links.new(separate_xyz_001.outputs[1], math_005.inputs[0])
			#math_003.Value -> math_009.Value
			seperate_by_xyz.links.new(math_003.outputs[0], math_009.inputs[1])
			#math_013.Value -> boolean_math_003.Boolean
			seperate_by_xyz.links.new(math_013.outputs[0], boolean_math_003.inputs[1])
			#boolean_math_003.Boolean -> boolean_math_004.Boolean
			seperate_by_xyz.links.new(boolean_math_003.outputs[0], boolean_math_004.inputs[1])
			#separate_xyz_001.X -> math_004.Value
			seperate_by_xyz.links.new(separate_xyz_001.outputs[0], math_004.inputs[0])
			#separate_xyz_002.X -> math_008.Value
			seperate_by_xyz.links.new(separate_xyz_002.outputs[0], math_008.inputs[0])
			#math_004.Value -> math_001.Value
			seperate_by_xyz.links.new(math_004.outputs[0], math_001.inputs[1])
			#separate_xyz.X -> math_1.Value
			seperate_by_xyz.links.new(separate_xyz.outputs[0], math_1.inputs[0])
			#boolean_math_001.Boolean -> boolean_math_002.Boolean
			seperate_by_xyz.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[1])
			#math_006.Value -> math_012.Value
			seperate_by_xyz.links.new(math_006.outputs[0], math_012.inputs[1])
			#separate_xyz_002.Z -> math_013.Value
			seperate_by_xyz.links.new(separate_xyz_002.outputs[2], math_013.inputs[0])
			#separate_xyz.Z -> math_011.Value
			seperate_by_xyz.links.new(separate_xyz.outputs[2], math_011.inputs[0])
			#math_005.Value -> math_002.Value
			seperate_by_xyz.links.new(math_005.outputs[0], math_002.inputs[1])
			#math_001.Value -> math_007.Value
			seperate_by_xyz.links.new(math_001.outputs[0], math_007.inputs[1])
			#separate_xyz.Y -> math_002.Value
			seperate_by_xyz.links.new(separate_xyz.outputs[1], math_002.inputs[0])
			#math_014.Value -> boolean_math_003.Boolean
			seperate_by_xyz.links.new(math_014.outputs[0], boolean_math_003.inputs[0])
			#separate_xyz_001.Z -> math_006.Value
			seperate_by_xyz.links.new(separate_xyz_001.outputs[2], math_006.inputs[0])
			#separate_xyz_002.Z -> math_014.Value
			seperate_by_xyz.links.new(separate_xyz_002.outputs[2], math_014.inputs[0])
			#boolean_math_002.Boolean -> boolean_math_004.Boolean
			seperate_by_xyz.links.new(boolean_math_002.outputs[0], boolean_math_004.inputs[0])
			#math_002.Value -> math_010.Value
			seperate_by_xyz.links.new(math_002.outputs[0], math_010.inputs[1])
			#math_008.Value -> boolean_math.Boolean
			seperate_by_xyz.links.new(math_008.outputs[0], boolean_math.inputs[0])
			#math_1.Value -> math_008.Value
			seperate_by_xyz.links.new(math_1.outputs[0], math_008.inputs[1])
			#math_012.Value -> math_013.Value
			seperate_by_xyz.links.new(math_012.outputs[0], math_013.inputs[1])
			#math_007.Value -> boolean_math.Boolean
			seperate_by_xyz.links.new(math_007.outputs[0], boolean_math.inputs[1])
			#separate_xyz.Y -> math_003.Value
			seperate_by_xyz.links.new(separate_xyz.outputs[1], math_003.inputs[0])
			#position_1.Position -> separate_xyz_002.Vector
			seperate_by_xyz.links.new(position_1.outputs[0], separate_xyz_002.inputs[0])
			#math_011.Value -> math_014.Value
			seperate_by_xyz.links.new(math_011.outputs[0], math_014.inputs[1])
			#separate_xyz_002.Y -> math_010.Value
			seperate_by_xyz.links.new(separate_xyz_002.outputs[1], math_010.inputs[0])
			#separate_xyz_002.X -> math_007.Value
			seperate_by_xyz.links.new(separate_xyz_002.outputs[0], math_007.inputs[0])
			#math_009.Value -> boolean_math_001.Boolean
			seperate_by_xyz.links.new(math_009.outputs[0], boolean_math_001.inputs[1])
			#math_004.Value -> math_1.Value
			seperate_by_xyz.links.new(math_004.outputs[0], math_1.inputs[1])
			#math_005.Value -> math_003.Value
			seperate_by_xyz.links.new(math_005.outputs[0], math_003.inputs[1])
			#separate_xyz.Z -> math_012.Value
			seperate_by_xyz.links.new(separate_xyz.outputs[2], math_012.inputs[0])
			#math_010.Value -> boolean_math_001.Boolean
			seperate_by_xyz.links.new(math_010.outputs[0], boolean_math_001.inputs[0])
			#group_input_001.Socket -> separate_geometry.Geometry
			seperate_by_xyz.links.new(group_input_001.outputs[1], separate_geometry.inputs[0])
			#separate_geometry.Inverted -> group_output_3.Inverted
			seperate_by_xyz.links.new(separate_geometry.outputs[1], group_output_3.inputs[0])
			#group_input_3.Z -> math_006.Value
			seperate_by_xyz.links.new(group_input_3.outputs[4], math_006.inputs[1])
			#attribute_statistic_1.Mean -> separate_xyz.Vector
			seperate_by_xyz.links.new(attribute_statistic_1.outputs[0], separate_xyz.inputs[0])
			#boolean_math_004.Boolean -> separate_geometry.Selection
			seperate_by_xyz.links.new(boolean_math_004.outputs[0], separate_geometry.inputs[1])
			#attribute_statistic_1.Standard Deviation -> separate_xyz_001.Vector
			seperate_by_xyz.links.new(attribute_statistic_1.outputs[6], separate_xyz_001.inputs[0])
			#group_input_3.Geometry -> attribute_statistic_1.Geometry
			seperate_by_xyz.links.new(group_input_3.outputs[0], attribute_statistic_1.inputs[0])
			#position_001_1.Position -> attribute_statistic_1.Attribute
			seperate_by_xyz.links.new(position_001_1.outputs[0], attribute_statistic_1.inputs[2])
			#group_input_3.Attribute -> raycast.Target Geometry
			seperate_by_xyz.links.new(group_input_3.outputs[2], raycast.inputs[0])
			#raycast.Is Hit -> attribute_statistic_1.Selection
			seperate_by_xyz.links.new(raycast.outputs[0], attribute_statistic_1.inputs[1])
			#group_input_3.XY -> math_004.Value
			seperate_by_xyz.links.new(group_input_3.outputs[3], math_004.inputs[1])
			#group_input_3.XY -> math_005.Value
			seperate_by_xyz.links.new(group_input_3.outputs[3], math_005.inputs[1])
			return seperate_by_xyz

		seperate_by_xyz = seperate_by_xyz_node_group()

		#initialize edgepolyline node group
		def edgepolyline_node_group():
			edgepolyline = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "EdgePolyline")

			edgepolyline.color_tag = 'NONE'
			edgepolyline.description = ""

			
			#edgepolyline interface
			#Socket Geometry
			geometry_socket_4 = edgepolyline.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_4.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_5 = edgepolyline.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_5.attribute_domain = 'POINT'
			
			#Socket Count
			count_socket = edgepolyline.interface.new_socket(name = "Count", in_out='INPUT', socket_type = 'NodeSocketInt')
			count_socket.default_value = 31
			count_socket.min_value = 1
			count_socket.max_value = 100000
			count_socket.subtype = 'NONE'
			count_socket.attribute_domain = 'POINT'
			
			
			#initialize edgepolyline nodes
			#node Group Output
			group_output_4 = edgepolyline.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = edgepolyline.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Resample Curve
			resample_curve = edgepolyline.nodes.new("GeometryNodeResampleCurve")
			resample_curve.name = "Resample Curve"
			resample_curve.mode = 'COUNT'
			#Selection
			resample_curve.inputs[1].default_value = True
			
			#node Curve to Mesh.001
			curve_to_mesh_001 = edgepolyline.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh_001.name = "Curve to Mesh.001"
			#Fill Caps
			curve_to_mesh_001.inputs[2].default_value = False
			
			#node Frame.001
			frame_001 = edgepolyline.nodes.new("NodeFrame")
			frame_001.label = "Separate Edge of Mesh"
			frame_001.name = "Frame.001"
			frame_001.label_size = 20
			frame_001.shrink = True
			
			#node Attribute Statistic
			attribute_statistic_2 = edgepolyline.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic_2.name = "Attribute Statistic"
			attribute_statistic_2.data_type = 'FLOAT'
			attribute_statistic_2.domain = 'CURVE'
			#Selection
			attribute_statistic_2.inputs[1].default_value = True
			
			#node Spline Length
			spline_length = edgepolyline.nodes.new("GeometryNodeSplineLength")
			spline_length.name = "Spline Length"
			spline_length.hide = True
			
			#node Compare.002
			compare_002 = edgepolyline.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'FLOAT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			#Epsilon
			compare_002.inputs[12].default_value = 0.0
			
			#node Separate Geometry.001
			separate_geometry_001 = edgepolyline.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'CURVE'
			
			#node Set Spline Cyclic
			set_spline_cyclic = edgepolyline.nodes.new("GeometryNodeSetSplineCyclic")
			set_spline_cyclic.name = "Set Spline Cyclic"
			#Selection
			set_spline_cyclic.inputs[1].default_value = True
			#Cyclic
			set_spline_cyclic.inputs[2].default_value = True
			
			#node Mesh to Curve.001
			mesh_to_curve_001 = edgepolyline.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_001.name = "Mesh to Curve.001"
			
			#node Compare.003
			compare_003 = edgepolyline.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'LESS_EQUAL'
			#B_INT
			compare_003.inputs[3].default_value = 1
			
			#node Edge Neighbors.002
			edge_neighbors_002 = edgepolyline.nodes.new("GeometryNodeInputMeshEdgeNeighbors")
			edge_neighbors_002.name = "Edge Neighbors.002"
			
			#node Viewer
			viewer = edgepolyline.nodes.new("GeometryNodeViewer")
			viewer.name = "Viewer"
			viewer.data_type = 'FLOAT'
			viewer.domain = 'AUTO'
			#Value
			viewer.inputs[1].default_value = 0.0
			
			#node Viewer.001
			viewer_001 = edgepolyline.nodes.new("GeometryNodeViewer")
			viewer_001.name = "Viewer.001"
			viewer_001.data_type = 'FLOAT'
			viewer_001.domain = 'AUTO'
			#Value
			viewer_001.inputs[1].default_value = 0.0
			
			
			
			#Set parents
			resample_curve.parent = frame_001
			curve_to_mesh_001.parent = frame_001
			attribute_statistic_2.parent = frame_001
			spline_length.parent = frame_001
			compare_002.parent = frame_001
			separate_geometry_001.parent = frame_001
			set_spline_cyclic.parent = frame_001
			mesh_to_curve_001.parent = frame_001
			compare_003.parent = frame_001
			edge_neighbors_002.parent = frame_001
			
			#Set locations
			group_output_4.location = (1107.48486328125, 0.0)
			group_input_4.location = (-1088.51513671875, 0.0)
			resample_curve.location = (-927.819580078125, 220.1479034423828)
			curve_to_mesh_001.location = (254.21292114257812, 259.97747802734375)
			frame_001.location = (425.05853271484375, -109.01971435546875)
			attribute_statistic_2.location = (-669.1614990234375, -15.506338119506836)
			spline_length.location = (-671.9161376953125, -331.8674621582031)
			compare_002.location = (-486.6707458496094, 8.920280456542969)
			separate_geometry_001.location = (-305.7835388183594, 297.6513671875)
			set_spline_cyclic.location = (-68.36480712890625, 285.95611572265625)
			mesh_to_curve_001.location = (-1115.638916015625, 243.434326171875)
			compare_003.location = (-1122.21923828125, 133.3899688720703)
			edge_neighbors_002.location = (-1121.1494140625, -18.6751708984375)
			viewer.location = (-495.5530700683594, 361.1207580566406)
			viewer_001.location = (299.47650146484375, 356.5062561035156)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			resample_curve.width, resample_curve.height = 140.0, 100.0
			curve_to_mesh_001.width, curve_to_mesh_001.height = 140.0, 100.0
			frame_001.width, frame_001.height = 1574.6666259765625, 722.0
			attribute_statistic_2.width, attribute_statistic_2.height = 140.0, 100.0
			spline_length.width, spline_length.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			set_spline_cyclic.width, set_spline_cyclic.height = 140.0, 100.0
			mesh_to_curve_001.width, mesh_to_curve_001.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			edge_neighbors_002.width, edge_neighbors_002.height = 140.0, 100.0
			viewer.width, viewer.height = 140.0, 100.0
			viewer_001.width, viewer_001.height = 140.0, 100.0
			
			#initialize edgepolyline links
			#resample_curve.Curve -> separate_geometry_001.Geometry
			edgepolyline.links.new(resample_curve.outputs[0], separate_geometry_001.inputs[0])
			#compare_002.Result -> separate_geometry_001.Selection
			edgepolyline.links.new(compare_002.outputs[0], separate_geometry_001.inputs[1])
			#attribute_statistic_2.Max -> compare_002.B
			edgepolyline.links.new(attribute_statistic_2.outputs[4], compare_002.inputs[1])
			#resample_curve.Curve -> attribute_statistic_2.Geometry
			edgepolyline.links.new(resample_curve.outputs[0], attribute_statistic_2.inputs[0])
			#separate_geometry_001.Selection -> set_spline_cyclic.Geometry
			edgepolyline.links.new(separate_geometry_001.outputs[0], set_spline_cyclic.inputs[0])
			#set_spline_cyclic.Geometry -> curve_to_mesh_001.Curve
			edgepolyline.links.new(set_spline_cyclic.outputs[0], curve_to_mesh_001.inputs[0])
			#group_input_4.Count -> resample_curve.Count
			edgepolyline.links.new(group_input_4.outputs[1], resample_curve.inputs[2])
			#curve_to_mesh_001.Mesh -> group_output_4.Geometry
			edgepolyline.links.new(curve_to_mesh_001.outputs[0], group_output_4.inputs[0])
			#group_input_4.Geometry -> mesh_to_curve_001.Mesh
			edgepolyline.links.new(group_input_4.outputs[0], mesh_to_curve_001.inputs[0])
			#edge_neighbors_002.Face Count -> compare_003.A
			edgepolyline.links.new(edge_neighbors_002.outputs[0], compare_003.inputs[2])
			#compare_003.Result -> mesh_to_curve_001.Selection
			edgepolyline.links.new(compare_003.outputs[0], mesh_to_curve_001.inputs[1])
			#mesh_to_curve_001.Curve -> resample_curve.Curve
			edgepolyline.links.new(mesh_to_curve_001.outputs[0], resample_curve.inputs[0])
			#mesh_to_curve_001.Curve -> viewer.Geometry
			edgepolyline.links.new(mesh_to_curve_001.outputs[0], viewer.inputs[0])
			#set_spline_cyclic.Geometry -> viewer_001.Geometry
			edgepolyline.links.new(set_spline_cyclic.outputs[0], viewer_001.inputs[0])
			#attribute_statistic_2.Max -> compare_002.A
			edgepolyline.links.new(attribute_statistic_2.outputs[4], compare_002.inputs[2])
			#spline_length.Length -> attribute_statistic_2.Attribute
			edgepolyline.links.new(spline_length.outputs[0], attribute_statistic_2.inputs[2])
			#spline_length.Length -> compare_002.B
			edgepolyline.links.new(spline_length.outputs[0], compare_002.inputs[3])
			#spline_length.Length -> compare_002.A
			edgepolyline.links.new(spline_length.outputs[0], compare_002.inputs[0])
			return edgepolyline

		edgepolyline = edgepolyline_node_group()

		#initialize poly_creation node group
		def poly_creation_node_group():
			poly_creation = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Poly Creation")

			poly_creation.color_tag = 'NONE'
			poly_creation.description = ""

			
			#poly_creation interface
			#Socket Polygon
			polygon_socket = poly_creation.interface.new_socket(name = "Polygon", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			polygon_socket.attribute_domain = 'POINT'
			
			#Socket Polyline
			polyline_socket = poly_creation.interface.new_socket(name = "Polyline", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			polyline_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_6 = poly_creation.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_6.attribute_domain = 'POINT'
			
			#Socket Count
			count_socket_1 = poly_creation.interface.new_socket(name = "Count", in_out='INPUT', socket_type = 'NodeSocketInt')
			count_socket_1.default_value = 31
			count_socket_1.min_value = 1
			count_socket_1.max_value = 100000
			count_socket_1.subtype = 'NONE'
			count_socket_1.attribute_domain = 'POINT'
			
			
			#initialize poly_creation nodes
			#node Group Output
			group_output_5 = poly_creation.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input
			group_input_5 = poly_creation.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Attribute Statistic.001
			attribute_statistic_001 = poly_creation.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic_001.name = "Attribute Statistic.001"
			attribute_statistic_001.data_type = 'FLOAT'
			attribute_statistic_001.domain = 'POINT'
			#Selection
			attribute_statistic_001.inputs[1].default_value = True
			
			#node Sample Index
			sample_index = poly_creation.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.clamp = True
			sample_index.data_type = 'FLOAT_VECTOR'
			sample_index.domain = 'POINT'
			
			#node Position.002
			position_002 = poly_creation.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Index
			index = poly_creation.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Math.015
			math_015 = poly_creation.nodes.new("ShaderNodeMath")
			math_015.name = "Math.015"
			math_015.operation = 'ADD'
			math_015.use_clamp = False
			#Value_001
			math_015.inputs[1].default_value = 1.0
			
			#node Mesh Circle
			mesh_circle = poly_creation.nodes.new("GeometryNodeMeshCircle")
			mesh_circle.name = "Mesh Circle"
			mesh_circle.fill_type = 'NGON'
			#Radius
			mesh_circle.inputs[1].default_value = 1.0
			
			#node Set Position.001
			set_position_001 = poly_creation.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Selection
			set_position_001.inputs[1].default_value = True
			#Offset
			set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Triangulate
			triangulate = poly_creation.nodes.new("GeometryNodeTriangulate")
			triangulate.name = "Triangulate"
			triangulate.ngon_method = 'BEAUTY'
			triangulate.quad_method = 'SHORTEST_DIAGONAL'
			#Selection
			triangulate.inputs[1].default_value = True
			#Minimum Vertices
			triangulate.inputs[2].default_value = 4
			
			#node Frame
			frame_1 = poly_creation.nodes.new("NodeFrame")
			frame_1.label = "Fill Curve"
			frame_1.name = "Frame"
			frame_1.label_size = 20
			frame_1.shrink = True
			
			#node Group.001
			group_001 = poly_creation.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = edgepolyline
			
			
			
			#Set parents
			attribute_statistic_001.parent = frame_1
			sample_index.parent = frame_1
			position_002.parent = frame_1
			index.parent = frame_1
			math_015.parent = frame_1
			mesh_circle.parent = frame_1
			set_position_001.parent = frame_1
			triangulate.parent = frame_1
			
			#Set locations
			group_output_5.location = (220.6656494140625, 93.11943817138672)
			group_input_5.location = (-2051.769775390625, 9.350010871887207)
			attribute_statistic_001.location = (32.38541793823242, 384.86328125)
			sample_index.location = (29.29925537109375, 3.2015228271484375)
			position_002.location = (-199.4605712890625, -102.96278381347656)
			index.location = (-213.3316650390625, -179.76565551757812)
			math_015.location = (194.6024932861328, 327.9139709472656)
			mesh_circle.location = (393.4267272949219, 343.6446838378906)
			set_position_001.location = (564.5072631835938, 331.6153259277344)
			triangulate.location = (754.7021484375, 306.52392578125)
			frame_1.location = (-1004.42822265625, -28.531341552734375)
			group_001.location = (-1624.6370849609375, 56.9328727722168)
			
			#Set dimensions
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			attribute_statistic_001.width, attribute_statistic_001.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			math_015.width, math_015.height = 140.0, 100.0
			mesh_circle.width, mesh_circle.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			triangulate.width, triangulate.height = 140.0, 100.0
			frame_1.width, frame_1.height = 1166.0, 680.5
			group_001.width, group_001.height = 140.0, 100.0
			
			#initialize poly_creation links
			#attribute_statistic_001.Max -> math_015.Value
			poly_creation.links.new(attribute_statistic_001.outputs[4], math_015.inputs[0])
			#index.Index -> attribute_statistic_001.Attribute
			poly_creation.links.new(index.outputs[0], attribute_statistic_001.inputs[2])
			#index.Index -> sample_index.Index
			poly_creation.links.new(index.outputs[0], sample_index.inputs[2])
			#sample_index.Value -> set_position_001.Position
			poly_creation.links.new(sample_index.outputs[0], set_position_001.inputs[2])
			#math_015.Value -> mesh_circle.Vertices
			poly_creation.links.new(math_015.outputs[0], mesh_circle.inputs[0])
			#mesh_circle.Mesh -> set_position_001.Geometry
			poly_creation.links.new(mesh_circle.outputs[0], set_position_001.inputs[0])
			#position_002.Position -> sample_index.Value
			poly_creation.links.new(position_002.outputs[0], sample_index.inputs[1])
			#set_position_001.Geometry -> triangulate.Mesh
			poly_creation.links.new(set_position_001.outputs[0], triangulate.inputs[0])
			#group_001.Geometry -> attribute_statistic_001.Geometry
			poly_creation.links.new(group_001.outputs[0], attribute_statistic_001.inputs[0])
			#group_input_5.Geometry -> group_001.Geometry
			poly_creation.links.new(group_input_5.outputs[0], group_001.inputs[0])
			#group_input_5.Count -> group_001.Count
			poly_creation.links.new(group_input_5.outputs[1], group_001.inputs[1])
			#group_001.Geometry -> sample_index.Geometry
			poly_creation.links.new(group_001.outputs[0], sample_index.inputs[0])
			#group_001.Geometry -> group_output_5.Polyline
			poly_creation.links.new(group_001.outputs[0], group_output_5.inputs[1])
			#triangulate.Mesh -> group_output_5.Polygon
			poly_creation.links.new(triangulate.outputs[0], group_output_5.inputs[0])
			return poly_creation

		poly_creation = poly_creation_node_group()

		#initialize smoothing node group
		def smoothing_node_group():
			smoothing = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Smoothing")

			smoothing.color_tag = 'NONE'
			smoothing.description = ""

			
			#smoothing interface
			#Socket Geometry
			geometry_socket_7 = smoothing.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_7.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_8 = smoothing.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_8.attribute_domain = 'POINT'
			
			#Socket Iterations
			iterations_socket_1 = smoothing.interface.new_socket(name = "Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			iterations_socket_1.default_value = 156
			iterations_socket_1.min_value = 0
			iterations_socket_1.max_value = 2147483647
			iterations_socket_1.subtype = 'NONE'
			iterations_socket_1.attribute_domain = 'POINT'
			
			
			#initialize smoothing nodes
			#node Group Output
			group_output_6 = smoothing.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Group Input
			group_input_6 = smoothing.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Set Position.002
			set_position_002_1 = smoothing.nodes.new("GeometryNodeSetPosition")
			set_position_002_1.name = "Set Position.002"
			#Offset
			set_position_002_1.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Edge Vertices.001
			edge_vertices_001 = smoothing.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices_001.name = "Edge Vertices.001"
			edge_vertices_001.hide = True
			
			#node Vector Math.002
			vector_math_002_1 = smoothing.nodes.new("ShaderNodeVectorMath")
			vector_math_002_1.name = "Vector Math.002"
			vector_math_002_1.hide = True
			vector_math_002_1.operation = 'ADD'
			
			#node Separate XYZ.005
			separate_xyz_005 = smoothing.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz_005.name = "Separate XYZ.005"
			separate_xyz_005.hide = True
			
			#node Combine XYZ.001
			combine_xyz_001 = smoothing.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001.name = "Combine XYZ.001"
			combine_xyz_001.hide = True
			
			#node Position.003
			position_003 = smoothing.nodes.new("GeometryNodeInputPosition")
			position_003.name = "Position.003"
			
			#node Separate XYZ.006
			separate_xyz_006 = smoothing.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz_006.name = "Separate XYZ.006"
			separate_xyz_006.hide = True
			
			#node Repeat Input.001
			repeat_input_001 = smoothing.nodes.new("GeometryNodeRepeatInput")
			repeat_input_001.name = "Repeat Input.001"
			#node Repeat Output.001
			repeat_output_001 = smoothing.nodes.new("GeometryNodeRepeatOutput")
			repeat_output_001.name = "Repeat Output.001"
			repeat_output_001.active_index = 0
			repeat_output_001.inspection_index = 0
			repeat_output_001.repeat_items.clear()
			# Create item "Geometry"
			repeat_output_001.repeat_items.new('GEOMETRY', "Geometry")
			
			#node Vector Math.003
			vector_math_003 = smoothing.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.hide = True
			vector_math_003.operation = 'SCALE'
			#Scale
			vector_math_003.inputs[3].default_value = 0.5
			
			#node Compare.002
			compare_002_1 = smoothing.nodes.new("FunctionNodeCompare")
			compare_002_1.name = "Compare.002"
			compare_002_1.data_type = 'INT'
			compare_002_1.mode = 'ELEMENT'
			compare_002_1.operation = 'EQUAL'
			#B_INT
			compare_002_1.inputs[3].default_value = 2
			
			#node Edge Neighbors.002
			edge_neighbors_002_1 = smoothing.nodes.new("GeometryNodeInputMeshEdgeNeighbors")
			edge_neighbors_002_1.name = "Edge Neighbors.002"
			
			
			#Process zone input Repeat Input.001
			repeat_input_001.pair_with_output(repeat_output_001)
			
			
			
			
			#Set locations
			group_output_6.location = (587.704833984375, 0.0)
			group_input_6.location = (-597.70458984375, 0.0)
			set_position_002_1.location = (79.939208984375, 180.40789794921875)
			edge_vertices_001.location = (-195.05419921875, -266.74505615234375)
			vector_math_002_1.location = (-195.91943359375, -231.43991088867188)
			separate_xyz_005.location = (-194.271728515625, -160.38494873046875)
			combine_xyz_001.location = (8.84814453125, -109.09173583984375)
			position_003.location = (-194.8160400390625, -49.35029602050781)
			separate_xyz_006.location = (-194.761962890625, -106.73977661132812)
			repeat_input_001.location = (-191.265869140625, 164.97784423828125)
			repeat_output_001.location = (397.704833984375, 222.20916748046875)
			vector_math_003.location = (-195.166259765625, -196.39572143554688)
			compare_002_1.location = (79.55814361572266, 438.2186584472656)
			edge_neighbors_002_1.location = (80.62784576416016, 286.1535339355469)
			
			#Set dimensions
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			set_position_002_1.width, set_position_002_1.height = 140.0, 100.0
			edge_vertices_001.width, edge_vertices_001.height = 140.0, 100.0
			vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
			separate_xyz_005.width, separate_xyz_005.height = 140.0, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			position_003.width, position_003.height = 140.0, 100.0
			separate_xyz_006.width, separate_xyz_006.height = 140.0, 100.0
			repeat_input_001.width, repeat_input_001.height = 140.0, 100.0
			repeat_output_001.width, repeat_output_001.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			compare_002_1.width, compare_002_1.height = 140.0, 100.0
			edge_neighbors_002_1.width, edge_neighbors_002_1.height = 140.0, 100.0
			
			#initialize smoothing links
			#position_003.Position -> separate_xyz_006.Vector
			smoothing.links.new(position_003.outputs[0], separate_xyz_006.inputs[0])
			#edge_vertices_001.Position 1 -> vector_math_002_1.Vector
			smoothing.links.new(edge_vertices_001.outputs[2], vector_math_002_1.inputs[0])
			#separate_xyz_006.X -> combine_xyz_001.X
			smoothing.links.new(separate_xyz_006.outputs[0], combine_xyz_001.inputs[0])
			#repeat_input_001.Geometry -> set_position_002_1.Geometry
			smoothing.links.new(repeat_input_001.outputs[0], set_position_002_1.inputs[0])
			#combine_xyz_001.Vector -> set_position_002_1.Position
			smoothing.links.new(combine_xyz_001.outputs[0], set_position_002_1.inputs[2])
			#edge_vertices_001.Position 2 -> vector_math_002_1.Vector
			smoothing.links.new(edge_vertices_001.outputs[3], vector_math_002_1.inputs[1])
			#vector_math_003.Vector -> separate_xyz_005.Vector
			smoothing.links.new(vector_math_003.outputs[0], separate_xyz_005.inputs[0])
			#edge_neighbors_002_1.Face Count -> compare_002_1.A
			smoothing.links.new(edge_neighbors_002_1.outputs[0], compare_002_1.inputs[2])
			#separate_xyz_005.Z -> combine_xyz_001.Z
			smoothing.links.new(separate_xyz_005.outputs[2], combine_xyz_001.inputs[2])
			#compare_002_1.Result -> set_position_002_1.Selection
			smoothing.links.new(compare_002_1.outputs[0], set_position_002_1.inputs[1])
			#separate_xyz_006.Y -> combine_xyz_001.Y
			smoothing.links.new(separate_xyz_006.outputs[1], combine_xyz_001.inputs[1])
			#set_position_002_1.Geometry -> repeat_output_001.Geometry
			smoothing.links.new(set_position_002_1.outputs[0], repeat_output_001.inputs[0])
			#vector_math_002_1.Vector -> vector_math_003.Vector
			smoothing.links.new(vector_math_002_1.outputs[0], vector_math_003.inputs[0])
			#group_input_6.Geometry -> repeat_input_001.Geometry
			smoothing.links.new(group_input_6.outputs[0], repeat_input_001.inputs[1])
			#repeat_output_001.Geometry -> group_output_6.Geometry
			smoothing.links.new(repeat_output_001.outputs[0], group_output_6.inputs[0])
			#group_input_6.Iterations -> repeat_input_001.Iterations
			smoothing.links.new(group_input_6.outputs[1], repeat_input_001.inputs[0])
			return smoothing

		smoothing = smoothing_node_group()

		#initialize normals_grouping node group
		def normals_grouping_node_group():
			normals_grouping = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Normals Grouping")

			normals_grouping.color_tag = 'NONE'
			normals_grouping.description = ""

			normals_grouping.is_modifier = True
			
			#normals_grouping interface
			#Socket Geometry
			geometry_socket_9 = normals_grouping.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_9.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_10 = normals_grouping.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_10.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_11 = normals_grouping.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_11.attribute_domain = 'POINT'
			
			#Socket Base/Top
			base_top_socket = normals_grouping.interface.new_socket(name = "Base/Top", in_out='INPUT', socket_type = 'NodeSocketBool')
			base_top_socket.default_value = False
			base_top_socket.attribute_domain = 'POINT'
			
			#Socket Nor Var
			nor_var_socket = normals_grouping.interface.new_socket(name = "Nor Var", in_out='INPUT', socket_type = 'NodeSocketFloat')
			nor_var_socket.default_value = 0.6000000238418579
			nor_var_socket.min_value = -10000.0
			nor_var_socket.max_value = 10000.0
			nor_var_socket.subtype = 'NONE'
			nor_var_socket.attribute_domain = 'POINT'
			
			#Socket Iterations
			iterations_socket_2 = normals_grouping.interface.new_socket(name = "Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			iterations_socket_2.default_value = 20
			iterations_socket_2.min_value = 0
			iterations_socket_2.max_value = 2147483647
			iterations_socket_2.subtype = 'NONE'
			iterations_socket_2.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket = normals_grouping.interface.new_socket(name = "Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distance_socket.default_value = 0.019999999552965164
			distance_socket.min_value = 0.0
			distance_socket.max_value = 3.4028234663852886e+38
			distance_socket.subtype = 'DISTANCE'
			distance_socket.attribute_domain = 'POINT'
			
			
			#initialize normals_grouping nodes
			#node Group Input
			group_input_7 = normals_grouping.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			group_input_7.outputs[2].hide = True
			
			#node Group Output
			group_output_7 = normals_grouping.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Attribute Statistic
			attribute_statistic_3 = normals_grouping.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic_3.name = "Attribute Statistic"
			attribute_statistic_3.data_type = 'FLOAT_VECTOR'
			attribute_statistic_3.domain = 'FACE'
			
			#node Compare
			compare = normals_grouping.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'FLOAT'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_EQUAL'
			#B
			compare.inputs[1].default_value = 0.10000000149011612
			
			#node Normal
			normal = normals_grouping.nodes.new("GeometryNodeInputNormal")
			normal.name = "Normal"
			
			#node Separate XYZ
			separate_xyz_1 = normals_grouping.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz_1.name = "Separate XYZ"
			separate_xyz_1.hide = True
			
			#node Separate XYZ.001
			separate_xyz_001_1 = normals_grouping.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz_001_1.name = "Separate XYZ.001"
			separate_xyz_001_1.hide = True
			
			#node Math
			math_2 = normals_grouping.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.hide = True
			math_2.operation = 'ADD'
			math_2.use_clamp = False
			
			#node Math.001
			math_001_1 = normals_grouping.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.hide = True
			math_001_1.operation = 'SUBTRACT'
			math_001_1.use_clamp = False
			
			#node Compare.001
			compare_001 = normals_grouping.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.hide = True
			compare_001.data_type = 'FLOAT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'LESS_THAN'
			
			#node Compare.002
			compare_002_2 = normals_grouping.nodes.new("FunctionNodeCompare")
			compare_002_2.name = "Compare.002"
			compare_002_2.hide = True
			compare_002_2.data_type = 'FLOAT'
			compare_002_2.mode = 'ELEMENT'
			compare_002_2.operation = 'GREATER_THAN'
			
			#node Separate XYZ.002
			separate_xyz_002_1 = normals_grouping.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz_002_1.name = "Separate XYZ.002"
			
			#node Boolean Math
			boolean_math_1 = normals_grouping.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.hide = True
			boolean_math_1.operation = 'AND'
			
			#node Math.002
			math_002_1 = normals_grouping.nodes.new("ShaderNodeMath")
			math_002_1.name = "Math.002"
			math_002_1.hide = True
			math_002_1.operation = 'ADD'
			math_002_1.use_clamp = False
			
			#node Math.003
			math_003_1 = normals_grouping.nodes.new("ShaderNodeMath")
			math_003_1.name = "Math.003"
			math_003_1.hide = True
			math_003_1.operation = 'SUBTRACT'
			math_003_1.use_clamp = False
			
			#node Compare.003
			compare_003_1 = normals_grouping.nodes.new("FunctionNodeCompare")
			compare_003_1.name = "Compare.003"
			compare_003_1.hide = True
			compare_003_1.data_type = 'FLOAT'
			compare_003_1.mode = 'ELEMENT'
			compare_003_1.operation = 'LESS_THAN'
			
			#node Compare.004
			compare_004 = normals_grouping.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.hide = True
			compare_004.data_type = 'FLOAT'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'GREATER_THAN'
			
			#node Boolean Math.001
			boolean_math_001_1 = normals_grouping.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.hide = True
			boolean_math_001_1.operation = 'AND'
			
			#node Boolean Math.002
			boolean_math_002_1 = normals_grouping.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_1.name = "Boolean Math.002"
			boolean_math_002_1.hide = True
			boolean_math_002_1.operation = 'AND'
			
			#node Vector Math
			vector_math_1 = normals_grouping.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'SCALE'
			
			#node Group
			group = normals_grouping.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = smoothing
			
			#node Store Named Attribute
			store_named_attribute = normals_grouping.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'BOOLEAN'
			store_named_attribute.domain = 'FACE'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "similar_normal"
			
			#node Merge by Distance
			merge_by_distance_1 = normals_grouping.nodes.new("GeometryNodeMergeByDistance")
			merge_by_distance_1.name = "Merge by Distance"
			merge_by_distance_1.mode = 'ALL'
			#Selection
			merge_by_distance_1.inputs[1].default_value = True
			
			#node Sample Nearest
			sample_nearest = normals_grouping.nodes.new("GeometryNodeSampleNearest")
			sample_nearest.name = "Sample Nearest"
			sample_nearest.domain = 'POINT'
			#Sample Position
			sample_nearest.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Accumulate Field
			accumulate_field = normals_grouping.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'FLOAT'
			accumulate_field.domain = 'POINT'
			
			#node Set ID
			set_id = normals_grouping.nodes.new("GeometryNodeSetID")
			set_id.name = "Set ID"
			#Selection
			set_id.inputs[1].default_value = True
			
			#node ID
			id = normals_grouping.nodes.new("GeometryNodeInputID")
			id.name = "ID"
			id.hide = True
			
			#node Named Attribute.001
			named_attribute_001 = normals_grouping.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'BOOLEAN'
			#Name
			named_attribute_001.inputs[0].default_value = "similar_normal"
			
			#node Math.004
			math_004_1 = normals_grouping.nodes.new("ShaderNodeMath")
			math_004_1.name = "Math.004"
			math_004_1.operation = 'DIVIDE'
			math_004_1.use_clamp = False
			
			#node Store Named Attribute.001
			store_named_attribute_001 = normals_grouping.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'FLOAT'
			store_named_attribute_001.domain = 'POINT'
			#Selection
			store_named_attribute_001.inputs[1].default_value = True
			#Name
			store_named_attribute_001.inputs[2].default_value = "avg pt val"
			
			#node Named Attribute.002
			named_attribute_002 = normals_grouping.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.hide = True
			named_attribute_002.data_type = 'FLOAT'
			#Name
			named_attribute_002.inputs[0].default_value = "avg pt val"
			
			#node Compare.005
			compare_005 = normals_grouping.nodes.new("FunctionNodeCompare")
			compare_005.name = "Compare.005"
			compare_005.data_type = 'FLOAT'
			compare_005.mode = 'ELEMENT'
			compare_005.operation = 'EQUAL'
			#B
			compare_005.inputs[1].default_value = 0.0
			#Epsilon
			compare_005.inputs[12].default_value = 0.0
			
			#node Accumulate Field.001
			accumulate_field_001 = normals_grouping.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'FLOAT'
			accumulate_field_001.domain = 'POINT'
			
			#node ID.002
			id_002 = normals_grouping.nodes.new("GeometryNodeInputID")
			id_002.name = "ID.002"
			id_002.hide = True
			
			#node Index
			index_1 = normals_grouping.nodes.new("GeometryNodeInputIndex")
			index_1.name = "Index"
			index_1.hide = True
			
			#node Separate Geometry
			separate_geometry_1 = normals_grouping.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_1.name = "Separate Geometry"
			separate_geometry_1.domain = 'POINT'
			
			#node Separate Geometry.002
			separate_geometry_002 = normals_grouping.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_002.name = "Separate Geometry.002"
			separate_geometry_002.domain = 'FACE'
			
			#node Compare.007
			compare_007 = normals_grouping.nodes.new("FunctionNodeCompare")
			compare_007.name = "Compare.007"
			compare_007.data_type = 'INT'
			compare_007.mode = 'ELEMENT'
			compare_007.operation = 'LESS_EQUAL'
			#B_INT
			compare_007.inputs[3].default_value = 1
			
			#node Edge Neighbors
			edge_neighbors = normals_grouping.nodes.new("GeometryNodeInputMeshEdgeNeighbors")
			edge_neighbors.name = "Edge Neighbors"
			
			#node Convex Hull
			convex_hull = normals_grouping.nodes.new("GeometryNodeConvexHull")
			convex_hull.name = "Convex Hull"
			
			#node Geometry Proximity
			geometry_proximity_2 = normals_grouping.nodes.new("GeometryNodeProximity")
			geometry_proximity_2.name = "Geometry Proximity"
			geometry_proximity_2.target_element = 'POINTS'
			#Group ID
			geometry_proximity_2.inputs[1].default_value = 0
			#Source Position
			geometry_proximity_2.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Sample Group ID
			geometry_proximity_2.inputs[3].default_value = 0
			
			#node Color Ramp.001
			color_ramp_001 = normals_grouping.nodes.new("ShaderNodeValToRGB")
			color_ramp_001.name = "Color Ramp.001"
			color_ramp_001.color_ramp.color_mode = 'RGB'
			color_ramp_001.color_ramp.hue_interpolation = 'NEAR'
			color_ramp_001.color_ramp.interpolation = 'LINEAR'
			
			#initialize color ramp elements
			color_ramp_001.color_ramp.elements.remove(color_ramp_001.color_ramp.elements[0])
			color_ramp_001_cre_0 = color_ramp_001.color_ramp.elements[0]
			color_ramp_001_cre_0.position = 0.0
			color_ramp_001_cre_0.alpha = 1.0
			color_ramp_001_cre_0.color = (0.0, 0.0, 0.0, 1.0)

			color_ramp_001_cre_1 = color_ramp_001.color_ramp.elements.new(0.0010000000474974513)
			color_ramp_001_cre_1.alpha = 1.0
			color_ramp_001_cre_1.color = (1.0, 1.0, 1.0, 1.0)

			
			#node Math.005
			math_005_1 = normals_grouping.nodes.new("ShaderNodeMath")
			math_005_1.name = "Math.005"
			math_005_1.operation = 'ADD'
			math_005_1.use_clamp = False
			#Value_001
			math_005_1.inputs[1].default_value = 1.0
			
			#node Switch
			switch = normals_grouping.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'GEOMETRY'
			
			#node Group Input.001
			group_input_001_1 = normals_grouping.nodes.new("NodeGroupInput")
			group_input_001_1.name = "Group Input.001"
			group_input_001_1.outputs[0].hide = True
			group_input_001_1.outputs[1].hide = True
			group_input_001_1.outputs[3].hide = True
			group_input_001_1.outputs[4].hide = True
			group_input_001_1.outputs[5].hide = True
			group_input_001_1.outputs[6].hide = True
			
			
			
			
			#Set locations
			group_input_7.location = (204.3592987060547, -181.8707733154297)
			group_output_7.location = (6431.77587890625, 540.7098999023438)
			attribute_statistic_3.location = (1312.442626953125, -38.12742233276367)
			compare.location = (895.8220825195312, -277.0682067871094)
			normal.location = (1077.4613037109375, -373.5410461425781)
			separate_xyz_1.location = (1736.876953125, -104.07755279541016)
			separate_xyz_001_1.location = (1736.46826171875, -236.03651428222656)
			math_2.location = (1945.6480712890625, -80.46106719970703)
			math_001_1.location = (1940.6861572265625, -225.7430877685547)
			compare_001.location = (2137.651611328125, -36.78117752075195)
			compare_002_2.location = (2137.077880859375, -187.2474365234375)
			separate_xyz_002_1.location = (1631.6925048828125, -406.3127746582031)
			boolean_math_1.location = (2322.5966796875, -47.019901275634766)
			math_002_1.location = (1950.35009765625, -121.25308990478516)
			math_003_1.location = (1945.38818359375, -266.53509521484375)
			compare_003_1.location = (2142.353515625, -77.57319641113281)
			compare_004.location = (2141.77978515625, -228.03944396972656)
			boolean_math_001_1.location = (2321.029296875, -138.80198669433594)
			boolean_math_002_1.location = (2482.539306640625, -90.97406005859375)
			vector_math_1.location = (1482.4205322265625, -115.81622314453125)
			group.location = (1080.1556396484375, 209.65174865722656)
			store_named_attribute.location = (2701.977294921875, 286.0773010253906)
			merge_by_distance_1.location = (3241.5791015625, 152.36489868164062)
			sample_nearest.location = (3427.8271484375, 151.2932891845703)
			accumulate_field.location = (4138.98095703125, 208.4441375732422)
			set_id.location = (3654.337158203125, 308.4366149902344)
			id.location = (3875.201904296875, 49.810333251953125)
			named_attribute_001.location = (3875.570068359375, 176.7607421875)
			math_004_1.location = (4369.71142578125, 114.70435333251953)
			store_named_attribute_001.location = (4571.10693359375, 443.477294921875)
			named_attribute_002.location = (4553.66796875, -167.8817138671875)
			compare_005.location = (4814.47021484375, 246.478759765625)
			accumulate_field_001.location = (4146.78271484375, -37.168243408203125)
			id_002.location = (4142.83740234375, -229.8467254638672)
			index_1.location = (3976.972412109375, -219.1879119873047)
			separate_geometry_1.location = (4988.58837890625, 500.7110595703125)
			separate_geometry_002.location = (5624.767578125, 681.9642333984375)
			compare_007.location = (5628.23974609375, 538.3463745117188)
			edge_neighbors.location = (5627.96533203125, 384.048828125)
			convex_hull.location = (429.6838073730469, -355.4820251464844)
			geometry_proximity_2.location = (633.99072265625, -375.6583251953125)
			color_ramp_001.location = (4558.341796875, 46.60982131958008)
			math_005_1.location = (3974.522705078125, -72.06031036376953)
			switch.location = (5446.2392578125, 629.37890625)
			group_input_001_1.location = (4965.74560546875, 696.3538208007812)
			
			#Set dimensions
			group_input_7.width, group_input_7.height = 140.0, 100.0
			group_output_7.width, group_output_7.height = 140.0, 100.0
			attribute_statistic_3.width, attribute_statistic_3.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			normal.width, normal.height = 140.0, 100.0
			separate_xyz_1.width, separate_xyz_1.height = 140.0, 100.0
			separate_xyz_001_1.width, separate_xyz_001_1.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			compare_002_2.width, compare_002_2.height = 140.0, 100.0
			separate_xyz_002_1.width, separate_xyz_002_1.height = 140.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			math_002_1.width, math_002_1.height = 140.0, 100.0
			math_003_1.width, math_003_1.height = 140.0, 100.0
			compare_003_1.width, compare_003_1.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			merge_by_distance_1.width, merge_by_distance_1.height = 140.0, 100.0
			sample_nearest.width, sample_nearest.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			set_id.width, set_id.height = 140.0, 100.0
			id.width, id.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			math_004_1.width, math_004_1.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			compare_005.width, compare_005.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			id_002.width, id_002.height = 140.0, 100.0
			index_1.width, index_1.height = 140.0, 100.0
			separate_geometry_1.width, separate_geometry_1.height = 140.0, 100.0
			separate_geometry_002.width, separate_geometry_002.height = 140.0, 100.0
			compare_007.width, compare_007.height = 140.0, 100.0
			edge_neighbors.width, edge_neighbors.height = 140.0, 100.0
			convex_hull.width, convex_hull.height = 140.0, 100.0
			geometry_proximity_2.width, geometry_proximity_2.height = 140.0, 100.0
			color_ramp_001.width, color_ramp_001.height = 240.0, 100.0
			math_005_1.width, math_005_1.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
			
			#initialize normals_grouping links
			#normal.Normal -> attribute_statistic_3.Attribute
			normals_grouping.links.new(normal.outputs[0], attribute_statistic_3.inputs[2])
			#attribute_statistic_3.Mean -> separate_xyz_1.Vector
			normals_grouping.links.new(attribute_statistic_3.outputs[0], separate_xyz_1.inputs[0])
			#separate_xyz_1.X -> math_2.Value
			normals_grouping.links.new(separate_xyz_1.outputs[0], math_2.inputs[0])
			#separate_xyz_001_1.X -> math_2.Value
			normals_grouping.links.new(separate_xyz_001_1.outputs[0], math_2.inputs[1])
			#separate_xyz_1.X -> math_001_1.Value
			normals_grouping.links.new(separate_xyz_1.outputs[0], math_001_1.inputs[0])
			#separate_xyz_001_1.X -> math_001_1.Value
			normals_grouping.links.new(separate_xyz_001_1.outputs[0], math_001_1.inputs[1])
			#normal.Normal -> separate_xyz_002_1.Vector
			normals_grouping.links.new(normal.outputs[0], separate_xyz_002_1.inputs[0])
			#separate_xyz_002_1.X -> compare_001.A
			normals_grouping.links.new(separate_xyz_002_1.outputs[0], compare_001.inputs[0])
			#math_2.Value -> compare_001.B
			normals_grouping.links.new(math_2.outputs[0], compare_001.inputs[1])
			#separate_xyz_002_1.X -> compare_002_2.A
			normals_grouping.links.new(separate_xyz_002_1.outputs[0], compare_002_2.inputs[0])
			#math_001_1.Value -> compare_002_2.B
			normals_grouping.links.new(math_001_1.outputs[0], compare_002_2.inputs[1])
			#compare_001.Result -> boolean_math_1.Boolean
			normals_grouping.links.new(compare_001.outputs[0], boolean_math_1.inputs[0])
			#compare_002_2.Result -> boolean_math_1.Boolean
			normals_grouping.links.new(compare_002_2.outputs[0], boolean_math_1.inputs[1])
			#math_002_1.Value -> compare_003_1.B
			normals_grouping.links.new(math_002_1.outputs[0], compare_003_1.inputs[1])
			#math_003_1.Value -> compare_004.B
			normals_grouping.links.new(math_003_1.outputs[0], compare_004.inputs[1])
			#separate_xyz_1.Y -> math_002_1.Value
			normals_grouping.links.new(separate_xyz_1.outputs[1], math_002_1.inputs[0])
			#separate_xyz_1.Y -> math_003_1.Value
			normals_grouping.links.new(separate_xyz_1.outputs[1], math_003_1.inputs[0])
			#separate_xyz_001_1.Y -> math_002_1.Value
			normals_grouping.links.new(separate_xyz_001_1.outputs[1], math_002_1.inputs[1])
			#separate_xyz_001_1.Y -> math_003_1.Value
			normals_grouping.links.new(separate_xyz_001_1.outputs[1], math_003_1.inputs[1])
			#separate_xyz_002_1.Y -> compare_003_1.A
			normals_grouping.links.new(separate_xyz_002_1.outputs[1], compare_003_1.inputs[0])
			#separate_xyz_002_1.Y -> compare_004.A
			normals_grouping.links.new(separate_xyz_002_1.outputs[1], compare_004.inputs[0])
			#compare_003_1.Result -> boolean_math_001_1.Boolean
			normals_grouping.links.new(compare_003_1.outputs[0], boolean_math_001_1.inputs[0])
			#compare_004.Result -> boolean_math_001_1.Boolean
			normals_grouping.links.new(compare_004.outputs[0], boolean_math_001_1.inputs[1])
			#boolean_math_1.Boolean -> boolean_math_002_1.Boolean
			normals_grouping.links.new(boolean_math_1.outputs[0], boolean_math_002_1.inputs[0])
			#boolean_math_001_1.Boolean -> boolean_math_002_1.Boolean
			normals_grouping.links.new(boolean_math_001_1.outputs[0], boolean_math_002_1.inputs[1])
			#attribute_statistic_3.Standard Deviation -> vector_math_1.Vector
			normals_grouping.links.new(attribute_statistic_3.outputs[6], vector_math_1.inputs[0])
			#vector_math_1.Vector -> separate_xyz_001_1.Vector
			normals_grouping.links.new(vector_math_1.outputs[0], separate_xyz_001_1.inputs[0])
			#boolean_math_002_1.Boolean -> store_named_attribute.Value
			normals_grouping.links.new(boolean_math_002_1.outputs[0], store_named_attribute.inputs[3])
			#group.Geometry -> store_named_attribute.Geometry
			normals_grouping.links.new(group.outputs[0], store_named_attribute.inputs[0])
			#merge_by_distance_1.Geometry -> sample_nearest.Geometry
			normals_grouping.links.new(merge_by_distance_1.outputs[0], sample_nearest.inputs[0])
			#sample_nearest.Index -> set_id.ID
			normals_grouping.links.new(sample_nearest.outputs[0], set_id.inputs[2])
			#named_attribute_001.Attribute -> accumulate_field.Value
			normals_grouping.links.new(named_attribute_001.outputs[0], accumulate_field.inputs[0])
			#math_004_1.Value -> store_named_attribute_001.Value
			normals_grouping.links.new(math_004_1.outputs[0], store_named_attribute_001.inputs[3])
			#set_id.Geometry -> store_named_attribute_001.Geometry
			normals_grouping.links.new(set_id.outputs[0], store_named_attribute_001.inputs[0])
			#store_named_attribute_001.Geometry -> separate_geometry_1.Geometry
			normals_grouping.links.new(store_named_attribute_001.outputs[0], separate_geometry_1.inputs[0])
			#compare_005.Result -> separate_geometry_1.Selection
			normals_grouping.links.new(compare_005.outputs[0], separate_geometry_1.inputs[1])
			#group_input_7.Iterations -> group.Iterations
			normals_grouping.links.new(group_input_7.outputs[4], group.inputs[1])
			#compare_007.Result -> separate_geometry_002.Selection
			normals_grouping.links.new(compare_007.outputs[0], separate_geometry_002.inputs[1])
			#edge_neighbors.Face Count -> compare_007.A
			normals_grouping.links.new(edge_neighbors.outputs[0], compare_007.inputs[2])
			#separate_geometry_002.Inverted -> group_output_7.Geometry
			normals_grouping.links.new(separate_geometry_002.outputs[1], group_output_7.inputs[0])
			#compare.Result -> attribute_statistic_3.Selection
			normals_grouping.links.new(compare.outputs[0], attribute_statistic_3.inputs[1])
			#group_input_7.Geometry -> group.Geometry
			normals_grouping.links.new(group_input_7.outputs[0], group.inputs[0])
			#group_input_7.Geometry -> convex_hull.Geometry
			normals_grouping.links.new(group_input_7.outputs[1], convex_hull.inputs[0])
			#convex_hull.Convex Hull -> geometry_proximity_2.Geometry
			normals_grouping.links.new(convex_hull.outputs[0], geometry_proximity_2.inputs[0])
			#geometry_proximity_2.Distance -> compare.A
			normals_grouping.links.new(geometry_proximity_2.outputs[1], compare.inputs[0])
			#group_input_7.Distance -> merge_by_distance_1.Distance
			normals_grouping.links.new(group_input_7.outputs[5], merge_by_distance_1.inputs[2])
			#store_named_attribute.Geometry -> merge_by_distance_1.Geometry
			normals_grouping.links.new(store_named_attribute.outputs[0], merge_by_distance_1.inputs[0])
			#store_named_attribute.Geometry -> set_id.Geometry
			normals_grouping.links.new(store_named_attribute.outputs[0], set_id.inputs[0])
			#accumulate_field_001.Total -> math_004_1.Value
			normals_grouping.links.new(accumulate_field_001.outputs[2], math_004_1.inputs[1])
			#accumulate_field.Total -> math_004_1.Value
			normals_grouping.links.new(accumulate_field.outputs[2], math_004_1.inputs[0])
			#group.Geometry -> attribute_statistic_3.Geometry
			normals_grouping.links.new(group.outputs[0], attribute_statistic_3.inputs[0])
			#index_1.Index -> math_005_1.Value
			normals_grouping.links.new(index_1.outputs[0], math_005_1.inputs[0])
			#math_005_1.Value -> accumulate_field_001.Value
			normals_grouping.links.new(math_005_1.outputs[0], accumulate_field_001.inputs[0])
			#id_002.ID -> accumulate_field_001.Group ID
			normals_grouping.links.new(id_002.outputs[0], accumulate_field_001.inputs[1])
			#id.ID -> accumulate_field.Group ID
			normals_grouping.links.new(id.outputs[0], accumulate_field.inputs[1])
			#named_attribute_002.Attribute -> color_ramp_001.Fac
			normals_grouping.links.new(named_attribute_002.outputs[0], color_ramp_001.inputs[0])
			#color_ramp_001.Color -> compare_005.A
			normals_grouping.links.new(color_ramp_001.outputs[0], compare_005.inputs[0])
			#group_input_7.Nor Var -> vector_math_1.Scale
			normals_grouping.links.new(group_input_7.outputs[3], vector_math_1.inputs[3])
			#separate_geometry_1.Selection -> switch.False
			normals_grouping.links.new(separate_geometry_1.outputs[0], switch.inputs[1])
			#separate_geometry_1.Inverted -> switch.True
			normals_grouping.links.new(separate_geometry_1.outputs[1], switch.inputs[2])
			#switch.Output -> separate_geometry_002.Geometry
			normals_grouping.links.new(switch.outputs[0], separate_geometry_002.inputs[0])
			#group_input_001_1.Base/Top -> switch.Switch
			normals_grouping.links.new(group_input_001_1.outputs[2], switch.inputs[0])
			return normals_grouping

		normals_grouping = normals_grouping_node_group()

		#initialize arch_sandv node group
		def arch_sandv_node_group():
			arch_sandv = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Arch SandV")

			arch_sandv.color_tag = 'NONE'
			arch_sandv.description = ""

			arch_sandv.is_modifier = True
			
			#arch_sandv interface
			#Socket Geometry
			geometry_socket_12 = arch_sandv.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_12.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_13 = arch_sandv.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_13.attribute_domain = 'POINT'
			
			#Socket Base Mesh
			base_mesh_socket = arch_sandv.interface.new_socket(name = "Base Mesh", in_out='INPUT', socket_type = 'NodeSocketObject')
			base_mesh_socket.attribute_domain = 'POINT'
			base_mesh_socket.description = "The base mesh for identification"
			
			#Socket Guide Mesh
			guide_mesh_socket = arch_sandv.interface.new_socket(name = "Guide Mesh", in_out='INPUT', socket_type = 'NodeSocketObject')
			guide_mesh_socket.attribute_domain = 'POINT'
			guide_mesh_socket.description = "Input if complex meshes above"
			
			#Socket Decimation Ration
			decimation_ration_socket = arch_sandv.interface.new_socket(name = "Decimation Ration", in_out='INPUT', socket_type = 'NodeSocketFloat')
			decimation_ration_socket.default_value = 0.8999999761581421
			decimation_ration_socket.min_value = 0.0
			decimation_ration_socket.max_value = 1.0
			decimation_ration_socket.subtype = 'FACTOR'
			decimation_ration_socket.attribute_domain = 'POINT'
			decimation_ration_socket.description = "Decimate ratio of point cloud used for caluculations"
			
			#Socket XY Variance
			xy_variance_socket = arch_sandv.interface.new_socket(name = "XY Variance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			xy_variance_socket.default_value = 5.0
			xy_variance_socket.min_value = -10000.0
			xy_variance_socket.max_value = 10000.0
			xy_variance_socket.subtype = 'NONE'
			xy_variance_socket.attribute_domain = 'POINT'
			
			#Socket Z Variance
			z_variance_socket = arch_sandv.interface.new_socket(name = "Z Variance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			z_variance_socket.default_value = 5.0
			z_variance_socket.min_value = -10000.0
			z_variance_socket.max_value = 10000.0
			z_variance_socket.subtype = 'NONE'
			z_variance_socket.attribute_domain = 'POINT'
			
			#Socket Normal Segmentation
			normal_segmentation_socket = arch_sandv.interface.new_socket(name = "Normal Segmentation", in_out='INPUT', socket_type = 'NodeSocketBool')
			normal_segmentation_socket.default_value = False
			normal_segmentation_socket.attribute_domain = 'POINT'
			normal_segmentation_socket.description = "Segment based on mesh normals. Can aid in the creation of polygons"
			
			#Socket Base?
			base__socket = arch_sandv.interface.new_socket(name = "Base?", in_out='INPUT', socket_type = 'NodeSocketBool')
			base__socket.default_value = False
			base__socket.attribute_domain = 'POINT'
			base__socket.description = "Tick if wanting to identify flat surface"
			
			#Socket Nor Var
			nor_var_socket_1 = arch_sandv.interface.new_socket(name = "Nor Var", in_out='INPUT', socket_type = 'NodeSocketFloat')
			nor_var_socket_1.default_value = 3.5
			nor_var_socket_1.min_value = -10000.0
			nor_var_socket_1.max_value = 10000.0
			nor_var_socket_1.subtype = 'NONE'
			nor_var_socket_1.attribute_domain = 'POINT'
			nor_var_socket_1.description = "Factor of normal variation to be filitered"
			
			#Socket Smo It
			smo_it_socket = arch_sandv.interface.new_socket(name = "Smo It", in_out='INPUT', socket_type = 'NodeSocketInt')
			smo_it_socket.default_value = 0
			smo_it_socket.min_value = 0
			smo_it_socket.max_value = 100
			smo_it_socket.subtype = 'NONE'
			smo_it_socket.attribute_domain = 'POINT'
			smo_it_socket.description = "Smooth mesh. Note: this makes the geometry less accurate but can make it easier to filter different normals"
			
			#Socket Grouping Dist
			grouping_dist_socket = arch_sandv.interface.new_socket(name = "Grouping Dist", in_out='INPUT', socket_type = 'NodeSocketFloat')
			grouping_dist_socket.default_value = 0.0
			grouping_dist_socket.min_value = 0.0
			grouping_dist_socket.max_value = 3.4028234663852886e+38
			grouping_dist_socket.subtype = 'DISTANCE'
			grouping_dist_socket.attribute_domain = 'POINT'
			grouping_dist_socket.description = "Groups normals based on distance input"
			
			#Socket Max Z
			max_z_socket = arch_sandv.interface.new_socket(name = "Max Z", in_out='INPUT', socket_type = 'NodeSocketFloat')
			max_z_socket.default_value = 500.0
			max_z_socket.min_value = -10000.0
			max_z_socket.max_value = 10000.0
			max_z_socket.subtype = 'NONE'
			max_z_socket.attribute_domain = 'POINT'
			max_z_socket.description = "Maximum Z value for mesh"
			
			#Socket Min Z
			min_z_socket = arch_sandv.interface.new_socket(name = "Min Z", in_out='INPUT', socket_type = 'NodeSocketFloat')
			min_z_socket.default_value = -0.4399999976158142
			min_z_socket.min_value = -10000.0
			min_z_socket.max_value = 10000.0
			min_z_socket.subtype = 'NONE'
			min_z_socket.attribute_domain = 'POINT'
			min_z_socket.description = "Minimum Z value for mesh"
			
			#Socket Poly Res
			poly_res_socket = arch_sandv.interface.new_socket(name = "Poly Res", in_out='INPUT', socket_type = 'NodeSocketInt')
			poly_res_socket.default_value = 31
			poly_res_socket.min_value = 1
			poly_res_socket.max_value = 100000
			poly_res_socket.subtype = 'NONE'
			poly_res_socket.attribute_domain = 'POINT'
			poly_res_socket.description = "Ploygon resolution"
			
			#Socket Translation
			translation_socket = arch_sandv.interface.new_socket(name = "Translation", in_out='INPUT', socket_type = 'NodeSocketVector')
			translation_socket.default_value = (0.0, 0.0, 0.0)
			translation_socket.min_value = -3.4028234663852886e+38
			translation_socket.max_value = 3.4028234663852886e+38
			translation_socket.subtype = 'TRANSLATION'
			translation_socket.attribute_domain = 'POINT'
			translation_socket.description = "Translate polygon: Note: useful if there is missing geometry above the mesh"
			
			#Socket Output
			output_socket_1 = arch_sandv.interface.new_socket(name = "Output", in_out='INPUT', socket_type = 'NodeSocketMenu')
			output_socket_1.default_value = "Mesh"
			output_socket_1.attribute_domain = 'POINT'
			
			#Socket Volume Resolution
			volume_resolution_socket = arch_sandv.interface.new_socket(name = "Volume Resolution", in_out='INPUT', socket_type = 'NodeSocketFloat')
			volume_resolution_socket.default_value = 0.0
			volume_resolution_socket.min_value = 0.0
			volume_resolution_socket.max_value = 3.4028234663852886e+38
			volume_resolution_socket.subtype = 'NONE'
			volume_resolution_socket.attribute_domain = 'POINT'
			volume_resolution_socket.description = "Fine tune value to achieve more accurate results. Higher the better for sphere volume. Lowere the better for voxel volume"
			
			#Socket Volume Sub Level
			volume_sub_level_socket = arch_sandv.interface.new_socket(name = "Volume Sub Level", in_out='INPUT', socket_type = 'NodeSocketInt')
			volume_sub_level_socket.default_value = 6
			volume_sub_level_socket.min_value = 2
			volume_sub_level_socket.max_value = 10
			volume_sub_level_socket.subtype = 'NONE'
			volume_sub_level_socket.attribute_domain = 'POINT'
			volume_sub_level_socket.description = "Subdivides mesh and dispalces to match original mesh"
			
			#Socket Simplify
			simplify_socket = arch_sandv.interface.new_socket(name = "Simplify", in_out='INPUT', socket_type = 'NodeSocketBool')
			simplify_socket.default_value = False
			simplify_socket.attribute_domain = 'POINT'
			simplify_socket.description = "Simplify mesh"
			
			#Socket End Resolution
			end_resolution_socket = arch_sandv.interface.new_socket(name = "End Resolution", in_out='INPUT', socket_type = 'NodeSocketFloat')
			end_resolution_socket.default_value = 0.029999999329447746
			end_resolution_socket.min_value = 0.0
			end_resolution_socket.max_value = 3.4028234663852886e+38
			end_resolution_socket.subtype = 'DISTANCE'
			end_resolution_socket.attribute_domain = 'POINT'
			end_resolution_socket.description = "Resolution of final mesh"
			
			
			#initialize arch_sandv nodes
			#node Group Output
			group_output_8 = arch_sandv.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Object Info
			object_info = arch_sandv.nodes.new("GeometryNodeObjectInfo")
			object_info.name = "Object Info"
			object_info.transform_space = 'RELATIVE'
			#As Instance
			object_info.inputs[1].default_value = False
			
			#node Mesh to Points
			mesh_to_points = arch_sandv.nodes.new("GeometryNodeMeshToPoints")
			mesh_to_points.name = "Mesh to Points"
			mesh_to_points.mode = 'FACES'
			#Selection
			mesh_to_points.inputs[1].default_value = True
			#Position
			mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Radius
			mesh_to_points.inputs[3].default_value = 0.009999999776482582
			
			#node Delete Geometry
			delete_geometry = arch_sandv.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'POINT'
			delete_geometry.mode = 'ALL'
			
			#node Random Value
			random_value = arch_sandv.nodes.new("FunctionNodeRandomValue")
			random_value.name = "Random Value"
			random_value.hide = True
			random_value.data_type = 'BOOLEAN'
			#ID
			random_value.inputs[7].default_value = 0
			#Seed
			random_value.inputs[8].default_value = 1
			
			#node Join Geometry
			join_geometry = arch_sandv.nodes.new("GeometryNodeJoinGeometry")
			join_geometry.name = "Join Geometry"
			
			#node Group
			group_1 = arch_sandv.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = volumeapproximation
			#Socket_2
			group_1.inputs[1].default_value = False
			#Socket_3
			group_1.inputs[2].default_value = (1.5, 1.5, 1.5)
			
			#node Group.001
			group_001_1 = arch_sandv.nodes.new("GeometryNodeGroup")
			group_001_1.name = "Group.001"
			group_001_1.node_tree = seperate_by_xyz
			
			#node Group.003
			group_003 = arch_sandv.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = poly_creation
			
			#node Convex Hull
			convex_hull_1 = arch_sandv.nodes.new("GeometryNodeConvexHull")
			convex_hull_1.name = "Convex Hull"
			
			#node Group.002
			group_002 = arch_sandv.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = normals_grouping
			
			#node Switch.002
			switch_002 = arch_sandv.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'GEOMETRY'
			
			#node Compare
			compare_1 = arch_sandv.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.hide = True
			compare_1.data_type = 'FLOAT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'LESS_THAN'
			
			#node Separate XYZ
			separate_xyz_2 = arch_sandv.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz_2.name = "Separate XYZ"
			separate_xyz_2.hide = True
			
			#node Position
			position_2 = arch_sandv.nodes.new("GeometryNodeInputPosition")
			position_2.name = "Position"
			position_2.hide = True
			
			#node Merge by Distance
			merge_by_distance_2 = arch_sandv.nodes.new("GeometryNodeMergeByDistance")
			merge_by_distance_2.name = "Merge by Distance"
			merge_by_distance_2.mode = 'ALL'
			#Selection
			merge_by_distance_2.inputs[1].default_value = True
			
			#node Group Input.003
			group_input_003 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[1].hide = True
			group_input_003.outputs[4].hide = True
			group_input_003.outputs[5].hide = True
			group_input_003.outputs[6].hide = True
			group_input_003.outputs[9].hide = True
			group_input_003.outputs[10].hide = True
			group_input_003.outputs[11].hide = True
			group_input_003.outputs[13].hide = True
			group_input_003.outputs[15].hide = True
			group_input_003.outputs[16].hide = True
			group_input_003.outputs[17].hide = True
			group_input_003.outputs[18].hide = True
			group_input_003.outputs[20].hide = True
			
			#node Object Info.001
			object_info_001 = arch_sandv.nodes.new("GeometryNodeObjectInfo")
			object_info_001.name = "Object Info.001"
			object_info_001.transform_space = 'RELATIVE'
			#As Instance
			object_info_001.inputs[1].default_value = False
			
			#node Join Geometry.001
			join_geometry_001 = arch_sandv.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001.name = "Join Geometry.001"
			
			#node Compare.001
			compare_001_1 = arch_sandv.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.hide = True
			compare_001_1.data_type = 'FLOAT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'GREATER_THAN'
			
			#node Group Input.004
			group_input_004 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_004.name = "Group Input.004"
			group_input_004.outputs[18].hide = True
			
			#node Delete Geometry.001
			delete_geometry_001 = arch_sandv.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry_001.name = "Delete Geometry.001"
			delete_geometry_001.domain = 'POINT'
			delete_geometry_001.mode = 'ALL'
			
			#node Compare.002
			compare_002_3 = arch_sandv.nodes.new("FunctionNodeCompare")
			compare_002_3.name = "Compare.002"
			compare_002_3.data_type = 'INT'
			compare_002_3.mode = 'ELEMENT'
			compare_002_3.operation = 'LESS_EQUAL'
			#B_INT
			compare_002_3.inputs[3].default_value = 1
			
			#node Vertex Neighbors
			vertex_neighbors = arch_sandv.nodes.new("GeometryNodeInputMeshVertexNeighbors")
			vertex_neighbors.name = "Vertex Neighbors"
			
			#node Transform Geometry
			transform_geometry_1 = arch_sandv.nodes.new("GeometryNodeTransform")
			transform_geometry_1.name = "Transform Geometry"
			transform_geometry_1.mode = 'COMPONENTS'
			#Rotation
			transform_geometry_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_1.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Boolean Math
			boolean_math_2 = arch_sandv.nodes.new("FunctionNodeBooleanMath")
			boolean_math_2.name = "Boolean Math"
			boolean_math_2.hide = True
			boolean_math_2.operation = 'AND'
			
			#node Raycast
			raycast_1 = arch_sandv.nodes.new("GeometryNodeRaycast")
			raycast_1.name = "Raycast"
			raycast_1.data_type = 'FLOAT'
			raycast_1.mapping = 'INTERPOLATED'
			#Attribute
			raycast_1.inputs[1].default_value = 0.0
			#Source Position
			raycast_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Ray Direction
			raycast_1.inputs[3].default_value = (0.0, 0.0, 1.0)
			#Ray Length
			raycast_1.inputs[4].default_value = 100.0
			
			#node Delete Geometry.002
			delete_geometry_002 = arch_sandv.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry_002.name = "Delete Geometry.002"
			delete_geometry_002.domain = 'POINT'
			delete_geometry_002.mode = 'ALL'
			
			#node Scale Elements
			scale_elements = arch_sandv.nodes.new("GeometryNodeScaleElements")
			scale_elements.name = "Scale Elements"
			scale_elements.domain = 'FACE'
			scale_elements.scale_mode = 'UNIFORM'
			#Selection
			scale_elements.inputs[1].default_value = True
			#Scale
			scale_elements.inputs[2].default_value = 1.2000000476837158
			#Center
			scale_elements.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Boolean Math.001
			boolean_math_001_2 = arch_sandv.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_2.name = "Boolean Math.001"
			boolean_math_001_2.operation = 'NOT'
			
			#node Switch.003
			switch_003 = arch_sandv.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'GEOMETRY'
			
			#node Group Input.002
			group_input_002 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[2].hide = True
			group_input_002.outputs[4].hide = True
			group_input_002.outputs[5].hide = True
			group_input_002.outputs[6].hide = True
			group_input_002.outputs[7].hide = True
			group_input_002.outputs[8].hide = True
			group_input_002.outputs[9].hide = True
			group_input_002.outputs[10].hide = True
			group_input_002.outputs[11].hide = True
			group_input_002.outputs[12].hide = True
			group_input_002.outputs[13].hide = True
			group_input_002.outputs[14].hide = True
			group_input_002.outputs[15].hide = True
			group_input_002.outputs[16].hide = True
			group_input_002.outputs[17].hide = True
			group_input_002.outputs[19].hide = True
			group_input_002.outputs[20].hide = True
			
			#node Reroute
			reroute = arch_sandv.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			reroute.hide = True
			#node Reroute.001
			reroute_001 = arch_sandv.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.004
			reroute_004 = arch_sandv.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			reroute_004.hide = True
			#node Reroute.006
			reroute_006 = arch_sandv.nodes.new("NodeReroute")
			reroute_006.name = "Reroute.006"
			#node Reroute.007
			reroute_007 = arch_sandv.nodes.new("NodeReroute")
			reroute_007.name = "Reroute.007"
			#node Reroute.008
			reroute_008 = arch_sandv.nodes.new("NodeReroute")
			reroute_008.name = "Reroute.008"
			#node Object Info.002
			object_info_002 = arch_sandv.nodes.new("GeometryNodeObjectInfo")
			object_info_002.name = "Object Info.002"
			object_info_002.transform_space = 'ORIGINAL'
			#As Instance
			object_info_002.inputs[1].default_value = False
			
			#node Attribute Statistic
			attribute_statistic_4 = arch_sandv.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic_4.name = "Attribute Statistic"
			attribute_statistic_4.data_type = 'FLOAT'
			attribute_statistic_4.domain = 'POINT'
			#Selection
			attribute_statistic_4.inputs[1].default_value = True
			
			#node Index
			index_2 = arch_sandv.nodes.new("GeometryNodeInputIndex")
			index_2.name = "Index"
			
			#node Compare.003
			compare_003_2 = arch_sandv.nodes.new("FunctionNodeCompare")
			compare_003_2.name = "Compare.003"
			compare_003_2.data_type = 'FLOAT'
			compare_003_2.mode = 'ELEMENT'
			compare_003_2.operation = 'GREATER_THAN'
			#B
			compare_003_2.inputs[1].default_value = 0.0
			
			#node Switch.005
			switch_005 = arch_sandv.nodes.new("GeometryNodeSwitch")
			switch_005.name = "Switch.005"
			switch_005.input_type = 'GEOMETRY'
			
			#node Frame
			frame_2 = arch_sandv.nodes.new("NodeFrame")
			frame_2.label = "Join geometry of meshes prior to analysis"
			frame_2.name = "Frame"
			frame_2.label_size = 20
			frame_2.shrink = True
			
			#node Frame.001
			frame_001_1 = arch_sandv.nodes.new("NodeFrame")
			frame_001_1.label = "simplify pointcould"
			frame_001_1.name = "Frame.001"
			frame_001_1.label_size = 20
			frame_001_1.shrink = True
			
			#node Frame.002
			frame_002 = arch_sandv.nodes.new("NodeFrame")
			frame_002.label = "XYZ variation filtering"
			frame_002.name = "Frame.002"
			frame_002.label_size = 20
			frame_002.shrink = True
			
			#node Frame.003
			frame_003 = arch_sandv.nodes.new("NodeFrame")
			frame_003.label = "Creation of polygon with option to transform polygon"
			frame_003.name = "Frame.003"
			frame_003.label_size = 20
			frame_003.shrink = True
			
			#node Frame.004
			frame_004 = arch_sandv.nodes.new("NodeFrame")
			frame_004.label = "Delete geometry not within polygon bounds"
			frame_004.name = "Frame.004"
			frame_004.label_size = 20
			frame_004.shrink = True
			
			#node Frame.005
			frame_005 = arch_sandv.nodes.new("NodeFrame")
			frame_005.label = "determine whether there is a guiding mesh"
			frame_005.name = "Frame.005"
			frame_005.label_size = 20
			frame_005.shrink = True
			
			#node Frame.006
			frame_006 = arch_sandv.nodes.new("NodeFrame")
			frame_006.label = "volume approximation"
			frame_006.name = "Frame.006"
			frame_006.label_size = 20
			frame_006.shrink = True
			
			#node Frame.008
			frame_008 = arch_sandv.nodes.new("NodeFrame")
			frame_008.label = "mesh simplification"
			frame_008.name = "Frame.008"
			frame_008.label_size = 20
			frame_008.shrink = True
			
			#node Menu Switch
			menu_switch = arch_sandv.nodes.new("GeometryNodeMenuSwitch")
			menu_switch.name = "Menu Switch"
			menu_switch.active_index = 0
			menu_switch.data_type = 'GEOMETRY'
			menu_switch.enum_items.clear()
			menu_switch.enum_items.new("Mesh")
			menu_switch.enum_items[0].description = ""
			menu_switch.enum_items.new("Polyline")
			menu_switch.enum_items[1].description = ""
			menu_switch.enum_items.new("Polygon")
			menu_switch.enum_items[2].description = ""
			menu_switch.enum_items.new("SphereVolume")
			menu_switch.enum_items[3].description = ""
			menu_switch.enum_items.new("VoxelVolume")
			menu_switch.enum_items[4].description = ""
			
			#node Delete Geometry.003
			delete_geometry_003 = arch_sandv.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry_003.name = "Delete Geometry.003"
			delete_geometry_003.domain = 'FACE'
			delete_geometry_003.mode = 'ALL'
			
			#node Boolean Math.002
			boolean_math_002_2 = arch_sandv.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_2.name = "Boolean Math.002"
			boolean_math_002_2.hide = True
			boolean_math_002_2.operation = 'NOT'
			
			#node Reroute.002
			reroute_002 = arch_sandv.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Group Input.005
			group_input_005 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_005.name = "Group Input.005"
			group_input_005.hide = True
			group_input_005.outputs[0].hide = True
			group_input_005.outputs[1].hide = True
			group_input_005.outputs[2].hide = True
			group_input_005.outputs[3].hide = True
			group_input_005.outputs[4].hide = True
			group_input_005.outputs[5].hide = True
			group_input_005.outputs[6].hide = True
			group_input_005.outputs[7].hide = True
			group_input_005.outputs[8].hide = True
			group_input_005.outputs[9].hide = True
			group_input_005.outputs[10].hide = True
			group_input_005.outputs[11].hide = True
			group_input_005.outputs[12].hide = True
			group_input_005.outputs[13].hide = True
			group_input_005.outputs[14].hide = True
			group_input_005.outputs[15].hide = True
			group_input_005.outputs[16].hide = True
			group_input_005.outputs[18].hide = True
			group_input_005.outputs[19].hide = True
			group_input_005.outputs[20].hide = True
			
			#node Group Input.006
			group_input_006 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_006.name = "Group Input.006"
			group_input_006.hide = True
			group_input_006.outputs[0].hide = True
			group_input_006.outputs[1].hide = True
			group_input_006.outputs[2].hide = True
			group_input_006.outputs[3].hide = True
			group_input_006.outputs[4].hide = True
			group_input_006.outputs[5].hide = True
			group_input_006.outputs[6].hide = True
			group_input_006.outputs[7].hide = True
			group_input_006.outputs[8].hide = True
			group_input_006.outputs[9].hide = True
			group_input_006.outputs[10].hide = True
			group_input_006.outputs[11].hide = True
			group_input_006.outputs[12].hide = True
			group_input_006.outputs[13].hide = True
			group_input_006.outputs[14].hide = True
			group_input_006.outputs[15].hide = True
			group_input_006.outputs[17].hide = True
			group_input_006.outputs[18].hide = True
			group_input_006.outputs[19].hide = True
			group_input_006.outputs[20].hide = True
			
			#node Group Input.007
			group_input_007 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_007.name = "Group Input.007"
			group_input_007.outputs[0].hide = True
			group_input_007.outputs[1].hide = True
			group_input_007.outputs[2].hide = True
			group_input_007.outputs[3].hide = True
			group_input_007.outputs[4].hide = True
			group_input_007.outputs[5].hide = True
			group_input_007.outputs[6].hide = True
			group_input_007.outputs[7].hide = True
			group_input_007.outputs[8].hide = True
			group_input_007.outputs[9].hide = True
			group_input_007.outputs[10].hide = True
			group_input_007.outputs[11].hide = True
			group_input_007.outputs[12].hide = True
			group_input_007.outputs[13].hide = True
			group_input_007.outputs[14].hide = True
			group_input_007.outputs[16].hide = True
			group_input_007.outputs[17].hide = True
			group_input_007.outputs[18].hide = True
			group_input_007.outputs[19].hide = True
			group_input_007.outputs[20].hide = True
			
			#node Group Input.008
			group_input_008 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_008.name = "Group Input.008"
			group_input_008.outputs[0].hide = True
			group_input_008.outputs[1].hide = True
			group_input_008.outputs[3].hide = True
			group_input_008.outputs[4].hide = True
			group_input_008.outputs[5].hide = True
			group_input_008.outputs[6].hide = True
			group_input_008.outputs[7].hide = True
			group_input_008.outputs[8].hide = True
			group_input_008.outputs[9].hide = True
			group_input_008.outputs[10].hide = True
			group_input_008.outputs[11].hide = True
			group_input_008.outputs[12].hide = True
			group_input_008.outputs[13].hide = True
			group_input_008.outputs[14].hide = True
			group_input_008.outputs[15].hide = True
			group_input_008.outputs[16].hide = True
			group_input_008.outputs[17].hide = True
			group_input_008.outputs[18].hide = True
			group_input_008.outputs[19].hide = True
			group_input_008.outputs[20].hide = True
			
			#node Group Input.001
			group_input_001_2 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_001_2.name = "Group Input.001"
			group_input_001_2.outputs[1].hide = True
			group_input_001_2.outputs[2].hide = True
			group_input_001_2.outputs[3].hide = True
			group_input_001_2.outputs[4].hide = True
			group_input_001_2.outputs[5].hide = True
			group_input_001_2.outputs[6].hide = True
			group_input_001_2.outputs[7].hide = True
			group_input_001_2.outputs[8].hide = True
			group_input_001_2.outputs[9].hide = True
			group_input_001_2.outputs[10].hide = True
			group_input_001_2.outputs[11].hide = True
			group_input_001_2.outputs[12].hide = True
			group_input_001_2.outputs[13].hide = True
			group_input_001_2.outputs[14].hide = True
			group_input_001_2.outputs[15].hide = True
			group_input_001_2.outputs[16].hide = True
			group_input_001_2.outputs[17].hide = True
			group_input_001_2.outputs[18].hide = True
			group_input_001_2.outputs[19].hide = True
			group_input_001_2.outputs[20].hide = True
			
			#node Group Input.009
			group_input_009 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_009.name = "Group Input.009"
			group_input_009.outputs[0].hide = True
			group_input_009.outputs[1].hide = True
			group_input_009.outputs[2].hide = True
			group_input_009.outputs[4].hide = True
			group_input_009.outputs[5].hide = True
			group_input_009.outputs[6].hide = True
			group_input_009.outputs[7].hide = True
			group_input_009.outputs[8].hide = True
			group_input_009.outputs[9].hide = True
			group_input_009.outputs[10].hide = True
			group_input_009.outputs[11].hide = True
			group_input_009.outputs[12].hide = True
			group_input_009.outputs[13].hide = True
			group_input_009.outputs[14].hide = True
			group_input_009.outputs[15].hide = True
			group_input_009.outputs[16].hide = True
			group_input_009.outputs[17].hide = True
			group_input_009.outputs[18].hide = True
			group_input_009.outputs[19].hide = True
			group_input_009.outputs[20].hide = True
			
			#node Group Input.010
			group_input_010 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_010.name = "Group Input.010"
			group_input_010.outputs[0].hide = True
			group_input_010.outputs[2].hide = True
			group_input_010.outputs[3].hide = True
			group_input_010.outputs[4].hide = True
			group_input_010.outputs[5].hide = True
			group_input_010.outputs[6].hide = True
			group_input_010.outputs[7].hide = True
			group_input_010.outputs[8].hide = True
			group_input_010.outputs[9].hide = True
			group_input_010.outputs[10].hide = True
			group_input_010.outputs[11].hide = True
			group_input_010.outputs[12].hide = True
			group_input_010.outputs[13].hide = True
			group_input_010.outputs[14].hide = True
			group_input_010.outputs[15].hide = True
			group_input_010.outputs[16].hide = True
			group_input_010.outputs[17].hide = True
			group_input_010.outputs[18].hide = True
			group_input_010.outputs[19].hide = True
			group_input_010.outputs[20].hide = True
			
			#node Group Input.011
			group_input_011 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_011.name = "Group Input.011"
			group_input_011.outputs[0].hide = True
			group_input_011.outputs[1].hide = True
			group_input_011.outputs[3].hide = True
			group_input_011.outputs[4].hide = True
			group_input_011.outputs[5].hide = True
			group_input_011.outputs[6].hide = True
			group_input_011.outputs[7].hide = True
			group_input_011.outputs[8].hide = True
			group_input_011.outputs[9].hide = True
			group_input_011.outputs[10].hide = True
			group_input_011.outputs[11].hide = True
			group_input_011.outputs[12].hide = True
			group_input_011.outputs[13].hide = True
			group_input_011.outputs[14].hide = True
			group_input_011.outputs[15].hide = True
			group_input_011.outputs[16].hide = True
			group_input_011.outputs[17].hide = True
			group_input_011.outputs[18].hide = True
			group_input_011.outputs[19].hide = True
			group_input_011.outputs[20].hide = True
			
			#node Group Input
			group_input_8 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			group_input_8.outputs[0].hide = True
			group_input_8.outputs[1].hide = True
			group_input_8.outputs[2].hide = True
			group_input_8.outputs[3].hide = True
			group_input_8.outputs[4].hide = True
			group_input_8.outputs[5].hide = True
			group_input_8.outputs[6].hide = True
			group_input_8.outputs[7].hide = True
			group_input_8.outputs[8].hide = True
			group_input_8.outputs[9].hide = True
			group_input_8.outputs[10].hide = True
			group_input_8.outputs[11].hide = True
			group_input_8.outputs[12].hide = True
			group_input_8.outputs[14].hide = True
			group_input_8.outputs[15].hide = True
			group_input_8.outputs[16].hide = True
			group_input_8.outputs[17].hide = True
			group_input_8.outputs[18].hide = True
			group_input_8.outputs[19].hide = True
			group_input_8.outputs[20].hide = True
			
			#node Group Input.012
			group_input_012 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_012.name = "Group Input.012"
			group_input_012.outputs[0].hide = True
			group_input_012.outputs[1].hide = True
			group_input_012.outputs[2].hide = True
			group_input_012.outputs[3].hide = True
			group_input_012.outputs[4].hide = True
			group_input_012.outputs[5].hide = True
			group_input_012.outputs[6].hide = True
			group_input_012.outputs[7].hide = True
			group_input_012.outputs[8].hide = True
			group_input_012.outputs[9].hide = True
			group_input_012.outputs[10].hide = True
			group_input_012.outputs[11].hide = True
			group_input_012.outputs[12].hide = True
			group_input_012.outputs[13].hide = True
			group_input_012.outputs[15].hide = True
			group_input_012.outputs[16].hide = True
			group_input_012.outputs[17].hide = True
			group_input_012.outputs[18].hide = True
			group_input_012.outputs[19].hide = True
			group_input_012.outputs[20].hide = True
			
			#node Reroute.003
			reroute_003 = arch_sandv.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Reroute.005
			reroute_005 = arch_sandv.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Reroute.009
			reroute_009 = arch_sandv.nodes.new("NodeReroute")
			reroute_009.name = "Reroute.009"
			#node Reroute.010
			reroute_010 = arch_sandv.nodes.new("NodeReroute")
			reroute_010.name = "Reroute.010"
			#node Reroute.011
			reroute_011 = arch_sandv.nodes.new("NodeReroute")
			reroute_011.name = "Reroute.011"
			#node Group Input.013
			group_input_013 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_013.name = "Group Input.013"
			group_input_013.outputs[0].hide = True
			group_input_013.outputs[1].hide = True
			group_input_013.outputs[2].hide = True
			group_input_013.outputs[3].hide = True
			group_input_013.outputs[5].hide = True
			group_input_013.outputs[6].hide = True
			group_input_013.outputs[7].hide = True
			group_input_013.outputs[8].hide = True
			group_input_013.outputs[9].hide = True
			group_input_013.outputs[10].hide = True
			group_input_013.outputs[11].hide = True
			group_input_013.outputs[12].hide = True
			group_input_013.outputs[13].hide = True
			group_input_013.outputs[14].hide = True
			group_input_013.outputs[15].hide = True
			group_input_013.outputs[16].hide = True
			group_input_013.outputs[17].hide = True
			group_input_013.outputs[18].hide = True
			group_input_013.outputs[19].hide = True
			group_input_013.outputs[20].hide = True
			
			#node Group Input.014
			group_input_014 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_014.name = "Group Input.014"
			group_input_014.outputs[0].hide = True
			group_input_014.outputs[1].hide = True
			group_input_014.outputs[2].hide = True
			group_input_014.outputs[3].hide = True
			group_input_014.outputs[4].hide = True
			group_input_014.outputs[6].hide = True
			group_input_014.outputs[7].hide = True
			group_input_014.outputs[8].hide = True
			group_input_014.outputs[9].hide = True
			group_input_014.outputs[10].hide = True
			group_input_014.outputs[11].hide = True
			group_input_014.outputs[12].hide = True
			group_input_014.outputs[13].hide = True
			group_input_014.outputs[14].hide = True
			group_input_014.outputs[15].hide = True
			group_input_014.outputs[16].hide = True
			group_input_014.outputs[17].hide = True
			group_input_014.outputs[18].hide = True
			group_input_014.outputs[19].hide = True
			group_input_014.outputs[20].hide = True
			
			#node Group Input.015
			group_input_015 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_015.name = "Group Input.015"
			group_input_015.outputs[0].hide = True
			group_input_015.outputs[1].hide = True
			group_input_015.outputs[2].hide = True
			group_input_015.outputs[3].hide = True
			group_input_015.outputs[4].hide = True
			group_input_015.outputs[5].hide = True
			group_input_015.outputs[6].hide = True
			group_input_015.outputs[7].hide = True
			group_input_015.outputs[8].hide = True
			group_input_015.outputs[9].hide = True
			group_input_015.outputs[10].hide = True
			group_input_015.outputs[12].hide = True
			group_input_015.outputs[13].hide = True
			group_input_015.outputs[14].hide = True
			group_input_015.outputs[15].hide = True
			group_input_015.outputs[16].hide = True
			group_input_015.outputs[17].hide = True
			group_input_015.outputs[18].hide = True
			group_input_015.outputs[19].hide = True
			group_input_015.outputs[20].hide = True
			
			#node Group Input.016
			group_input_016 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_016.name = "Group Input.016"
			group_input_016.outputs[0].hide = True
			group_input_016.outputs[1].hide = True
			group_input_016.outputs[2].hide = True
			group_input_016.outputs[3].hide = True
			group_input_016.outputs[4].hide = True
			group_input_016.outputs[5].hide = True
			group_input_016.outputs[6].hide = True
			group_input_016.outputs[7].hide = True
			group_input_016.outputs[8].hide = True
			group_input_016.outputs[9].hide = True
			group_input_016.outputs[10].hide = True
			group_input_016.outputs[11].hide = True
			group_input_016.outputs[13].hide = True
			group_input_016.outputs[14].hide = True
			group_input_016.outputs[15].hide = True
			group_input_016.outputs[16].hide = True
			group_input_016.outputs[17].hide = True
			group_input_016.outputs[18].hide = True
			group_input_016.outputs[19].hide = True
			group_input_016.outputs[20].hide = True
			
			#node Group Input.017
			group_input_017 = arch_sandv.nodes.new("NodeGroupInput")
			group_input_017.name = "Group Input.017"
			group_input_017.outputs[0].hide = True
			group_input_017.outputs[1].hide = True
			group_input_017.outputs[2].hide = True
			group_input_017.outputs[3].hide = True
			group_input_017.outputs[4].hide = True
			group_input_017.outputs[5].hide = True
			group_input_017.outputs[7].hide = True
			group_input_017.outputs[8].hide = True
			group_input_017.outputs[9].hide = True
			group_input_017.outputs[10].hide = True
			group_input_017.outputs[11].hide = True
			group_input_017.outputs[12].hide = True
			group_input_017.outputs[13].hide = True
			group_input_017.outputs[14].hide = True
			group_input_017.outputs[15].hide = True
			group_input_017.outputs[16].hide = True
			group_input_017.outputs[17].hide = True
			group_input_017.outputs[18].hide = True
			group_input_017.outputs[19].hide = True
			group_input_017.outputs[20].hide = True
			
			
			
			#Set parents
			object_info.parent = frame_2
			mesh_to_points.parent = frame_001_1
			delete_geometry.parent = frame_001_1
			random_value.parent = frame_001_1
			join_geometry.parent = frame_006
			group_1.parent = frame_006
			group_001_1.parent = frame_002
			group_003.parent = frame_003
			convex_hull_1.parent = frame_002
			merge_by_distance_2.parent = frame_008
			group_input_003.parent = frame_008
			object_info_001.parent = frame_2
			join_geometry_001.parent = frame_2
			delete_geometry_001.parent = frame_008
			compare_002_3.parent = frame_008
			vertex_neighbors.parent = frame_008
			transform_geometry_1.parent = frame_003
			raycast_1.parent = frame_004
			delete_geometry_002.parent = frame_004
			scale_elements.parent = frame_004
			boolean_math_001_2.parent = frame_004
			object_info_002.parent = frame_005
			attribute_statistic_4.parent = frame_005
			index_2.parent = frame_005
			compare_003_2.parent = frame_005
			switch_005.parent = frame_006
			menu_switch.parent = frame_008
			group_input_005.parent = frame_006
			group_input_006.parent = frame_006
			group_input_009.parent = frame_001_1
			group_input_012.parent = frame_003
			group_input_013.parent = frame_002
			
			#Set locations
			group_output_8.location = (9872.6240234375, 385.742431640625)
			object_info.location = (-1002.3025512695312, 395.0776062011719)
			mesh_to_points.location = (651.7927856445312, -35.688079833984375)
			delete_geometry.location = (822.020751953125, -62.109283447265625)
			random_value.location = (818.935546875, -215.0519561767578)
			join_geometry.location = (6327.96875, -124.3108901977539)
			group_1.location = (6888.54736328125, 172.8320770263672)
			group_001_1.location = (1321.1658935546875, -10.873616218566895)
			group_003.location = (3105.609375, -931.3862915039062)
			convex_hull_1.location = (998.698486328125, -270.3301086425781)
			group_002.location = (1654.13330078125, -463.4346618652344)
			switch_002.location = (1882.9439697265625, -298.5397033691406)
			compare_1.location = (1830.12890625, -771.37060546875)
			separate_xyz_2.location = (1831.4156494140625, -737.195068359375)
			position_2.location = (1830.6929931640625, -705.6486206054688)
			merge_by_distance_2.location = (8145.1357421875, 6.8497314453125)
			group_input_003.location = (7910.197265625, -58.66612243652344)
			object_info_001.location = (-1004.02294921875, 200.48052978515625)
			join_geometry_001.location = (-626.213134765625, 351.1382751464844)
			compare_001_1.location = (1833.6826171875, -804.2164916992188)
			group_input_004.location = (962.8855590820312, -405.0161437988281)
			delete_geometry_001.location = (8343.5107421875, 76.26475524902344)
			compare_002_3.location = (8337.3095703125, -77.5423583984375)
			vertex_neighbors.location = (8343.2392578125, -234.5266876220703)
			transform_geometry_1.location = (3412.369384765625, -854.5142211914062)
			boolean_math_2.location = (2006.57861328125, -782.6784057617188)
			raycast_1.location = (4080.0654296875, -378.3426818847656)
			delete_geometry_002.location = (4442.80908203125, -384.0328063964844)
			scale_elements.location = (3897.076416015625, -479.8783264160156)
			boolean_math_001_2.location = (4256.60693359375, -548.4243774414062)
			switch_003.location = (9579.5869140625, 388.8095397949219)
			group_input_002.location = (9577.8779296875, 471.0426330566406)
			reroute.location = (987.6797485351562, 323.719970703125)
			reroute_001.location = (252.33367919921875, 314.3369445800781)
			reroute_004.location = (4115.23779296875, 323.0516662597656)
			reroute_006.location = (6088.72021484375, -916.142333984375)
			reroute_007.location = (7029.46435546875, -916.142333984375)
			reroute_008.location = (4734.90771484375, -176.3975372314453)
			object_info_002.location = (5810.76708984375, -375.0498962402344)
			attribute_statistic_4.location = (6004.02392578125, -295.5960998535156)
			index_2.location = (5814.56005859375, -571.9496459960938)
			compare_003_2.location = (6193.82958984375, -399.2239685058594)
			switch_005.location = (6612.71728515625, -292.0635681152344)
			frame_2.location = (0.0, 0.0)
			frame_001_1.location = (-81.81982421875, 7.4418840408325195)
			frame_002.location = (0.0, 0.0)
			frame_003.location = (0.0, 0.0)
			frame_004.location = (0.0, 0.0)
			frame_005.location = (54.6015625, 979.738525390625)
			frame_006.location = (30.990234375, 0.221923828125)
			frame_008.location = (743.7744140625, 129.0619659423828)
			menu_switch.location = (7634.595703125, 188.7558135986328)
			delete_geometry_003.location = (2376.151123046875, -668.2239379882812)
			boolean_math_002_2.location = (2182.274169921875, -782.6648559570312)
			reroute_002.location = (2398.904052734375, 233.62469482421875)
			group_input_005.location = (6633.10986328125, -38.48883056640625)
			group_input_006.location = (6627.87353515625, 5.687906742095947)
			group_input_007.location = (8117.62060546875, 315.8629150390625)
			group_input_008.location = (5656.81494140625, 535.8052368164062)
			group_input_001_2.location = (746.59912109375, -293.4263000488281)
			group_input_009.location = (645.4197387695312, -209.9334716796875)
			group_input_010.location = (-1202.500732421875, 261.3804626464844)
			group_input_011.location = (-1225.8795166015625, 65.75022888183594)
			group_input_8.location = (2887.9443359375, -1037.66064453125)
			group_input_012.location = (3106.050537109375, -868.918212890625)
			reroute_003.location = (3338.921875, -1213.1029052734375)
			reroute_005.location = (6783.87890625, -1255.9334716796875)
			reroute_009.location = (8129.49072265625, 175.2739715576172)
			reroute_010.location = (7027.73046875, -862.3976440429688)
			reroute_011.location = (8129.49072265625, 198.8519744873047)
			group_input_013.location = (1000.0664672851562, -120.99077606201172)
			group_input_014.location = (1004.27197265625, -175.68931579589844)
			group_input_015.location = (1624.3897705078125, -748.247802734375)
			group_input_016.location = (1625.8292236328125, -808.7300415039062)
			group_input_017.location = (1650.6856689453125, -118.47991180419922)
			
			#Set dimensions
			group_output_8.width, group_output_8.height = 140.0, 100.0
			object_info.width, object_info.height = 140.0, 100.0
			mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			random_value.width, random_value.height = 140.0, 100.0
			join_geometry.width, join_geometry.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			group_001_1.width, group_001_1.height = 140.0, 100.0
			group_003.width, group_003.height = 140.0, 100.0
			convex_hull_1.width, convex_hull_1.height = 140.0, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			separate_xyz_2.width, separate_xyz_2.height = 140.0, 100.0
			position_2.width, position_2.height = 140.0, 100.0
			merge_by_distance_2.width, merge_by_distance_2.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			object_info_001.width, object_info_001.height = 140.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			group_input_004.width, group_input_004.height = 140.0, 100.0
			delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
			compare_002_3.width, compare_002_3.height = 140.0, 100.0
			vertex_neighbors.width, vertex_neighbors.height = 140.0, 100.0
			transform_geometry_1.width, transform_geometry_1.height = 140.0, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			raycast_1.width, raycast_1.height = 150.0, 100.0
			delete_geometry_002.width, delete_geometry_002.height = 140.0, 100.0
			scale_elements.width, scale_elements.height = 140.0, 100.0
			boolean_math_001_2.width, boolean_math_001_2.height = 140.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			reroute_006.width, reroute_006.height = 16.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			reroute_008.width, reroute_008.height = 16.0, 100.0
			object_info_002.width, object_info_002.height = 140.0, 100.0
			attribute_statistic_4.width, attribute_statistic_4.height = 140.0, 100.0
			index_2.width, index_2.height = 140.0, 100.0
			compare_003_2.width, compare_003_2.height = 140.0, 100.0
			switch_005.width, switch_005.height = 140.0, 100.0
			frame_2.width, frame_2.height = 576.0, 465.16668701171875
			frame_001_1.width, frame_001_1.height = 374.66668701171875, 292.5
			frame_002.width, frame_002.height = 520.6666870117188, 399.8333435058594
			frame_003.width, frame_003.height = 505.33349609375, 343.16668701171875
			frame_004.width, frame_004.height = 743.333251953125, 411.1666564941406
			frame_005.width, frame_005.height = 581.3330078125, 392.5
			frame_006.width, frame_006.height = 758.6669921875, 670.5
			frame_008.width, frame_008.height = 906.666015625, 560.5
			menu_switch.width, menu_switch.height = 140.0, 100.0
			delete_geometry_003.width, delete_geometry_003.height = 140.0, 100.0
			boolean_math_002_2.width, boolean_math_002_2.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			group_input_005.width, group_input_005.height = 133.7897186279297, 100.0
			group_input_006.width, group_input_006.height = 140.0, 100.0
			group_input_007.width, group_input_007.height = 140.0, 100.0
			group_input_008.width, group_input_008.height = 140.0, 100.0
			group_input_001_2.width, group_input_001_2.height = 140.0, 100.0
			group_input_009.width, group_input_009.height = 140.0, 100.0
			group_input_010.width, group_input_010.height = 140.0, 100.0
			group_input_011.width, group_input_011.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			group_input_012.width, group_input_012.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			reroute_009.width, reroute_009.height = 16.0, 100.0
			reroute_010.width, reroute_010.height = 16.0, 100.0
			reroute_011.width, reroute_011.height = 16.0, 100.0
			group_input_013.width, group_input_013.height = 140.0, 100.0
			group_input_014.width, group_input_014.height = 140.0, 100.0
			group_input_015.width, group_input_015.height = 140.0, 100.0
			group_input_016.width, group_input_016.height = 140.0, 100.0
			group_input_017.width, group_input_017.height = 140.0, 100.0
			
			#initialize arch_sandv links
			#random_value.Value -> delete_geometry.Selection
			arch_sandv.links.new(random_value.outputs[3], delete_geometry.inputs[1])
			#group_001_1.Inverted -> group_002.Geometry
			arch_sandv.links.new(group_001_1.outputs[0], group_002.inputs[0])
			#group_001_1.Inverted -> switch_002.False
			arch_sandv.links.new(group_001_1.outputs[0], switch_002.inputs[1])
			#separate_xyz_2.Z -> compare_1.A
			arch_sandv.links.new(separate_xyz_2.outputs[2], compare_1.inputs[0])
			#position_2.Position -> separate_xyz_2.Vector
			arch_sandv.links.new(position_2.outputs[0], separate_xyz_2.inputs[0])
			#group_002.Geometry -> switch_002.True
			arch_sandv.links.new(group_002.outputs[0], switch_002.inputs[2])
			#group_input_003.End Resolution -> merge_by_distance_2.Distance
			arch_sandv.links.new(group_input_003.outputs[19], merge_by_distance_2.inputs[2])
			#separate_xyz_2.Z -> compare_001_1.A
			arch_sandv.links.new(separate_xyz_2.outputs[2], compare_001_1.inputs[0])
			#group_input_004.Base? -> group_002.Base/Top
			arch_sandv.links.new(group_input_004.outputs[7], group_002.inputs[2])
			#group_input_004.Nor Var -> group_002.Nor Var
			arch_sandv.links.new(group_input_004.outputs[8], group_002.inputs[3])
			#group_input_004.Smo It -> group_002.Iterations
			arch_sandv.links.new(group_input_004.outputs[9], group_002.inputs[4])
			#group_input_004.Grouping Dist -> group_002.Distance
			arch_sandv.links.new(group_input_004.outputs[10], group_002.inputs[5])
			#merge_by_distance_2.Geometry -> delete_geometry_001.Geometry
			arch_sandv.links.new(merge_by_distance_2.outputs[0], delete_geometry_001.inputs[0])
			#compare_002_3.Result -> delete_geometry_001.Selection
			arch_sandv.links.new(compare_002_3.outputs[0], delete_geometry_001.inputs[1])
			#vertex_neighbors.Vertex Count -> compare_002_3.A
			arch_sandv.links.new(vertex_neighbors.outputs[0], compare_002_3.inputs[2])
			#compare_001_1.Result -> boolean_math_2.Boolean
			arch_sandv.links.new(compare_001_1.outputs[0], boolean_math_2.inputs[1])
			#compare_1.Result -> boolean_math_2.Boolean
			arch_sandv.links.new(compare_1.outputs[0], boolean_math_2.inputs[0])
			#scale_elements.Geometry -> raycast_1.Target Geometry
			arch_sandv.links.new(scale_elements.outputs[0], raycast_1.inputs[0])
			#transform_geometry_1.Geometry -> scale_elements.Geometry
			arch_sandv.links.new(transform_geometry_1.outputs[0], scale_elements.inputs[0])
			#raycast_1.Is Hit -> boolean_math_001_2.Boolean
			arch_sandv.links.new(raycast_1.outputs[0], boolean_math_001_2.inputs[0])
			#boolean_math_001_2.Boolean -> delete_geometry_002.Selection
			arch_sandv.links.new(boolean_math_001_2.outputs[0], delete_geometry_002.inputs[1])
			#mesh_to_points.Points -> delete_geometry.Geometry
			arch_sandv.links.new(mesh_to_points.outputs[0], delete_geometry.inputs[0])
			#delete_geometry.Geometry -> group_001_1.Geometry
			arch_sandv.links.new(delete_geometry.outputs[0], group_001_1.inputs[0])
			#delete_geometry_001.Geometry -> switch_003.True
			arch_sandv.links.new(delete_geometry_001.outputs[0], switch_003.inputs[2])
			#switch_003.Output -> group_output_8.Geometry
			arch_sandv.links.new(switch_003.outputs[0], group_output_8.inputs[0])
			#group_input_002.Simplify -> switch_003.Switch
			arch_sandv.links.new(group_input_002.outputs[18], switch_003.inputs[0])
			#reroute.Output -> group_001_1.Socket
			arch_sandv.links.new(reroute.outputs[0], group_001_1.inputs[1])
			#reroute_001.Output -> reroute.Input
			arch_sandv.links.new(reroute_001.outputs[0], reroute.inputs[0])
			#reroute_001.Output -> mesh_to_points.Mesh
			arch_sandv.links.new(reroute_001.outputs[0], mesh_to_points.inputs[0])
			#reroute.Output -> reroute_004.Input
			arch_sandv.links.new(reroute.outputs[0], reroute_004.inputs[0])
			#reroute_004.Output -> delete_geometry_002.Geometry
			arch_sandv.links.new(reroute_004.outputs[0], delete_geometry_002.inputs[0])
			#transform_geometry_1.Geometry -> reroute_006.Input
			arch_sandv.links.new(transform_geometry_1.outputs[0], reroute_006.inputs[0])
			#reroute_006.Output -> join_geometry.Geometry
			arch_sandv.links.new(reroute_006.outputs[0], join_geometry.inputs[0])
			#reroute_006.Output -> reroute_007.Input
			arch_sandv.links.new(reroute_006.outputs[0], reroute_007.inputs[0])
			#delete_geometry_002.Geometry -> reroute_008.Input
			arch_sandv.links.new(delete_geometry_002.outputs[0], reroute_008.inputs[0])
			#convex_hull_1.Convex Hull -> group_001_1.Attribute
			arch_sandv.links.new(convex_hull_1.outputs[0], group_001_1.inputs[2])
			#object_info_001.Geometry -> join_geometry_001.Geometry
			arch_sandv.links.new(object_info_001.outputs[4], join_geometry_001.inputs[0])
			#group_003.Polygon -> transform_geometry_1.Geometry
			arch_sandv.links.new(group_003.outputs[0], transform_geometry_1.inputs[0])
			#join_geometry_001.Geometry -> reroute_001.Input
			arch_sandv.links.new(join_geometry_001.outputs[0], reroute_001.inputs[0])
			#object_info_002.Geometry -> attribute_statistic_4.Geometry
			arch_sandv.links.new(object_info_002.outputs[4], attribute_statistic_4.inputs[0])
			#compare_003_2.Result -> switch_005.Switch
			arch_sandv.links.new(compare_003_2.outputs[0], switch_005.inputs[0])
			#delete_geometry_002.Geometry -> switch_005.True
			arch_sandv.links.new(delete_geometry_002.outputs[0], switch_005.inputs[2])
			#join_geometry.Geometry -> switch_005.False
			arch_sandv.links.new(join_geometry.outputs[0], switch_005.inputs[1])
			#switch_005.Output -> group_1.Geometry
			arch_sandv.links.new(switch_005.outputs[0], group_1.inputs[0])
			#index_2.Index -> attribute_statistic_4.Attribute
			arch_sandv.links.new(index_2.outputs[0], attribute_statistic_4.inputs[2])
			#attribute_statistic_4.Max -> compare_003_2.A
			arch_sandv.links.new(attribute_statistic_4.outputs[4], compare_003_2.inputs[0])
			#group_1.SphereVolume -> menu_switch.SphereVolume
			arch_sandv.links.new(group_1.outputs[0], menu_switch.inputs[4])
			#menu_switch.Output -> switch_003.False
			arch_sandv.links.new(menu_switch.outputs[0], switch_003.inputs[1])
			#menu_switch.Output -> merge_by_distance_2.Geometry
			arch_sandv.links.new(menu_switch.outputs[0], merge_by_distance_2.inputs[0])
			#boolean_math_2.Boolean -> boolean_math_002_2.Boolean
			arch_sandv.links.new(boolean_math_2.outputs[0], boolean_math_002_2.inputs[0])
			#boolean_math_002_2.Boolean -> delete_geometry_003.Selection
			arch_sandv.links.new(boolean_math_002_2.outputs[0], delete_geometry_003.inputs[1])
			#switch_002.Output -> delete_geometry_003.Geometry
			arch_sandv.links.new(switch_002.outputs[0], delete_geometry_003.inputs[0])
			#delete_geometry_003.Geometry -> group_003.Geometry
			arch_sandv.links.new(delete_geometry_003.outputs[0], group_003.inputs[0])
			#group_1.VoxelVolume -> menu_switch.VoxelVolume
			arch_sandv.links.new(group_1.outputs[1], menu_switch.inputs[5])
			#switch_002.Output -> reroute_002.Input
			arch_sandv.links.new(switch_002.outputs[0], reroute_002.inputs[0])
			#reroute_002.Output -> menu_switch.Mesh
			arch_sandv.links.new(reroute_002.outputs[0], menu_switch.inputs[1])
			#group_input_005.Volume Sub Level -> group_1.Voxel Amount
			arch_sandv.links.new(group_input_005.outputs[17], group_1.inputs[4])
			#group_input_006.Volume Resolution -> group_1.Sphere Volume Iterations
			arch_sandv.links.new(group_input_006.outputs[16], group_1.inputs[3])
			#group_input_007.Output -> menu_switch.Menu
			arch_sandv.links.new(group_input_007.outputs[15], menu_switch.inputs[0])
			#group_input_008.Guide Mesh -> object_info_002.Object
			arch_sandv.links.new(group_input_008.outputs[2], object_info_002.inputs[0])
			#group_input_001_2.Geometry -> convex_hull_1.Geometry
			arch_sandv.links.new(group_input_001_2.outputs[0], convex_hull_1.inputs[0])
			#group_input_009.Decimation Ration -> random_value.Probability
			arch_sandv.links.new(group_input_009.outputs[3], random_value.inputs[6])
			#group_input_010.Base Mesh -> object_info.Object
			arch_sandv.links.new(group_input_010.outputs[1], object_info.inputs[0])
			#group_input_011.Guide Mesh -> object_info_001.Object
			arch_sandv.links.new(group_input_011.outputs[2], object_info_001.inputs[0])
			#group_input_8.Poly Res -> group_003.Count
			arch_sandv.links.new(group_input_8.outputs[13], group_003.inputs[1])
			#group_input_012.Translation -> transform_geometry_1.Translation
			arch_sandv.links.new(group_input_012.outputs[14], transform_geometry_1.inputs[1])
			#group_003.Polyline -> reroute_003.Input
			arch_sandv.links.new(group_003.outputs[1], reroute_003.inputs[0])
			#reroute_003.Output -> reroute_005.Input
			arch_sandv.links.new(reroute_003.outputs[0], reroute_005.inputs[0])
			#reroute_007.Output -> reroute_009.Input
			arch_sandv.links.new(reroute_007.outputs[0], reroute_009.inputs[0])
			#reroute_009.Output -> menu_switch.Polygon
			arch_sandv.links.new(reroute_009.outputs[0], menu_switch.inputs[3])
			#reroute_005.Output -> reroute_010.Input
			arch_sandv.links.new(reroute_005.outputs[0], reroute_010.inputs[0])
			#reroute_010.Output -> reroute_011.Input
			arch_sandv.links.new(reroute_010.outputs[0], reroute_011.inputs[0])
			#reroute_011.Output -> menu_switch.Polyline
			arch_sandv.links.new(reroute_011.outputs[0], menu_switch.inputs[2])
			#group_input_013.XY Variance -> group_001_1.XY
			arch_sandv.links.new(group_input_013.outputs[4], group_001_1.inputs[3])
			#group_input_014.Z Variance -> group_001_1.Z
			arch_sandv.links.new(group_input_014.outputs[5], group_001_1.inputs[4])
			#group_input_015.Max Z -> compare_1.B
			arch_sandv.links.new(group_input_015.outputs[11], compare_1.inputs[1])
			#group_input_016.Min Z -> compare_001_1.B
			arch_sandv.links.new(group_input_016.outputs[12], compare_001_1.inputs[1])
			#group_input_017.Normal Segmentation -> switch_002.Switch
			arch_sandv.links.new(group_input_017.outputs[6], switch_002.inputs[0])
			#group_input_004.Geometry -> group_002.Geometry
			arch_sandv.links.new(group_input_004.outputs[0], group_002.inputs[1])
			#object_info.Geometry -> join_geometry_001.Geometry
			arch_sandv.links.new(object_info.outputs[4], join_geometry_001.inputs[0])
			#reroute_008.Output -> join_geometry.Geometry
			arch_sandv.links.new(reroute_008.outputs[0], join_geometry.inputs[0])
			return arch_sandv

		arch_sandv = arch_sandv_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Arch SandV", type = 'NODES')
		mod.node_group = arch_sandv
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Arch_SandV.bl_idname)
			
def register():
	bpy.utils.register_class(Arch_SandV)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Arch_SandV)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
