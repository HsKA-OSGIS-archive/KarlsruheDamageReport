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
      <sld:Name>reportlines</sld:Name>
      <sld:Title/>
      <sld:FeatureTypeStyle>
                
                
                     <sld:Rule>
                      <sld:Name>Road Block</sld:Name>
                      <ogc:Filter>
                         <ogc:And>
                           <ogc:PropertyIsEqualTo>
                             <ogc:PropertyName>type</ogc:PropertyName>
                             <ogc:Literal>Road Blocks</ogc:Literal>
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
                      <sld:MaxScaleDenominator>75000</sld:MaxScaleDenominator>
                      <sld:LineSymbolizer>
                            <sld:Stroke>
                              <sld:GraphicStroke>
                                    <sld:Graphic>
                                      <sld:Mark>
                                            <sld:WellKnownName>circle</sld:WellKnownName>
                                            <sld:Fill>
                                              <sld:CssParameter name="fill">#FFB82B</sld:CssParameter>
                                            </sld:Fill>
                                      </sld:Mark>
                                      <sld:Size>
                                            <ogc:Literal>6</ogc:Literal>
                                      </sld:Size>
                                    </sld:Graphic>
                              </sld:GraphicStroke>
                              <sld:CssParameter name="stroke-dasharray">6 18</sld:CssParameter>
                            </sld:Stroke>
                      </sld:LineSymbolizer>
                      <sld:LineSymbolizer>
                            <sld:Stroke>
                              <sld:CssParameter name="stroke">#FFB82B</sld:CssParameter>
                            </sld:Stroke>
                      </sld:LineSymbolizer>
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
                      <sld:MaxScaleDenominator>75000</sld:MaxScaleDenominator>
                      <sld:LineSymbolizer>
                            <sld:Stroke>
                              <sld:CssParameter name="stroke">#FFB82B</sld:CssParameter>
                              <sld:CssParameter name="stroke-dasharray">5 7</sld:CssParameter>
                              <sld:CssParameter name="stroke-dashoffset">7</sld:CssParameter>
                            </sld:Stroke>
                      </sld:LineSymbolizer>
                    </sld:Rule>
                
                
                
              </sld:FeatureTypeStyle>
            </sld:UserStyle>
      </sld:UserLayer>
    </sld:StyledLayerDescriptor>