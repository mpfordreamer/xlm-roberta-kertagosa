import pandas as pd
import os

# Configuration
# Adjust the path if your file is in a different location
INPUT_FILE = "dataset/kertagosa.xlsx"
OUTPUT_FILE = "dataset/kertagosa_cleaned.xlsx"

def clean_dataset():
    print("--- 🧹 Starting Data Cleaning ---")
    
    # 1. Load the dataset
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: File not found at '{INPUT_FILE}'")
        print("   Please check the file path and try again.")
        return

    try:
        df = pd.read_excel(INPUT_FILE)
        initial_rows = len(df)
        print(f"📄 Loaded '{INPUT_FILE}': {initial_rows} rows.")
    except Exception as e:
        print(f"❌ Error loading Excel file: {e}")
        return

    # 2. Clean 'text' column
    # Step A: Drop NaN / None values in 'text'
    df_clean = df.dropna(subset=['text'])
    
    # Step B: Drop empty strings or whitespace-only strings
    # Ensure column is string type, strip whitespace, and check if empty
    df_clean = df_clean[df_clean['text'].astype(str).str.strip() != ""]
    
    # Calculate stats
    final_rows = len(df_clean)
    removed_rows = initial_rows - final_rows
    
    print(f"🗑️  Removed {removed_rows} rows (Empty text or NaN).")
    print(f"✅ Remaining rows: {final_rows}")

    # 3. Save the cleaned dataset
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        
        df_clean.to_excel(OUTPUT_FILE, index=False)
        print(f"💾 Saved cleaned data to: '{OUTPUT_FILE}'")
    except Exception as e:
        print(f"❌ Error saving cleaned file: {e}")

if __name__ == "__main__":
    clean_dataset()
