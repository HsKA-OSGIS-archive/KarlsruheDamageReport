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
      <sld:Name>reportspolygons</sld:Name>
      <sld:Title/>
      <sld:FeatureTypeStyle>


     <sld:Rule>
          <sld:Name>Floodling</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Flooding</ogc:Literal>
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
          <sld:PolygonSymbolizer>
                <sld:Fill>
                    <sld:GraphicFill>
                    <sld:Graphic>
                     <sld:ExternalGraphic>
                      <sld:OnlineResource xlink:type="simple" xlink:href="waterdrop_orange.png" />
                      <sld:Format>image/png</sld:Format>
                     </sld:ExternalGraphic>
                  <sld:Size>12</sld:Size>
                  </sld:Graphic>
                  </sld:GraphicFill>
              </sld:Fill>                                
                <sld:Stroke>
                <sld:CssParameter name="Stroke">#FFB82B</sld:CssParameter>
          		    <sld:CssParameter name="Stroke-width">2</sld:CssParameter>
                </sld:Stroke>
            </sld:PolygonSymbolizer>
        </sld:Rule>       

      <Rule>
        <sld:Name>Road Block</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsEqualTo>
                <ogc:PropertyName>type</ogc:PropertyName>
                <ogc:Literal>Road Block</ogc:Literal>
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
         <sld:PolygonSymbolizer>
          	<sld:Fill>
          		<sld:GraphicFill>
          			<sld:Graphic>
          				<sld:Mark>
          					<sld:WellKnownName>cross</sld:WellKnownName>
          					<sld:Fill>
          						<sld:CssParameter name="fill">#FFB82B</sld:CssParameter>
          					</sld:Fill>
          				</sld:Mark>
                 <Size>4</Size>
          			</sld:Graphic>
          		</sld:GraphicFill>
          	</sld:Fill>
          	<sld:Stroke>
          		<sld:CssParameter name="Stroke">#FFB82B</sld:CssParameter>
          		<sld:CssParameter name="Stroke-width">2</sld:CssParameter>
          	</sld:Stroke>
         </sld:PolygonSymbolizer>
       </Rule>
        

       <sld:Rule>
            <sld:Name>Construction Site</sld:Name>
            <ogc:Filter>
              <ogc:And>
                <ogc:PropertyIsEqualTo>
                  <ogc:PropertyName>type</ogc:PropertyName>
                  <ogc:Literal>Construction Site</ogc:Literal>
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
            <sld:PolygonSymbolizer>
                  <sld:Fill>
                      <sld:GraphicFill>
                      <sld:Graphic>
                      <sld:ExternalGraphic>
                      <sld:OnlineResource xlink:type="simple" xlink:href="triangle_orange.png" />
                      <sld:Format>image/png</sld:Format>
                      </sld:ExternalGraphic>
                      <sld:Size>10</sld:Size>
                      </sld:Graphic>
                      </sld:GraphicFill>
                      </sld:Fill>                                
                      <sld:Stroke>
                      <sld:CssParameter name="Stroke">#FFB82B</sld:CssParameter>
              <sld:CssParameter name="Stroke-width">2</sld:CssParameter>
                  </sld:Stroke>
              </sld:PolygonSymbolizer>
          </sld:Rule>               


          <sld:Rule>
               <sld:Name>Zombie outbreak</sld:Name>
               <ogc:Filter>
                 <ogc:And>
                   <ogc:PropertyIsEqualTo>
                     <ogc:PropertyName>type</ogc:PropertyName>
                     <ogc:Literal>Zombie outbreak</ogc:Literal>
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
               <sld:PolygonSymbolizer>
                     <sld:Fill>
                         <sld:GraphicFill>
                         <sld:Graphic>
                          <sld:ExternalGraphic>
                           <sld:OnlineResource xlink:type="simple" xlink:href="zombie2_orange.png" />
                           <sld:Format>image/png</sld:Format>
                          </sld:ExternalGraphic>
                         <sld:Size>12</sld:Size>
                        </sld:Graphic>
                       </sld:GraphicFill>
                      </sld:Fill>                                
                     <sld:Stroke>
                     <sld:CssParameter name="Stroke">#FFB82B</sld:CssParameter>
                       <sld:CssParameter name="Stroke-width">2</sld:CssParameter>
                     </sld:Stroke>
                 </sld:PolygonSymbolizer>
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
          <sld:PolygonSymbolizer>
                <sld:Fill>
                    <sld:GraphicFill>
                    <sld:Graphic>
                     <sld:ExternalGraphic>
                      <sld:OnlineResource xlink:type="simple" xlink:href="Other2_orange.png" />
                      <sld:Format>image/png</sld:Format>
                     </sld:ExternalGraphic>
                  <sld:Size>12</sld:Size>
                  </sld:Graphic>
                  </sld:GraphicFill>
              </sld:Fill>                                
                <sld:Stroke>
                <sld:CssParameter name="Stroke">#FFB82B</sld:CssParameter>
          		    <sld:CssParameter name="Stroke-width">2</sld:CssParameter>
                </sld:Stroke>
            </sld:PolygonSymbolizer>
        </sld:Rule>       
        
        
       </sld:FeatureTypeStyle>
     </sld:UserStyle>
   </sld:UserLayer>
 </sld:StyledLayerDescriptor>