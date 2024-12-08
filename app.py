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

    # Social Media Growth and Suicide Rate Relationship (Line Graph)
    st.subheader("Social Media Growth Trends")
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=suicide_data["year"], y=suicide_data["Total social media growth"], label="Total Growth", color="green")
    sns.lineplot(x=suicide_data["year"], y=suicide_data["Social Media Impact Score"], label="Impact Score", color="blue")
    plt.title("Total Social Media Growth and Impact Over the Years", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Scores", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(plt)

    # Add comment
    st.markdown(
        "This graph showcases the total growth of social media platforms and their calculated impact scores over the years."
    )


# Page 3: Analysis
elif page == "Analysis":
    st.title("Data Analysis")

    # Combined Trends
    st.subheader("Combined Social Media Trends Over the Years")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=suicide_data, x="year", y="Total social media growth", label="Total Growth", color="green")
    sns.lineplot(data=suicide_data, x="year", y="Social Media Impact Score", label="Impact Score", color="blue")
    plt.title("Social Media Growth and Impact Trends")
    plt.xlabel("Year")
    plt.ylabel("Score")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

    # Year Filtering Example
    st.subheader("Filter Data by Year")
    min_year = st.slider("Select Minimum Year", int(suicide_data["year"].min()), int(suicide_data["year"].max()), step=1)
    filtered_data = suicide_data[suicide_data["year"] >= min_year]
    st.write(f"Filtered Data from Year {min_year}:")
    st.dataframe(filtered_data)

elif page == "Fancy Graph":
    st.title("Relationship Between Suicide Rate Change and Social Media User Growth")

    plt.figure(figsize=(12, 6))

    # Twitter User Growth (circles)
    twitter_scatter = plt.scatter(
        suicide_data["Twitter user count % change since 2010"],
        suicide_data["Suicide Rate % change since 2010"],
        c=suicide_data["year"],
        cmap="viridis",
        s=100,  # Bubble size for Twitter
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
