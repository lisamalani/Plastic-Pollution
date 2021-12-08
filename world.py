import streamlit as st
import streamlit.components.v1 as components

# Reference for data and information
# https://ourworldindata.org/plastic-pollution

def app():
        # GLOBAL STATISTIC
        st.markdown('''Global production of plastics is increasing every year and the 
        amount of plastic litter that is finding its way into the environment and into 
        the oceans is also increasing, especially in the areas of the world where waste 
        management practices are not keeping up with the rapid development.
        There is however a lack of information on how much plastic debris finds its 
        way to the oceans and how much of it there already is in the oceans. In order to 
        identify the information needs and to explore what is already known and being done 
        in the world.<br><br>''', unsafe_allow_html=True)

        banner = "images/banner.png"
        st.image(banner)

        # >>> How much plastic does the world produce? <<<  
        st.markdown("<h4><b>How much plastic does the world produce?</b></h4>", 
                        unsafe_allow_html=True)   
        st.markdown('''<b>How much plastic has the world produced cumulatively?</b> The
        chart shows that by 2015, the world had produced <b>7.8 billion tonnes</b> of 
        plastic — more than one tonne of plastic for every person alive today.''', 
                        unsafe_allow_html=True)
        
        # Chart 01 and 02
        html_global = """<div class='tableauPlaceholder' id='viz1638939008927' style='position: relative'><noscript><a href='#'><img alt='A_v2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution01&#47;A_v2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution01&#47;A_v2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution01&#47;A_v2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638939008927');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_global, height=830)

        st.markdown("<h4><b>How much plastic will the world produce?</b></h4>", 
                        unsafe_allow_html=True)
        st.markdown("""Try different regression models and predict the increase in the plastic production if no factors
        directly impacting the result has changed behaviour.""", 
                        unsafe_allow_html=True)   
        # Chart 01 and 02
        html_globalPred = """<div class='tableauPlaceholder' id='viz1638963432849' style='position: relative'><noscript><a href='#'><img alt='A_v2 (2) ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution13&#47;A_v22&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution13&#47;A_v22' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution13&#47;A_v22&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638963432849');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_globalPred, height=800)

        st.image(banner)

        # >>> How do we dispose of our plastic? <<<
        st.markdown("<h4><b>How do we dispose of our plastic?</b></h4><br>", 
                        unsafe_allow_html=True)
      
        st.markdown("""<b>How has global plastic waste disposal method changed over 
        time?</b> In the chart we see the share of global plastic waste that is discarded, 
        recycled or incinerated from 1980 through to 2015. Prior to 1980, 
        recycling and incineration of plastic was negligible; 100% was 
        therefore discarded. From 1980 for incineration, and 1990 for recycling, 
        rates increased on average by about 0.7% per year. In 2015, an 
        estimated 55% \\of global plastic waste was discarded, 25% 
        was incinerated, and 20% \\recycled.""", unsafe_allow_html=True)  

        # Chart 03
        html_dispose = """<div class='tableauPlaceholder' id='viz1638938950027' style='position: relative'><noscript><a href='#'><img alt='C ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution03&#47;C&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution03&#47;C' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution03&#47;C&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638938950027');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_dispose, height=800)

        st.image(banner)

        # >>> Which sectors produce the most plastic? <<<
        st.markdown("<h4><b>Which sectors produce the most plastic?</b></h4><br>", 
                        unsafe_allow_html=True)
           
        st.markdown("<h5><b>Use</b></h5>", 
                unsafe_allow_html=True)
        st.markdown("""<b>To which industries and product uses is primary plastic 
        production allocated?</b> In the chart we see plastic production allocation 
        by sector for 2015. Packaging was the dominant use of primary plastics, 
        with 42% \\of plastics entering the use phase. Building and 
        construction was the second largest sector utilizing 19% \\of the 
        total. Primary plastic production does not directly reflect plastic waste 
        generation (as shown in the next section), since this is also influenced 
        by the polymer type and lifetime of the end product.<br>""", 
                        unsafe_allow_html=True)

        # Chart 04
        html_sectors = """<div class='tableauPlaceholder' id='viz1638938977035' style='position: relative'><noscript><a href='#'><img alt='B ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution02&#47;B&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution02&#47;B' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution02&#47;B&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638938977035');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='827px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_sectors, height=800)

        st.markdown("<h5><b>Waste</b></h5>", 
                unsafe_allow_html=True)
        st.markdown("""In the chart we see these same sectors in terms of plastic waste generation. 
        Plastic waste generation is strongly influenced by primary plastic use, 
        but also the product <b>lifetime</b>. Packaging, for example, has a very short 
        ‘in-use’ lifetime (typically around 6 months or less). This is in contrast 
        to building and construction, where plastic use has a mean lifetime of 35 years.
        Packaging is therefore the dominant generator of plastic waste, 
         responsible for almost half of the global total. In 2015, primary 
         plastics production was 407 million tonnes; around three-quarters 
         (302 million tonnes) ended up as waste.""", 
                        unsafe_allow_html=True)

        # Chart 05
        html_meanUse = """<div class='tableauPlaceholder' id='viz1638938919534' style='position: relative'><noscript><a href='#'><img alt='D ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution04&#47;D&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution04&#47;D' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution04&#47;D&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638938919534');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_meanUse, height=800)
