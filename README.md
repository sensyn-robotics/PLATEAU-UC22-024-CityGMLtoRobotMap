
# CityGMLtoRobotMap

## process

### CityGML
#### create obj model from city gml
1, download plateau data  
2, gml to obj : convert to obj `python gml2obj.py` with custom coordinate origin 

#####  extract lod3
`./citygml-tools-1.4.4/citygml-tools filter-lods --lod=3 --mode=maximum *.gml`

#### create pointcloud from obj model
`python create_sampling_point_cloud.py`


### fit bim model to city gml model
1, convert ifc to obj  
2, align bim model to city gml


### BIM(ifc)
`ifcconvert `


### post process
merge multi pointcloud
