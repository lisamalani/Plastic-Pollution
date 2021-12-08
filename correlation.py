import streamlit as st
import streamlit.components.v1 as components

def app():
        # CORRELATION

        # >>> What determines how much mismanaged waste we produce? <<<
        st.markdown("<h4><b>What determines how much mismanaged waste we produce?</b></h4>", 
                        unsafe_allow_html=True)    
        st.markdown("<h5><b>Per capita</b></h5>", 
                        unsafe_allow_html=True)  
        st.markdown("""Whilst per capita plastic waste generation tends to 
        increase with income, this general relationship does not 
        hold when we consider mismanaged plastic waste. In the chart we show the 
        mismanaged per capita plastic waste generation rate versus GDP per capita.
        Here we see an inverse-U curve pattern. Mismanaged waste generation tends 
        to be low at very low incomes (since per capita waste is small); it then 
        rises towards middle incomes; and then falls again at higher incomes.
        Countries around the middle of the global income spectrum therefore tend 
        to have the highest per capita mismanaged plastic rates.
        This has typically occurred in countries that have rapidly industrialized, 
        but failed to make progress in waste management at the same speed.
        The development of effective waste management infrastructure, particularly 
        in middle-income countries, is therefore crucial to make progress against 
        plastic pollution.""")

        # Chart 01
        html_CR01 = """<div class='tableauPlaceholder' id='viz1638938507972' style='position: relative'><noscript><a href='#'><img alt='Cor_A ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution11&#47;Cor_A&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution11&#47;Cor_A' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution11&#47;Cor_A&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638938507972');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_CR01, height=800)

        banner = "images/banner.png"
        st.image(banner)

        st.markdown("<h5><b>Coastal Population</b></h5>", 
                        unsafe_allow_html=True)  
        st.markdown("""It is also the case that countries with high levels of 
        mismanaged waste also have large coastal populations (as shown in the 
        chart). This exacerbates the challenge of ocean plastic pollution 
        because poorly-managed waste is at high risk of entering the ocean.""")

        # Chart 02
        html_CR02 = """<div class='tableauPlaceholder' id='viz1638938479283' style='position: relative'><noscript><a href='#'><img alt='Cor_B ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution12&#47;Cor_B&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution12&#47;Cor_B' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution12&#47;Cor_B&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638938479283');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_CR02, height=800)