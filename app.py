import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_dataset.csv")  # Ensure your dataset is named correctly

suicide_data = load_data()

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Visualizations", "Analysis", "Fancy Graph"])

# Page 1: Overview
if page == "Overview":
    st.title("Dataset Overview")
    st.write("Here is the dataset being analyzed:")
    st.dataframe(suicide_data)

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(suicide_data.describe())
# Page 2: Visualizations
elif page == "Visualizations":
    st.title("Data Visualizations")

    # Twitter Growth vs Suicide Rate
    st.subheader("Twitter Growth vs Suicide Rate Change")
    plt.figure(figsize=(12, 6))
    twitter_scatter = plt.scatter(
        suicide_data["Twitter user count % change since 2010"],
        suicide_data["Suicide Rate % change since 2010"],
        c=suicide_data["year"],
        cmap="coolwarm",
        s=100,
        edgecolor="black",
        alpha=0.8,
        marker="o"  # Circular marker
    )
    cbar = plt.colorbar(twitter_scatter)
    cbar.set_label("Year")
    plt.title("Twitter Growth vs Suicide Rate Change", fontsize=14)
    plt.xlabel("Twitter Growth (% Change Since 2010)", fontsize=12)
    plt.ylabel("Suicide Rate (% Change Since 2010)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(plt)

    # Add comment
    st.markdown(
        "As seen in the graph, the growth of Twitter users correlates with slight changes in suicide rates. "
        "This suggests that the growth of social media platforms might influence mental health trends."
    )

    # Facebook Growth vs Suicide Rate
    st.subheader("Facebook Growth vs Suicide Rate Change")
    plt.figure(figsize=(12, 6))
    facebook_scatter = plt.scatter(
        suicide_data["Facebook user count % change since 2010"],
        suicide_data["Suicide Rate % change since 2010"],
        c=suicide_data["year"],
        cmap="magma",
        s=150,
        edgecolor="black",
        alpha=0.85,
        marker="s"  # Square marker
    )
    cbar = plt.colorbar(facebook_scatter)
    cbar.set_label("Year")
    plt.title("Facebook Growth vs Suicide Rate Change", fontsize=14)
    plt.xlabel("Facebook Growth (% Change Since 2010)", fontsize=12)
    plt.ylabel("Suicide Rate (% Change Since 2010)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(plt)

    # Add comment
    st.markdown(
        "The relationship between Facebook user growth and suicide rates highlights a steady trend. "
        "This could be due to Facebook's broader user base and potential for both positive and negative mental health impacts."
    )

    # Twitter User Growth Over the Years
    st.subheader("Twitter User Growth Over the Years")
    plt.figure(figsize=(10, 6))
    plt.plot(
        suicide_data['year'],
        suicide_data['Twitter user count % change since 2010'],
        label="Twitter User Growth (%)",
        marker='o',
        color='purple'
    )
    plt.title("Twitter User Growth Over the Years", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Percentage", fontsize=12)
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)
    st.markdown("**Comments:** The number of Twitter users skyrocketed in 2010 until 2014 and gradually increased with slight fluctuations later.")
    st.markdown(
        "**Hypothesis:** Twitter's initial growth was driven by widespread adoption of social media platforms during this period. "
        "Fluctuations may reflect market saturation or competition."
    )

    # Facebook User Growth Over the Years
    st.subheader("Facebook User Growth Over the Years")
    plt.figure(figsize=(10, 6))
    plt.plot(
        suicide_data['year'],
        suicide_data['Facebook user count % change since 2010'],
        label="Facebook User Growth (%)",
        marker='o',
        color='orange'
    )
    plt.title("Facebook User Growth Over the Years", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Percentage", fontsize=12)
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)
    st.markdown("**Comments:** The graph shows a moderate increase during the whole period.")
    st.markdown(
        "**Hypothesis:** Facebook's steady growth suggests market saturation and competition from other platforms, limiting sharper growth."
    )

    # Facebook vs. Twitter User Growth Comparison
    st.subheader("Facebook vs. Twitter User Growth")
    plt.figure(figsize=(10, 6))
    plt.plot(
        suicide_data['year'],
        suicide_data['Twitter user count % change since 2010'],
        label="Twitter User Growth (%)",
        marker='o',
        color='purple'
    )
    plt.plot(
        suicide_data['year'],
        suicide_data['Facebook user count % change since 2010'],
        label="Facebook User Growth (%)",
        marker='s',
        color='orange'
    )
    plt.title("Facebook vs. Twitter User Growth Over the Years", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Percentage", fontsize=12)
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)
    st.markdown(
        "**Hypothesis:** Twitter likely attracted users with its unique format and real-time interaction appeal but faced challenges maintaining growth. "
        "Facebook's global reach and feature integration contributed to its steady growth."
    )

# Page 3: Analysis
elif page == "Analysis":
    st.title("Data Analysis")

    # Social Media Trends with Dual Axis
    st.subheader("Social Media Trends Over the Years")
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax2 = ax1.twinx()
    ax1.plot(suicide_data['year'], suicide_data['Total social media growth'],
             label="Total Growth (%)", color='green')
    ax2.plot(suicide_data['year'], suicide_data['Social Media Impact Score'],
             label="Impact Score", color='blue')
    ax1.set_xlabel("Year", fontsize=12)
    ax1.set_ylabel("Total Growth (%)", fontsize=12)
    ax2.set_ylabel("Impact Score", fontsize=12)
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")
    plt.title("Social Media Growth and Impact Trends", fontsize=14)
    st.pyplot(fig)

# Page 4: Fancy Graph
elif page == "Fancy Graph":
    st.title("Fancy Graph: Social Media and Suicide Rates")

    # Combined Fancy Graph
    plt.figure(figsize=(12, 6))
    plt.scatter(suicide_data["Twitter user count % change since 2010"],
                suicide_data["Suicide Rate % change since 2010"],
                c=suicide_data["year"], cmap="viridis", s=150, edgecolor="black",
                alpha=0.8, label="Twitter User Growth")
    plt.scatter(suicide_data["Facebook user count % change since 2010"],
                suicide_data["Suicide Rate % change since 2010"],
                c=suicide_data["year"], cmap="viridis", s=150, edgecolor="black",
                alpha=0.85, marker='s', label="Facebook User Growth")
    plt.colorbar(label="Year")
    plt.title("Social Media and Suicide Rates", fontsize=14)
    plt.xlabel("Social Media User Growth (%)", fontsize=12)
    plt.ylabel("Suicide Rate (%)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    st.pyplot(plt)
    st.markdown("**Conclusion:** The growth of social media platforms, with Twitter experiencing rapid growth and Facebook showing steady growth, correlates with changes in suicide rates. This highlights both positive and negative mental health influences.")
