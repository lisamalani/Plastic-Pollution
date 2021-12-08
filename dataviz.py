
# def data_viz():
#     st.markdown("<br><br><br>",unsafe_allow_html=True)  
#     st.markdown("<h5>Results:</h5>",unsafe_allow_html=True)  
#     _, data_df = read_gsheet()
#     sns.set_style("whitegrid", {"grid.color": ".6", "grid.linestyle": ":"})

#     col1, col2, col3 = st.columns(3)
#     # col2.metric("Recyclers at Heart:", len(data_df[data_df["Recycle01"] == "Yes"]))
#     with col1:
#         st.metric("Total Responses:", len(data_df), delta=None, delta_color="normal")
#     with col2:
#         st.metric("Active plastic recyclers:", len(data_df[data_df["Recycle01"] == "Yes"]), delta=None, delta_color="normal")
#     with col3:
#         st.metric("Aware of plastic leak:", len(data_df[data_df["Recycle04"] == "Yes"]), delta=None, delta_color="normal")


#     # Chart 01
#     with st.container():
#         val_yes = [len(asia_df[asia_df["Recycle01"] == "Yes"]),
#                 len(africa_df[africa_df["Recycle01"] == "Yes"]),
#                 len(au_df[au_df["Recycle01"] == "Yes"]),
#                 len(europe_df[europe_df["Recycle01"] == "Yes"]),
#                 len(na_df[na_df["Recycle01"] == "Yes"]),
#                 len(sa_df[sa_df["Recycle01"] == "Yes"])]

        
#         region_df = pd.DataFrame({
#             "Region": names,
#             "Total Responses": val,
#             "Yes": val_yes
#         })

#         f, ax = plt.subplots(figsize=(30, 10))
#         sns.barplot(x="Total Responses", y="Region", data=region_df,
#                 label="Total")

#         sns.barplot(x="Yes", y="Region", data=region_df,
#                 label="Responded Yes")

#         # Add a legend and informative axis label
#         ax.legend(ncol=2, loc="lower right", frameon=True)
#         ax.set(ylabel="", xlabel="Responses per Region")
#         sns.despine(left=True, bottom=True)
#         sns.set(rc = {'figure.figsize':(30,10)})
#         st.pyplot(f, use_container_width=True)
    
    
#     # Chart 02
#     with st.container():
#         col1, col2 = st.columns(2)
#         names = ['10-18', '19-27', '28-36', '37-45', '46-54', '54+']

#         age_10_df = data_df[data_df["Age Group"] == "10-18"]
#         age_19_df = data_df[data_df["Age Group"] == "19-27"]
#         age_28_df = data_df[data_df["Age Group"] == "28-36"]
#         age_37_df = data_df[data_df["Age Group"] == "37-45"]
#         age_46_df = data_df[data_df["Age Group"] == "46-54"]
#         age_54_df = data_df[data_df["Age Group"] == "54+"]
#         val = [len(age_10_df),
#                 len(age_19_df),
#                 len(age_28_df),
#                 len(age_37_df),
#                 len(age_46_df),
#                 len(age_54_df)]

#         val_yes = [len(age_10_df[age_10_df["Recycle02"] == "Yes"]),
#                 len(age_19_df[age_19_df["Recycle02"] == "Yes"]),
#                 len(age_28_df[age_28_df["Recycle02"] == "Yes"]),
#                 len(age_37_df[age_37_df["Recycle02"] == "Yes"]),
#                 len(age_46_df[age_46_df["Recycle02"] == "Yes"]),
#                 len(age_54_df[age_54_df["Recycle02"] == "Yes"])]

#         val_occ = [len(age_10_df[age_10_df["Recycle02"] == "Occasionally"]),
#                 len(age_19_df[age_19_df["Recycle02"] == "Occasionally"]),
#                 len(age_28_df[age_28_df["Recycle02"] == "Occasionally"]),
#                 len(age_37_df[age_37_df["Recycle02"] == "Occasionally"]),
#                 len(age_46_df[age_46_df["Recycle02"] == "Occasionally"]),
#                 len(age_54_df[age_54_df["Recycle02"] == "Occasionally"])]
        
#         age_df = pd.DataFrame({
#             "Age Group": names,
#             "Total Responses": val,
#             "Yes_total": val_yes,
#             "Occasionally": val_occ
#         })

#         age_df["Yes"] = age_df["Yes_total"] + age_df["Occasionally"] 
#         f2, ax2 = plt.subplots(figsize=(30, 10))

#         sns.barplot(x="Total Responses", y="Age Group", data=age_df,
#                 label="Total", color="b")

#         sns.barplot(x="Yes", y="Age Group", data=age_df,
#                 label="Responded Yes", color="b")

#         sns.barplot(x="Occasionally", y="Age Group", data=age_df,
#                 label="Responded Occasionally", color="lightblue")

#         # Add a legend and informative axis label
#         ax2.legend(ncol=2, loc="lower right", frameon=True)
#         ax2.set(ylabel="", xlabel="Responses per Age Group")
#         sns.despine(left=True, bottom=True)
#         sns.set(rc = {'figure.figsize':(30,10)})
#         st.pyplot(f2, use_container_width=True)


#     # Chart 3
#     with st.container():
#         names = ['Everyday', 'About once a week', 'Few times a week', 
#                             'About once a month', 'A few times a month', 'Never']
#         n0_df = data_df[data_df["Recycle03"] == names[0]]
#         n1_df = data_df[data_df["Recycle03"] == names[1]]
#         n2_df = data_df[data_df["Recycle03"] == names[2]]
#         n3_df = data_df[data_df["Recycle03"] == names[3]]
#         n4_df = data_df[data_df["Recycle03"] == names[4]]
#         n5_df = data_df[data_df["Recycle03"] == names[5]]
#         val = [len(n0_df),
#                 len(n1_df),
#                 len(n2_df),
#                 len(n3_df),
#                 len(n4_df),
#                 len(n5_df)]

#         recycle_df = pd.DataFrame({
#             "Responses": names,
#             "Counts": val
#         })
#         f3, ax3 = plt.subplots(figsize=(30, 10))

#         sns.set_color_codes("pastel")
#         sns.barplot(y="Counts", x="Responses", data=recycle_df,
#                 label="Response Count", color="b")

#         # Add a legend and informative axis label
#         ax3.legend(ncol=2, loc="lower right", frameon=True)
#         ax3.set(ylabel="", xlabel="Responses per Region")
#         sns.despine(left=True, bottom=True)
#         sns.set(rc = {'figure.figsize':(30, 10)})
#         st.pyplot(f3, use_container_width=True)

