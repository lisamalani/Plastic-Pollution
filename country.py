import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR


def app():
        # Country
        # >>> Which countries produce the most plastic waste? <<<
        st.markdown("<h4><b>Which countries produce the most plastic waste?</b></h4>", 
                unsafe_allow_html=True)
        st.markdown("<h5><b>Plastic waste per person</b></h5>", 
                        unsafe_allow_html=True)  
        st.markdown('''In the chart we see the per capita rate of plastic waste 
        generation, measured in kilograms per person per day. Here we see differences 
        of around an order of magnitude: daily per capita plastic waste across 
        the highest countries – Kuwait, Guyana, Germany, Netherlands, Ireland, 
        the United States – is more than 10 times higher than across many 
        countries such as India, Tanzania, Mozambique and Bangladesh.
        Note that these figures represent total plastic waste generation and do 
        not account for differences in waste management, recycling or incineration. 
        They therefore do not represent quantities of plastic at risk of loss to 
        the ocean or other waterways.''', unsafe_allow_html=True)

        # Chart 01
        html_capita = """<div class='tableauPlaceholder' id='viz1638938876909' style='position: relative'><noscript><a href='#'><img alt='C_A ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution05&#47;C_A&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution05&#47;C_A' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution05&#47;C_A&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638938876909');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_capita, height=800)

        banner = "images/banner.png"
        st.image(banner)

        # >>>Total plastic waste generation <<<
        st.markdown("<h5><b>Total plastic waste by country</b></h5>", 
                        unsafe_allow_html=True)  
        st.markdown('''In the chart we see the total plastic waste generation by 
        country, measured in tonnes per year. This therefore takes account of per 
        capita waste generation and population size. This estimate is available 
        only for the year 2010, but as we see later in this entry, the relative 
        global picture is similar in projections to 2025.
        <br>
        With the largest population, China produced the largest quantity of 
        plastic, at nearly 60 million tonnes. This was followed by the United 
        States at 38 million, Germany at 14.5 million and Brazil at 12 million tonnes.
        Like the per capita figures above, note that these figures represent total 
        plastic waste generation and do not account for differences in waste 
        management, recycling or incineration. They therefore do not represent 
        quantities of plastic at risk of loss to the ocean or other waterways.
        ''', unsafe_allow_html=True)

        # Chart 02
        html_generation = """<div class='tableauPlaceholder' id='viz1638938834696' style='position: relative'><noscript><a href='#'><img alt='C_B ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution06&#47;C_B&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution06&#47;C_B' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution06&#47;C_B&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638938834696');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='1027px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_generation, height=830)


        # >>> Mismanaged plastic waste <<<
        st.markdown("<h5><i>Mismanaged plastic waste</i></h5>", 
                unsafe_allow_html=True)
        st.markdown('''Mismanaged waste is material which is at high risk of 
        entering the ocean via wind or tidal transport, or carried to coastlines 
        from inland waterways. Mismanaged waste is the sum of material which is 
        either littered or inadequately disposed.<br>''', 
        unsafe_allow_html=True)

        st.markdown("<h5><b>Share of plastic waste that is inadequately disposed</b></h5>", 
                        unsafe_allow_html=True)  
        st.markdown('''In the world map (above) we see estimates on the share of plastic 
        waste that is defined as inadequately managed and therefore at risk of 
        entering the oceans and other environments. We see very large differences 
        in the effectiveness of waste management across the world:
        <br><br><b>High-income countries</b>, including most of Europe, North America, Australia, 
        New Zealand, Japan and South Korea have very effective waste management 
        infrastructure and systems; this means discarded plastic waste (even 
        that which is not recycled or incinerated) is stored in secure, closed 
        landfills. Across such countries almost no plastic waste is considered 
        inadequately managed. Note this does not mean there is no plastic at 
        risk of entering the natural environment — there is also littering. Across 
        many <b>low-to-middle-income income countries</b>, inadequately 
        disposed waste can be high; across many countries in South Asia and 
        Sub-Saharan Africa, between 80-90% \\of plastic waste is inadequately 
        disposed of, and therefore at risk of polluting rivers and oceans. This 
        is strongly reflected in the global distribution of mismanaged waste and 
        inputs from river systems.<br>''', unsafe_allow_html=True)

        st.markdown("<h5><b>Share of global total mismanaged plastic waste</b></h5>", 
                        unsafe_allow_html=True)  
        st.markdown('''After correcting for these factors, the share of global 
        mismanaged plastic waste by country is shown in the chart (below). This data is 
        available to explore on a per capita basis and on an absolute basis 
        (in tonnes per country). Note that whilst this data is available only 
        for the year 2010, projections of global trends for the year 2025 
        (discussed in the section below) show a very similar distribution.
        <br>
        Here we see a very strong geographical clustering of mismanaged plastic 
        waste, a high share of the world’s ocean plastics pollution has its origin 
        in Asia. China contributes the highest share of mismanaged plastic waste 
        with around 28% \\of the global total, followed by 10% \\in 
        Indonesia, 6% \\for both the Philippines and Vietnam. Other leading 
        countries include Thailand (3.2%); Egypt (3%); Nigeria 
        (2.7%) and South Africa (2%). We discuss why such countries 
        have high mismanaged plastic waste rates later in this entry.
        <br>
        Whilst many countries across Europe and North America had high rates of 
        per capita plastic generation, once corrected for waste management, their 
        contribution to mismanaged waste at risk of ocean pollution is 
        significantly lower.''', unsafe_allow_html=True)

        # Chart 03
        html_share = """<div class='tableauPlaceholder' id='viz1638938820306' style='position: relative'><noscript><a href='#'><img alt='C_C ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution07&#47;C_C&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution07&#47;C_C' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution07&#47;C_C&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638938820306');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_share, height=800)

        st.markdown('''The East Asia and Pacific region dominates global mismanaged 
        plastic waste, accounting for 60% \\of the world total.
        There is a wide gap between East Asia and the other regions — South Asia 
        ranks second but contributes around 5 times less with 11% \\of the 
        total. This is followed by Sub-Saharan Africa (9%); Middle East & 
        North Africa (8.3%); Latin America (7.2%); Europe and 
        Central Asia (3.6%) and North America (1%).
        <br>
        If we aim to address the ocean plastic problem, an understanding of this 
        global picture is important. It highlights the fundamental role of waste 
        management in preventing ocean pollution; whilst countries across North 
        America and Europe generate significant quantities of plastic waste 
        (particularly on a per capita basis), well-managed waste streams mean 
        that very little of this is at risk of ocean pollution. In fact, if 
        North America & Europe were to completely eliminate plastic use, global 
        mismanaged plastic would decline by less than 5%''', unsafe_allow_html=True)

        # Chart 04
        html_trade = """<div class='tableauPlaceholder' id='viz1638938719785' style='position: relative'><noscript><a href='#'><img alt='C_D ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution08&#47;C_D&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlasticPollution08&#47;C_D' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlasticPollution08&#47;C_D&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638938719785');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_trade, height=800)

        st.markdown('''This has important implications for managing global 
        plastic waste: if countries with effective waste management systems – 
        predominantly high-income countries – export plastic waste to middle to 
        low-income countries with poor waste management systems, they could be 
        adding to the ocean plastic problem in this way.
        <br>
        <b>Who were the main plastic exporters to China?: </b>
        In the chart we 
        see the quantity of plastic exported to China from the top 10 exporting 
        countries. Collectively, these countries are responsible for around 76 
        percent of its imports.
        As we see, Hong Kong typically acts as an entry point for Chinese 
        imports; it is therefore the largest ‘exporting’ country to China. 
        Many high-income countries are included in this top 10: Japan, USA, 
        Germany, Belgium, Australia and Canada are all major plastic exporters.'''
        , unsafe_allow_html=True)
 
        st.markdown('''<b>Future mismanaged plastic:</b> Overall we see that the global distribution is projected 
        to change only slightly; whilst China’s contribution falls by a couple 
        of percentage points, East Asia & Pacific maintain around 60% \\of 
        the total. South Asia’s contribution — largely driven by India — increases 
        slightly, as does Sub-Saharan Africa. Latin America, the Middle East & 
        North Africa, Europe and North America all fall in relative terms.''', 
        unsafe_allow_html=True)

        
