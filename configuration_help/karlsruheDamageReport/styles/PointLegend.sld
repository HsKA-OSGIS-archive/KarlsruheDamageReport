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
          <sld:Name>Fallen Tree</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Fallen Trees</ogc:Literal>
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
                <sld:OnlineResource xlink:type="simple" xlink:href="treedown_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

      

        <sld:Rule>
          <sld:Name>Water Leak</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Water Leaks</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="water_leak2_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

        <sld:Rule>
          <sld:Name>Fire</sld:Name>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="fire_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

        <sld:Rule>
          <sld:Name>Road Closed</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Road Closed</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="closedroad_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>


        <sld:Rule>
          <sld:Name>Powerline Down</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Powerline Down</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="powerlinepole_ornage2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

        <sld:Rule>
          <sld:Name>Zombie</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Zombie</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="zombie-outbreak_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

        <sld:Rule>
          <sld:Name>Cash Machine</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Cash Machine</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="atm_euro_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

        <sld:Rule>
          <sld:Name>Fire Hydrant</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Fire Hidrants</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="fire-hydrant_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>  

        <sld:Rule>
          <sld:Name>Manhole</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Manholes</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="manhole_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>


        <sld:Rule>
          <sld:Name>Parking Meter</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Parking Meter</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="parking_meter_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>


        <sld:Rule>
          <sld:Name>Post Box</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Postboxes</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="post_box_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

        <sld:Rule>
          <sld:Name>Pothole</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Pothole</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="pothole_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

        <sld:Rule>
          <sld:Name>Street Light</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Street Lights</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="street_light_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>


        <sld:Rule>
          <sld:Name>Street Sign</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Street Signs</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="street_signs_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

        <sld:Rule>
          <sld:Name>Trash Can</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Trash Cans</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="trash_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

        <sld:Rule>
          <sld:Name>Traffic Light</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Traffic Lights</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="traffic_light_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

        <sld:Rule>
          <sld:Name>Other</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Other</ogc:Literal>
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
            <sld:Graphic>
              <sld:ExternalGraphic>
                <sld:OnlineResource xlink:type="simple" xlink:href="other_orange2.png" />
                <sld:Format>image/png</sld:Format>
              </sld:ExternalGraphic>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>


      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:UserLayer>
</sld:StyledLayerDescriptor>