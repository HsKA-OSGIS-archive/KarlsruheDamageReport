<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor
                           xmlns="http://www.opengis.net/sld"
                           xmlns:sld="http://www.opengis.net/sld"
                           xmlns:ogc="http://www.opengis.net/ogc"
                           xmlns:gml="http://www.opengis.net/gml"
                           xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0.0">

  <sld:UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>reportspoints</sld:Name>
      <sld:Title/>
      <sld:FeatureTypeStyle>


        <sld:Rule>
          <sld:Name>Normal Issue</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Fire</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>solved</ogc:PropertyName>
                <ogc:Literal>false</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>emergency</ogc:PropertyName>
                <ogc:Literal>false</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:MaxScaleDenominator>100000</sld:MaxScaleDenominator>
          <sld:PointSymbolizer>
            <Geometry>
               <ogc:Function name="offset">
                  <ogc:PropertyName>geometry</ogc:PropertyName>
                  <ogc:Literal>0</ogc:Literal>
                 <ogc:Literal>131.2</ogc:Literal>
                 </ogc:Function>
            </Geometry>
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="fire_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

                <sld:Rule>
          <sld:Name>Solved Issue</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Fire</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>solved</ogc:PropertyName>
                <ogc:Literal>false</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:MaxScaleDenominator>100000</sld:MaxScaleDenominator>
          <sld:PointSymbolizer>
            <Geometry>
               <ogc:Function name="offset">
                  <ogc:PropertyName>geometry</ogc:PropertyName>
                  <ogc:Literal>0</ogc:Literal>
                 <ogc:Literal>131.2</ogc:Literal>
                 </ogc:Function>
            </Geometry>
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="fire_green2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

      

        <sld:Rule>
          <sld:Name>Emergency</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Fire</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>solved</ogc:PropertyName>
                <ogc:Literal>false</ogc:Literal>
              </ogc:PropertyIsEqualTo>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>emergency</ogc:PropertyName>
                <ogc:Literal>true</ogc:Literal>
              </ogc:PropertyIsEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:MaxScaleDenominator>100000</sld:MaxScaleDenominator>
          <sld:PointSymbolizer>
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="fire_red2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>




      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:UserLayer>
</sld:StyledLayerDescriptor>