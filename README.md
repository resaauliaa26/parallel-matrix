# Parallel Matrix Multiplication

## Description

This project demonstrates matrix multiplication using:

1. Sequential implementation (SISD)
2. Parallel implementation using multiprocessing (MIMD)

The goal is to understand the difference between sequential and parallel computing based on Flynn’s Taxonomy.

---

## Flynn’s Taxonomy Explanation

### 1. SISD (Single Instruction Single Data)

- One processor
- One instruction
- One data at a time
- Sequential execution

Example in this project:
matrix_sequential.py

The program executes matrix multiplication step by step in a single process.

---

### 2. SIMD (Single Instruction Multiple Data)

- One instruction
- Multiple data processed simultaneously
- Common in GPUs and vector processors

Example:
Image processing, GPU matrix operations.

---

### 3. MISD (Multiple Instruction Single Data)

- Multiple instructions
- Single data
- Rarely used
- Mostly for fault-tolerant systems

---

### 4. MIMD (Multiple Instruction Multiple Data)

- Multiple processors
- Multiple instructions
- Multiple data
- True parallel computing

Example in this project:
matrix_parallel.py

Each process computes a different row of the matrix simultaneously.

---

## Architecture Used in This Project

Sequential version → SISD  
Parallel version → MIMD

The parallel implementation uses Python multiprocessing.
Each process computes one row of the result matrix.
This allows the computation to run simultaneously on multiple CPU cores.

---

## How to Run

### Run Sequential Version

### Run Parallel Version

---

## Conclusion

Parallel computing improves performance by dividing work across multiple processors.

In this project:

- Sequential version represents SISD
- Parallel version represents MIMD
