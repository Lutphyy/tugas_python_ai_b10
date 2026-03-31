import numpy as np
import pandas as pd
import os

# biar hasil random konsisten
np.random.seed(42)


# ======================
# NUMPY
# ======================
nilai_np = np.random.randint(50, 100, size=10)

rata2 = np.mean(nilai_np)
median = np.median(nilai_np)
std = np.std(nilai_np)
nilai_min = np.min(nilai_np)
nilai_max = np.max(nilai_np)


# ======================
# PANDAS
# ======================
data = {
    "nama": ["Andi", "Budi", "Citra", "Dewi", "Eka"],
    "nim": ["A001", "A002", "A003", "A004", "A005"],
    "nilai": nilai_np[:5]  # ambil dari numpy
}

df = pd.DataFrame(data)

# tambah kolom status
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")


# ======================
# FILE I/O
# ======================
def tulis_ringkasan(path):
    with open(path, "w") as f:
        f.write("=== RINGKASAN NUMPY ===\n")
        f.write(f"Rata-rata : {rata2:.2f}\n")
        f.write(f"Median    : {median}\n")
        f.write(f"Std Dev   : {std:.2f}\n")
        f.write(f"Min       : {nilai_min}\n")
        f.write(f"Max       : {nilai_max}\n\n")

        f.write("=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah data : {len(df)}\n")
        lulus = (df["status"] == "LULUS").sum()
        tidak = (df["status"] == "TIDAK LULUS").sum()
        f.write(f"Lulus       : {lulus}\n")
        f.write(f"Tidak lulus : {tidak}\n")


# ======================
# OOP
# ======================
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return float(self.df["nilai"].mean())

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        lulus = (self.df["nilai"] >= threshold).sum()
        return (lulus / total) * 100 if total > 0 else 0.0

    def save_summary(self, path: str):
        with open(path, "a") as f:  # append
            f.write("\n=== GRADEBOOK ===\n")
            f.write(f"Rata-rata : {self.average():.2f}\n")
            f.write(f"Pass rate : {self.pass_rate():.2f}%\n")

    def __str__(self):
        return f"GradeBook(jumlah={len(self.df)}, rata={self.average():.2f})"


# ======================
# DEMO
# ======================
if __name__ == "__main__":
    print("=== NUMPY ===")
    print("Data:", nilai_np)
    print("Rata-rata:", rata2)
    print("Median:", median)
    print("Std Dev:", std)
    print("Min:", nilai_min)
    print("Max:", nilai_max)

    print("\n=== PANDAS ===")
    print(df.head())

    # tulis file
    file_path = "ringkasan_tugas6.txt"
    tulis_ringkasan(file_path)

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)

    print(gb)
    print("Average:", gb.average())
    print("Pass rate:", gb.pass_rate(), "%")

    gb.save_summary(file_path)

    print("\nRingkasan disimpan ke:", file_path)