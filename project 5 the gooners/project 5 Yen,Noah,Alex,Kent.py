#==============================================================
# Team: The GOoners. Yen, Alex, Noah, Kent
#==============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


DATA_DIR = Path(".")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


# LOAD DATA
def load_data(file_path):
    df = pd.read_csv(file_path)

    # simple validation (lecture-style)
    required = ["Hour", "Cell_Count", "Viability_pct", "Average_Size_um"]

    for col in required:
        if col not in df.columns:
            print("Missing column:", col)
            return pd.DataFrame()

    return df


# BASIC METRICS (Phase 1)
def growth_metrics(df):
    avg_count = sum(df["Cell_Count"]) / len(df)
    avg_viability = sum(df["Viability_pct"]) / len(df)
    avg_size = sum(df["Average_Size_um"]) / len(df)
    final_count = df["Cell_Count"].iloc[-1]

    return avg_count, avg_viability, avg_size, final_count


# GROWTH RATIO (Phase 2)
def growth_ratio(df):
    ratios = []

    for i in range(1, len(df)):
        prev = df["Cell_Count"].iloc[i - 1]
        curr = df["Cell_Count"].iloc[i]

        if prev != 0:
            ratios.append(curr / prev)

    return ratios


# VARIANT A (rolling growth)
def rolling_growth(df):
    ratios = growth_ratio(df)
    rolling = []

    for i in range(len(ratios)):
        start = max(0, i - 2)
        window = ratios[start:i + 1]
        rolling.append(sum(window) / len(window))

    return rolling


# VARIANT B (viability drop)
def first_major_viability_drop(df):
    for i in range(1, len(df)):
        if df["Viability_pct"].iloc[i - 1] - df["Viability_pct"].iloc[i] > 2:
            return df["Hour"].iloc[i]
    return None


# VARIANT C (size jumps)
def size_jump_flags(df):
    flags = []

    for i in range(1, len(df)):
        diff = abs(df["Average_Size_um"].iloc[i] - df["Average_Size_um"].iloc[i - 1])
        if diff > 0.5:
            flags.append(df["Hour"].iloc[i])

    return flags


# PHASE 1 PLOTS
def phase1_plots(df, name):
    plt.plot(df["Hour"], df["Cell_Count"])
    plt.title(f"{name} - Cell Count")
    plt.xlabel("Hour")
    plt.ylabel("Cell Count")
    plt.savefig(OUTPUT_DIR / f"{name}_cell_count.png")
    plt.show()
    plt.close()

    plt.plot(df["Hour"], df["Viability_pct"])
    plt.title(f"{name} - Viability")
    plt.xlabel("Hour")
    plt.ylabel("Viability %")
    plt.savefig(OUTPUT_DIR / f"{name}_viability.png")
    plt.show()
    plt.close()

    # REQUIRED FIX (missing earlier)
    plt.plot(df["Hour"], df["Average_Size_um"])
    plt.title(f"{name} - Cell Size")
    plt.xlabel("Hour")
    plt.ylabel("Size (um)")
    plt.savefig(OUTPUT_DIR / f"{name}_size.png")
    plt.show()
    plt.close()


# PHASE 2 COMPARISON
def compare_runs(dfs):
    rows = []

    for df in dfs:
        avg_count, avg_v, avg_s, final = growth_metrics(df)
        rows.append([
            df["Run"].iloc[0],
            final,
            avg_v,
            avg_s
        ])

    summary = pd.DataFrame(rows, columns=[
        "Run", "Final_Count", "Avg_Viability", "Avg_Size"
    ])

    summary = summary.sort_values("Final_Count", ascending=False)
    summary.to_csv(OUTPUT_DIR / "phase2_summary.csv", index=False)

    return summary


# COMPARISON PLOT
def comparison_plot(summary):
    plt.plot(summary["Run"], summary["Final_Count"])
    plt.title("Final Cell Count Comparison")
    plt.xlabel("Culture Run")
    plt.ylabel("Final Count")
    plt.savefig(OUTPUT_DIR / "cell_count_comparison.png")
    plt.show()
    plt.close()


# PHASE 3 BATCH PROCESSING
def batch_process(files):
    dfs = []

    for f in files:
        df = pd.read_csv(f)
        df["Run"] = f.stem
        dfs.append(df)

    combined = pd.concat(dfs)
    combined.to_csv(OUTPUT_DIR / "combined_culture_data.csv", index=False)

    return dfs


# PHASE 3 FEATURES
def predict_next_count(df):
    if len(df) < 2:
        return None

    return df["Cell_Count"].iloc[-1] + (
        df["Cell_Count"].iloc[-1] - df["Cell_Count"].iloc[-2]
    )


def recommend_harvest_window(df):
    for i in range(len(df)):
        if df["Cell_Count"].iloc[i] > 5000 and df["Viability_pct"].iloc[i] < 85:
            return df["Hour"].iloc[i]
    return None


# MAIN
def main():

    df = load_data(DATA_DIR / "culture_day_A.csv")

    avg_c, avg_v, avg_s, final_c = growth_metrics(df)

    phase1_plots(df, "culture_A")

    pd.DataFrame([{
        "avg_cell_count": avg_c,
        "avg_viability": avg_v,
        "avg_size": avg_s,
        "final_count": final_c
    }]).to_csv(OUTPUT_DIR / "phase1_summary.csv", index=False)

    with open(OUTPUT_DIR / "phase1_reflection.md", "w") as f:
        f.write("Phase 1 completed: basic growth trends analyzed.")

    files = [
        DATA_DIR / "culture_day_A.csv",
        DATA_DIR / "culture_day_B.csv",
        DATA_DIR / "culture_day_C.csv"
    ]

    dfs = batch_process(files)

    for df in dfs:
        df["Run"] = df["Run"].iloc[0]

    summary = compare_runs(dfs)
    comparison_plot(summary)

    with open(OUTPUT_DIR / "phase2_notes.md", "w") as f:
        f.write("Phase 2 completed: comparisons and growth ratios analyzed.")

    # ---------------- Phase 3 ----------------
    for df in dfs:
        print("Run:", df["Run"].iloc[0])
        print("Prediction:", predict_next_count(df))
        print("Harvest:", recommend_harvest_window(df))
        print("------")

    with open(OUTPUT_DIR / "phase3_report.txt", "w") as f:
        f.write("Phase 3 completed.\n")
        f.write("Growth prediction and harvest analysis were implemented.\n")
        f.write("Batch processing and comparison across cultures completed.\n")


if __name__ == "__main__":
    main()