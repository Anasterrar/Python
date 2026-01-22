# 🔓 Vigenère Cipher — Cryptanalysis (Crack)

## 1️⃣ Key Length Detection (Kasiski Examination)

Repeated **n-grams** (trigrams by default, bigrams for short texts) are detected in the ciphertext.

For each repeated pattern:
- The distances between occurrences are computed
- The **greatest common divisor (GCD)** of distances is used to extract candidate key lengths

**Formula:**

\[
\text{gcd}(d_1, d_2, \dots, d_n) \Rightarrow L \in \{ \text{possible key lengths} \}
\]

Key lengths are filtered by a maximum bound `L ≤ L_{max}`.

---

### 2️⃣ Column Decomposition

For each candidate key length \( L \), the ciphertext is split into \( L \) columns:

\[
C_j = \{ x_i \mid i \equiv j \ (\text{mod } L) \}
\]

Each column corresponds to a **Caesar cipher**.

---

### 3️⃣ Frequency Analysis (per Column)

For each column \( C_j \), all 26 shifts are tested.

Each shift is scored using letter frequency comparison (French / English).

**Score function:**

\[
S(s) = \sum_{c \in \mathcal{A}} \left| f_{obs}(c) - f_{lang}(c) \right|
\]

Only the **Top-N shifts** per column are retained.

---

### 4️⃣ Key Reconstruction

Candidate keys are generated using a cartesian product of the retained shifts:

\[
K = \prod_{j=1}^{L} \{ s_{j,1}, \dots, s_{j,N} \}
\]

To reduce computation time, only a **prefix of the ciphertext** is decrypted.

---

### 5️⃣ Global Scoring & Selection

Each decrypted candidate is evaluated using:
- Letter frequency score
- Dictionary word detection
- Syllable detection

The best candidate maximizes the global score:

\[
K^* = \arg\max_{K} \ \text{Score}(\text{Decrypt}(C, K))
\]

---

## ⏱ Complexity (Informal)

Let:
- \( L \) = key length
- \( N \) = Top-N per column

Worst-case combinations:

\[
O(N^L)
\]

In practice, execution time is controlled by:
- Adaptive `Top-N`
- Key length bounds
- Early scoring and pruning
- Partial decryption

---

##

This crack exploits **statistical weaknesses** of the Vigenère cipher and works only when:
- The ciphertext is long enough
- The key is shorter (max: 1/4) than the message

This implementation is **educational** and not intended for real-world cryptography.

---
