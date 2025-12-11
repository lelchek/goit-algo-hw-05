# String Search Algorithms Efficiency Analysis

## Overview

This project compares the efficiency of three major substring search algorithms:
1.  **Boyer-Moore**
2.  **Knuth-Morris-Pratt (KMP)**
3.  **Rabin-Karp**

The goal is to determine the fastest algorithm for searching substrings within text files using Python. The benchmarks measure execution time for both **existing** and **non-existing** substrings across two different text articles.

## Methodology

* **Environment:** Python 3.x
* **Measurement Tool:** `timeit` module
* **Data:** Two text files (`article_1.txt`, `article_2.txt`) containing natural language text.
* **Metrics:** Execution time in seconds (lower is better).

## Results

### Raw Performance Data (seconds)

| Algorithm | Article 1 (Exist) | Article 1 (Not Exist) | Article 2 (Exist) | Article 2 (Not Exist) |
| :--- | :---: | :---: | :---: | :---: |
| **Boyer-Moore** | **0.000151 s** | **0.000210 s** | **0.000168 s** | **0.000216 s** |
| **Knuth-Morris-Pratt** | 0.000923 s | 0.000772 s | 0.001301 s | 0.001089 s |
| **Rabin-Karp** | 0.002677 s | 0.001916 s | 0.002117 s | 0.002465 s |

> **Note:** Times indicate the average duration of a single search operation.

## Conclusions

Based on the benchmark results, we can draw the following conclusions regarding the performance of the algorithms for each text and overall.

### 1. Performance by Text
* **Article 1:** The **Boyer-Moore** algorithm demonstrated the best performance, being approximately **6x faster** than Knuth-Morris-Pratt and over **11x faster** than Rabin-Karp.
* **Article 2:** The trend remained consistent. **Boyer-Moore** was significantly faster than the competition. Rabin-Karp showed the slowest results.

### 2. Overall Efficiency

* **Fastest: Boyer-Moore**
    It is the clear winner in all scenarios.

* **Intermediate: Knuth-Morris-Pratt (KMP)**
    KMP performs reliably but is consistently slower than Boyer-Moore in this test.

* **Slowest: Rabin-Karp**
    Rabin-Karp was consistently the slowest.

### Final Verdict

For general text searching tasks similar to the provided articles, the **Boyer-Moore algorithm** is the most efficient choice, outperforming both KMP and Rabin-Karp by a significant margin.

## Usage

To run the benchmark script:

```bash
python main.py