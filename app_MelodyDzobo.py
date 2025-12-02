# ============================================
# Restaurant Dashboard - Streamlit Application Template
# ITOM6265 - Database Homework
#
# INSTRUCTIONS:
# 1. Update database credentials in Block 3
# 2. Fill in all TODO sections
# 3. Test each tab individually
# 4. Read the hints and documentation links
# ============================================

# Block 1: Import required libraries (KEEP THIS AS-IS)
import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import folium
from streamlit_folium import st_folium

# Block 2: Page configuration (KEEP THIS AS-IS)
st.set_page_config(
    page_title="ITOM6265-HW1",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Block 3: Database connection (UPDATE CREDENTIALS ONLY)
# ===== UPDATE THESE VALUES WITH YOUR DATABASE INFORMATION =====
try:
    connection = mysql.connector.connect(
        host='db-mysql-itom-do-user-28250611-0.j.db.ondigitalocean.com',  # TODO: Update with your host
        port=25060,  # TODO: Update with your port (usually 3306 for local, 25060 for DigitalOcean)
        user='restaurant_readonly',  # TODO: Update with your username
        password='SecurePassword123!',  # TODO: Update with your password
        database='restaurant'  # TODO: Update with your database name
    )
    db_connected = True
    st.success("✅ Database connected successfully!")
except Error as e:
    st.error(f"❌ Error connecting to MySQL Database: {e}")
    st.info("Please check your database credentials in the code (Block 3)")
    db_connected = False
    connection = None

# Block 4: Sidebar navigation (KEEP THIS AS-IS)
st.sidebar.title("🍽️ ITOM6265-HW1")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigation",
    ["HW Summary", "Q1-DB Query", "Q2-Maps"],
    help="Select a page to navigate"
)
st.sidebar.markdown("---")
st.sidebar.info("Restaurant Database Dashboard")

# ============================================
# TAB 1: HW SUMMARY
# ============================================
if page == "HW Summary":
    st.markdown("# 📝 Homework Summary")
    st.markdown("---")

    # HEADER
    st.markdown("""
    <div style="
        padding:20px; 
        background-color:#eaf2f8; 
        border-radius:10px;
        border-left:6px solid #3b82f6;
        font-size:22px;">
        <strong>This HW was submitted by MELODY DZOBO of ITOM6265</strong>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ============================================
    # APPROACH & IMPLEMENTATION  (Markdown bullets)
    # ============================================
    st.markdown("""
    <div style="
        background-color:#f2f8ff;
        padding:25px;
        border-radius:12px;
        border:1px solid #c9ddff;">
    """, unsafe_allow_html=True)

    st.markdown("## Approach and Implementation")

    st.markdown("""
- **How did you connect to the database?**  
  I connected to the MySQL database using the `pymysql` library after setting up a clean virtual environment.  
  At first the environment was broken because several packages—including Streamlit—could not install correctly.  
  After reinstalling Python and creating a fresh `.venv`, the connection worked.  
  I used `pandas.read_sql()` to run queries and load results into a DataFrame.

- **What libraries did you use and why?**  
  I used `pymysql` for database connections because it works reliably with MySQL.  
  I used `pandas` to run SQL queries and format the results.  
  Streamlit was required for the frontend interface.

- **What challenges did you face?**  
  The biggest challenge was fixing the Python environment.  
  Several libraries failed to install, especially `pyarrow`, and I had version conflicts with numpy and protobuf.  
  I reinstalled Python, rebuilt the virtual environment, and installed each dependency manually until Streamlit launched correctly.

- **How did you test your queries?**  
  I tested each SQL query inside MySQL Workbench first.  
  Then I added them to Streamlit and verified DataFrames loaded correctly.  
  I refreshed Streamlit after each change to ensure everything worked together.
""")

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # ============================================
    # CUSTOMIZATIONS (Markdown bullets)
    # ============================================
    st.markdown("""
<style>
div[data-testid="stAlert"]:has(div svg[data-testid="stSuccessIcon"]) {
    display: none !important;
}

/* Older Streamlit versions use this */
div[data-testid="stSuccess"] {
    display: none !important;
}
   [data-testid="stAppViewContainer"] {
        background-color: #f5f5f5 !important;
    }
 [data-testid="stSidebar"] {
        background-color: #2c3e50 !important;
    }

   [data-testid="stSidebar"] * {
        color: red !important;
    }
div[role="radiogroup"] label span {
        color: red !important;
        font-weight: 500 !important;
    }
    
    .stButton button {
        background-color: #3498db;
        color: blue;
        border: none;
        padding: 0.5rem 1.2rem;
        border-radius: 6px;
        font-size: 1rem;
        transition: 0.3s ease;
    }

    .stButton button:hover {
        background-color: #217dbb;
        transform: scale(1.03);
    }
    .info-box {
        background-color: white !important;
        border-left: 6px solid #3498db;
        padding: 18px 22px !important;
        border-radius: 8px !important;
        margin-top: 15px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .block-container {
        padding-top: 20px !important;
        padding-bottom: 20px !important;
    }
</style>
""", unsafe_allow_html=True)

    st.markdown("## Customizations Made")

    st.markdown("""
1. **Color Scheme & Styling:**
   - Dark blue (#2c3e50) sidebar for professional appearance  
   - Light gray (#f5f5f5) background for better readability  
   - Blue accent colors (#3498db) for interactive elements  
   - Custom button styling with hover effects  
""")
    st.markdown("""
2. **Layout Approach**
   - Wide layout for better data visualization  
   - Info boxes with left border accent for important information  
   - Consistent spacing and padding throughout  
""")

    st.markdown("""
3. **Map Customization**
   - CartoDB Positron tiles instead of default OpenStreetMap  
   - Custom blue markers with restaurant names in popups  
   - Optimized zoom level for London area  
""")


    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    # --------------------------------------------
    # TECHNOLOGIES SECTION (unchanged)
    # --------------------------------------------
    st.markdown("### 🛠️ Technologies Used")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Frontend:** Streamlit")
    with col2:
        st.info("**Database:** MySQL + Pandas")
    with col3:
        st.info("**Maps:** Folium")


# ============================================
# TAB 2: Q1-DB QUERY
# ============================================
elif page == "Q1-DB Query":
    st.markdown("# 🔍 Database Query")
    st.markdown("---")

    if not db_connected:
        st.error("Database connection not available. Please check your connection settings.")
    else:
        # ===== STUDENT TODO: STEP 1 - Get Min/Max Votes =====

        vote_query = """
            SELECT 
                MIN(votes) AS min_votes,
                MAX(votes) AS max_votes
            FROM business_location
            WHERE votes IS NOT NULL;
        """

        vote_range_df = pd.read_sql(vote_query, connection)

        min_votes = int(vote_range_df["min_votes"][0])
        max_votes = int(vote_range_df["max_votes"][0])

        # Create layout with columns
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown("### Filter Options")

            # ===== STUDENT TODO: STEP 2 - Create Input Widgets =====

            name_pattern = st.text_input(
                "Pattern of Name:",
                value="",
                placeholder="e.g., Dishoom",
                help="Enter part of a restaurant name to search for (uses SQL LIKE pattern matching)"
            )

            vote_range = st.slider(
                "Range of votes to search for:",
                min_value=min_votes,
                max_value=max_votes,
                value=(min_votes, max_votes)
            )

            search_button = st.button(
                "🔍 Get results",
                type="primary",
                use_container_width=True
            )

        with col2:
            st.markdown("### Search Results")

            # ===== STUDENT TODO: STEP 3 - Query and Display Results =====
            if search_button:

                min_selected, max_selected = vote_range

                # CASE 1: User entered name pattern → filter by BOTH name and votes
                if name_pattern.strip() != "":
                    sql_query = f"""
                        SELECT name, votes, city
                        FROM business_location
                        WHERE votes BETWEEN {min_selected} AND {max_selected}
                        AND name LIKE '%{name_pattern}%'
                        ORDER BY votes DESC;
                    """

                # CASE 2: User left name blank → filter ONLY by votes
                else:
                    sql_query = f"""
                        SELECT name, votes, city
                        FROM business_location
                        WHERE votes BETWEEN {min_selected} AND {max_selected}
                        ORDER BY votes DESC;
                    """

                df = pd.read_sql(sql_query, connection)

                if not df.empty:
                    st.success(f"Found {len(df)} restaurants")

                    st.dataframe(
                        df,
                        use_container_width=True,
                        height=400,
                        hide_index=True,
                        column_config={
                            "name": st.column_config.TextColumn("Restaurant Name"),
                            "votes": st.column_config.NumberColumn("Votes", format="%d"),
                            "city": st.column_config.TextColumn("City"),
                        }
                    )

                else:
                    st.warning("No restaurants found matching your criteria.")
 # ============================================
# TAB 3: Q2-MAPS
# ============================================                    
    
elif page == "Q2-Maps":
    st.markdown("# 🗺️ Restaurant Map")
    st.markdown("---")

    if not db_connected:
        st.error("Database connection not available. Please check your connection settings.")
    else:

        # ---- SESSION STATE FIX (keeps map open) ----
        if "show_map" not in st.session_state:
            st.session_state.show_map = False

        # Center the button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:

            # STEP 1: Display Map Button
            if st.button("🗺️ Display map!", type="primary", use_container_width=True):
                st.session_state.show_map = True  # map stays open

            st.caption("Map of restaurants in London. Click on teardrop to check names.")

        # ---- ONLY RUN MAP CODE IF BUTTON WAS CLICKED ----
        if st.session_state.show_map:

            # STEP 2: Query Location Data
            query = """
                SELECT
                    name,
                    latitude,
                    longitude
                FROM business_location
                WHERE latitude IS NOT NULL
                  AND longitude IS NOT NULL;
            """

            location_df = pd.read_sql(query, connection)

            # STEP 3: Create Folium Map with custom tiles
            london_map = folium.Map(
                location=[51.5074, -0.1278],
                zoom_start=11,
                tiles="CartoDB Positron"
            )

            # STEP 4: Add Markers
            for idx, row in location_df.iterrows():
                folium.Marker(
                    location=[row["latitude"], row["longitude"]],
                    popup=folium.Popup(row["name"], max_width=200),
                    tooltip=row["name"],
                    icon=folium.Icon(color="blue", icon="cutlery", prefix="fa")
                ).add_to(london_map)

            # STEP 5: Display Map
            st_folium(
                london_map,
                width=None,
                height=600,
                use_container_width=True
            )

            st.success(f"Successfully mapped {len(location_df)} restaurants!")