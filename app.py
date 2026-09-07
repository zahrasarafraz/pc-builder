import streamlit as st
import pandas as pd

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Page routing
if st.session_state.page == "home":
    st.title("PC Builder")
    
    components = pd.read_csv("components.csv")
    
    st.write("Available Components")
    st.dataframe(components)
    
    # Add navigation buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📚 Start Learning", use_container_width=True):
            st.session_state.page = "learning"
            st.rerun()
    
    with col2:
        if st.button("💡 Get Recommendation", use_container_width=True):
            st.session_state.page = "recommendation"
            st.rerun()

elif st.session_state.page == "learning":
    st.title("📚 Start Learning - PC Components Guide")
    
    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()
    
    st.subheader("Learn about PC Components")
    
    components_info = {
        "CPU (Processor)": "The brain of your computer. Handles all calculations and instructions.",
        "GPU (Graphics Card)": "Processes graphics and rendering. Essential for gaming and video editing.",
        "RAM (Memory)": "Temporary memory for running programs. More RAM = better multitasking.",
        "SSD/HDD (Storage)": "Permanent storage for files and programs. SSDs are faster than HDDs.",
        "Motherboard": "Connects all components together. Central circuit board of your PC.",
        "Power Supply": "Provides power to all components. Choose one with enough wattage.",
        "Case": "Houses all components and provides cooling through airflow.",
        "Cooling": "Keeps components cool. Can be air or liquid cooling."
    }
    
    for component, description in components_info.items():
        with st.expander(component):
            st.write(description)

elif st.session_state.page == "recommendation":
    st.title("💡 PC Recommendation Builder")
    
    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()
    
    st.subheader("Get PC Recommendations Based on Your Needs")
    
    col1, col2 = st.columns(2)
    
    with col1:
        purpose = st.selectbox(
            "What will you use this PC for?",
            ["Gaming", "Content Creation", "Programming", "Office Work", "Data Analysis"]
        )
    
    with col2:
        budget = st.slider(
            "What's your budget? ($)",
            min_value=300,
            max_value=5000,
            step=100,
            value=1000
        )
    
    if st.button("Generate Recommendation"):
        st.success(f"✅ Generating recommendation for {purpose} with ${budget} budget...")
        
        recommendations = {
            "Gaming": {
                "300-800": {
                    "CPU": "AMD Ryzen 5 5500",
                    "GPU": "GTX 1650 / RX 6600",
                    "RAM": "16GB DDR4",
                    "Storage": "512GB SSD"
                },
                "800-1500": {
                    "CPU": "AMD Ryzen 5 5600X",
                    "GPU": "RTX 3060 / RX 6700 XT",
                    "RAM": "16GB DDR4",
                    "Storage": "1TB SSD"
                },
                "1500-3000": {
                    "CPU": "Intel i7-12700K / AMD Ryzen 7 5800X3D",
                    "GPU": "RTX 3080 / RX 6800 XT",
                    "RAM": "32GB DDR4",
                    "Storage": "1TB NVMe SSD"
                },
                "3000+": {
                    "CPU": "Intel i9-13900K / AMD Ryzen 9 7950X",
                    "GPU": "RTX 4090 / RX 7900 XTX",
                    "RAM": "64GB DDR5",
                    "Storage": "2TB NVMe SSD"
                }
            },
            "Content Creation": {
                "300-800": {
                    "CPU": "AMD Ryzen 5 5500",
                    "GPU": "RTX 3050 / RX 6600",
                    "RAM": "16GB DDR4",
                    "Storage": "512GB SSD"
                },
                "800-1500": {
                    "CPU": "AMD Ryzen 7 5700X",
                    "GPU": "RTX 3070 / RTX 4070",
                    "RAM": "32GB DDR4",
                    "Storage": "1TB SSD"
                },
                "1500-3000": {
                    "CPU": "Intel i7-12700K / AMD Ryzen 9 5900X",
                    "GPU": "RTX 4080 / RTX A4500",
                    "RAM": "64GB DDR5",
                    "Storage": "2TB NVMe SSD"
                },
                "3000+": {
                    "CPU": "Intel i9-13900K / AMD Ryzen 9 7950X",
                    "GPU": "RTX 6000 Ada / RTX A6000",
                    "RAM": "128GB DDR5",
                    "Storage": "4TB NVMe SSD"
                }
            },
            "Programming": {
                "300-800": {
                    "CPU": "Intel i5-12400 / AMD Ryzen 5 5500",
                    "GPU": "Integrated",
                    "RAM": "16GB DDR4",
                    "Storage": "512GB SSD"
                },
                "800-1500": {
                    "CPU": "Intel i7-12700 / AMD Ryzen 7 5700X",
                    "GPU": "Integrated / RTX 3050",
                    "RAM": "32GB DDR4",
                    "Storage": "1TB SSD"
                },
                "1500-3000": {
                    "CPU": "Intel i9-12900K / AMD Ryzen 9 5900X",
                    "GPU": "RTX 4070",
                    "RAM": "64GB DDR5",
                    "Storage": "2TB NVMe SSD"
                },
                "3000+": {
                    "CPU": "Intel i9-13900K / AMD Ryzen 9 7950X",
                    "GPU": "RTX 4090",
                    "RAM": "128GB DDR5",
                    "Storage": "4TB NVMe SSD"
                }
            },
            "Office Work": {
                "300-800": {
                    "CPU": "Intel i3-12100 / AMD Ryzen 3 5100",
                    "GPU": "Integrated",
                    "RAM": "8GB DDR4",
                    "Storage": "256GB SSD"
                },
                "800-1500": {
                    "CPU": "Intel i5-12400 / AMD Ryzen 5 5500",
                    "GPU": "Integrated",
                    "RAM": "16GB DDR4",
                    "Storage": "512GB SSD"
                },
                "1500-3000": {
                    "CPU": "Intel i7-12700 / AMD Ryzen 7 5700X",
                    "GPU": "Integrated",
                    "RAM": "32GB DDR4",
                    "Storage": "1TB SSD"
                },
                "3000+": {
                    "CPU": "Intel i9-12900K / AMD Ryzen 9 5900X",
                    "GPU": "Integrated / RTX 3050",
                    "RAM": "64GB DDR5",
                    "Storage": "2TB NVMe SSD"
                }
            },
            "Data Analysis": {
                "300-800": {
                    "CPU": "AMD Ryzen 5 5500 / Intel i5-12400",
                    "GPU": "Integrated",
                    "RAM": "16GB DDR4",
                    "Storage": "512GB SSD"
                },
                "800-1500": {
                    "CPU": "AMD Ryzen 7 5700X / Intel i7-12700",
                    "GPU": "RTX 3050",
                    "RAM": "32GB DDR4",
                    "Storage": "1TB SSD"
                },
                "1500-3000": {
                    "CPU": "AMD Ryzen 9 5900X / Intel i9-12900K",
                    "GPU": "RTX 4070",
                    "RAM": "64GB DDR5",
                    "Storage": "2TB NVMe SSD"
                },
                "3000+": {
                    "CPU": "AMD Ryzen 9 7950X / Intel i9-13900K",
                    "GPU": "RTX 4090",
                    "RAM": "128GB DDR5",
                    "Storage": "4TB NVMe SSD"
                }
            }
        }
        
        # Find budget range
        def get_budget_range(budget_val):
            if budget_val <= 800:
                return "300-800"
            elif budget_val <= 1500:
                return "800-1500"
            elif budget_val <= 3000:
                return "1500-3000"
            else:
                return "3000+"
        
        budget_range = get_budget_range(budget)
        rec = recommendations[purpose][budget_range]
        
        st.subheader("Recommended Configuration:")
        cols = st.columns(len(rec))
        for col, (component, value) in zip(cols, rec.items()):
            with col:
                st.info(f"**{component}**\n\n{value}")
