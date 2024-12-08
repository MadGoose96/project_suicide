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

# Page 3: Analysis
elif page == "Analysis":
    st.title("Data Analysis")

    # Combined Trends with Improved Visualization
    st.subheader("Combined Social Media Trends Over the Years")
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot the blue line for Impact Score
    ax1.plot(
        suicide_data["year"],
        suicide_data["Social Media Impact Score"],
        label="Impact Score",
        color="blue",
        linewidth=2,
    )
    ax1.set_xlabel("Year", fontsize=12)
    ax1.set_ylabel("Impact Score", fontsize=12, color="blue")
    ax1.tick_params(axis="y", labelcolor="blue")
    ax1.grid(True, linestyle="--", alpha=0.5)

    # Create a second y-axis for Total Growth
    ax2 = ax1.twinx()
    ax2.plot(
        suicide_data["year"],
        suicide_data["Total social media growth"],
        label="Total Growth",
        color="green",
        linewidth=2,
    )
    ax2.set_ylabel("Total Social Media Growth", fontsize=12, color="green")
    ax2.tick_params(axis="y", labelcolor="green")

    # Add title and legend
    fig.suptitle("Social Media Growth and Impact Trends", fontsize=14)
    fig.tight_layout()
    st.pyplot(fig)

    # Add comment
    st.markdown(
        "This graph illustrates the social media trends over the years. The **blue line** represents the "
        "Social Media Impact Score, which shows significant growth, and the **green line** represents the "
        "Total Social Media Growth. To make the trends more readable, a secondary axis for Total Growth has been added."
    )


# Page 4: Fancy Graph
elif page == "Fancy Graph":
    st.title("Relationship Between Suicide Rate Change and Social Media User Growth")

    plt.figure(figsize=(12, 6))

    # Twitter User Growth (circles)
    twitter_scatter = plt.scatter(
        suicide_data["Twitter user count % change since 2010"],
        suicide_data["Suicide Rate % change since 2010"],
        c=suicide_data["year"],
        cmap="viridis",
        s=150,  # Bubble size for Twitter
        alpha=0.8,
        edgecolor="black",
        marker="o",  # Circular marker
        label="Twitter User Growth"
    )

    # Facebook User Growth (squares)
    facebook_scatter = plt.scatter(
        suicide_data["Facebook user count % change since 2010"],
        suicide_data["Suicide Rate % change since 2010"],
        c=suicide_data["year"],
        cmap="viridis",
        s=150,  # Bubble size for Facebook
        alpha=0.85,
        edgecolor="black",
        marker="s",  # Square marker
        label="Facebook User Growth"
    )

    # Add colorbar for the year
    cbar = plt.colorbar(twitter_scatter)  # Use one of the scatter plots for the colorbar
    cbar.set_label("Year")

    # Customize plot
    plt.title("Relationship Between Suicide Rate Change and Social Media User Growth (Twitter & Facebook)", fontsize=14)
    plt.xlabel("Social Media User Growth (% Change Since 2010)", fontsize=12)
    plt.ylabel("Suicide Rate (% Change Since 2010)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend(fontsize=12, loc="lower left")

    st.pyplot(plt)

    # Add comment
    st.markdown(
        "The combined graph shows a comparison between Twitter and Facebook user growth against suicide rates, "
        "illustrating how user trends on different platforms might correlate with societal factors."
    )

    # Add conclusion
    st.subheader("Conclusion")
    st.markdown(
        "The growth of social media platforms, with Twitter experiencing rapid initial growth followed by fluctuations and "
        "Facebook showing steady, moderate growth, appears to have a potential correlation with changes in suicide rates. "
        "This suggests that social media may influence mental health trends, reflecting both positive effects, such as increased "
        "connectivity, and negative effects, such as cyberbullying or social comparison."
    )
