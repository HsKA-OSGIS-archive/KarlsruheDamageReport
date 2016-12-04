function loadmap(){

	//Define base layer
	var baseLayer = new ol.layer.Tile({source: new ol.source.OSM({})});

	// The features are not added to a regular vector layer/source, but to a feature overlay which holds a collection of features.
	// This collection is passed to the modify and also the draw interaction, so that both can add or modify features.
	// Create vector layer
	var limitsLayer = new ol.layer.Vector({
	        source: new ol.source.StaticVector({
	        //url: 'data.json',
	        format: new ol.format.TopoJSON(),
	        projection: 'EPSG:3857'
	    })
	});

	var reportsPolygons = new ol.layer.Tile({
	    source: new ol.source.TileWMS({
	    url: 'http://localhost:8080/geoserver/wms',
	    params: {'LAYERS': 'karlsruheDamageReport:reportsPolygons', 'TILED': true}
	    })
	});

	var reportsPoints = new ol.layer.Tile({
	    source: new ol.source.TileWMS({
	    url: 'http://localhost:8080/geoserver/wms',
	    params: {'LAYERS': 'karlsruheDamageReport:reportsPoints', 'TILED': true}
	    })
	});

	var reportsLines = new ol.layer.Tile({
	    source: new ol.source.TileWMS({
	    url: 'http://localhost:8080/geoserver/wms',
	    params: {'LAYERS': 'karlsruheDamageReport:reportsLines', 'TILED': true}
	    })
	});

	var view = new ol.View({
	        center: ol.proj.transform([8.4, 49.01], 'EPSG:4326', 'EPSG:3857'),
	        zoom: 13
	});

	//We create the map variables
	var map = new ol.Map({target: 'map',layers: [baseLayer, limitsLayer,reportsPolygons,reportsLines, reportsPoints],view: view});

	//Interactions
	var button = $('#pan').button('toggle');

	var interaction;
	$('div.btn-group button').on('click', function(event) {
	    var id = event.target.id;
	    // Toggle buttons
	    button.button('toggle');
	    button = $('#'+id).button('toggle');
	    
	    // Remove previous interaction
	    map.removeInteraction(interaction);
	    
	    // Update active interaction
	    switch(event.target.id) {
	        case "select": // id="select"
	            interaction = new ol.interaction.Select();
	            map.addInteraction(interaction);
	            break;
	        case "point": // id="point"
	            interaction = new ol.interaction.Draw({type: 'Point',source: limitsLayer.getSource()});
	            map.addInteraction(interaction);
	            break;
	        case "line": // id="line"
	            interaction = new ol.interaction.Draw({type: 'LineString',source: limitsLayer.getSource()});
	            map.addInteraction(interaction);
	            break;
	        case "polygon": // id="polygon"
	            interaction = new ol.interaction.Draw({type: 'Polygon',source: limitsLayer.getSource()});
	            map.addInteraction(interaction);
	            break;
	        case "modify": // id="modify"
	            interaction = new ol.interaction.Modify({features: new ol.Collection(limitsLayer.getSource().getFeatures())});
	            map.addInteraction(interaction);
	            break;
	        //case "clear": // id="clear"
	        //    interaction = new ol.source.Clear();
	        //    limitsLayer.clear(limitsLayer);
	        //    break;
	        default:
	            break;
	    }
	});
}