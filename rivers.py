import streamlit as st
import streamlit.components.v1 as components

def app():
        # RIVERS and OCEANS

        # >>> How much of ocean plastics come from land and marine sources? <<<
        st.markdown("<h4><b>How much of ocean plastics come from land and marine sources?</b></h4>", 
                        unsafe_allow_html=True)    
        st.markdown('''Plastic in our oceans can arise from both land-based or 
        marine sources. Plastics pollution from marine sources refers to the 
        pollution caused by fishing fleets that leave behind fishing nets, lines, 
        ropes, and sometimes abandoned vessels. There is often intense debate 
        about the relative importance of marine and land sources for ocean 
        pollution. <i>What is the relative contribution of each?</i>  
        At the global level, best estimates suggest that approximately 80% \\of 
        ocean plastics come from land-based sources, and the remaining 20% \\from
         marine sources.<br>''', unsafe_allow_html=True)

        st.markdown("<h5><b>River inputs to the ocean</b></h5>", 
                        unsafe_allow_html=True)  

        st.markdown("""There are multiple routes by which plastic can enter the 
        ocean environment. One key input is through river systems. This can 
        transport plastic waste from further inland to coastal areas where it 
        can enter the ocean. As we see in the following charts, there is high 
        concentration of plastic within river systems geographically.""")
        st.markdown("""<b>Top 20 river sources:</b> In the chart listed are the 
        estimated input of plastic to the oceans from the most polluting rivers 
        across the world.
        The top 20 polluting rivers accounted for two-thirds – 67% – of 
        the global annual river input. Geographically we see that the majority 
        of the most polluting rivers are located in Asia. River Yangtze, the top 
        polluting river, had an input of approximately 333,000 tonnes in 2015 — 
        over 4% \\of annual ocean plastic pollution.""", unsafe_allow_html=True) 

        st.markdown("""<h6><b>River inputs by region:</b> In the chart we see river 
        plastic inputs to the ocean 
        aggregated by region — this is given as a share of the global total.
        Most river plastic originates from Asia, which represents  86% \\of the 
        global total. This is followed by Africa at 7.8%, and 
        South America at 4.8%. Collectively, Central & North America, 
        Europe and the Australia-Pacific region account for just over one 
        percent of the world total.""")

        # Chart 01
        html_Oc01 = """<div class='tableauPlaceholder' id='viz1638938606096' style='position: relative'><noscript><a href='#'><img alt='RO_A ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution09&#47;RO_A&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution09&#47;RO_A' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution09&#47;RO_A&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638938606096');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='927px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_Oc01, height=800)

        banner = "images/banner.png"
        st.image(banner)

        # >>> Which oceans have the most plastic waste? <<<
        st.markdown("<h4><b>Which oceans have the most plastic waste?</b></h4>", 
                        unsafe_allow_html=True)    
        st.markdown('''Plastic enters the oceans from coastlines, rivers, tides, 
        and marine sources. <b>But once it is there, where does it go?</b> <br>
        The distribution and accumulation of ocean plastics is strongly influenced 
        by oceanic surface currents and wind patterns. Plastics are typically 
        buoyant, allowing them to be 
        transported by the prevalent wind and surface current routes. As a result, 
        plastics tend to accumulate in oceanic gyres, with high concentrations of 
        plastics at the centre of ocean basins, and much less around the perimeters. 
        After entry to oceans from coastal regions, plastics tend to migrate towards 
        the centre of ocean basins. <br><br>
        In the chart we see estimates of the mass of plastics in surface ocean 
        waters by ocean basin. It is estimated that there was 
        approximately 269,000 tonnes of plastic in surface waters across the world. 
        Note that this at least an order of magnitude lower than estimated inputs 
        of plastics to the ocean; the discrepancy here relates to a surprising, 
        but long-standing question in the research literature on plastics: <b>“where 
        is the missing plastic going?“.</b> As we see, basins in the Northern 
        Hemisphere had the highest quantity of 
        plastics. This would be expected since the majority of the world’s population 
        – and in particular, <i>coastal populations.</i> – live within the Northern Hemisphere. 
        However, authors were still surprised by the quantity of plastic accumulation 
        in Southern oceans — while it was lower than in the Northern Hemisphere, 
        it was still of the same order of magnitude. Considering the lack of 
        coastal populations and plastic inputs in the Southern Hemisphere, 
        this was an unexpected result. The authors suggest this means plastic 
        pollution can be moved between oceanic gyres and basins much more 
        readily than previously assumed.''', unsafe_allow_html=True)

        # Chart 03
        html_Oc02 = """<div class='tableauPlaceholder' id='viz1638938558673' style='position: relative'><noscript><a href='#'><img alt='RO_B ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution10&#47;RO_B&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution10&#47;RO_B' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution10&#47;RO_B&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638938558673');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='1027px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_Oc02, height=800)
