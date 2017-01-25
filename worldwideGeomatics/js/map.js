function loadmap(){

	//Define base layer
	var baseLayer = new ol.layer.Group({
	    'title': 'Base maps',
	    layers: [
	     new ol.layer.Tile({
	         title: 'OpenStreetMaps',
	         type: 'base',
	         visible: true,
	         source: new ol.source.OSM({})
	     }),
	     new ol.layer.Tile({
	         title: 'Satellite',
	         type: 'base',
	         visible: false,
	         source: new ol.source.BingMaps({
	         key: 'AuMYsjPiJV8n-I3rDG51XpAku8YE0O2G91d6fkTD9cySpaRF9lRxrjF1dMqCEMyy',
	         imagerySet:'AerialWithLabels'})
	    })
	    ]});

	// The features are not added to a regular vector layer/source, but to a feature overlay which holds a collection of features.
	// This collection is passed to the modify and also the draw interaction, so that both can add or modify features.
	// Create vector drawing layer
	drawingLayer = new ol.layer.Vector({
	        source: new ol.source.Vector({
	        format: new ol.format.TopoJSON(),
	        projection: 'EPSG:4326'
	    }),
	    //We add the style for the vector drawing layer
	    style: new ol.style.Style ({
	          fill: new ol.style.Fill({
	             color: 'rgba(0,128,250,0.6)'
	           }),
	           stroke: new ol.style.Stroke({
	            color: 'rgba(0,128,250)',
	            width: 3
	           }),
	           image: new ol.style.Circle({
	                        radius: 5,
	                        fill: new ol.style.Fill({
	                            color: 'rgba(0,128,250)'
	                        })
	                    })
	        })
	});

	var reportsPoints = new ol.layer.Tile({
	    source: new ol.source.TileWMS({
	    url: 'http://localhost:8080/geoserver/wms',
	    params: {'LAYERS': 'karlsruheDamageReport:reportspoints', 'TILED': true}
	    })
	});

	var reportsLines = new ol.layer.Tile({
	    source: new ol.source.TileWMS({
	    url: 'http://localhost:8080/geoserver/wms',
	    params: {'LAYERS': 'karlsruheDamageReport:reportslines', 'TILED': true}
	    })
	});

	var reportsPolygons = new ol.layer.Tile({
	    source: new ol.source.TileWMS({
	    url: 'http://localhost:8080/geoserver/wms',
	    params: {'LAYERS': 'karlsruheDamageReport:reportspolygons', 'TILED': true}
	    })
	});

	var view = new ol.View({
			projection: 'EPSG:4326',
	        center: [8.403, 49.009],
	        zoom: 15
	});

	//We create the map variables
	map = new ol.Map({target: 'map_container',layers: [baseLayer, drawingLayer,reportsPolygons,reportsLines, reportsPoints],view: view});

	var interaction; //http://openlayers.org/en/master/apidoc/ol.interaction.Draw.html
	
	olHelper = {};
	geometry=[]
	
	olHelper.dpoint = function() {
			map.removeInteraction(interaction); //Removes the previous interaction
		    console.log("Selected button to draw points");
		    interaction = new ol.interaction.Draw({
		    	type: 'Point',
		    	source: drawingLayer.getSource(), 
		    	geometryFunction: function(coords, geom) {
													        if (!geom) {
													            geom = new ol.geom.Point(null);
													        }
													        geom.setCoordinates(coords);
													        geometry.push(geom.A);
													        if (geometry.length > 0) {
													        	map.removeInteraction(interaction);
													        }
													        return geom;
													    }});
		    
		    map.addInteraction(interaction); //Adds the new interaction
		    $("#map_container").click(function(){
		    	document.getElementById("drawPoint").disabled=true;
		    	document.getElementById("drawLine").disabled=true;
		    	document.getElementById("drawPolygon").disabled=true;
			});
	};

	olHelper.dline=function() {
	    map.removeInteraction(interaction); //Removes the previous interaction
	    console.log("Selected button to draw lines");
	    interaction = new ol.interaction.Draw({
	    	type: 'LineString',
	    	source: drawingLayer.getSource(),
	    	geometryFunction: function(coords, geom) {
													        if (!geom) {
													            geom = new ol.geom.LineString(null);
													        }
													        geom.setCoordinates(coords);
													        if (drawingLayer.getSource().getFeatures().length > 0) {
													        	map.removeInteraction(interaction);
													        	
													        }
													        return geom;
													    }});

	    
	    map.addInteraction(interaction); //Adds the new interaction
	    $("#map_container").click(function(){
	    	document.getElementById("drawPoint").disabled=true;
	    	document.getElementById("drawLine").disabled=true;
	    	document.getElementById("drawPolygon").disabled=true;
		});
	    $("#map_container").dblclick(function(){
			geometry.push(drawingLayer.getSource().getFeatures()[0].f.target.A);
		});
	};

	olHelper.dpolygon= function() {
	    map.removeInteraction(interaction); //Removes the previous interaction
	    console.log("Selected button to draw polygons");
	    interaction = new ol.interaction.Draw({
	    	type: 'Polygon',
	    	source: drawingLayer.getSource(),
	    	geometryFunction: function(coords, geom) {
													        if (!geom) {
													            geom = new ol.geom.Polygon(null);
													        }
													        geom.setCoordinates(coords);
													        if (drawingLayer.getSource().getFeatures().length > 0) {
													        	map.removeInteraction(interaction);
													        }
													        return geom;
													    }});
	    map.addInteraction(interaction); //Adds the new interaction
	    $("#map_container").click(function(){
	    	document.getElementById("drawPoint").disabled=true;
	    	document.getElementById("drawLine").disabled=true;
	    	document.getElementById("drawPolygon").disabled=true;
		});
	    $("#map_container").dblclick(function(){
			geometry.push(drawingLayer.getSource().getFeatures()[0].f.target.A);
		});
	};

	olHelper.modify= function() {
	    map.removeInteraction(interaction); //Removes the previous interaction
	    console.log("Selected button to modify");
	    interaction = new ol.interaction.Modify({features: new ol.Collection(drawingLayer.getSource().getFeatures())});
	    map.addInteraction(interaction); //Adds the new interaction
	};

	olHelper.del= function() {
		geometry=[]
		document.getElementById("drawPoint").disabled=false;
    	document.getElementById("drawLine").disabled=false;
    	document.getElementById("drawPolygon").disabled=false;
	    console.log("Clear the map");
	    var features = drawingLayer.getSource().getFeatures();
	    var source = drawingLayer.getSource();
	    source.clear();
	    //features.clear();
	};
	
	//Add Layer Switcher
	var layerSwitcher = new ol.control.LayerSwitcher({tipLabel: 'Choose a base layer'});
	map.addControl(layerSwitcher);
}